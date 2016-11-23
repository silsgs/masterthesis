#CONSTRUIMOS fichero a partir con datos media de la expresion genica
#desviacion de la media de expresion(std), coeficiente de volatilidad,
# y propiedades topologicas: k, l y C

import sys

path = '/Users/andromeda/Desktop/Project/'

in_file1 = path + 'Volatility_analysis/Temporary_files/' + sys.argv[1]
in_file2 = path + 'Input_files/Ath_InterFull_TS.txt'
out_file = path + 'Volatility_analysis/Temporary_files/Uniq_genes_expression_volatility_topo.txt'

in_f1 = open(in_file1, 'r')
in_f2 = open(in_file2, 'r')
out_f = open(out_file, 'w')

out_f.write('#id\tmean\tVolatilityCoefficient\tDegree\tAverageShortestPathLength\tClusteringCoefficient\n')


def ParseFile1(in_f1):
    data_mean = {}
    data_vcoeff = {}
    atlist1 = []
    for line in in_f1:
        if '#' in line:
            continue
        else:
            line = line.strip().split('\t')
            id = line[0]
            atlist1.append(id)
            mean = line[1]
            vcoeff = line[3]
            data_mean[id] = mean
            data_vcoeff[id] = vcoeff
    return data_mean, data_vcoeff, atlist1

def ParseFile2(in_f2):
    data_k = {}
    data_l = {}
    data_C = {}
    atlist2 = []
    for line in in_f2:
        if '#' in line:
            continue
        else:
            line = line.strip().split('\t')
            id = line[0]
            atlist2.append(id)
            k = line[1]
            l = line[5]
            C = line[6]
            data_k[id] = k
            data_l[id] = l
            data_C[id] = C
    return data_k, data_l, data_C, atlist2


DataFile1 = ParseFile1(in_f1)
data_mean = dict(DataFile1[0])
data_vcoeff = dict(DataFile1[1])
atlist1 = DataFile1[2]

DataFile2 = ParseFile2(in_f2)
data_k = dict(DataFile2[0])
data_l = dict(DataFile2[1])
data_C = dict(DataFile2[2])
atlist2 = DataFile2[3]

#print len(data_mean), len(data_vcoeff), len(data_k), len(data_l), len(data_C)

k = 'n/a'
l = 'n/a'
C = 'n/a'
for i in atlist1:
    if i in atlist2:
        #p += 1
        #print p
        out_f.write(i + '\t' + data_mean[i] + '\t' + data_vcoeff[i] + '\t' + data_k[i] + '\t' + data_l[i] + '\t' + data_C[i] + '\n')
    else:
        out_f.write(i + '\t' + data_mean[i] + '\t' + data_vcoeff[i] + '\t' + k + '\t' + l + '\t' + C + '\n')


in_f1.close()
in_f2.close()
out_f.close()
