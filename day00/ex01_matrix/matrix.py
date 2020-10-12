from vector import Vector

######## MATRIX CLASS ########

# je mets dans une variable le tuple
# je mets dans une autre variable la liste de liste
# Si il y a autre chose que ça je raise ValueError

class Matrix:
	def __init__(self, *args, Filer = 0, Vectored = None):
		self.shape = []
		self.value = []
		try:
			size= sorted(element for element in args if type(element) is tuple)
			content = sorted(element for element in args if type(element) is list)
			error_args = sorted(element for element in args if type(element) is not list and type(element) is not tuple)
			if len(size) != 0: #gestion du tuple
				if len(size[0]) != 2 or len(size) != 1:
					error_args.append(size)
					raise ValueError
				if size[0][1] < 0 or size[0][0] < 0:
					error_args.append(size)
					raise ValueError
				self.shape = size[0]
			if len(content) != 0: #gestion des listes
				if len(content) != 1:
					error_args.append(content)
				else:
					for x in content[0]:
						if len(x) != len(content[0][0]):
							error_args.append(content)
							raise ValueError
					if len(self.shape) == 0:
						self.shape.append(len(content[0]))
						self.shape.append(len(content[0][0]))
					content = content[0]
					self.value = [[content[y][x] * 1.00 for x in range(self.shape[1])] for y in range(self.shape[0])]
			if len(error_args) != 0:
				raise EnvironmentError
			if len(content) == 0 and len(size) > 0:
				self.value = [[Filer * 1.00 for x in range(size[0][1])] for y in range(size[0][0])]
				self.shape = size[0]

		except ValueError:
			print("Error with arguments {}, Matrix class must only contain :".format(error_args))
			print("A list of vector, a tupe of len 2 for the POSITIVE size and eventually Filer and Vectored unset to 'none'")
			print("All raw must have the same size")
			self.shape = (0,0)
			self.value = None
			return(None)
		except EnvironmentError:
			print("Error value with arguments {}, Matrix class arguments are :".format(error_args))
			print("A (m,n) single tuple for the size of the vector and same size vectors. Options are:")
			print("Filer = int(x) to file youre matrix with x and Vectored = 'Yes' to create Class Vector each lines of your matrix instead of list")
			self.shape = (0,0)
			self.value = None
			return(None)
	
	def __add__(self, m2):
		try:
			if type(m2) == list:
				m2 = Matrix(m2)
				print(m2)
			if type(m2) == Matrix:
				if self.shape[0] == m2.shape[0] and self.shape[1] == m2.shape[1]:
					res = [[self.value[y][x] + m2.value[y][x] for x in range(self.shape[1])] for y in range(self.shape[0])]
					return(Matrix(res))
			raise ValueError
		except ValueError:
			print("Arguments must be the same size")
	
	def __radd__(self, m2):
		__add__(m2)

	def __sub__(self, m2):
		try:
			if type(m2) == list:
				m2 = Matrix(m2)
				print(m2)
			if type(m2) == Matrix:
				if self.shape[0] == m2.shape[0] and self.shape[1] == m2.shape[1]:
					res = [[self.value[y][x] - m2.value[y][x] for x in range(self.shape[1])] for y in range(self.shape[0])]
					return(Matrix(res))
			raise ValueError
		except ValueError:
			print("Arguments must be the same size")

	def __rsub__(self, m2):
		try:
			if type(m2) == list:
				m2 = Matrix(m2)
				print(m2)
			if type(m2) == Matrix:
				if self.shape[0] == m2.shape[0] and self.shape[1] == m2.shape[1]:
					res = [[m2.value[y][x] - self.value[y][x] for x in range(self.shape[1])] for y in range(self.shape[0])]
					return(Matrix(res))
			raise ValueError
		except ValueError:
			print("Arguments must be the same size")

	def __truediv__(self, scalar):
		try:
			if type(scalar) == int or type(scalar) == float:
				res = [list(map(lambda x: x / scalar, self.value[y])) for y in range(self.shape[0])]
				return (res)
			raise ValueError
		except ValueError:
			print("You can only divide a matrix by a scalar")

	def __rtruediv__(self, scalar):
		__truediv__(scalar)

	#we can multiply an n × m matrix by an m×p matrix
	def __mul__(self, m2):
		try:
			if type(m2) == int or type(m2) == float:
				res = [list(map(lambda x: x * m2, self.value[y])) for y in range(self.shape[0])]
			if type(m2) == list:
				m2 = Matrix(m2)
			if type(m2) == Vector:
				if self.shape[1] == m2.size:
					res = [[sum(value[y][x] * m2.value[x] for x in range(self.shape[1]))] for value in self.value]
					return(Matrix(res))
			if type(m2) == Matrix:
				if self.shape[1] == m2.shape[0]:						
					res = [[sum([value[k]*m2.value[k][j] for k in range(self.shape[1])]) for j in range(m2.shape[1])] for value in self.value]
					return (Matrix(res))
			raise ValueError
		except ValueError:
			print("blabla")
		def __rmul__(self, m2):
			try:
				if type(m2) == int or type(m2) == float:
					res = [list(map(lambda x: x * m2, self.value[y])) for y in range(self.shape[0])]
				if type(m2) == list:
					m2 = Matrix(m2)
				if type(m2) == Vector:
					if self.shape[1] == m2.size:
						res = [[sum(value[y][x] * m2.value[x] for x in range(self.shape[1]))] for value in self.value]
						return(res)
				if type(m2) == Matrix:
					if self.shape[1] == m2.shape[0]:
						res = [[sum([value[k]*m2.value[k][j] for k in range(self.shape[1])]) for j in range(m2.shape[1])] for value in self.value]
						return (Matrix(res))
				raise ValueError
			except ValueError:
				print("blabla")

		def __str__(self):
			res = "Matrix {}".format(self.value)
			return(res)
		
		def __repr__(self):
			res = "Matrix {}".format(self.value)
			return (res)
if __name__ == "__main__":
	m1 = Matrix([[5,1],[2,3], [3,4]] ,Vectored = "no")	
	m2 = Matrix([[1,2,0],[4,3,-1]])
	print(m1.value)
	
	
	pass