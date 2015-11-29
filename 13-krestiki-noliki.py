m = [[0, 0, 0],
[0, 0, 0],
[0, 0, 0]]
for c in range (0,9):
	for i in [0,1,2]:
		s = ""
		for j in [0, 1, 2]:
			if m[i][j] == 1:
				s += "X"
			elif m[i][j] == -1:
				s += "O"
			else:
				s += "_"
		print s
	if c in [0,2,4,6,8]:
		print "Hod Krestika"
	else:
		print "Hod Nolika"
	while True:
		x = raw_input("vvedite x>")
		x = int(x)
		y = raw_input("vvedite y>")
		y = int(y)
		if not x in [0,1,2]:
			print "vveden nevernii X"
			continue
		if not y in [0,1,2]:
			print "vveden nevernii Y"
			continue
		if m[x][y] != 0:
			print "kletka zaniata"
			continue
		else:
			break
	if c in [0,2,4,6,8]:
		m[x][y]=1
	else:
		m[x][y]=-1
	for i in [0,1,2]:
		if m[i][0] == 1:
			if m[i][1]== 1:
				if m[i][2] == 1:
					print "winX"
					break
		if m[i][0] == -1 and m[i][1]== -1 and m[i][2] == -1:
			print "winO"
			break
	for i in [0,1,2]:
		if m[0][i] == 1:
			if m[1][i]== 1:
				if m[2][i] == 1:
					print "winX"
					break
		if m[0][i] == -1 and m[1][i]== -1 and m[2][i] == -1:
			print "winO"
			break
	if m[0][0] == 1 and m[1][1]== 1 and m[2][2] == 1:
			print "winX"
			break
	if m[0][0] == -1 and m[1][1]== -1 and m[2][2] == -1:
			print "winO"
			break
	if m[0][2] == 1 and m[1][1]== 1 and m[2][0] == 1:
			print "winX"
			break
	if m[0][2] == -1 and m[1][1]== -1 and m[2][0] == -1:
			print "winO"
			break