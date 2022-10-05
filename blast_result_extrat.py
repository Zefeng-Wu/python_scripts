#!/bin/python

from Bio import SeqIO
import sys


Blast_out_file = sys.argv[1]
target_species_prots = "proteins/"+Blast_out_file.replace("MT_NIN2","").replace(".txt","")+".fasta"
print (target_species_prots)
record = SeqIO.to_dict(SeqIO.parse(target_species_prots,"fasta"))
print (len(record))


outfile_fa = open("2Nin_proteins/"+Blast_out_file.replace("MT_NIN2","").replace(".txt","")+"_nin.fa","w")
 
target_seq = []
with open(Blast_out_file) as fh:
	for row in fh:
		if row.startswith("#"):
			continue
		else:
			data = row.strip().split("\t")
			if data[1] not in target_seq:
				target_seq.append(data[1])
				SeqIO.write(record[data[1]],outfile_fa,"fasta")
print (target_seq)				
