if x1 != x2 and y1 != y2:
			print "vveden nevernii hod. Figura tak ne hodit."
			continue
		if x1 == x2:
			a = min(y1, y2)
			b = max(y1, y2)
			flag = False
			for i in range (a+1,b):
				if m[x1][i] != 0:
					print "vveden nevernii hod. Nelzya pereprigivat cherez figuru."
					flag = True
					break
			if flag:
				continue
		if y1 == y2:
			a = min(x1, x2)
			b = max(x1, x2)
			flag = False
			for i in range (a+1,b):
				if m[i][y1] != 0:
					print "vveden nevernii hod. Nelzya pereprigivat cherez figuru."
					flag = True
					break
			if flag:
				continue