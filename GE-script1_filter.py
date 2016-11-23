#Remove ";" character and separate into different lines

import sys

# Definitions

path = '/Users/andromeda/Desktop/Project/Input_files/'
expression_file = path + sys.argv[1]

out_file = 'Temp_' + sys.argv[1]

#Opening

f1 = open(expression_file, 'r')

out = open(out_file, 'w')

out.write('#id\tmean\tstd\n')

#Processing f1

for line in f1:
	vec_line = line.strip().split('\t')
	data = {}

	vec_ids = vec_line[0].split(';')
	#print len(vec_ids)
	if len(vec_ids) > 1:
		for id in vec_ids:
			data['id'] = id
			data['meanGE'] = vec_line[-2]
			data['stdGE'] = vec_line[-1]
			#print data
			out.write(data['id'] + '\t' + data['meanGE'] + '\t' + data['stdGE'] + '\n')

	else:
		#print len(vec_ids)
		data['id'] = vec_line[0]
		data['meanGE'] = vec_line[-2]
		data['stdGE'] = vec_line[-1]
		#print data
		out.write(data['id'] + '\t' + data['meanGE'] + '\t' + data['stdGE'] + '\n')

#Close

f1.close()
#f2.close()
out.close()
