f = open("slovar.txt", "r")
f2 = open("slovar3.txt", "w")
l = f.readlines()

s = raw_input("vvedite nomera strok cherez zapyatuu>")
a= 0
b = 0
for i in s:
	b+=1
	if i == ",":
		x =int(s[a:b-1])
		a = b
		print a, b, x
		if (x-1) > len(l):
			print "Vveden nevernii nomer stroki."
			continue
		else:
			f2.write(l[x-1])
x =int(s[a:b])
if (x-1) > len(l):
	print "Vveden nevernii nomer stroki."
else:
	f2.write(l[x-1])
	