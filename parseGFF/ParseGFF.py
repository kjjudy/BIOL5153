#! /usr/bin/env python3

#columns 4-5 are start-end in .gff
#read in and store genome (.fasta) using SeqIO
from Bio import SeqIO
for genome in SeqIO.parse("/Users/kathrynjudy/Desktop/watermelon_files/watermelon.fsa", "fasta"):
    #set variable
    genome=genome.seq
    #print(genome.seq) to test path (or command-line input, eventually)
#open .gff file
file=open("/Users/kathrynjudy/Desktop/watermelon_files/watermelon.gff")
#give list input each line of .gff file
for line in file:
#split each line into lists of strings at the tab 
    list=line.split("\t")

#print some "header info"? (organism name, intron/exon, etc in .fasta style)


#print data from genome at coordinates
    print(genome[(int(list[3])-1):(int(list[4])-1)])
#close .gff file
file.close()
