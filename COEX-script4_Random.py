#generar numeros random para crear una lista nueva de combinaciones aleatorias de genes

import sys
import random
path = '/Users/andromeda/Desktop/Project/'

input_file = path + 'Input_files/' + sys.argv[1] #interact global
output_file = path + 'Coexpression_analysis/Temporary_files/Random_coexpression_genes.txt'

in_f = open(input_file, 'r')
out_f = open(output_file, 'w')

atlist = []

for line in in_f:
    if '#' in line:
        continue
    else:
        line = line.strip().split('\t')
        atlist.append(line[0])

for M in list(range(0, 720000)):
    i = random.randrange(1, 23139)
    j = random.randrange(1, 23139)
    out_f.write(atlist[i] + '\t' + atlist[j] + '\n')

in_f.close()
out_f.close()
