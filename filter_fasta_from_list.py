#! /usr/bin/env python3

#filters out FASTA files based on header info (exact matches), prints the rest to STDOUT
#load the modules
import argparse
from Bio import SeqIO

#create an ArgumentParser object ('parser') to hold all info from command line
parser=argparse.ArgumentParser(description="This script filters out sequences from a FASTA file that match sequence identifiers and prints the remaining sequences in FASTA format")

#add argument to accept FASTA file
parser.add_argument("fasta", help="name of FASTA file, must be first argument")

#add argument to accept file of sequence identifiers
parser.add_argument("seqIDs", help="name of file containing list of sequence identifiers. Must be second argument")

#parse the arguments
args=parser.parse_args()

#grab the values
print("We're going to open this FASTA file:", args.fasta)
print("Sequences with identifiers from the list", args.seqIDs, "will not be printed")

#print sequences not listed to STDOUT:

#create list of seqIDs values
IDs=open(args.seqIDs).read().splitlines()

#print files that do not match the list
for sequence in SeqIO.parse(args.fasta,"fasta"):
    if sequence.id not in IDs:
    #print files by sequence.id using SeqIO
        print(sequence.format("fasta"))
