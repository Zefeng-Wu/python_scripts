import re,string,time,sys,operator
from operator import itemgetter, attrgetter
from Bio import SeqIO
from optparse import OptionParser

parser=OptionParser()
parser.add_option("-s","--seq",dest = "seq_name",help= "Input  sequence file formatted in fasta",metavar = "sequence")

parser.set_defaults(regex_expression = '([gG]{3,}\w{1,7}){3,}[gG]{3,}')
parser.add_option("-r","--regex",dest = "regex_expression",help = "Regex to be searched in the fasta file\t[([gG]{3,}\w{1,7}){3,}[gG]{3,}]",metavar = "regex")

parser.set_defaults(outfile_name = "G4.OUT")
parser.add_option("-o","--out",dest = "outfile_name",help = "Please set a outfile name",metavar = "out")
(options,args)=parser.parse_args()

seq_file = str(options.seq_name)
outfile_name = str(options.outfile_name) 
outfile = open(outfile_name,'w')
regex = str(options.regex_expression)

print("The sequence file name is :  %s"%(seq_file))
print("The regular expression is :  %s"%(regex))
print("The outfile name is :  %s"%(outfile_name))
start=time.time()

chr_len=[]
records=list(SeqIO.parse(seq_file,"fasta"))
count=0

def compl_seq(sequence):      # define a reverse_complement function
    sequence = sequence.upper()
    c_sequence = sequence.translate(string.maketrans("ATCG", "TAGC"))
    return c_sequence;

def G4_Classifier(G4_motif):    
    loop=re.compile('[G]{3,}')
    tract=re.compile('[G]{3,}')
    G_tract = []         # list of length of each G_tract in a G4-motif
    G_tracts_num = 0 
    list_loops =[]       # list of length of each loop in a G4-motif
    loops = loop.finditer(G4_motif)
    tracts = tract.finditer(G4_motif)
    G_pos=[]
    if G4_motif.count('G') != len(G4_motif): 
        for n in tracts:
            G_tract.append(n.end()-n.start())
            G_tracts_num +=1
            G_pos.append([n.start(),n.end()])                  
    else:
        G_tracts_num = 1     #GGG repeat numbers
        G_tract = [len(G4_motif)]
        list_loops = [0]
	
    for i  in range(len(G_pos)-1):
	list_loops.append(G_pos[i+1][0]-G_pos[i][1]) 
    return [G_tracts_num,max(G_tract),min(G_tract),max(list_loops),min(list_loops)]

def C4_Classifier(C4_motif):
    loop=re.compile('[C]{3,}')
    tract=re.compile('[C]{3,}')
    C_tract = []
    C_tracts_num = 0
    list_loops = []
    loops = loop.finditer(C4_motif)
    tracts = tract.finditer(C4_motif)
    C_pos=[]
    if C4_motif.count('C')!=len(C4_motif):
        for n in tracts:
            C_tract.append(n.end()-n.start())
            C_tracts_num += 1
	    C_pos.append([n.start(),n.end()])
    else:
        C_tracts_num = 1
        C_tract = [len(C4_motif)]
        list_loops = [0]
    for i  in range(len(C_pos)-1):
	list_loops.append(C_pos[i+1][0]-C_pos[i][1])    
    return [C_tracts_num,max(C_tract),min(C_tract),max(list_loops),min(list_loops)]

col_list = [] 
for i in records:
    aa = re.compile(regex)
    bb = aa.finditer(str(i.seq.upper()))
    cc = aa.finditer(compl_seq(str(i.seq.upper())))
    for n in bb:
	col_list.append([i.id,n.start(),n.end(),"+",n.end()-n.start(),n.group()]+G4_Classifier(n.group()))   #group:G4-motif sequence
    for m in cc:
	col_list.append([i.id,m.start(),m.end(),"-",m.end()-m.start(),compl_seq(m.group())]+C4_Classifier(compl_seq(m.group())))	
out_items=['Chr_ID','start','end','strand','length','sequence','C/G_runs_counts','max_C/G-runs_length','min_C/G-runs_length','max_loops_length','min_loops_length']
outfile.write('\t'.join(out_items)+'\n')	
table_sorted = sorted(col_list,key = itemgetter(0,1,2))
for line in table_sorted:
    line = '\t'.join([str(x) for x in line])
    outfile.write(line+'\n')    
outfile.close()
elapsed = time.time()-start
print("Time used : %.2f s"%(elapsed))
print('Finished !')
