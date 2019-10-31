# unary_test.py

import pytest
import numpy as np
from src.AD import AD as ad
from src.AD import unary

def test_sqrt_AD():
	x = unary.sqrt(ad.AD(4.0))
	y = ad.AD(2.0, 1/4)
	assert (x == y)

def test_sqrt_num():
	assert(unary.sqrt(4.0) == np.sqrt(4.0))

def test_ln_AD():
	assert (unary.ln(ad.AD(4.0)).val == pytest.approx(1.3862, 0.001))
	assert (unary.ln(ad.AD(4.0)).der == 1/4)

def test_ln_num():
	assert(unary.ln(4.0) == np.log(4.0))

def test_sin_AD():
	assert(unary.sin(ad.AD(3.0)).val == pytest.approx(0.1411, 0.001))
	assert(unary.sin(ad.AD(3.0)).der == unary.cos(ad.AD(3.0)).val)

def test_sin_num():
	assert(unary.sin(3.0) == pytest.approx(0.1411, 0.001))

def test_cos_AD():
	assert(unary.cos(ad.AD(5.0)).val == pytest.approx(0.2836, 0.001))
	assert(unary.cos(ad.AD(5.0)).der == (-1 *unary.sin(ad.AD(5.0)).val))

def test_cos_num():
	assert(unary.cos(5.0) == pytest.approx(0.2836, 0.001))
