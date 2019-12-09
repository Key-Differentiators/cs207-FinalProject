# diff_test.py

import pytest
import mock
from keydifferentiator import __main__ as module

def test_diff():
	f = '3 * x + 3'
	x = 1
	val, der = module.diff(f, x)
	assert(val == 6)
	assert(der == 3)

def test_init():
    with mock.patch.object(module, "input", return_value='q'):
        module.main()
