'''
def f(x, y):
	a = 7
	b = x+y
	return b
	
z = 9
q = f(4,z) + 1
'''
# s = math.sqrt(p* p-a * p-b * p-c)

import math
a = 5
b = 7
c = 13
d = 9
def s(x, y, z):
	if x+y<z:
		return -1
	if x+z<y:
		return -1
	if y+z<x:
		return -1
	p = 0.5*(x+y+z)
	k = math.sqrt(p* (p-x) * (p-y) * (p-z))
	return k
q = s (a,b,c)
m = s (a,b,d)
l = s (a,c,d)
n = s (b,c,d)
def f(x):
	if x == -1:
		g = "oshibka"
	else:
		g = x
	return g
q1 = f (q)
m1 = f (m)
l1 = f (l)
n1 = f (n)
print q1, m1, l1, n1
