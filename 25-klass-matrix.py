#-*- coding: utf-8 -*-
#from __future__ import unicode_literals
# l список элементами которого являются строки
#chisla2.write("\n")

class matrix:
	m = []
	def read(self, file):
		chisla = open(file, "r")
		l = chisla.readlines()
		a2=[]
		for i in l:
			a=i.split(",")
			a1=[]
			for m in a:
				a = int(m)
				a1.append(a)
			a2.append(a1)
		self.m = a2

	def write(self, filename):
		chisla2 = open(filename, "w")
		strs = []
		matrix = self.m
		for row in matrix:
			a3 = []
			for el in row:
				a3.append(str(el))
			s = ",".join(a3)
			strs.append(s)
		chisla2.write("\n".join(strs))
#a2= read("chisla.txt")
#write(a2,"chisla2.txt")
a = matrix()
a.read("chisla.txt")
a.write("chisla2.txt")