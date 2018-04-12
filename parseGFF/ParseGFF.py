#! /usr/bin/env python3

#currently only returns first "header" ... why?
#issue probably within rev_comp_test

#import modules
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

#write function to parse GFF file
#variables should be defined relative to other functions in main
def gff_parse(f,g):
	#read in and store genome (.fasta) using SeqIO
	for genome in SeqIO.parse(f, "fasta"):
   		#set variable
		genome=genome.seq

	#open .gff file
	file=open(g)

	#give list input each line of .gff file
	for line in file:
		#split each line into lists of strings at the tab
		list=line.split("\t")
		attribute=list[8].split(";")
		gene_info=attribute[0].split()
		#gene_name=gene_info[1], intron/exon=gene_info[2:3] but not always present-write as if/else to prevent code failure

		#provide FASTA style header- >organism gene (more later)
		return ">"+list[0]+"_"+gene_info[1]

		#return nt sequence or reverse complement (uses following function)
		return rev_comp_test(list,genome)

		#close .gff file
	file.close()

#write function to calc reverse complement if needed
def rev_comp_test(list,genome):
#not fixed if list[6] is made into a variable, or if moved above prev
	#determine if strand is + or -, calculate reverse complement of - strand nt
	if list[6] == "+":
		return genome[(int(list[3])-1):(int(list[4])-1)]
	else:
		rev_comp=reverse_complement(genome[(int(list[3])-1):(int(list[4])-1)])
		return rev_comp

#define main function (connects all the modular pieces)
def main():
	print(gff_parse(args.fasta,args.gff))

#call command-line arguments
args=get_args()

#run main function
main()
