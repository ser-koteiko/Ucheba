'''
f = open("f.txt", "r")
s = f.read()
l = f.readlines()
for s in f.readlines():
	print s
	
for s in f:
	print s
	
f2 = open("f2.txt", "w")
f2.write("wqertyuio")

f.close()
'''
f = open("slovar.txt", "r")
eng = ""
rus = ""
cur = 0
dic = {}
for s in f:
	s = s.strip() #s.replace("\n", "")
	if cur % 2 == 0:
		eng = s
		cur += 1
		continue
	else:
		rus = s
		cur += 1
		if not rus in dic:
			dic[rus] =eng 
		else:
			dic[rus] += "," + eng
f.close()
f2 = open("slovar2.txt", "w")
for i in dic:
	f2.write(i + "\n")
	f2.write(dic[i] + "\n")