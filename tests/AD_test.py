# AD_test.py

import pytest
import numpy as np
from src.AD import AD

def test_add():
	x = AD.AD(2.0) + AD.AD(1.0)
	y = AD.AD(3.0)
	assert(x == y)

def test_radd():
	x = 2 + AD.AD(1.0)
	y = AD.AD(3.0)
	assert(x == y)

def test_mult():
	x = AD.AD(2.0) * AD.AD(1.0)
	y = AD.AD(2.0)
	assert(x == y)

def test_rmult():
	x = 2 * AD.AD(1.0)
	y = AD.AD(2.0)
	assert(x == y)

def test_sub():
	x = AD.AD(2.0) - AD.AD(1.0)
	y = AD.AD(1.0)
	assert(x == y)

def test_rsub():
	x = 2 - AD.AD(1.0)
	y = AD.AD(1.0)
	assert(x == y)

def test_truediv():
	x = AD.AD(2.0) / AD.AD(1.0)
	y = AD.AD(2.0)
	assert(x == y)

def test_rtruediv():
	x = 2 / AD.AD(1.0)
	y = AD.AD(2.0)
	assert(x == y)

def test_pow():
	x = AD.AD(2.0)**2
	y = AD.AD(4.0)
	assert(x == y)	

def test_rpow():
	x = 2**AD.AD(2.0)
	y = AD.AD(4.0)
	assert(x == y)

def test_sqrt_AD():
	x = sqrt(AD.AD(4.0))
	y = AD.AD(2.0)
	assert (x == y)

def test_sqrt_num():
	assert(sqrt(4.0) == np.sqrt(4.0))

# def test_ln_AD():

# def test_ln_num():

# def test_sin_AD():

# def test_sin_num():

# def test_cos_AD():

# def test_cos_num():

def test_add_radd_mult_rmult():
	x = AD.AD(2.0)
	alpha = 2.0
	beta = 3.0

	functions = []
	functions.append(('alpha * x + beta', alpha * x + beta))
	functions.append(('x * alpha + beta', x * alpha + beta))
	functions.append(('beta + alpha * x', beta + alpha * x))
	functions.append(('beta + x * alpha', beta + x * alpha))

	for (name, val) in functions:
		assert (val.val == 7)
		assert (val.der == 2)