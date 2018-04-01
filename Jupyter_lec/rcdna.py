#! /usr/bin/env python3

dna0="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

dna=dna0.upper()
print("original "+dna)

dna2=dna.replace("A","t")
dna3=dna2.replace("C","g")
dna4=dna3.replace("T","a")
dna5=dna4.replace("G","c")

rcdna=dna5.upper()

ccont1=dna.count("C")
gcont1=dna.count("G")
acont1=dna.count("A")
tcont1=dna.count("T")

ccont2=rcdna.count("C")
gcont2=rcdna.count("G")
acont2=rcdna.count("A")
tcont2=rcdna.count("T")

total1=len(dna)
total2=len(rcdna)

GC1or=(ccont1+gcont1)/total1

print("GC content of original is "+str("%.4f" % GC1or))

GC2or=(ccont2+gcont2)/total2

print(" ")
print("reverse "+rcdna)
print(" ")
print("reverse complement "+rcdna[::-1])
print("GC content of reverse complement is "+str("%.4f" % GC2or))
