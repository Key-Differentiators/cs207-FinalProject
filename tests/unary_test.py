# unary_test.py

import pytest
import numpy as np
from keydifferentiator import AD as ad
from keydifferentiator import unary

def test_neg_AD():
	x = unary.neg(ad.AD(5.0))
	y = ad.AD(-5.0, -1.0)
	assert (x == y)

def test_neg_num():
	assert(unary.neg(5.0) == -5.0)

def test_sqrt_AD():
	x = unary.sqrt(ad.AD(4.0))
	y = ad.AD(2.0, 1/4)
	assert (x == y)

def test_sqrt_num():
	assert(unary.sqrt(4.0) == np.sqrt(4.0))

def test_ln_AD():
	assert (unary.ln(ad.AD(4.0)).val == pytest.approx(1.3862, 0.001))
	assert (unary.ln(ad.AD(4.0)).der == pytest.approx(0.25, 0.001))

def test_ln_num():
	assert(unary.ln(4.0) == np.log(4.0))

def test_sin_AD():
	assert(unary.sin(ad.AD(3.0)).val == pytest.approx(0.1411, 0.001))
	assert(unary.sin(ad.AD(0.5)).der == pytest.approx(0.8775, 0.001))

def test_sin_num():
	assert(unary.sin(3.0) == pytest.approx(0.1411, 0.001))

def test_cos_AD():
	assert(unary.cos(ad.AD(5.0)).val == pytest.approx(0.2836, 0.001))
	assert(unary.cos(ad.AD(0.5)).der == pytest.approx(-0.4794, 0.001))

def test_cos_num():
	assert(unary.cos(5.0) == pytest.approx(0.2836, 0.001))

def test_tan_AD():
	assert(unary.tan(ad.AD(5.0)).val == pytest.approx(-3.3805, 0.001))
	assert(unary.tan(ad.AD(0.5)).der == pytest.approx(1.2984, 0.001))

def test_tan_num():
	assert(unary.tan(5.0) == pytest.approx(-3.3805, 0.001))

def test_arcsin_AD():
	assert(unary.arcsin(ad.AD(0.5)).val == pytest.approx(0.5235, 0.001))
	assert(unary.arcsin(ad.AD(0.5)).der == pytest.approx(1.1547, 0.001))

def test_arcsin_num():
	assert(unary.arcsin(0.5) == pytest.approx(0.5235, 0.001))

def test_arccos_AD():
	assert(unary.arccos(ad.AD(0.5)).val == pytest.approx(1.0472, 0.001))
	assert(unary.arccos(ad.AD(0.5)).der == pytest.approx(-1.1547, 0.001))

def test_arccos_num():
	assert(unary.arccos(0.5) == pytest.approx(1.0472, 0.001))

def test_arctan_AD():
	assert(unary.arctan(ad.AD(0.5)).val == pytest.approx(0.4636, 0.001))
	assert(unary.arctan(ad.AD(0.5)).der == pytest.approx(0.8, 0.001))

def test_arctan_num():
	assert(unary.arctan(0.5) == pytest.approx(0.4636, 0.001))

def test_sinh_AD():
	assert(unary.sinh(ad.AD(0.5)).val == pytest.approx(0.5210, 0.001))
	assert(unary.sinh(ad.AD(0.5)).der == pytest.approx(1.1276, 0.001))

def test_sinh_num():
	assert(unary.sinh(0.5) == pytest.approx(0.5210, 0.001))

def test_cosh_AD():
	assert(unary.cosh(ad.AD(0.5)).val == pytest.approx(1.1276, 0.001))
	assert(unary.cosh(ad.AD(0.5)).der == pytest.approx(0.5210, 0.001))

def test_cosh_num():
	assert(unary.cosh(0.5) == pytest.approx(1.1276, 0.001))

def test_tanh_AD():
	assert(unary.tanh(ad.AD(0.5)).val == pytest.approx(0.4621, 0.001))
	assert(unary.tanh(ad.AD(0.5)).der == pytest.approx(0.7864, 0.001))

def test_tanh_num():
	assert(unary.tanh(0.5) == pytest.approx(0.4621, 0.001))

def test_sub_unary():
	x = ad.AD(2.0)
	assert((unary.cos(x**2) - unary.cos(x**2)) == ad.AD(0.0, 0.0))

def test_sqrt_pow():
	x = ad.AD(4.0)
	print(unary.sqrt(x**2).val)
	print(unary.sqrt(x**2).der)
	assert(unary.sqrt(x**2) == ad.AD(4.0, 1.0))
