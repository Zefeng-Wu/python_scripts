#coding:utf-8
from Bio import SeqIO
from Bio.Seq import Seq
from optparse import OptionParser

parser=OptionParser()
parser.add_option("-f","--file", dest="genome_file", help="input your genome file", metavar="FIIL")
parser.add_option("-i","--chrom",dest="chr_id", help="input chromosome id", metavar="CHROMOSOME")
parser.add_option("-s","--start", dest="seq_start", help="input seq start", metavar="START")
parser.add_option("-e","--end", dest="seq_end", help="input seq end postion",metavar="END")
parser.add_option("-d","--direct",dest="seq_direct",help="Input direct of seq(pos or neg)",metavar="DIRECT")
(options,args)=parser.parse_args()

genome=SeqIO.to_dict(SeqIO.parse(options.genome_file,'fasta'))
chromosome=str(options.chr_id)
start=int(options.seq_start)
end=int(options.seq_end)
strand=str(options.seq_direct)

if strand=="pos":
    print(str(genome[chromosome].seq[start:end]))
else:
    print(str(Seq.reverse_complement(genome[chromosome].seq[start:end])))
