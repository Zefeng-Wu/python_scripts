from Bio import SeqIO
records = list(SeqIO.parse('/home/wuzefeng/Desktop/Genome/Arabidopsis/CpGIslands/Arabidopsis_thaliana.TAIR10.26.dna.toplevel.fa','fasta'))
for record in records: 
    print record.id
    outfile = open(record.id+'.fa','w')
    SeqIO.write(record,outfile,"fasta")
    outfile.close()
print 'ok'

