#Procesamiento fichero Ath_network_coexpression.txt
#Eliminar ';', dividir elementos de filas en columnas con su gen coexpresado asociado


#Definitions
path = '/Users/andromeda/Desktop/Project/'

input_file = path + 'Input_files/Ath_network_coexpression.txt'
output_file = path + 'Coexpression_analysis/Temporary_files/Filtered_Ath_net_coexpress.txt'

in_f = open(input_file, 'r')
out_f = open(output_file, 'w')

out_f.write('#AT1\tAT2\n')

#Separacion columnas, formar vecs

for line in in_f:
    line = line.strip().split('\t')
    i = line[0].split(';')
    j = line[1].split(';')

    if len(i) == 1 and len(j) == 1:
        out_f.write(i[0] + '\t' + j[0] + '\n')

    elif len(i) == 1 and len(j) > 1:
        for n in j:
            out_f.write(i[0] + '\t' + n + '\n')

    elif len(i) > 1 and len(j) == 1:
        for a in i:
            out_f.write(a + '\t' + j[0] + '\n')

    elif len(i) > 1 and len(j) > 1:
        for a in i:
            for n in j:
                out_f.write(a + '\t' + n + '\n')

in_f.close()
out_f.close()
