#! /bin/python

import urllib2
from bs4 import BeautifulSoup

kegg_list = []
kegg_anno = []
Mt_pathway_kegg_page = 'https://www.genome.jp/dbget-bin/get_linkdb?-t+pathway+gn:T01716'

page = urllib2.urlopen(Mt_pathway_kegg_page)
soup = BeautifulSoup(page, 'html.parser')

data = soup.find('pre').text  #findChildren():
lines = data.splitlines()[2:]
for line in lines:
  items = line.strip().split()[0]
  anno =  line.strip().split(None,1)[1]
  kegg_list.append(str(items))
  kegg_anno.append(str(anno))
  
print len(kegg_list)
print len(kegg_anno)

outfile = open("Mt_kegg.txt","w")
for pathway in kegg_list:
  pathway_gene_page = 'https://www.genome.jp/dbget-bin/get_linkdb?-t+genes+path:' + pathway
  page = urllib2.urlopen(pathway_gene_page)
  soup = BeautifulSoup(page, 'html.parser')

  data = soup.find('pre').text  #findChildren():
  lines = data.splitlines()
  for line in lines:
    outfile.write(pathway+"\t"+kegg_anno[kegg_list.index(pathway)]+"\t"+line.strip()+"\n")
  

print 'ok'


