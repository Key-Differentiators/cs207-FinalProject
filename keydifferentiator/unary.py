# unary.py

import numpy as np
import keydifferentiator.AD as ad

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
	try:
		return ad.AD(np.tan(x.val), x.der*(np.cos(x.val)**2+np.sin(x.val)**2)/(np.cos(x.val)**2))
	except AttributeError:
		return np.tan(x)

def arcsin(x):
	try:
		return ad.AD(np.arcsin(x.val), x.der/np.sqrt(1-x.val**2))
	except AttributeError:
		return np.arcsin(x)

def arccos(x):
	try:
		return ad.AD(np.arccos(x.val), -1*x.der/np.sqrt(1-x.val**2))
	except AttributeError:
		return np.arccos(x)

def arctan(x):
	try:
		return ad.AD(np.arctan(x.val), x.der/(1+x.val**2))
	except AttributeError:
		return np.arctan(x)

def sinh(x):
	try:
		return ad.AD(np.sinh(x.val), x.der*np.cosh(x.val))
	except AttributeError:
		return np.sinh(x)

def cosh(x):
	try:
		return ad.AD(np.cosh(x.val), x.der*np.sinh(x.val))
	except AttributeError:
		return np.cosh(x)

def tanh(x):
	try:
		return ad.AD(np.tanh(x.val), x.der*(1-np.tanh(x.val)**2))
	except AttributeError:
		return np.tanh(x)
