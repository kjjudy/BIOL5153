#! /usr/bin/env python3

#this script will parse a GFF file, extracting sequences for the annotated features

#import modules
import sys
import os
import re
import argparse
from Bio import SeqIO

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

	#create lists for adding values
	#header=[]
	#body=[]

	#give list input each line of .gff file
	for line in file:
		#split each line into lists of strings at the tab
		(seqid, source, feature, start, end, length, strand, frame, attributes)=line.split("\t")
		#list=line.split("\t")
		#attribute=attributes.split(" ; ")
		#gene_info=attribute[0].split()
		#gene_name=gene_info[1], intron/exon=gene_info[2:3] but not always present-write as if/else to prevent code failure
		#pull out exons for further processing:
		if(feature=="CDS" or feature=="tRNA" or feature=="rRNA"):
			atts=attributes.split(" ; ")
			gene_name=re.search("^Gene\s+(\S+)" , atts[0])
			exon=re.search("exon\s+(\d+)")
			if(gene_name and exon):
				print(">"+seqid.replace(" ","_")+"_"+gene_name.group(1)+"_"exon.group(1))
				#header.append(">"+seqid.replace(" ","_")+"_"+gene_name.group(1)+"_"exon.group(1))
			else:
				print(">"+seqid.replace(" ","_")+"_"+gene_name.group(1))
				#header.append(">"+seqid.replace(" ","_")+"_"+gene_name.group(1))

			if strand == "+":
				print(f[(int(start)-1):(int(end)])

			else:
				print(rev_comp(genome[(int(start)-1):(int(end)])
			#body.append(rev_comp_test(start,end,strand,f))
		#header.append(">"+list[0]+"_"+gene_info[1])
		#body.append(rev_comp_test(list,genome))

	length=len(header)

	#return header,body,length
	return length
#currently quits after one iteration of for loop bc of return... how to fix?

		#close .gff file
	file.close()

#write function to calc reverse complement if needed
#def rev_comp_test(start,end,strand,genome):
#not fixed if list[6] is made into a variable, or if moved above prev
	#determine if strand is + or -, calculate reverse complement of - strand nt
	#if strand == "+":
		#return genome[(int(start)-1):(int(end)]
	#else:
		#reverse_complement=rev_comp(genome[(int(start)-1):(int(end)])
		#return reverse_complement

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

#define main function (connects all the modular pieces)
def main():
	genome=fasta_parse(args.fasta)
	parse_gff()
	#header,body,length=gff_parse(genome,args.gff)

	#for i in range(length):
		#print(header[i])
		#print(body[i])

#call command-line arguments
args=get_args()

#run main function
main()
