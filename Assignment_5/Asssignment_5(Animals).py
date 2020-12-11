class Animal(object):

	def __init__(self, name, colour):
		self.name = name
		self.colour = colour
		
	def introduce(self):
		print('\nMy name is', self.name, 'and I am', self.species(), '\nMy colour is', self.colour, '\nI say', self.sound(), '\nI live', self.home(), '\nI eat', self.food())
	
	
class wild_animal(Animal):

	def home(self):
		return 'in Jungle.'
		
		
class pet_animal(Animal):

	def home(self):
		return 'with Humans.'


class carnivorous(Animal):

	def food(self):
		return 'Meat.'
		
		
class herbivorous(Animal):

	def food(self):
		return 'grass, fruits, vegetables etc.'


class omnivorous(Animal):

	def food(self):
		return 'both non-veg and veg.'
		
		
class dog(pet_animal, omnivorous):

	def __init__(self, name, colour):
		super().__init__(name, colour)
		
	def sound(self):
		return 'bark.'
		
	def species(self):
		return 'dog.'
		
		
class cat(pet_animal, omnivorous):

	def __init__(self, name, colour):
		super().__init__(name, colour)
		
	def sound(self):
		return 'meow.'
		
	def species(self):
		return 'cat.'
		
		
class cow(pet_animal, herbivorous):

	def __init__(self, name, colour):
		super().__init__(name, colour)
		
	def sound(self):
		return 'moo.'
		
	def species(self):
		return 'cow.'
		
		
class tiger(wild_animal, carnivorous):

	def __init__(self, name, colour):
		super().__init__(name, colour)
		
	def sound(self):
		return 'roar.'
		
	def species(self):
		return 'tiger.'
		
		
class horse(pet_animal, herbivorous):

	def __init__(self, name, colour):
		super().__init__(name, colour)
		
	def sound(self):
		return 'neigh.'
		
	def species(self):
		return 'horse.'
		
		
class elephant(wild_animal, herbivorous):

	def __init__(self, name, colour):
		super().__init__(name, colour)
		
	def sound(self):
		return 'trumpet.'
		
	def species(self):
		return 'elephant.'
	

class deer(wild_animal, herbivorous):

	def __imit__(self, name, colour):
		super().__init__(name, colour)
		
	def sound(self):
		return 'bellow.'
		
	def species(self):
		return 'deer.'
		


class sheep(pet_animal, herbivorous):

	def __imit__(self, name, colour):
		super().__init__(name, colour)
		
	def sound(self):
		return 'bleat.'
		
	def species(self):
		return 'sheep.'
		
		
class zebra(wild_animal, herbivorous):

	def __imit__(self, name, colour):
		super().__init__(name, colour)
		
	def sound(self):
		return 'neigh.'
		
	def species(self):
		return 'zebra.'
		
		
class bear(wild_animal, carnivorous):

	def __init__(self, name, colour):
		super().__init__(name, colour)
		
	def sound(self):
		return 'bear.'
		
	def species(self):
		return 'growl.'
		
		
		
a = cat('Tom', 'white')
b = tiger('Max', 'Orange with black stipes')
c = dog('Sweety', 'black')
d = cow('Bella', 'black and white')
e = horse('Rose', 'White')
f = elephant('Jumbo', 'grey')
g = deer('Lily', 'reddish brown')
h = sheep('Shaun', 'white')
i = zebra('Sam','black and white stripes')
j = bear('Jack', 'black')
a.introduce()
b.introduce()
c.introduce()
d.introduce()
e.introduce()
f.introduce()
g.introduce()
h.introduce()
i.introduce()
j.introduce()




		
	
