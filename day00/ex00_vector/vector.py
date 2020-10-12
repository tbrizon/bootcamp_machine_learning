
import numpy as np

class Vector:
	def __init__(self, value):
		if type(value) == list:
			self.value = list(value)
		if type(value) == int:
			self.value = list(x * 1.00 for x in range(0, value))
		if type(value) == tuple:
			try: 
				if len(value) != 2:
					raise ValueError
				else:
					if value[0] < value[1]:
						self.value = list(x * 1.00 for x in range(value[0], value[1]))
					else:
						self.value = list(x * 1.00 for x in range(value[0], value[1], -1))
			except ValueError:
				print("Error : Must have a 2 number of value tuple")
		self.size = len(self.value)
	
	def __add__(self, y):
		try:
			if type(y) == Vector and self.size != y.size:
				raise ValueError
			elif type(y) == Vector:
				result = [self.value[i] + y.value[i] for i in range(self.size)]
				return(Vector(result))
			result = Vector(list(map(lambda x: x + y, self.value)))
			return(result)
		except ValueError:
			print("Error : Add by a same size vectors or with a scalar")
		except TypeError:
			print("Error : class Vector can only get added by an other Vector or a scalar")
	def __radd__(self, y):
		self.__add__(y)
	
	def __sub__(self, y):
		try:
			if type(y) == Vector and self.size != y.size:
				raise ValueError
			elif type(y) == Vector:
				result = [self.value[i] - y.value[i] for i in range(self.size)]
				return(Vector(result))
			result = Vector(list(map(lambda x: x - y, self.value)))
			return(result)
		except ValueError:
			print("Error : Sub by a same size vectors or with a scalar")
		except TypeError:
			print("Error : class Vectors can only get subed by a same size vector or a scalar")
	def __rsub__(self, y):
		try:
			if type(y) == Vector and self.size != y.size:
				raise ValueError
			elif type(y) == Vector:
				result = [y.value[i] - self.value[i] for i in range(self.size)]
				return(Vector(result))
			raise ValueError
		except ValueError:
			print("Error : Vectors has to be the same len, vector can be sub by a scalar but a scalar can't be subbed by a vector")
		except TypeError:
			print("Error : Vectors has to be the same len, vector can be sub by a scalar but a scalar can't be subbed by a vector")

	def __truediv__(self, y):
		try:
			if type(y) == float or type(y) == int:
				result = list(map(lambda x: x / y, self.value))
				return(Vector(result))
			raise ValueError
		except ValueError:
			print("Error : class Vector can only get divided by a scalare")
		except ZeroDivisionError:
			print("Error : Number can't get divided by 0")
	def __rtruediv__(self, y):
		print("Error : Objects can't be divided by class Vector")

	#dot product multiplication
	def __mul__(self, y):
		try:
			if type(y) == int or type(y) == float:
				result = Vector(list(map(lambda x: x * y, self.value))) 
				return (result)
			if type(y) == Vector:
				if y.size != self.size:
					raise ValueError
				else:
					result = sum([self.value[i] * y.value[i] for i in range(self.size)])
					return (result)
			raise TypeError
		except TypeError:
			print("Error : Vectors can only get multiplied by same size vectors or scalar")
		except ValueError:
			print("Error : Vectors can only get multiplied by same size vectors or scalar")
	
	def __str__(self):
		return (str(self.value))

				

if __name__ == "__main__":
	v1 = Vector((10, 15))
	v2 = Vector(5)
	v1 = np.array(v1.value)
	v3 = Vector(list(v1))
	print(v1)
	print(v3)
	pass