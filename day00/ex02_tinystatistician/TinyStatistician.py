
import numpy as np

class TinyStatistician:
	def __init__(self):
		pass
	def mean(x):
		if type(x) == list:
			return (sum(x)/ len(x))
		else:
			return None
	#tri la suite puis prend la n eme valeure telle que n * 2 = len(a)
	def median(x):
		if type(x) == list:
			x.sort()
			size = len(x) - 1
			if size % 2 == 0:
				return x[int(size / 2)]
			else:
				indice = size / 2 + 0.5 
				return (x[int(indice)])
		else:
			return None
	def quartile(x, pourcentile):
		if type(x) == list:
			x.sort()
			size = len(x) - 1
			index = (size * pourcentile) / 100
			return(x[round(index)])
		else:
			return None
	def variance(x):
		if type(x) == list:
			mean = TinyStatistician.mean(x)
			res = sum([(i - mean)**2 for i in x])/len(x) 
			return (res)
		else:
			return None
	def std(x):
		if type(x) == list:
			return (TinyStatistician.variance(x)**0.5)
		return None


if __name__ == "__main__":
	a = [1, 42, 300, 10, 59, 42,342,4]
	b = np.std(a)
	print(b)
	tst = TinyStatistician
	print(tst.std(a))
	pass