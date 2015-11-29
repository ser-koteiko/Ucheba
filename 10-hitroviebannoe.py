l = "fhaa"
l1 = []
l2 = []
for m in l:
	if m == "a":
		l1.append(m)
	elif m == "e":
		l1.append(m)
	elif m == "y":
		l1.append(m)
	elif m == "u":
		l1.append(m)
	elif m == "i":
		l1.append(m)
	elif m == "o":
		l1.append(m)
	else:
		l2.append(m)
x = len(l1)
z = len(l2)
print x, z
if x == z:
	s1 = ""
	for i in l:
		s1 += i+i
	print s1
if x != z:
	s2 = ""
	b = len(l)
	while b != 0:
		s2 += (l[b-1])
		b = b-1
	print s2