print "kalkuliator na slogenie i vichitanie"
while True:
	x = raw_input("vvedite primer bez probelov>")
	x1=""
	c=0
	error=0
	for i in x:
		if i not in "0123456789" and i!="+" and i!="-":
			print "oshibka v vvode primera"
			error=1
			break
		if i=="+" or i=="-":
			x1+=i
			c+=1
		if i.isdigit() and c>=2:
			print "oshibka v vvode primera"
			error=1
			break
		if i.isdigit() and c<2:	
			c=0
			x1+=i
	if error:
		continue
	else:
		break
a=""
a1=[]
for i in x1:
	if i !="+" and i!="-":
		a+=i
	if i =="+":
		a = int(a)
		a1.append(a)
		a=""
	if i =="-":
		a = int(a)
		a1.append(a)
		a="-"
a = int(a)
a1.append(a)
y=sum(a1)
print "otvet:", y