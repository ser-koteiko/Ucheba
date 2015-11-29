import random
print "10_primerov"
yes = 0
no = 0
for i in range (4):
	x = random.randint(1, 50)
	y = random.randint(1, 50)
	z = random.randint(1, 3)
	if z == 1:
		print x,"+",y
		m = x + y
	elif z== 2:
		print x,"-",y
		m = x - y
	else:
		print x,"*",y
		m = x * y
	k = raw_input("vvedite otvet>")
	k = int(k)
	if m == k:
		yes += 1
	else:
		no += 1
print "spasibo_vash_rezultat_pravilno", yes,"nepravilno",no
		