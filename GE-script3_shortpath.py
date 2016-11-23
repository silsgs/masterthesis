#Average Shortest Path Length

import sys

#Definitions

path = '/Users/andromeda/Desktop/Project/'

file1 = path + 'Gene_expression/' + sys.argv[1] #Uniq_genes_expression.txt
file2 = path + 'Input_files/Ath_InterFull_TS.txt' #Full Interactome

outfile = 'ShortPath_' + sys.argv[1].replace('Uniq_', '')

out = open(outfile, 'w')

out.write('#id\tmean\tstd\tAverageShortestPath\n')

#READ File2
f2 = open(file2, 'r')
data = {}
for line in f2:
    if '#' in line:
		continue
    else:
        vec_line2 = line.strip().split('\t')
        AT = vec_line2[0]
        spath = vec_line2[5]
        data[AT] = spath
f2.close()

#READ File1
f1 = open(file1, 'r')

for line in f1:
    if '#' in line:
		continue
    else:
        vec_line1 = line.strip().split('\t')
        ATt = vec_line1[0]
        mean = vec_line1[1]
        std = vec_line1[2]
        spath = 'n/a'
        if ATt in data:
            out.write(ATt + '\t' + mean + '\t' + std + '\t' + data[ATt] + '\n')
        else:
            out.write(ATt + '\t' + mean + '\t' + std + '\t' + spath + '\n')

#close
f1.close()
out.close()
