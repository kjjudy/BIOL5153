#! /usr/bin/env python3

#columns 4-5 are start-end in .gff
#import modules
import argparse
from Bio import SeqIO

#setup command-line argument input for module use with argparse
#create ArgumentParser object to hold all info
parser=argparse.ArgumentParser(description="This script writes out individual genes from a .fasta genome based on locations specified in a GenBank .gff file")

#add arguments
parser.add_argument("fasta",help="name of FASTA file, must be the first argument. Input the full path name if the file is not in current working directory.")
parser.add_argument("gff",help="name of GFF file, must be the second argument. Input the full path name if file is not in current working directory.")

#parse the arguments
args=parser.parse_args()

#read in and store genome (.fasta) using SeqIO
for genome in SeqIO.parse(args.fasta, "fasta"):
   	#set variable
	genome=genome.seq

#open .gff file
file=open(args.gff)

#give list input each line of .gff file
for line in file:

#split each line into lists of strings at the tab 
	list=line.split("\t")
	print(">"+list[0])
	print(genome[(int(list[3])-1):(int(list[4])-1)])
#print some "header info" (organism name, intron/exon, etc in .fasta style)

#print data from genome at coordinates

#close .gff file
file.close()
