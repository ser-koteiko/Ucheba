'''
for i in range(1,19):
	for m in range(0,10):
		for n in range(0,10):
			if n + m == i:
				print n, "+", m, "=", i
'''

'''
for m in range(0,10):
	for n in range(0,10):
		for a in range(0, 10):
			for b in range(0, 10):
				if m+n == a+b:
					print m, n, a, b
'''
for i in range(1000, 10000):
	a = i/1000
	b = i%1000/100
	c = i%1000%100/10
	d = i%1000%100%10
	if a+b == c+d:
		print a, b, c, d