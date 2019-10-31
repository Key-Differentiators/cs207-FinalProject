# unary.py
import numpy as np
from src.AD import AD as ad

def ln(x):
	try:
		return ad.AD(np.log(x.val), x.der / x.val)
	except:
		return np.log(x)

def sqrt(x):
	try:
		return ad.AD(np.sqrt(x.val), 0.5 * x.der / np.sqrt(x.val))
	except AttributeError:
		return np.sqrt(x)

def sin(x):
	try:
		return ad.AD(np.sin(x.val), x.der * np.cos(x.val))
	except AttributeError:
		return np.sin(x)

def cos(x):
	try:
		return ad.AD(np.cos(x.val), -1 * x.der * np.sin(x.val))
	except AttributeError:
		return np.cos(x)

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