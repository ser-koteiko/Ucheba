m=[]
import random

class Card:
	Jacket = 11
	Queen = 12
	King = 13
	Ace = 14
	
	Hearts = 101
	Diamonds = 102
	Clubs = 103
	Spades = 104

class Combination:
	Pair = 200
	TwoPair = 300
	Three = 400
	Straight = 500
	Flush = 600
	Full = 700
	Care = 800
	RoyalFlush = 900

for i in range (0,13):
	for j in range (0,4):
		m.append([i,j])
x=[i,j]
karta={0:"2", 1:"3", 2:"4", 3:"5", 4:"6", 5:"7", 6:"8", 7:"9", 8:"10", 9:"J", 10:"Q", 11:"K", 12:"A"}
mast={0:"chervi", 1:"bubni", 2:"trefi", 3:"piki"}
combination = {Combination.Pair:"pair", Combination.TwoPair: "two pairs", Combination.Three:"three", 
	Combination.Straight:"straight", Combination.Flush:"flush", Combination.Full:"full house",
	Combination.Care:"care", Combination.RoyalFlush:"royal flush"}
def pechat_karti(x):
	print karta[x[0]], mast[x[1]],
#for i in m:
#	pechat_karti(i)
s=[]
while len(s)!= 9:
	r=random.randint(0,51)
	if not r in s:
		s.append(r)

player1=[m[s[0]],m[s[1]]]
player2=[m[s[2]],m[s[3]]]
table=[m[s[4]],m[s[5]],m[s[6]],m[s[7]],m[s[8]]]
s1=player1+table
s2=player2+table
#s1= [[4,0],[5,1],[4,2],[6,1],[5,3],[3,1]]
#s2= [[7,0],[6,1],[7,2],[6,0],[5,3],[5,1],[9,0],[4,1]]
'''
print "\n","igrok1"
for i in player1:
	pechat_karti(i)
print "\n","idrok2" 
for i in player2:
	pechat_karti(i)
print "\n","stol"
for i in table:
	pechat_karti(i)
'''	
def para(l):
	l1=[]
	m2=-1
	for i in l:
		l1.append(i[0])
	for m in range(0,13):
		d=0
		m1 = 12-m
		for i in l1:
			if i==m1:
				d+=1
		if d==2:
			m2=m1
			break
	return m2

def troika(l):
	l1=[]
	m2=-1
	for i in l:
		l1.append(i[0])
	for m in range(0,13):
		d=0
		m1 = 12-m
		for i in l1:
			if i==m1:
				d+=1
		if d==3:
			m2=m1
			break
	return m2

def kare(l):
	l1=[]
	m2=-1
	for i in l:
		l1.append(i[0])
	for m in range(0,13):
		d=0
		m1 = 12-m
		for i in l1:
			if i==m1:
				d+=1
		if d==4:
			m2=m1
			break
	return m2
def flash(l):
	l1=[]
	l2=[]
	m2=-1
	for i in l:
		l1.append(i[1])
	for m in range(0,4):
		d=0
		for i in l1:
			if i==m:
				d+=1
		if d>=5:
			for i in l:
				if i[1]==m:
					l2.append(i[0])
			m2=max(l2)
			break
	return m2

def dve_pari(l):
	l1=[]
	m2=-1
	n=0
	for i in l:
		l1.append(i[0])
	for m in range(0,13):
		d=0
		for i in l1:
			if i==m:
				d+=1
		if d==2 and n==2:
			m2=m2/100
			m2+=m*100
			n+=1
		if d==2 and n==1:
			m2+=m*100
			n+=1
		if d==2 and n==0:
			m2=m
			n+=1	
	if n<2:
		m2=-1
			
	return m2	
	
