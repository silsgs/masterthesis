#Calculo del coeficiente de variacion de la volatilidad.

import sys

path = '/Users/andromeda/Desktop/Project/'

in_file = path + 'Input_files/Filtered_input_files/Uniq_genes_expression.txt'
out_file = path + 'Volatility_analysis/Uniq_genes_expression_volatility.txt'

in_f = open(in_file, 'r')
out_f = open(out_file, 'w')

out_f.write('#id\tmean\tstd\tVolatilityCoefficient\n')


def VolatilityCoeff(mean, volatility):
    volatilityCoeff = volatility/mean
    return volatilityCoeff

coefficients = []

for line in in_f:
    if '#' in line:
        continue
    else:
        line = line.strip().split('\t')
        at = line[0]
        mean = float(line[1])
        volatility = float(line[2])

        Vcoeff = VolatilityCoeff(mean, volatility)
        #coefficients.append(Vcoeff)

        out_f.write(at + '\t' + str(mean) + '\t' + str(volatility) + '\t' + str(Vcoeff) + '\n')

#print len(coefficients)


in_f.close()
out_f.close()
