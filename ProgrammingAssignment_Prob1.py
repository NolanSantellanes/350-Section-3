from math import *

def  Euclidean_Algorithm(x, y, EA=True):
	if x < y: # We want x >= y
		return Euclidean_Algorithm(y, x, EA)
	print()
	while y != 0:
		if EA: print('%s = %s * %s + %s' % (x, floor(x/y), y, x % y))
		(x, y) = (y, x % y)
	
	if EA: print('gcd is %s' % x) 
	return x


Euclidean_Algorithm(35,153)
print("_________________")
Euclidean_Algorithm(78,90)

