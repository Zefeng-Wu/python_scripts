#! /usr/bin/python
import re
from Bio import SeqIO

rgx = "[KR]{3,4}.{1,6}[LI].[LI]"
pattern = re.compile(rgx)
#seq = "MKRKTTIELAMYSGGT"

records = list(SeqIO.parse("/home/wuzefeng/Desktop/StPP2C.fasta","fasta"))
for record in records:
    seq_id = record.id
    seq = str(record.seq)
    for match in pattern.finditer(seq):
        print(seq_id,match.group(),match.span())
        