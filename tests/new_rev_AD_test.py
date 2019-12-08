# new_rev_Rev_test.py

# AD_test.py

import pytest
import numpy as np
from keydifferentiator.Reverse import *

def test_add_Rev_Rev():
	x = Reverse(2.0) + Reverse(3.0)
	print(x)
	y = Reverse(5.0)
	assert(x == y)

def test_add_Rev_reg():
	x = Reverse(2.0) + 3
	y = Reverse(5.0)
	assert(x == y)

def test_add_reg_Rev():
	x = 2 + Reverse(1.0)
	y = Reverse(3.0)
	assert(x == y)

def test_mult_Rev_Rev():
	x = Reverse(2.0) * Reverse(1.0)
	y = Reverse(2.0)
	assert(x == y)

def test_mult_Rev_reg():
	x = Reverse(2.0) * 2.0
	y = Reverse(4.0)
	assert(x == y)

def test_mult_reg_Rev():
	x = 2 * Reverse(1.0)
	y = Reverse(2.0)
	assert(x == y)

def test_sub_Rev_Rev():
	x = Reverse(2.0) - Reverse(1.0)
	y = Reverse(1.0)
	assert(x == y)

def test_sub_Rev_reg():
	x = Reverse(2.0) - 1.0
	y = Reverse(1.0)
	assert(x == y)

def test_sub_reg_Rev():
	x = 2 - Reverse(1.0)
	y = Reverse(1.0)
	assert(x == y)

def test_truediv_Rev_Rev():
	x = Reverse(6.0) / Reverse(3.0)
	y = Reverse(2.0)
	assert(x == y)

def test_truediv_Rev_reg():
	x = Reverse(6.0) / 3.0
	y = Reverse(2.0)
	assert(x == y)

def test_truediv_reg_Rev():
	x = 2 / Reverse(1.0)
	y = Reverse(2.0)
	assert(x == y)

def test_pow_Rev_Rev():
	x = Reverse(2.0)**Reverse(2.0)
	assert(x.value == 4.0)

def test_pow_Rev_reg():
	x = Reverse(2.0)**2
	y = Reverse(4.0)
	assert(x == y)	

def test_pow_reg_Rev():
	x = 2**Reverse(2.0)
	assert(x.value == 4.0)

def test_add_radd_mult_rmult():
	x = Reverse(2.0)
	alpha = 2.0
	beta = 3.0

	functions = []
	functions.append(('alpha * x + beta', alpha * x + beta))
	functions.append(('x * alpha + beta', x * alpha + beta))
	functions.append(('beta + alpha * x', beta + alpha * x))
	functions.append(('beta + x * alpha', beta + x * alpha))

	for (name, value) in functions:
		assert (value.value == 7)

def test_linear_combos():
	x = Reverse(3.0)
	eq = x**2 + x
	y = Reverse(12.0)
	assert(eq == y)

def test_identity():
	x = Reverse(3.0)
	eq = (2 * x) / (2 * x)
	y = Reverse(1.0)
	assert(eq == y)

