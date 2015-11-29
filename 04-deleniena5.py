for a in range (1,20):
	for b in range (1,20):
		#if (a+b) % 5 != 0:
			#continue
		if (a+b) % 5 == 0:
			print a, "+", b
			
print "================="

a=1
while a != 20:
	b = 1
	while b != 20:
		if (a+b) % 5 == 0:
			print a, "+", b
		b=b+1
	a=a+1