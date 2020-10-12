import numpy as np

def	simple_predict(x, theta):
	"""Computes the vector of prediction y_hat from two non-empty numpy.ndarray.
	Args:
	  x: has to be an numpy.ndarray, a vector of dimension m * 1.
	  theta: has to be an numpy.ndarray, a vector of dimension 2 * 1.
	Returns:
	  y_hat as a numpy.ndarray, a vector of dimension m * 1.
	  None if x or theta are empty numpy.ndarray.
	  None if x or theta dimensions are not appropriate.
	Raises:
	  This function should not raise any Exception.
	"""
	pass



if __name__ == "__main__":
	theta1 = np.array([5, 0])
	theta2 = np.array([0, 1])
	theta3 = np.array([5, 3])
	theta4 = np.array([-3, 1])
	x = np.arange(1, 6)

	print(theta1, theta2,theta3,theta4)
	print(x)
	pass