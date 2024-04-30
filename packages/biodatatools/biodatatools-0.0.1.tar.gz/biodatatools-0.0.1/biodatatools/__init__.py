import sys
import simplevc
simplevc.register(sys.modules[__name__], "0.0.1")

import tempfile
import os
import subprocess
import shutil

import pysam
import pyBigWig

from biodata.baseio import BaseWriter
from biodata.bed import BEDPE
from biodata.delimited import DelimitedReader, DelimitedWriter

from commonhelper import convert_to_bool, safe_inverse_zip, nested_default_dict
from mphelper import ProcessWrapPool
	
	
	

def check_binaries_validity(*binary_names): # Change to decorator in the future
	missing_binary_names = [binary_name for binary_name in binary_names if shutil.which(binary_name) is None]
	if len(missing_binary_names) > 0:
		raise Exception("The following binaries are not found: " + ",".join(binary_names))
	
def bash_command(cmd):
	p = subprocess.run(cmd, shell=True, executable='/bin/bash')
	if p.returncode != 0:
		raise Exception("Bash command fails: " + cmd)
	
	
@vt(
	description="A wrapper to bedGraphToBigWig", helps=dict(
		i="Input bedgraph file", g="chrom size file", o="output bigwig file",
		autosort="Perform sorting on bedgraph file before running bedGraphToBigWig",
		filter_chr="Remove chromosomes in bedgraph file that are not present in chrom.sizes file", 
		nthread="Number of threads used in sorting")
)
@vc
def _convert_bedgraph_to_bigwig_20240423(i:str, g:str, o:str, autosort:convert_to_bool=False, filter_chr:convert_to_bool=False, nthread:int=1):
	'''
	Convert bedgraph into bigwig files. Auto sort and filter bedgraphs prior to calling bedGraphToBigWig
	:param i: Input bedgraph file
	:param g: chrom.size file
	:param o: Output bw file
	:param autosort: Perform sorting on bedgraph file before running bedGraphToBigWig
	:param filter_chr: Remove chromosomes in bedgraph file that are not present in chrom.sizes file
	'''
	check_binaries_validity("zcat", "sort", "bedGraphToBigWig")
	tmpfiles = []
	if filter_chr:
		inputfile = tempfile.NamedTemporaryFile(mode='w+', suffix=".bg", delete=False).name
		tmpfiles.append(inputfile)
		with DelimitedReader(g) as dr:
			chromosomes = set([d[0] for d in dr])
		with DelimitedReader(i) as dr, DelimitedWriter(inputfile) as dw:
			for d in dr:
				if d[0] in chromosomes:
					dw.write(d)
		i = inputfile
	
	if autosort:
		inputfile = tempfile.NamedTemporaryFile(mode='w+', suffix=".bg", delete=False).name
		tmpfiles.append(inputfile)
		if nthread > 1:
			added_param = f"--parallel={nthread} "
		else:
			added_param = ""
		if i.endswith(".gz"):
			result0 = subprocess.run(f"zcat {i} | sort -k1,1 -k2,2n {added_param}> {inputfile}", shell=True)
		else:
			result0 = subprocess.run(f"sort -k1,1 -k2,2n {added_param}{i} > {inputfile}", shell=True)
		if result0.returncode != 0:
			raise Exception("Exception in sorting bg")
		i = inputfile
		
	result = subprocess.run(f"bedGraphToBigWig {i} {g} {o}", shell=True, executable="/bin/bash")
	if result.returncode != 0:
		raise Exception("Exception in running bedGraphToBigWig")
	for tmpfile in tmpfiles:
		os.unlink(tmpfile)

@vt(description="Convert GROcap/PROcap/GROseq/PROseq bam file to bigwig files (paired-end reads). Returns 4 bigwig files representing 5' and 3' end of the molecules on plus or minus strand", 
	helps=dict(i="Input bam file", g="chrom size file", o="output bigwig file prefix",
			paired_end="True: paired-end sequencing; False: single-end sequencing",
			rna_strand="Indicate whether RNA strand is forward or reverse. In paired-end, forward represents that first read is 5'."
			)
		)
