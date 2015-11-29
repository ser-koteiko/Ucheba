m = \
[["rb", "hb", "eb", "qb", "kb", "eb", "hb", "rb"],
["pb", "pb", "pb", "pb", "pb", "pb", "pb", "pb"],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
["pw", "pw", "pw", "pw", "pw", "pw", "pw", "pw"], 
["rw", "hw", "ew", "qw", "kw", "ew", "hw", "rw"]]
wking=[7,4]
bking=[0,4]
def printboard (m):
	for i in [0, 1, 2, 3, 4, 5, 6, 7]:
		s = ""
		for j in [0, 1, 2, 3, 4, 5, 6, 7]:
			if m[i][j] == 0:
				s += "___"
			else:
				s += m[i][j]
				s += " "
		print s
def check_king (x1,y1,x2,y2,m):
	if x1-x2 >= 2:
		return False	
	if x1-x2 <= -2:
		return False	
	if y1-y2 >= 2:
		return False
	if y1-y2 <= -2:
		return False
	return True
def check_rook (x1,y1,x2,y2,m):
	if x1 != x2 and y1 != y2:
		return False
	if x1 == x2:
		a = min(y1, y2)
		b = max(y1, y2)
		for i in range (a+1,b):
			if m[x1][i] != 0:
				return False
	if y1 == y2:
		a = min(x1, x2)
		b = max(x1, x2)
		for i in range (a+1,b):
			if m[i][y1] != 0:
				return False				
	return True
def check_elefant (x1,y1,x2,y2,m):
	a = min(x1, x2)
	b = max(x1, x2)
	c = min(y1, y2)
	d = max(y1, y2)
	if b-a != d-c:
		return False
	for i in range(1, b-a):
		if m[x1+i*(x2-x1)/abs(x2-x1)][y1+i*(y2-y1)/abs(y2-y1)] != 0:
			return False
	return True
def check_queen (x1, y1, x2, y2, m):
	if not check_elefant(x1, y1, x2, y2, m) and not check_rook(x1, y1, x2, y2, m):
		return False
	return True
def check_horse (x1,y1,x2,y2,m):
	a = min(x1, x2)
	b = max(x1, x2)
	c = min(y1, y2)
	d = max(y1, y2)
	if b-a == 1 and d-c == 2:
		return True
	if b-a == 2 and d-c == 1:
		return True
	return False
def check_pawn (x1, y1, x2, y2,m):
	a = m[x1][y1]
	c = min(y1, y2)
	d = max(y1, y2)
	if m[x2][y2] == 0:
		if a[1] == "w" and y1==y2 and x1-x2 ==1:
			return True
		if a[1] == "b" and y1==y2 and x2-x1 ==1:	
			return True
		if a[1] == "w" and y1==y2 and x1==6 and x1-x2 ==2:
			return True
		if a[1] == "b" and y1==y2 and x1==1 and x2-x1 ==2:	
			return True
	else:
		if a[1] == "w" and d-c==1 and x1-x2 == 1 and m[x2][y2] !=0:
			return True
		if a[1] == "b"  and d-c==1 and x2-x1 ==1 and m[x2][y2] !=0:	
			return True
	return False
def myabs(x):
	if x > 0:
		return x
	else:
		return -x

def getking(m, color):
	for i in range(0, 8):
		for j in range(0, 8):
			if m[i][j] != 0:
				if m[i][j][0] == "k":
					if m[i][j][1] == color:
						return i, j
		
def othercolor(color):
	if color == "w":
		return "b"
	else:
		return "w"
		
def check(m, color):
	for x1 in [0, 1, 2, 3, 4, 5, 6, 7]:
		for y1 in [0, 1, 2, 3, 4, 5, 6, 7]:
			if m[x1][y1] != 0:
				c = m[x1][y1][1]
				piece = m[x1][y1][0]
				if c == color:
					x2, y2 = getking(m, othercolor(color))
					if piece == "r":
						if check_rook(x1, y1, x2, y2, m):
							return True
					if piece == "h":
						if check_horse(x1, y1, x2, y2, m):
							return True
					if piece == "e":
						if check_elefant(x1, y1, x2, y2, m):
							return True
					if piece == "q":
						if check_queen(x1, y1, x2, y2, m):
							return True
					if piece == "p":
						if check_pawn(x1, y1, x2, y2, m):
							return True
					if piece == "k":
						if check_king(x1, y1, x2, y2, m):
							return True
