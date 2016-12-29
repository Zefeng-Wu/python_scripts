from BCBio import GFF
from Bio import SeqIO
from optparse import OptionParser
import fileinput,time

parser=OptionParser()
parser.add_option("-a","--annotation",dest="GFF3_annotation_file",help="Please input your gff3 file",metavar="GFF3")
parser.add_option("-g","--genome",dest="genome_file",help="Please input your genome file(.fa)",metavar="GENOME")
parser.add_option("-e","--element",dest="gene_element",help="Chooose gene element('CDS','gene')",metavar="ELEMENT")
(options,agrs)=parser.parse_args()

GFF_file=options.GFF3_annotation_file
genome_file=options.genome_file
gene_element=options.gene_element

gff3_infile=fileinput.input(GFF_file)
genome_records=list(SeqIO.parse(genome_file,"fasta"))

outfile_name=gene_element+"_sequences"
outfie=open(outfile_name,'w')

limit_info = dict(gff_type = [gene_element])
handle=GFF.parse(gff3_infile,limit_info=limit_info)
for record in handle:
	for items in record.features:
		if record.id[-1]=="C":
			chr_num=5
		if record.id[-1]=="M":
			chr_num=6
		else:
			chr_num=int(record[-1]-1)
		start=int(items.location.start.position)
		end=int(items.location.start.position)
		outfile.write(">"+record.id+items.id+'\n'+str(genome_records[chr_num].seq[start:end]+'\n'))		
infile.close()
