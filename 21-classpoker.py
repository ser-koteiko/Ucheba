class Player:
	name = ""
	hand = []
	stack = 0
	
	def __init__(self, name, stack):
		self.name = name
		self.stack = stack
		
	def bet(self, bet):
		self.stack -= bet
		
		
class Card:
	Jacket = 11
	Queen = 12
	King = 13
	Ace = 14
	
	Hearts = 101
	Diamonds = 102
	Clubs = 103
	Spades = 104
	
	value = 0
	set = 0
	
	def __init__(self, value, set):
		self.value = value
		self.set = set
	
class Deck:
	cards = []
	
	def __init__(self):
		for i in range(2, 15):
			for j in range(101, 105):
				self.cards.append(Card)
		
p = Player("vasya", 100)
p2 = Player("petya", 200)
p.bet(10)
p2.bet(20)

class Figure:
	points = []
	def perimeter(self):
		return 0
		
	def area(self):
		pass
	
class Square(Figure):
	def area(self):
		return a*a
	
class Triangle(Figure):
	def area(self):
		return math.sqrt(p*(p-a)*(p-b)*(p-c))

s = []
s.append(Figure())
s.append(Square())
s.append(Triangle())
for f in s:
	print f.area()
	print f.perimeter()