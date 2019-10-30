# AD.py

class AD():

	def __init__(self, val, der=1.0):
		self.val = val
		self.der = der

	def __str__(self):
		return "f(x)= %s f'(x) %s" % (str(self.val), str(self.der))

	def __eq__(self, other):
		return (self.val == other.val)

	def __add__(self, other):
		try:
			return AD(self.val + other.val, self.der)
		except AttributeError:
			return AD(self.val + other, self.der)

	def __radd__(self, other):
		return self.__add__(other)

	def __mul__(self, other):
		try:
			return AD(self.val * other.val, self.val*other.der + self.der*other.val)
		except AttributeError:
			return AD(self.val * other, self.der * other)

	def __rmul__(self, other):
		return self.__mul__(other)

	def __sub__(self, other):
		return NotImplementedError

	def __rsub__(self, other):
		return NotImplementedError
		
	def __truediv__(self, other):
		return NotImplementedError

	def __rtruediv__(self, other):
		return NotImplementedError

	def __pow__(self, pow):
		return NotImplementedError

	def __rpow__(self, pow):
		return NotImplementedError

	def log(x):
		return NotImplementedError

	def ln(x):
		return NotImplementedError

	def sqrt(x):
		return NotImplementedError

	def sin(x):
		return NotImplementedError

	def cos(x):
		return NotImplementedError

	def tan(x):
		return NotImplementedError

	def arcsin(x):
		return NotImplementedError

	def arccos(x):
		return NotImplementedError

	def arctan(x):
		return NotImplementedError 

	def sinh(x):
		return NotImplementedError

	def cosh(x):
		return NotImplementedError

	def tanh(x):
		return NotImplementedError
