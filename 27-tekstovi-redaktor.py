#-*- coding: utf-8 -*-
#from __future__ import unicode_literals

class MyValueErrorException(BaseException):
	pass

import os
tekst2 = open("tekst2.txt", "r")
l = tekst2.readlines()
for li in l:
	print li.decode('utf8'),
print""
m=[]
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
			m=[]
			h=raw_input("Vvedite tekst:")
			#tekst3 = open("tekst3.txt", "w")
			while h != "%end":
				#tekst3.write(h)
				#tekst3.write("\n")
				#tekst3.flush()
				#os.fsync(tekst3)
				m.append(h)
				h=raw_input(">")
		elif komanda=="insert":
			if param:
				d = int(param[0])
				if not d in range(0,len(m)+1):
					raise MyValueErrorException
			h=raw_input("Vvedite tekst:")
			l1=[]
			l=[]
			if param:
				l=m[:d-1]
				l2=m[d-1:]
				l.append(h)
				l=l+l2
				m=l
			else:
				m.append(h)
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
					m=m[:d-1]+m[d1:]
					print m
				else:
					d = int(param[0])
					m=m[:d-1]
			else:
				m=[]
		elif komanda=="print":
			if param:
				if len(param)>=2:
					d = int(param[0])
					d1 = int(param[1])
					l=m[d-1:d1]
					b=0
					for i in l:
						b+=1
						print b, ":", i
				else:
					d = int(param[0])
					l=m[d-1:]
					b=0
					for i in l:
						b+=1
						print b, ":", i
			else:
				b=0
				for i in m:
					b+=1
					print b, ":", i
		elif komanda=="replace":
			h=raw_input("Vvedite tekst:")
			l1=[]
			l=[]
			if param:
				if len(param)>=2:
					d = int(param[0])
					d1 = int(param[1])
					l=m[:d-1]
					l2=m[d1:]
					l.append(h)
					l=l+l2
					m=l
				else:
					d = int(param[0])
					l=m[:d-1]
					l2=m[d:]
					l.append(h)
					l=l+l2
					m=l
			else:
				m=[]
				m.append(h)
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
				param1.write("\n".join(m))
				#for i in m:
					#param1.write(i)
					#param1.write("\n")
				param1.close()
			else:
				temp = open("temp.txt", "w")
				m1="\n".join(m)
				temp.write(m1)
				#for i in m:
					#temp.write(i)
					#temp.write("\n")
				temp.close()
			continue
		elif komanda=="load":
			m=[]
			param1=open(param[0],"r")
			for i in param1:
				m.append(i.strip())
			for i in m:
				print i
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
