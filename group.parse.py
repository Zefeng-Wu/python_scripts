#!/bin/python

import numpy as np
n_species=7
group_number = 31333
matrix = np.zeros(shape=(group_number,n_species)) #define matrix 


name_list=["maize","rice","tair","sbicolor","castor","lyrata","sly"]
group_count=0
with open("groups.txt") as fh:
    for row in fh:
        data= row.strip().split()
        for species in name_list:
            matrix[group_count,name_list.index(species)]+= len([m.startswith(species) for m in data if m.startswith(species) is True])
        group_count+=1
        
#print matrix[1:50]
np.savetxt("group.stat", matrix, delimiter='\t', fmt='%.2f')
print "OK"
        