@vc
def _process_PROcap_bam_to_bigwig_20240423(i:str, g:str, o:str, paired_end : convert_to_bool, rna_strand : str):
	'''
	first_read_is_5 --> strand == Forward
	'''
	check_binaries_validity("samtools", "bedtools", "zcat", "sort", "bedGraphToBigWig")
	
	tmpfiles = [tempfile.NamedTemporaryFile(mode='w+', suffix=".bg", delete=False).name for _ in range(4)]
	bg5_pl, bg5_mn, bg3_pl, bg3_mn = tmpfiles
	thread = 16
	pwpool = ProcessWrapPool(4)
	if paired_end:
		tmpfiles_bam = [tempfile.NamedTemporaryFile(mode='w+', suffix=".bam", delete=False).name for _ in range(2)]
		bam5, bam3 = tmpfiles_bam		
		if rna_strand == "forward":
			bam5_pid = pwpool.run(bash_command, args=[f"samtools view -f 66 --write-index -@ {thread} -o {bam5} {i}"])
			bam3_pid = pwpool.run(bash_command, args=[f"samtools view -f 130 --write-index -@ {thread} -o {bam3} {i}"])
		elif rna_strand == "reverse":
			bam5_pid = pwpool.run(bash_command, args=[f"samtools view -f 130 --write-index -@ {thread} -o {bam5} {i}"])
			bam3_pid = pwpool.run(bash_command, args=[f"samtools view -f 66 --write-index -@ {thread} -o {bam3} {i}"])
		else:
			raise Exception()
		# Be careful of the strand. We assumed F1R2 setup 
		bgpl_pid = pwpool.run(bash_command, args=[f"bedtools genomecov -ibam {bam5} -5 -strand + -bg > {bg5_pl}"], dependencies=[bam5_pid])
		bgmn_pid = pwpool.run(bash_command, args=[f"bedtools genomecov -ibam {bam5} -5 -strand - -bg | awk {{'printf (\"%s\\t%s\\t%s\\t-%s\\n\", $1, $2, $3, $4)'}} > {bg5_mn}"], dependencies=[bam5_pid])
		bg3pl_pid = pwpool.run(bash_command, args=[f"bedtools genomecov -ibam {bam3} -5 -strand - -bg > {bg3_pl}"], dependencies=[bam3_pid])
		bg3mn_pid = pwpool.run(bash_command, args=[f"bedtools genomecov -ibam {bam3} -5 -strand + -bg | awk {{'printf (\"%s\\t%s\\t%s\\t-%s\\n\", $1, $2, $3, $4)'}} > {bg3_mn}"], dependencies=[bam3_pid])
	else:
		tmpfiles_bam = [] # No bam files needed
		bgpl_pid = pwpool.run(bash_command, args=[f"bedtools genomecov -ibam {i} -5 -strand + -bg > {bg5_pl}"])
		bgmn_pid = pwpool.run(bash_command, args=[f"bedtools genomecov -ibam {i} -5 -strand - -bg | awk {{'printf (\"%s\\t%s\\t%s\\t-%s\\n\", $1, $2, $3, $4)'}} > {bg5_mn}"])
		bg3pl_pid = pwpool.run(bash_command, args=[f"bedtools genomecov -ibam {i} -3 -strand + -bg > {bg3_pl}"])
		bg3mn_pid = pwpool.run(bash_command, args=[f"bedtools genomecov -ibam {i} -3 -strand - -bg | awk {{'printf (\"%s\\t%s\\t%s\\t-%s\\n\", $1, $2, $3, $4)'}} > {bg3_mn}"])
		
	pwpool.run(_convert_bedgraph_to_bigwig_20240423, args=[bg5_pl, g, o + "_5pl.bw"], kwargs=dict(autosort=True, filter_chr=True), dependencies=[bgpl_pid])
	pwpool.run(_convert_bedgraph_to_bigwig_20240423, args=[bg5_mn, g, o + "_5mn.bw"], kwargs=dict(autosort=True, filter_chr=True), dependencies=[bgmn_pid])
	pwpool.run(_convert_bedgraph_to_bigwig_20240423, args=[bg3_pl, g, o + "_3pl.bw"], kwargs=dict(autosort=True, filter_chr=True), dependencies=[bg3pl_pid])
	pwpool.run(_convert_bedgraph_to_bigwig_20240423, args=[bg3_mn, g, o + "_3mn.bw"], kwargs=dict(autosort=True, filter_chr=True), dependencies=[bg3mn_pid])
	pwpool.get(wait=True)
	pwpool.close()
	for tmpfile in tmpfiles + tmpfiles_bam:
		os.unlink(tmpfile)

@vt(description="Convert GROcap/PROcap/GROseq/PROseq bam file to bed files Returns 2 bed files with the 4th column as a comma separated list of RNA distances from TSS", 
	helps=dict(i="Input bam file", o="output bed file prefix. Two files, _dpl.bed.gz and _dmn.bed.gz are output",
			paired_end="True: paired-end sequencing; False: single-end sequencing",
			rna_strand="Indicate whether RNA strand is forward or reverse. In paired-end, forward represents that first read is 5'.",
			min_rna_len="Minimum RNA length to record",
			max_rna_len="Maximum RNA length to record"
			)
		)
