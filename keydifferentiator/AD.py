# AD.py

class AD():

	def __init__(self, val, der=1.0):
		self.val = val
		self.der = der

	def __str__(self):
		return "f(x)={:.2f}, f'(x)={:.2f}".format(self.val, self.der)

	def __eq__(self, other):
		return (self.val == other.val and self.der == other.der)

	def __add__(self, other):
		try:
			return AD(self.val + other.val, self.der + other.der)
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
		try:
			return AD(self.val - other.val, self.der - other.der)
		except AttributeError:
			return AD(self.val - other, self.der)

	def __rsub__(self, other):
		try:
			return AD(self.val -  other.val, self.der -  other.der)
		except AttributeError:
			return AD(other - self.val, self.der)
		
	def __truediv__(self, other):
		try:
			return AD(self.val / other.val, (self.der * other.val - self.val * other.der)/(other.val)**2)
		except AttributeError:
			return AD(self.val / other, self.der / other)

	def __rtruediv__(self, other):
		return AD(other / self.val, -(other * self.der) / self.val ** 2)

	def __pow__(self, other):
		try:
			return AD(self.val**other.val, (self.val**other.val) * ((other.val / self.val * self.der) + (other.der * np.log(self.val))))
		except AttributeError:
			return AD(self.val**other, other * (self.val**(other - 1)) * self.der)

	def __rpow__(self, other):
		return AD(other**self.val, self.der * np.log(other) * other**self.val)

