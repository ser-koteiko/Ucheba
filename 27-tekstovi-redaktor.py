#-*- coding: utf-8 -*-
#from __future__ import unicode_literals

class MyValueErrorException(BaseException):
	pass
	
class Text:
	def __init__(self):
		self.m=[]
	def clear(self):
		self.m=[]
	def add_line(self,l):
		self.m.append(l)
	def insert_line(self,l,d):
		l1=m[:d-1]
		l2=m[d-1:]
		l1.append(l)
		m=l+l2
	def delete_line(self,d):
		m=m[:d-1]+m[d:]
	def delete_lines(self,d,d1):
		#m=m[:d-1]+m[d1:]
		d0=d1-d
		for i in range (0,d0):
			self.delete_line(d)
	def print_line(self,d):
		l=self.m[d-1]
		print d-1, ":", l
	def print_lines(self,d,d1):
		l=self.m[d-1:d1]
		b=d-1
		for i in l:
			b+=1
			print b, ":", i
	def print_all_lines(self):
		#b=0
		#for i in self.m:
			#b+=1
			#print b, ":", i
		self.print_lines(self,1,len(self.m))
	def load(self,param1):
		for i in param1:
			self.m.append(i.strip())
	def save(self,param1):
	`	param1.write("\n".join(self.m))
		
import os
tekst2 = open("tekst2.txt", "r")
l = tekst2.readlines()
for li in l:
	print li.decode('utf8'),
print""
t = Text()
f=[]
komanda=[]
param=[]
while True:
	k=raw_input("Naberite komandu:")
	f=k.split(" ")
	komanda=f[0]
	param=f[1:]
	try:
		if komanda=="enter":
			t.clear()
			h=raw_input("Vvedite tekst:")
			#tekst3 = open("tekst3.txt", "w")
			while h != "%end":
				#tekst3.write(h)
				#tekst3.write("\n")
				#tekst3.flush()
				#os.fsync(tekst3)
				t.add_line(h)
				h=raw_input(">")
		elif komanda=="insert":
			if param:
				d = int(param[0])
				if not d in range(0,len(m)+1):
					raise MyValueErrorException
			h=raw_input("Vvedite tekst:")
			if param:
				t.insert_line(h,d)
			else:
				t.add_line(h)
		elif komanda=="delete":
			if param:
				d = int(param[0])
				if not d in range(0,len(m)+1):
					raise MyValueErrorException
				d = int(param[1])
				if not d in range(0,len(m)+1):
					raise MyValueErrorException
			if param:
				if len(param)>=2:
					d = int(param[0])
					d1 = int(param[1])
					t.delete_lines(d,d1)
				else:
					d = int(param[0])
					t.delete_line(d)
			else:
				t.clear()
		elif komanda=="print":
			if param:
				d = int(param[0])
				if not d in range(0,len(m)+1):
					raise MyValueErrorException
				d = int(param[1])
				if not d in range(0,len(m)+1):
					raise MyValueErrorException
			if param:
				if len(param)>=2:
					d = int(param[0])
					d1 = int(param[1])
					t.print_lines(d,d1)
				else:
					d = int(param[0])
					t.print_line(d)
			else:
				t.print_all_lines()
		elif komanda=="replace":
			h=raw_input("Vvedite tekst:")
			if param:
				d = int(param[0])
				if not d in range(0,len(m)+1):
					raise MyValueErrorException
				d = int(param[1])
				if not d in range(0,len(m)+1):
					raise MyValueErrorException
			if param:
				if len(param)>=2:
					d = int(param[0])
					d1 = int(param[1])
					t.delete_lines(d,d1)
					t.insert_line(h,d)
				else:
					d = int(param[0])
					t.delete_line(d)
					t.insert_line(h,d)
			else:
				t.clear()
				t.add_line(h)
		elif komanda=="find":
			if param:
				b=0
				for i in m:
					if param[0]in i:
						b+=1
						print b, ":", i
					else:
						b+=1
						continue
			else:
				continue
		elif komanda=="save":
			if param:
				param1=open(param[0],"w")
				t.save(param1)
				param1.close()
			else:
				param1 = open("temp.txt", "w")
				t.save(param1)
				param1.close()
			continue
		elif komanda=="load":
			param1=open(param[0],"r")
			t.load(param1)
			t.print_all_lines()
			continue
		else:
			print "neverno vvedena komanda"
			continue
	except MyValueErrorException:
		print "nevernii vvod"
		continue
	except ValueError:
		print "nevernii vvod parametra"
		continue
	except IOError:
		print "nevernii vvod parametra"
		continue
'''
Написать консольный текстовый редактор. Работать должно примерно так:
1. Программа запускается. В этом режиме модно вводить команды. Одна из команд должна быть "ввод текста" (enter)
2. Если пользователь вводит эту команду, то программа переключается в режим ввода текста. Все, что вводит пользователь, должно сохраняться. Если пользователь вводит специальную строку, например, "%end", ввод текста прекращается, и программа снова в режиме команд
3. Должны быть также доступны следующие команды:
- enter - ввод текста с нуля
- insert <номер i> - ввод текста после i-й строки. Если i не указано, текст дозаписывается в конец.
- delete <i> <j> - удалить строки с номерами i по j. Если не указано j - удалить до конца. Если не указано i и j, удаляет все
- print <i> <j> - напечатать строки с i по j, если номера не указаны, то аналогично delete
- replace <i> <j> - ввести текст вместо строк с i по j
- find <s> - найти все строки, где есть слово s, и напечатать их вместе с номерами
- save <s> - сохранить в файл с именем s. Если s не задано, сохраняет в temp.txt
- load <s> <i> - загрузить из файла текст (текущий удаляется)
'''
