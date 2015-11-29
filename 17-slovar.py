'''
l = [1,2,3]
l.append(3)
l[0] = 7
d = {"vasya":2, "petya":5, "kolya":[4,5,6,67]}
l = (1,2,3)
d = {}
d["vasya"] = 6
x = d["vasya"]
if "vasya" in d:
	x = d["vasya"]
d.values()
d.keys()
for i in d.keys():
	x = d[i]
'''

s = "iwehfghfdjkvklsdnvklnlkdfnsvfjgfdgklfdgvnbiroesbnfdnbkl"
d={}
for i in s:
	if not i in d:
		d[i] = 1
	else:
		d[i] += 1
print d
a= min (d.values())
b= max (d.values())
for i in d.keys():
	if d[i]==a:
		print "min", i
	if d[i]==b:
		print "max", i
