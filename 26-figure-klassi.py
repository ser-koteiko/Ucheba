import math

class Point:
	x = 0
	y = 0
	def __init__(self, x, y):
		self.x = x
		self.y = y

class Figure:
	points = []
	
	def __init__(self, pts):
		self.points = pts
	
	def perimeter(self):
		p = 0
		for i in range(len(self.points)-1):
			p1 = self.points[i]
			p2 = self.points[i+1]
			p += math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)
		p1 = self.points[0]
		p2 = self.points[len(self.points)-1]
		p += math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)
		return p
		
	def area(self):
		pass
	
class Square(Figure):
	a = 0
	
	def __init__(self, pts):
		#super(Figure, self).__init__(pts)
		Figure.__init__(self, pts)
		p1 = pts[0]
		p2 = pts[1]
		self.a = math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)
		
	def area(self):
		return self.a ** 2
		
	def perimeter(self):
		return self.a * 4
	
class Triangle(Figure):
	a=0
	b=0
	c=0
	
	def __init__(self, pts):
		#super(Figure, self).__init__(pts)
		Figure.__init__(self, pts)
		p1 = pts[0]
		p2 = pts[1]
		p3 = pts[2]
		self.a = math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)
		self.b = math.sqrt((p2.x - p3.x) ** 2 + (p2.y - p3.y) ** 2)
		self.c = math.sqrt((p3.x - p1.x) ** 2 + (p3.y - p1.y) ** 2)
	def area(self):
		p=0.5* self.perimeter()
		return math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))
		
	def perimeter(self):
		return self.a + self.b+ self.c
'''
class Summator:
	def __init__(self):
		pass
		
	def sum2and2(self):
		return 2+2
		
s = Summator()
print s.sum2and2()
'''
	
s = []
s.append(Figure([Point(0, 0), Point(0,1), Point(1,1), Point(1,0)]))
s.append(Square([Point(0, 0), Point(0,1), Point(1,1), Point(1,0)]))
s.append(Triangle([Point(0, 0), Point(0,1), Point(1,1)]))
for f in s:
	print f.area()
	print f.perimeter()