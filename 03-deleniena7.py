'''
n = 17*23*3*3*3*3*2*7*5*10
while n != 1:
	for i in xrange(2,n+1):
		if n % i != 0:
			continue
		if n % i == 0:
			print i
			n = n / i
			break
'''
for i in range (1,100):
	if i % 7 == 0:
		print i
print "================="

n=1
while n != 100:
	if n % 7 == 0:
		print n
	n=n+1