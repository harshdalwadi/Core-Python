'''
Types of variables
1. Instance variable
2. Class(static) variable
'''

class car:
	def __init__(self):
		self.company = 'FORD'
		self.color = 'Red'
		self.mileage = 20

c1 = car()
c2 = car()

c1.company = "BMW"
print(c1.company,c1.color,c1.mileage)
print(c2.company,c2.color,c2.mileage)

'''
-> In this, if we change one object, it does not affect on other object
-> if we want to change it globally, we should define it outside

Define variable outside __init__ -> Class Variable
Define variable inside __init__ -> Instance Varibale
'''

class car:
	wheel = 4

	def __init__(self):
		self.company = 'FORD'
		self.color = 'Red'
		self.mileage = 20

c1 = car()
c2 = car()

c1.company = "BMW"
print(c1.company,c1.color,c1.mileage,c1.wheel)
print(c2.company,c2.color,c2.mileage,c2.wheel)

'''
Namespace : Area where you create and store object/variable.

2 Types of namespace:
1) Class namespace
2) Object/Instance namespace


class car:
	wheel = 4  ->  Class Namespace

	def __init__(self):
		self.company = 'FORD' }
		self.color = 'Red'	  }  INSTANCE Namespace
		self.mileage = 20	  }
'''

class car:
	wheel = 4

	def __init__(self):
		self.company = 'FORD'
		self.color = 'Red'
		self.mileage = 20

c1 = car()
c2 = car()

car.wheel = 8

c1.company = "BMW"
print(c1.company,c1.color,c1.mileage,c1.wheel)
print(c2.company,c2.color,c2.mileage,c2.wheel)