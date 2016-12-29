import sys

fast_infile = sys.argv[1]
f = open(fast_infile,'r')

seq_dict = {}
lines = f.readlines()

for line in lines:
    if line.lstrip().startswith('>'):
        h = line.strip().strip('>')
        seq_dict[h] = ''
    else:
        if len(line.strip())!=0:
            seq_dict[h] += line.strip()

print len(seq_dict)