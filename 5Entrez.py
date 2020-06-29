#!/bin/python
from Bio import Entrez
from Bio import SeqIO
#---------get pubmed information---------------------------
'''Entrez.email = "examle@mail.com"
search_handle = Entrez.esearch(db="pubmed",term="biopython")
record = Entrez.read(search_handle)
query_pubmed_id =  record['IdList'][0]
print query_pubmed_id

entrez_handle = Entrez.efetch(db="pubmed",id=query_pubmed_id)
print entrez_handle.geturl()
'''
#---------search nucleic squence information and fetch it--

Entrez.email = "example@mail.com"
search_handle = Entrez.esearch(db="nucleotide",term="p53")
record = Entrez.read(search_handle)
print record['IdList']

entrez_handle = Entrez.efetch(db="nucleotide",id=record['IdList'],rettype="fasta")
records=list(SeqIO.parse(entrez_handle,'fasta'))
print len(records)
print records[0].id
