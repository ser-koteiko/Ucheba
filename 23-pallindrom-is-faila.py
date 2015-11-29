#-*- coding: utf-8 -*-
#from __future__ import unicode_literals
# пользователь с клавиатуры вводит слова, программа проверяет их на симметричность, если симметрично, то записывает в файл. Выход после введения с клавиатуры exit
g2 = open("g2.txt", "w")
while True:
	x = raw_input("введите слово:>")
	if x=="exit":
		#False
		break
	else:
		x1= x[::-1]
		if x==x1:
			print x
			g2.write(x)
			g2.write("\n")
		else:
			continue
'''
		m=len(x)-1
		m0=0
		m3=(len(x)-1)/2
		m1=0
		for i in range (0,m3):
			if x[m0]==x[m]:
				m0+=1
				m+=-1
				m1+=1
				if m1==m3:
					print x
					g2.write(x)
					g2.write("\n")
			else:
				break
'''