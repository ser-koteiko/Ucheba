#-*- coding: utf-8 -*-
#from __future__ import unicode_literals
#программа складывающая числа из строк через запятую из открытого файла
chisla = open("chisla.txt", "r")
chisla2 = open("chisla2.txt", "w")
l = chisla.readlines()
# l список элементами которого являются строки
a2=""
for i in l:
	a=i.split(",")
	a1=[]
	for m in a:
		a = int(m)
		a1.append(a)
	#print sum(a1)
	chisla2.write(x)
	chisla2.write("\n")