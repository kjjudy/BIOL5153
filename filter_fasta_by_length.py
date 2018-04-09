#! /usr/bin/env python3

#filter .fasta by length
#load the required modules
import argparse
from Bio import SeqIO

#create an ArgumentParser object ('parser') that will hold all the info to parse the command line
parser=argparse.ArgumentParser(description="This script filters out sequences from a FASTA file that are shorter than a user-specified length cutoff")

#add arguments (two types: required [positional-when/where they are entered in the command line is meaningful] vs optional 
#positional arguments added with add.argument() method
#argparse treats all options as strings by default
parser.add_argument("fasta", help="name of FASTA file")

#add an optional argument of the length cutoff
parser.add_argument("-m", "--lengthMin",help="filter sequences that are <= lengthMin in length (default=300nt)", type=int, default=300)


#parse the arguments
args=parser.parse_args()

#grab the values
print("We're going to open this FASTA file:", args.fasta)
print("filter sequences less than", args.lengthMin, "nt in length")