@vc
def _process_PROcap_bam_to_TSS_RNA_len_20240423(i, o, paired_end, rna_strand, min_rna_len=0, max_rna_len=100000, target_chromosomes:str=None): 
	'''
	'''
	check_binaries_validity("bgzip")
	def _to_position(alignment):
		position = alignment.reference_end if alignment.is_reverse else (alignment.reference_start + 1)
		strand = "-" if alignment.is_reverse else "+"
		return (alignment.reference_name, position, strand)

	if not paired_end:
		raise Exception("Single-end not supported yet.")
	saved_reads = {}
	TSS_counter = nested_default_dict(3, list)
	with pysam.AlignmentFile(i) as samfh: 
		for alignment in samfh:
# 			if target_chromosomes is not None and alignment.reference_name not in target_chromosomes:
# 				continue
			if alignment.query_name in saved_reads:
				prev_alignment = saved_reads.pop(alignment.query_name)
				alignment1 = prev_alignment if prev_alignment.is_read1 else alignment
				alignment2 = prev_alignment if prev_alignment.is_read2 else alignment
				p1 = _to_position(alignment1) # read1: Pol
				p2 = _to_position(alignment2) # read2: TSS
				
				b = BEDPE(p1[0], p1[1] - 1, p1[1], p2[0], p2[1] - 1, p2[1], strand1 = p1[2], strand2 = p2[2])
				if (b.chrom1 == b.chrom2
					and (   (b.strand1 == "+" and b.strand2 == "-" and b.start1 <= b.start2 and b.stop1 <= b.stop2 and min_rna_len <= b.stop2 - b.start1 <= max_rna_len)
						 or (b.strand1 == "-" and b.strand2 == "+" and b.start2 <= b.start1 and b.stop2 <= b.stop1 and min_rna_len <= b.stop1 - b.start2 <= max_rna_len))):
					
					
					d = b.stop2 - b.start1 if b.strand1 == "+" else b.stop1 - b.start2
					if rna_strand == "forward":
						strand = b.strand1
						if strand == "+":
							TSS_counter[strand][b.chrom1][b.genomic_pos1.start].append(d)
						else:
							TSS_counter[strand][b.chrom1][b.genomic_pos1.stop].append(d)
					elif rna_strand == "reverse":
						strand = b.strand2
						if strand == "+":
							TSS_counter[strand][b.chrom1][b.genomic_pos2.stop].append(d)
						else:
							TSS_counter[strand][b.chrom1][b.genomic_pos2.start].append(d)
					else:
						raise Exception()

			else:
				saved_reads[alignment.query_name] = alignment
		for output_file, strand in zip([f"{o}_dpl.bed.gz", f"{o}_dmn.bed.gz"], ["+", "-"]):
			with BaseWriter(output_file) as bwd:
				regions = TSS_counter[strand]
				for r in sorted(regions.keys()):
					positions = regions[r]
					for p in sorted(positions.keys()):
						v = sorted(positions[p])
						bwd.write(f"{r}\t{p - 1}\t{p}\t{','.join(list(map(str, v)))}\n")
						
						


	
@vt(description="Modify bigwig files according to the func", 
helps=dict(i="Input bigwig file", o="Output bigwig file", func="Function to modify bigwig. Either a python function or a string to be evaluated as python lambda function. For example, to convert all positive values into negative values, 'lambda x: x * -1'")
													)

@vc
def _modify_bigwig_values_20240423(i:str, o:str, func:str):
	'''
	Extract all intervals that overlap with the selected regions
	'''
	if isinstance(func, str):
		func = eval(func, {}) # While unsafe to use eval, disable access to global variables to make it a little bit safer..
	input_bw = pyBigWig.open(i)
	def _get_pyBigWig_all_interval_generator(bw):
		for chrom in bw.chroms():
			if bw.intervals(chrom) is not None:
				for interval in bw.intervals(chrom):
					yield (chrom, *interval)
	output_bw = pyBigWig.open(o, "w")
	output_bw.addHeader(list(input_bw.chroms().items()))
	all_intervals = list(_get_pyBigWig_all_interval_generator(input_bw))
	chroms, starts, ends, values = safe_inverse_zip(all_intervals, 4)
	values = list(map(func, values))
	output_bw.addEntries(list(chroms), list(starts), ends=list(ends), values=list(values))
	output_bw.close()
	input_bw.close()
	
	
if __name__ == "__main__":
	main()

		
