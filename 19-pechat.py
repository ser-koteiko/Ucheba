f = open("slovar.txt", "r")
f2 = open("slovar3.txt", "w")
l = f.readlines()
while True:
	s = raw_input("vvedite nomer stroki>")
	if s == "end":
		break
	else:
		x =int(s)
		if (x-1) > len(l):
			print "Vveden nevernii nomer stroki."
			continue
		else:
			f2.write(l[x-1])
	
	