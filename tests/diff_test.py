# diff_test.py

import pytest
from keydifferentiator import diff

def test_diff():
	f = '3 * x + 3'
	x = 1
	val, der = diff.diff(f, x)
	assert(val == 6)
	assert(der == 3)