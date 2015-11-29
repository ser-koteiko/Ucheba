s = raw_input(">")
m = ""
z = 1
x = len(s)
if (s[0] == s[x-2]) and (s[1] == s[x-1]):
	print s[0:10]
else:
	for i in s:
		if z % 2 != 0:
			m += i
		z += 1
	print m