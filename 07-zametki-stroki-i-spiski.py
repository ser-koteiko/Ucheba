'''
l = [2,3,4,5,6,7]
s = "abcdef"
s1 = "ab"
s2 = "cd"
s3 = s1 + s2
Добавление в список
l.append(9)
l += [9,6,7]
l1 = [1,2,3]
l2 = [4,5,6]
l3 = l1 + l2
Добавление в строку
s += "qwerty"

Сортировка
l.sort()
l = [2,3, "bnd", [4,5,6]]
len(s)
x == 5
x > 5
x in l
for i in s:
	x = 5

x = x + 1
x += 1
'''

'''
l = [1,2,3,4,5]
while len(l) != 1:
	n = len(l)
	l[0] = l[0] + l[n-1]
	l = l[0:n-1]
print l[0]
'''
'''
l = [1,2,3,4,5]
s = 0
for i in l:
	s = s + i
print s
print sum(l)
'''

s="jbjhjlmjhbghykjkn"
l = []
for i in s:
	l.append(i)
for i in l:
	i=i+i
m = ""
for i in l:
	m.append(i)
print m

s="jbjhjlmjhbghykjkn"
s1 = ""
for i in s:
	s1.append(i)
	s1.append(i)