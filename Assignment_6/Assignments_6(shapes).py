import turtle
import math

t = turtle.Turtle()
t.speed(0)
t.color('red')


class shape(object):
	
	def area(self):
		pass
		
	def perimeter(self):
		pass
		
	def draw(self):
		pass

		
	def info(self):
		print('\n',self.shape(), '\nArea: {:.2f}'.format(self.area()), '\nPerimeter: {:.2f}'.format(self.perimeter()))
		

		
	
class square(shape):

	def __init__(self, side):
		self.side = side
        	
	def shape(self):
		return 'Square'
        	
	def area(self):
        	return self.side * self.side
        	
	def perimeter(self):
        	return 4 * self.side
        	
	def draw(self):
        	t.forward(self.side)
        	t.left(90)
        	t.forward(self.side)
        	t.left(90)
        	t.forward(self.side)
        	t.left(90)
        	t.forward(self.side)
        	t.left(90)
        	turtle.done()
        	
class rectangle(shape):

	def shape(self):
		return 'Rectangle'
	
	def __init__(self, l, w):
		self.len = l
		self.wid = w
		
	def area(self):
		return self.len*self.wid
		
	def perimeter(self):
		return 2 * self.len + 2 * self.wid
		
	def draw(self):
		t.forward(self.len)
		t.left(90)
		t.forward(self.wid)
		t.left(90)
		t.forward(self.len)
		t.left(90)
		t.forward(self.wid)
		t.left(90)
		turtle.done()
		
		
class circle(shape):

	def shape(self):
		return 'Circle'
		
	def __init__(self, r):
		self.rad = r
		
	def area(self):
		return math.pi * self.rad * self.rad
		
	def perimeter(self):
		return 2 * math.pi * self.rad
		
	def draw(self):
		t.circle(self.rad)
		turtle.done()
		
		
class hexagon(shape):

	def shape(self):
		return 'Hexagon'
		
	def __init__(self, side):
        	self.side = side
        	
	def area(self):
        	return 3 * math.sqrt(3) * self.side * self.side / 2
        	
	def perimeter(self):
        	return 6 * self.side
        	
	def draw(self):
        	for i in range(6):
        		t.forward(self.side)
        		t.left(300)
        	turtle.done()
		
		
class eq_triangle(shape):
	
	def __init__(self, side):
        	self.side = side
        	
	def shape(self):
		return 'Equilateral triangle'
		
	def area(self):
		return math.sqrt(3) * self.side * self.side
		
	def perimeter(self):
		return 3 * self.side
		
	def draw(self):
		t.forward(self.side)
		t.left(120)
		t.forward(self.side)
		t.left(120)
		t.forward(self.side)
		turtle.done()
		
	
        	

s = square(100)
s.info()
#s.draw()

r = rectangle(100, 50)
r.info()
#r.draw()

c = circle(100)
c.info()
#c.draw()

h = hexagon(100)
h.info()
h.draw()

tri = eq_triangle(100)
tri.info()
#tri.draw()
        
