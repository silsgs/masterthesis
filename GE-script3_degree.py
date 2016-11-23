import sys

#Definitions

path = '/Users/andromeda/Desktop/Project/'

file1 = path + 'Gene_expression/' + sys.argv[1]
file2 = path + 'Input_files/Ath_InterFull_TS.txt'

outfile = 'Degree_' + sys.argv[1].replace('Uniq_', '')

out = open(outfile, 'w')

out.write('#id\tmean\tstd\tdegree\n')

#READ File2
f2 = open(file2, 'r')
data = {}
for line in f2:
    if '#' in line:
		continue
    else:
        vec_line2 = line.strip().split('\t')
        AT = vec_line2[0]
        k = vec_line2[1]
        data[AT] = k
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
        degree = 'n/a'
        if ATt in data:
            out.write(ATt + '\t' + mean + '\t' + std + '\t' + data[ATt] + '\n')
        else:
            out.write(ATt + '\t' + mean + '\t' + std + '\t' + degree + '\n')

#close
f1.close()
out.close()
