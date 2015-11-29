s = raw_input(">")
m = ""
x = len(s)
while x != 0:
	m += s[x-1]
	x = x-1
if m == s:
	print "yes"
else:
	print "no"