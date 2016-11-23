
path = '/Users/andromeda/Desktop/Project/Coexpression_analysis/'
file1 = path + 'Ath_network_coexpression_random100.txt'
outfile = path + 'Ath_network_coexpression_random100_v2.txt'

f1 = open(file1, 'r')
out = open(outfile, 'w')


for line in f1:
    line = line.replace('   ','\t')
    line = line.strip().split('\t')
    out.write(line[0] + '\t' + line[1] + '\t' + line[2] + '\n')

f1.close()
out.close()
