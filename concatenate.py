#!/usr/bin/python

from Bio import AlignIO
import glob

filelist = glob.glob('./*.phy')
i = 0
for file in filelist:
  print file
  alignment = AlignIO.read(file, "phylip-relaxed")
  alignment.sort()  # sort the sequence identifiers so they match in all files
  print("Alignment of length %i" % alignment.get_alignment_length())
  if i==0:
    cat_algn = alignment
  else:
    cat_algn += alignment
  i += 1

print "Concatenated:"
print("Alignment of length %i" % cat_algn.get_alignment_length())

outfh = open("superalgn.phy", "w")
AlignIO.write(cat_algn, outfh, "phylip-relaxed")

outfh.close()


