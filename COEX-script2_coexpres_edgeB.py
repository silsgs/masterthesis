#Combinar fichero coexpresion(Temp1)
#asociar valores de edgeBetweeness de las interacciones del interactoma
import sys

path = '/Users/andromeda/Desktop/Project/'

input_file1 = path + 'Coexpression_analysis/Temporary_files/' + sys.argv[1]
input_file2 = path + 'Input_files/Ath_InterFull_edgesTS.txt'

out_file = path + 'Coexpression_analysis/Temporary_files/' + sys.argv[1].replace('.txt', '_edgesTS.txt')

#Opens
in_f1 = open(input_file1, 'r')
in_f2 = open(input_file2, 'r')

out_f = open(out_file, 'w')

#Processing file1
data = {}

for line in in_f1:
    line = line.strip().split('\t')
    i = line[0]
    j = line[1]
    data[i] = j
    #print line
#print data

#Processing file2

for line in in_f2:
    line = line.replace('   ','\t')
    line = line.strip().split('\t')
    if len(line) == 3:
        if line[1] in data.keys():
            if data[line[1]] == line[2]:
                #print 'yes'
                out_f.write(line[0] + '\t' + line[1] + '\t' + line[2] + '\n')

in_f1.close()
in_f2.close()
out_f.close()
