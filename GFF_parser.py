from BCBio import GFF
infile=open(r'TAIR10_GFF3_genes.gff','r')
outfile=open(r'snRNA.txt','w')
limit_info = dict(
        gff_id = ["Chr1"],
        gff_type = ["snRNA"])
handle=GFF.parse(infile,limit_info=limit_info)
for record in handle:
	for items in record.features:
		outfile.write(record.id+'\t'+str(items.location)+'\n')
infile.close()
