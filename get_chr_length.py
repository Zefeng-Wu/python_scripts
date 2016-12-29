def get_chromsomose_lengths(reference_filename):
    chr_id = []
    chr_length = []
    length = None
    with open(reference_filename) as fh:
        for row in fh:
            if row.startswith(">"):
                chr_name = row[1:].strip() # Can be modified
                chr_id.append(chr_name)
                if length is not None:     # test not the first chromsome
                    chr_length.append(length)
                length = 0
            else:
                length += len(row.strip())
        chr_length.append(length) # get the last chromosome length        
    return (chr_id,chr_length)

print (get_chromsomose_lengths("test.fasta"))