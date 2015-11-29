a=1
b=1
while (a+b) != 40:
	if (a+b) % 5 == 0:
		print a, "+", b 
	a=a+1
	if a == 21:
		b = b + 1
		a = b