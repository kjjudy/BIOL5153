#! /usr/bin/env python3

#filters out FASTA files based on header info (exact matches), prints the rest to STDOUT
#load the modules
import argparse
from Bio import SeqIO
from io import StringIO

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

#build index of records from FASTA file (accessible by record.id)
record_dict = SeqIO.index(args.fasta, "fasta")

#create list of seqIDs values
IDs=open(args.seqIDs).readlines()

#determine number of times to iterate over list
n=len(IDs)

#create an empty list to fill with sequence.id values
SeqList=[]

#fill list with values
for sequence in SeqIO.parse(args.fasta,"fasta"):
    SeqList.append(sequence.id)

    #based on number of IDs in seqIDs file, iterate over IDs in seqID list
    for i in range(n):
        if sequence.id == IDs[i]:
            SeqList.remove(sequence.id)

#print remaining FASTA files by their sequence.id using SeqIO
for record in SeqList:
    #pull record info from index by identifier remaining in list
    data=record_dict[record]

    #write output into FASTA format
    out_handle=StringIO()
    SeqIO.write(data, out_handle, "fasta")
    fasta_data=out_handle.getvalue()
    print(fasta_data)

#WHY DOESNT THIS WORK

#close index
record_dict.close()
