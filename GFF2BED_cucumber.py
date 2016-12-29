#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<>
  Purpose: calculate the repeat elements in genes and other elements
  Created: 2015年05月08日
"""
import time
from collections import defaultdict

genes = []
genes_info = {}

with open('/media/wuzefeng/MY_DISK/gff2bed/cucumber_v2.gff3','r') as fh:
    for row in fh:
        data = row.strip().split('\t')
        if len(data)<9:
            break
        
        if data[2] =='gene':  # get the protein coding gene list
            gene_id = data[8].split(';')[0].split('=')[1].replace("G","M")
            gene_start = data[3]
            gene_end = data[4]
            gene_strand = data[6]
            genes.append(gene_id)
            genes_info[gene_id] = [data[0],gene_start,gene_end,gene_strand]
            
print len(genes)

transcripts = defaultdict()
for gene in genes:
    transcripts[gene]=[]
    
with open('/media/wuzefeng/MY_DISK/gff2bed/cucumber_v2.gff3','r') as fh:
    for row in fh:
        data = row.strip().split('\t')
        if len(data)<9:
            break
        
        if data[2] =='mRNA':
            parent_gene = data[8].split(';')[1].split('=')[1].replace("G","M")
            transcript_id = data[8].split(';')[2].split('=')[1]
            transcript_length= int(data[4])-int(data[3])+1
            #print parent_gene, transcript_id
            transcripts[parent_gene].append([transcript_id,transcript_length]) # get the transcripts of each gene
            
for gene in transcripts.keys():
    transcripts[gene] = sorted(transcripts[gene],key= lambda x:x[1])[0] # get the longest transcript for each gene
    #print gene, transcripts[gene]

transcripts_exons = defaultdict()# output transcript with several exons 
for gene in transcripts.keys():
    transcripts_exons[transcripts[gene][0]]=[]
    #print transcripts[gene][0]
    

with open('/media/wuzefeng/MY_DISK/gff2bed/cucumber_v2.gff3','r') as fh:
    for row in fh:
        data = row.strip().split('\t')
        if len(data)<9:
            break    

        if data[2] =='exon':
            parent_transcript = data[8].split(';')[1].split('=')[1]
            exon_start = int(data[3])
            exon_end = int(data[4])
            if parent_transcript in transcripts_exons.keys():   #slow
                transcripts_exons[parent_transcript].append([exon_start,exon_end,exon_end-exon_start+1])
               # print transcripts_exons[parent_transcript]#[[1879518, 1879568, 51], [1879821, 1879964, 144], [1880168, 1880303, 136], [1880351, 1880395, 45], [1880493, 1880718, 226], [1880818, 1880871, 54]]
for key in transcripts_exons.keys():
    #print key, transcripts_exons[key]
    gene_info = genes_info[key.split('.')[0]]
    total_exons_len = sum([ a[2] for a in transcripts_exons[key]])
    first_exon_start = sorted(transcripts_exons[key],key= lambda x:x[0])[0][0]
    last_exon_end = sorted(transcripts_exons[key],key= lambda x:x[0])[-1][-2]
    exon_len_list = [str(length[2]) for length in transcripts_exons[key]]
    exon_relative_start_list = [str(m[0]-first_exon_start) for m in transcripts_exons[key]]
    print '\t'.join([gene_info[0],gene_info[1],gene_info[2],key, str(total_exons_len), gene_info[3],str(first_exon_start),str(last_exon_end),'0',str(len(transcripts_exons[key])), ','.join(exon_len_list), ','.join(exon_relative_start_list)])



              

            
            