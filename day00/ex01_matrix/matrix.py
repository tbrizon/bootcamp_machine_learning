
class Vector:
	def __init__(self, value, filer = None):
		
		if type(value) == list:
			self.value = list(value)
		if type(value) == int and filer == None:
			self.value = list(x * 1.00 for x in range(0, value))
		if type(value) == int and type(filer) == int:
			self.value = [filer * 1.00 for x in range(0, value)]
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




######## MATRIX CLASS ########


#Creer des matrices a l'aide de listes.
#Si vectored est mis a "Yes", les lignes de la matrice sont formee de classes vector. ça sert un peu a r mais bon
#
"""
class Matrix:
	def __init__(self, *args, filer = None, vectored = None):
		self.shape = [0,0]
		self.value = []
		size = sorted((element for element in args if type(element) is tuple))
		try:
			if len(size) == 1:
				self.shape[0] = size[0][0]
				self.shape[1] = size[0][1]
			elif len(size) > 1:
				raise ValueError
			for arg in args:
				if type (arg) != list and type(arg) != tuple:
					raise ValueError
				if type(arg) == list: 
					if self.shape[0] == 0:
						self.shape[0] = len(arg)
						self.shape[1] = len(arg[0])
					if vectored == "Yes":
						self.value = [Vector(arg[i]) for i in range(self.shape[0])]
					else:
						self.value = [arg[i] for i in range(self.shape[0])]
				if type(arg) == tuple and not self.value and filer == None:
					self.value = [[0 for j in range(arg[1])] for i in range(arg[0])]
				if type(arg) == tuple and not self.value and filer != None:
					self.value = [[filer for j in range(arg[1])] for i in range(arg[0])]
		except ValueError:
			print("Matrix must be filled by list, tupe or class Vector. Size is automatically return but your matrix can be reshaped")
			print("shape of a matrix is defined by one and only one  (m, n) tuple")
		

"""

# je mets dans une variable le tuple
# je mets dans une autre variable la liste de liste
# Si il y a autre chose que ça je raise ValueError

class Matrix:
	def __init__(self, *args, Filer = None, Vectored = None):
		try:
			size= sorted(element for element in args if type(element) is tuple)
			self.value = sorted(element for element in args if type(element) is list)
			error = sorted(element for element in args if type(element) is not list and type(element) is not tuple)
			if size[0] != None: #gestion du tuple
				if len(size[0]) != 2 or len(size) != 1:
					error = size
					raise ValueError
			if len(error) != 0:
				raise TypeError
			
		
		except TypeError:
			print("Error with arguments {}, Matrix class must only contain :".format(error))
			print("A list of vector, a tupe of len 2 for the size and eventually Filer and Vectored unset to 'none'")
		except ValueError:
			print("Error value with arguments {}, Matrix class arguments are :".format(error))
			print("A (m,n) single tuple for the size of the vector and same size vectors. Options are:")
			print("Filer = int(x) to file youre matrix with x and Vectored = 'Yes' to create Class Vector each lines of your matrix instead of list")

		
		print(len(self.value))
		print(self.value)



if __name__ == "__main__":
	m1 = Matrix([[1, 2, 3], [3, 2, 0], [2, 4, 6], [0, 0, 0]], (4,4), Filer = "yes", Vectored = "no")

	
	
	
	pass