# AD_test.py

import pytest
import numpy as np
from keydifferentiator import AD
from keydifferentiator import unary

def test_invalid_init():
	x = AD.AD(3.0)
	with pytest.raises(TypeError, match="Invalid input type"):
		assert AD.AD(x)

def test_str():
	x = AD.AD(3.0)
	assert(str(x)=='AD(3.0, [1.])')

def test_jacobian():
	x = AD.AD(3.0, [1.0,0.0,0.0])
	y = AD.AD(2.0, [0.0,1.0,0.0])
	z = AD.AD(1.0, [0.0,0.0,1.0])
	vals, ders = AD.AD.get_jacobian([x*y, x+y, z, unary.sin(x)])
	test_jac = np.array([[2.0,3.0,0.0],[1.0,1.0,0.0],[0.0,0.0,1.0],[np.cos(3.0),0.0,0.0]])
	assert(vals[0]==6.0)
	assert(vals[2]==1.0)
	assert(np.array_equal(ders, test_jac))

def test_jacobian_exception():
	x = AD.AD(3.0)
	y = AD.AD(2.0, [0.0,1.0])
	with pytest.raises(Exception, match="Incorrect dimension"):
		assert AD.AD.get_jacobian([x,y])
	with pytest.raises(TypeError, match="Invalid input type: not a function"):
		assert AD.AD.get_jacobian([x,3.0])
	with pytest.raises(Exception, match="Empty list of functions"):
		assert AD.AD.get_jacobian([])

def test_add_AD_AD():
	x = AD.AD(2.0) + AD.AD(3.0)
	y = AD.AD(5.0, 2.0)
	assert(x == y)

def test_add_AD_reg():
	x = AD.AD(2.0) + 3
	y = AD.AD(5.0, 1.0)
	assert(x == y)

def test_add_reg_AD():
	x = 2 + AD.AD(1.0)
	y = AD.AD(3.0, 1.0)
	assert(x == y)

def test_mult_AD_AD():
	x = AD.AD(2.0) * AD.AD(1.0)
	y = AD.AD(2.0, 3.0)
	assert(x == y)

def test_sub_AD_AD():
	x = AD.AD(2.0) - AD.AD(1.0)
	y = AD.AD(1.0, 0.0)
	assert(x == y)

def test_sub_AD_reg():
	x = AD.AD(2.0) - 1.0
	y = AD.AD(1.0, 1.0)
	assert(x == y)

def test_sub_reg_AD():
	x = 2 - AD.AD(1.0)
	y = AD.AD(1.0, -1.0)
	assert(x == y)

def test_mult_AD_reg():
	x = AD.AD(2.0) * 2.0
	y = AD.AD(4.0, 2.0)
	assert(x == y)

def test_mult_reg_AD():
	x = 2 * AD.AD(1.0)
	y = AD.AD(2.0, 2.0)
	assert(x == y)

def test_truediv_AD_AD():
	x = AD.AD(6.0) / AD.AD(3.0)
	y = AD.AD(2.0, -1/3)
	assert(x == y)

def test_truediv_AD_reg():
	x = AD.AD(6.0) / 3.0
	y = AD.AD(2.0, 1/3)
	assert(x == y)

def test_truediv_reg_AD():
	x = 2 / AD.AD(1.0)
	y = AD.AD(2.0, -2.0)
	assert(x == y)

def test_truediv_zero_deno():
	with pytest.raises(Exception, match="Zero cannot be denominator"):
		assert AD.AD(2.0)/0
	with pytest.raises(Exception, match="Zero cannot be denominator"):
		assert AD.AD(2.0)/AD.AD(0.0)

def test_pow_AD_reg():
	x = AD.AD(2.0)**2
	y = AD.AD(4.0, 4.0)
	assert(x == y)	

def test_pow_reg_AD():
	x = 2**AD.AD(2.0)
	assert(x.val == 4.0)
	assert(x.der == pytest.approx(4.0 * np.log(2.0)))

def test_zero_pow():
	x = AD.AD(0.0)**3
	assert(x.val == 0.0)

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

def test_eq():
	x = AD.AD(3.0)
	y = 3.0
	assert (x==y)

def test_ne():
	x = AD.AD(3.0, [1.0,0.0])
	y = AD.AD(3.0)
	assert (x!=y)

def test_neg():
	x = AD.AD(3.0, [1.0,0.0])
	y = AD.AD(2.0, [0.0,1.0])
	f = -x*y
	assert(f.val == -6.0)
	assert(np.array_equal(f.der,np.array([-2.0,-3.0])))

def test_linear_combos():
	x = AD.AD(3.0)
	eq = x**2 + x
	y = AD.AD(12.0, 7.0)
	assert(eq == y)

def test_identity():
	x = AD.AD(3.0)
	eq = (2 * x) / (2 * x)
	y = AD.AD(1.0, 0.0)
	assert(eq == y)