def fool_house(l):
	l1=[]
	m2=-1
	for i in l:
		l1.append(i[0])
	for m in range(0,13):
		d=0
		m1 = 12-m
		for i in l1:
			if i==m1:
				d+=1
		if d>=3:
			three = m1
			m2=100*m1	
			l1=[]
			for i in l:
				if i[0] != three:
					l1.append(i[0])
			for m in range(0,13):
				d=0
				m1 = 12-m
				for i in l1:
					if i==m1:
						d+=1
				if d>=2:
					m2+=m1
					return m2
			return -1
	return -1
	
def streit(l):#straight
	l1=[]
	m2=-1
	for i in l:
		l1.append(i[0])
	l1.sort()
	b=0
	for i in range(0,len(l1)-1):
		if l1[i+1]-l1[i]==1:
			b+=1
			if b >= 4:
				m2=l1[i+1]
		elif l1[i+1]==l1[i]:
			continue
		elif l1[i+1]-l1[i]>1 and b>=5:
			break
		else:
			b=0
			m2=-1
	return m2
		
def royal_flash(l):
	l0=[]
	l1=[]
	l2=[]
	l3=[]
	m2=-1
	for i in l:
		if i[1]==0:
			l0.append(i)
		if i[1]==1:
			l1.append(i)
		if i[1]==2:
			l2.append(i)
		if i[1]==3:
			l3.append(i)
	if len(l0)>=5:
		x=streit(l0)
		if x != -1:
			m2=x
			return m2
	if len(l1)>=5:
		x=streit(l1)
		if x != -1:
			m2=x
			return m2
	if len(l2)>=5:
		x=streit(l2)
		if x != -1:
			m2=x
			return m2
	if len(l3)>=5:
		x=streit(l3)
		if x != -1:
			m2=x
			return m2
	return m2	
def vse_kombinacii(l):
	x=royal_flash(l)
	if x!=-1:
		m=Combination.RoyalFlush
		return m, x
	x=kare(l)
	if x!=-1:
		m=Combination.Care
		return m, x
	x=fool_house(l)
	if x!=-1:
		m=Combination.Full
		return m, x
	x=flash(l)
	if x!=-1:
		m=Combination.Flush
		return m, x
	x=streit(l)
	if x!=-1:
		m=Combination.Straight
		return m, x
	x=troika(l)
	if x!=-1:
		m=Combination.Three
		return m, x
	x=dve_pari(l)
	if x!=-1:
		m=Combination.TwoPair
		return m, x
	x=para(l)
	#print l
	if x!=-1:
		m=Combination.Pair
		return m, x
	m=-1
	return m, -1
'''
c1, x1 = vse_kombinacii(s1)
if c1 != -1:
	print "\nPlayer 1 has ", combination[c1], " with highest card ", karta[x1]
c2, x2 = vse_kombinacii(s2)
if c2 != -1:
	print "\nPlayer 2 has ", combination[c2], " with highest card ", karta[x2 / 100]
if c1 > c2:
	print "Player 1 wins"
elif c2 > c1:
	print "Player 2 wins"
else:
	if x1 > x2:
		print "Player 1 wins"
	elif x2 > x1:
		print "Player 2 wins"
	# kicker
'''

bank=0
stek1=1000
stek2=1000
stavka1=0
stavka2=0
print "stek player1", stek1
print "stek player1", stek1
print "player2 onoidite ot kompa"
print "player1 mogu pokazat vam karti?"
while True:
	k=raw_input("Nazmite 1, esli da:")
	if k=="1":
		print"\n","vashi karti"
		for i in player1:
			pechat_karti(i)
		break
print "player1 zapomnili karti? Otoidite ot kompa i pozovite player2"
while True:
	k=raw_input("Nazmite 1, esli da:")
	if k=="1":
		break
for i in range (1,20):
	print "\n"
print "player2 mogu pokazat vam karti?"
while True:
	k=raw_input("Nazmite 1, esli da:")
	if k=="1":
		print"\n","vashi karti"
		for i in player2:
			pechat_karti(i)
		break
print "player2 zapomnili karti? Pozovite player1"
while True:
	k=raw_input("Nazmite 1, esli da:")
	if k=="1":
		break
