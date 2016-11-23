import sys
from math import sqrt

# Definitions

path = '/Users/andromeda/Desktop/Project/Gene_expression/'

expression_file = path + sys.argv[1]
out_file = 'Uniq_' + sys.argv[1].replace('Temp2_', '')

#Opening

f1 = open(expression_file, 'r')
out = open(out_file, 'w')

out.write('#id\tmean\tstd\n')

#Select repeats

AT = []
mean = []
std = []

for line in f1:
	if '#' in line:
		continue
	else:
		vec_line = line.strip().split('\t')	
	  	AT1 = vec_line[0]
	  	mean1 = float(vec_line[1])
	  	std1 = float(vec_line[2])
	  	if AT1 not in AT:
	    		AT.append(AT1)
	    		mean.append(mean1)
	    		std.append(std1)
		else:
			mean2 = mean[-1]
			std2 = std[-1]
			mean[-1] = (mean1+mean2)/2
			std[-1] = sqrt((std1*std1+std2*std2)/2)

for i in range(0, len(AT)):
	out.write(AT[i] + '\t' + str(mean[i]) + '\t' + str(std[i]) + '\n')

f1.close()
out.close()