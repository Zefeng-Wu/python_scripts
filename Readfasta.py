def Read_fasta(fa_file):
    seq = {}
    with open(fa_file) as fh:
        for row in fh:
            data = row.strip()
            if data == "":
                continue
            if data.startswith(">"):
                header = data.lstrip(">")
                seq[header]=""
            else:
                seq[header]+=data
    return(seq)

print Read_fasta("test.fa")


                