for i in range (1,20):
	print "\n"
print "Na stole otkriti 3 karti", 
pechat_karti(m[s[4]])
pechat_karti(m[s[5]])
pechat_karti(m[s[6]])
print "\nPervii krug stavok. Player1 na malom blainde, player2 na bolshom blainde."
stavka1=5
stavka2=10
def round_stavok(stavka1,stavka2):
	bank=stavka1+stavka2
	stek1=1000-stavka1
	stek2=1000-stavka2
	x=True
	hod=0 
	raund=0
	while stavka1!=stavka2 or hod%2!=0 or raund!=1:
		#print "Current bets: ", stavka1, stavka2, hod, raund
		if stavka1<=stavka2 and hod%2==0:
			print "Player1 vash hod"
			k=raw_input("f-fold,c-chek,rXXX-raise i razmer stavki:")
			if k=="f":
				stek2+=bank
				x= False
				print"Igra okonchena."
				print "Player1", stek1
				print "Player2", stek2
				break
			if k=="c":
				bank-=stavka1
				stavka1=stavka2
				bank+=stavka1
				stek1=1000-stavka1
				hod+=1
				continue
			if k[0]=="r":
				l = int(k[1:])
				bank-=stavka1
				stavka1=l+stavka2
				bank+=stavka1
				stek1=1000-stavka1
				hod+=1
				continue
		if stavka1>=stavka2 and hod%2!=0:
			print "Player2 vash hod"
			k=raw_input("f-fold,c-chek,rXXX-raise i razmer stavki:")
			if k=="f":
				stek1+=bank
				x= False
				print"Igra okonchena."
				print "Player1", stek1
				print "Player2", stek2
				break
			if k=="c":
				bank-=stavka2
				stavka2=stavka1
				bank+=stavka2
				stek2=1000-stavka2
				hod+=1
				raund+=1
				continue
			if k[0]=="r":
				l = int(k[1:])
				bank-=stavka2
				stavka2=l+stavka1
				bank+=stavka2
				stek2=1000-stavka2
				hod+=1
				continue
	return x, bank
x, bank = round_stavok(5,10)
if x == True:
	print "bank:", bank
	print "otkritie 4 karti"
	pechat_karti(m[s[7]])
	print"\n"
	x, bank = round_stavok(bank/2,bank/2)
	if x == True:
		print "bank:", bank
		print "otkritie 5 karti"	
		pechat_karti(m[s[8]])
		print"\n"
		x, bank = round_stavok(bank/2,bank/2)
		if x == True:
			print "bank:", bank
			
			for i in s1:
				pechat_karti(i)
			print "\n"	
			for i in s2:
				pechat_karti(i)	
			print "\n"

						
			c1, x1 = vse_kombinacii(s1)
			if c1 != -1:
				if x1 < 100:
					hc = karta[x1]
				else:
					hc = karta[x1 / 100]
				print "\nPlayer 1 has ", combination[c1], " with highest card ",hc
			c2, x2 = vse_kombinacii(s2)
			if c2 != -1:
				if x2 < 100:
					hc = karta[x2]
				else:
					hc = karta[x2 / 100]
				print "\nPlayer 2 has ", combination[c2], " with highest card ", hc

			if c1 > c2:
				print "Player 1 wins"
				x=1000+bank/2
				y=1000-bank/2
				print "1 igrok", x
				print "2 igrok", y
			elif c2 > c1:
				print "Player 2 wins"
				x=1000+bank/2
				y=1000-bank/2
				print "1 igrok", y
				print "2 igrok", x
			else:
				if x1 > x2:
					print "Player 1 wins"
					x=1000+bank/2
					y=1000-bank/2
					print "1 igrok", x
					print "2 igrok", y
				elif x2 > x1:
					print "Player 2 wins"	
					x=1000+bank/2
					y=1000-bank/2
					print "1 igrok", y
					print "2 igrok", x
