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

	#create lists for adding values
	header=[]
	body=[]

	#give list input each line of .gff file
	for line in file:
		#split each line into lists of strings at the tab
		list=line.split("\t")
		attribute=list[8].split(";")
		gene_info=attribute[0].split()
		#gene_name=gene_info[1], intron/exon=gene_info[2:3] but not always present-write as if/else to prevent code failure

		header.append(">"+list[0]+"_"+gene_info[1])
		body.append(rev_comp_test(list,genome))

	length=len(header)

	return header,body,length
#currently quits after one iteration of for loop bc of return... how to fix?

		#close .gff file
	file.close()

#write function to calc reverse complement if needed
def rev_comp_test(list,genome):
#not fixed if list[6] is made into a variable, or if moved above prev
	#determine if strand is + or -, calculate reverse complement of - strand nt
	if list[6] == "+":
		return genome[(int(list[3])-1):(int(list[4])-1)]
	else:
		reverse_complement=rev_comp(genome[(int(list[3])-1):(int(list[4])-1)])
		return reverse_complement

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
	header,body,length=gff_parse(args.fasta,args.gff)
	for i in range(length):
		print(header[i])
		print(body[i])

#call command-line arguments
args=get_args()

#run main function
main()
