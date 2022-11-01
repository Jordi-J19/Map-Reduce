import sys

f = open('vector.txt', 'r')
v = map(float, f.read().split())

for line in sys.stdin:
	matrix_element = line.strip().split()
	i = int(matrix_element[0])
	j = int(matrix_element[1])
	val = float(matrix_element[2])
	print("%s\t%s" % (i, v[j]*val))