def vse_hodi (m, color):
	s=[]
	for i in [0, 1, 2, 3, 4, 5, 6, 7]:
		for j in [0, 1, 2, 3, 4, 5, 6, 7]:
			if m[i][j] != 0:
				x1= i
				y1= j
				if m[i][j][1] != color:
					continue
			else:
				continue
			piece = m[i][j][0]
			for i1 in [0, 1, 2, 3, 4, 5, 6, 7]:
				for j1 in [0, 1, 2, 3, 4, 5, 6, 7]:
					x2=i1
					y2=j1
					if m[x2][y2] != 0 and color =="w" and m[x2][y2] [1]=="w":
						continue
					if m[x2][y2] != 0 and color=="b" and m[x2][y2][1]=="b":
						continue
					if piece == "r":
						if check_rook(x1, y1, x2, y2, m):
							s.append((x1,y1,x2,y2))
					if piece == "h":
						if check_horse(x1, y1, x2, y2, m):
							s.append((x1,y1,x2,y2))
					if piece == "e":
						if check_elefant(x1, y1, x2, y2, m):
							s.append((x1,y1,x2,y2))
					if piece == "q":
						if check_queen(x1, y1, x2, y2, m):
							s.append((x1,y1,x2,y2))
					if piece == "p":
						if check_pawn(x1, y1, x2, y2, m):
							s.append((x1,y1,x2,y2))
					if piece == "k":
						if check_king(x1, y1, x2, y2, m):
							s.append((x1,y1,x2,y2))
	return s
def mat (m, color):
	if not check(m, color):
		return False
	moves = vse_hodi(m, othercolor(color))
	for move in moves:
		m1 = []
		for i in range(0,8):
			m2 = []
			for j in range(0,8):
				m2.append(m[i][j])
			m1.append(m2)
		x1 = move[0]
		y1 = move[1]
		x2 = move[2]
		y2 = move[3]
		m1[x2][y2] = m1[x1][y1]
		m1[x1][y1] = 0
		if not check(m1, color):
			print "protection ", x1, y1, x2, y2
			return False
	return True
#RA1-A2	
printboard(m)
player = 0
while True:
	if check(m, "b"):
		print "white is in check"
	if check(m, "w"):
		print "black is in check"
	if mat(m, "b"):
		print "white is in checkmate"
		break
	if mat(m, "w"):
		print "black is in checkmate"
		break
	if player % 2 == 0:
		s = raw_input("vvedite hod.white>")
	else:
		s = raw_input("vvedite hod.black>")
	piece = s[0]
	x1 = 8 - int(s[2])
	x2 = 8 - int(s[5])
	y1 = ord(s[1])-ord("a")
	y2 = ord(s[4])-ord("a")
	if len(s) < 7:
		f = 0
	else:
		f = s[6]
	l = m[x1][y1]
	l2 = m[x2][y2]
	if m[x1][y1] == 0:
		print "vveden nevernii hod. Kletka pusta."
		continue
	if piece != l[0]:
		print "vveden nevernii hod. Vvedite korrektno figuru."
		continue
	if player % 2 ==0 and l[1]=="b":
		print "vveden nevernii hod. Hodite svoimi figurami."
		continue
	if player % 2 !=0 and l[1]=="w":
		print "vveden nevernii hod. Hodite svoimi figurami."
		continue
	if m[x2][y2] != 0 and player % 2 ==0 and l2[1]=="w":
			print "vveden nevernii hod. Kletka zaniata."
			continue
	if m[x2][y2] != 0 and player % 2 !=0 and l2[1]=="b":
			print " Kletka zaniata."
			continue
	if piece == "k":
		if not check_king (x1,y1,x2,y2,m):
			print "vveden nevernii hod. Figura tak ne hodit."
			continue
		if player % 2 == 0:
			wking = [x2,y2]
		else:
			bking = [x2,y2]
	if piece == "r":
		if not check_rook (x1,y1,x2,y2,m):
			print "vveden nevernii hod. Figura tak ne hodit."
			continue
	if piece == "e":
		if not check_elefant (x1,y1,x2,y2,m):
			print "vveden nevernii hod. Figura tak ne hodit."
			continue
	if piece == "q":
		if not check_queen (x1,y1,x2,y2,m):
			print "vveden nevernii hod. Figura tak ne hodit."
			continue
	if piece == "h":
		if not check_horse (x1,y1,x2,y2,m):
			print "vveden nevernii hod. Figura tak ne hodit."
			continue
	if piece == "p":
		if not check_pawn (x1,y1,x2,y2,m):
			print "vveden nevernii hod. Figura tak ne hodit."
			continue
		a = m[x1][y1]
		b = m[x2][y2]
		if a[1] == "w" and x2==8:
			b[0] = "q"
		if a[1]=="b" and x2==1:
			b[0]="q"
	if f != "q" and f != "h" and f !="e" and f !="r" and f !=0:
		print "vveden nevernii hod. Neverno ukazana figura prevrashenia."
		continue
	a = m[x1][y1]	
	if f == 0 and piece == "p" and a[1]=="w" and x2==0:
		print "vveden nevernii hod. Neverno ukazana figura prevrashenia."
		continue
	if f == 0 and piece == "p" and a[1]=="b" and x2==7:
		print "vveden nevernii hod. Neverno ukazana figura prevrashenia."
		continue
	m[x2][y2]= m[x1][y1]
	m[x1][y1]= 0
	if piece == "p":
		b = m[x2][y2]
		if b[1] == "w" and x2==0:
			#if f==0:
				#f="q"
			m[x2][y2] = f + b[1]
		if b[1] == "b" and x2==7:
			#if f ==0:
				#f="q"
			m[x2][y2] = f + b[1]
	printboard(m)
	player +=1