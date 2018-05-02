#! /usr/bin/env python3

#this script will parse a GFF file, extracting sequences for the annotated features

#import modules
import sys
import os
import re
import argparse
from Bio import SeqIO
from collections import defaultdict
#define functions

#write function to take specific command-line input with argparse
def get_args():
	#create ArgumentParser object to hold all info
	parser=argparse.ArgumentParser(description="This script writes out individual genes from a .fasta genome based on locations specified in a GenBank .gff file. The reverse complement of genes on the - strand are given.")

	#add arguments
	parser.add_argument("fasta",help="name of FASTA file, must be the first argument. Input the full path name if the file is not in current working directory.")
	parser.add_argument("gff",help="name of GFF file, must be the second argument. Input the full path name if file is not in current working directory.")

	#parse the arguments
	return parser.parse_args()

#write function to parse fasta file
def fasta_parse(fasta):
	#read in and return genome (.fasta) using SeqIO
# for single-sequence fasta:
	genome = SeqIO.read(fasta,"fasta")
	return genome.seq
#for multi-sequence fasta: (set as condition later)
	#for genome in SeqIO.parse(fasta,"fasta"):
		#return genome.seq

#write function to parse GFF file
#variables should be defined relative to other functions in main
def gff_parse(f,g):

	#open .gff file
	file=open(g)

	#make dictionary to fill with names,sequence_lists (k,v)
	data=defaultdict(list)

	#make list for gene names (to build lists from)
	list_list=[]

	#give list input each line of .gff file
	for line in file:
		#split each line into lists of strings at the tab
		(seqid, source, feature, start, end, length, strand, frame, attributes)=line.split("\t")

		#pull out exons for further processing:
		if(feature=="CDS" or feature=="tRNA" or feature=="rRNA"):
			atts=attributes.split(" ; ")
			gene_name=re.search("^Gene\s+(\S+)" , atts[0])
			#exon=re.search("exon\s+(\d+)")

			g_name=gene_name.group(1)
		#make list for exon position value(s) (or not if preexisting)

			if strand == "+":
				list_list.append((g_name, f[(int(start)-1):(int(end))]))

			else:
				list_list.append((g_name, rev_comp(f[(int(start)-1):(int(end))])))

	for gene, sequence in list_list:
		data[gene].append(sequence)


	return data,seqid

		#close .gff file
	file.close()

#write function that calculates reverse complement
def rev_comp(DNAseq):
	#turn object into string and ensure all DNA is uppercase
	dna=str(DNAseq.upper())

	#change bases to lowercase complement
	a_comp=(dna.replace("A", "t"))
	t_comp=(a_comp.replace("T", "a"))
	c_comp=(t_comp.replace("C", "g"))
	g_comp=(c_comp.replace("G", "c"))

	#return to uppercase
	dna_comp=g_comp.upper()

	#return reverse complement
	return dna_comp[::-1]

#write function to print pieces
def seqprint(data,seqid):
	for gene,sequences in data.items():
		print(">"+seqid.replace(" ","_")+"_"+gene)
		print(sequences)

#define main function (connects all the modular pieces)
def main():
	genome=fasta_parse(args.fasta)
	dictionary,seqname=gff_parse(genome,args.gff)
	seqprint(dictionary,seqname)

#call command-line arguments
args=get_args()

#run main function
main()
