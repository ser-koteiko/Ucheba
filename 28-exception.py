class MyValueErrorException(BaseException):
	pass

s = "sssss"
s2 = "2"

def my_int(s):
	for i in s:
		if not i in "0123456789":
			raise MyValueErrorException()
	res = 0
	for i in s:
		res = res * 10 + ord(i) - ord('0')
	return res

try:
	x = my_int("12345ssss")
	print x
	#raise MyValueErrorException()
	print "no excetion"
	x = my_int(s)
	y = my_int(s2)
except MyValueErrorException:
	print "exception: incorrect number"