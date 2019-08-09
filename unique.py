infile = open("test.txt")

temp_parent_info = ""
temp_noncoding_info = ""

outfile = open("out","w")
with open("test.txt","r") as fh:
    for row in fh:
        data = row.strip().split("\t")
        #print data
        if (data[0]+data[1]+data[2]+data[3])==temp_parent_info and data[4]+data[5]+data[6]==temp_noncoding_info:
            continue
        else:
            outfile.write("\t".join(data)+"\n")
            temp_parent_info = data[0]+data[1]+data[2]+data[3]
            temp_noncoding_info = data[4]+data[5]+data[6]
print 'ok'
