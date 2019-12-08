# test_rev_AD.py

import pytest
import numpy as np
from keydifferentiator.Reverse import *
from pytest import approx, raises

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

def test_str():
    x = Reverse(5)
    f = sin(x) + 2
    f.gradient_value = 1.0
    assert str(f) == 'value = 1.0410757253368614, gradient_value = 1.0'

def test_single_var():
    x = Reverse(1) + 2
    f = x
    f.gradient_value = 1.0
    assert f.value == approx(3)
    assert x.get_gradient() == approx(1)

def test_neg_Rev():
    x = -(Reverse(5.0))
    y = Reverse(-5.0)
    assert (x == y)

def test_exp_Rev():
    x = exp(Reverse(4.0))
    assert (x.value == pytest.approx(54.5981, 0.001))

def test_exp_num():
    assert (exp(4.0) == np.exp(4.0))

def test_sqrt_Rev():
    x = sqrt(Reverse(4.0))
    y = Reverse(2.0)
    assert (x == y)

def test_sqrt_num():
    assert(sqrt(4.0) == np.sqrt(4.0))

def test_ln_Rev():
    assert (ln(Reverse(4.0)).value == pytest.approx(1.3862, 0.001))

def test_ln_num():
    assert(ln(4.0) == np.log(4.0))

def test_sin_Rev():
    assert(sin(Reverse(3.0)).value == pytest.approx(0.1411, 0.001))

def test_sin_num():
    assert(sin(3.0) == pytest.approx(0.1411, 0.001))

def test_cos_Rev():
    assert(cos(Reverse(5.0)).value == pytest.approx(0.2836, 0.001))

def test_cos_num():
    assert(cos(5.0) == pytest.approx(0.2836, 0.001))

def test_tan_Rev():
    assert(tan(Reverse(5.0)).value == pytest.approx(-3.3805, 0.001))

def test_tan_num():
    assert(tan(5.0) == pytest.approx(-3.3805, 0.001))

def test_sinh_Rev():
    assert(sinh(Reverse(0.5)).value == pytest.approx(0.5210, 0.001))

def test_sinh_num():
    assert(sinh(0.5) == pytest.approx(0.5210, 0.001))

def test_cosh_Rev():
    assert(cosh(Reverse(0.5)).value == pytest.approx(1.1276, 0.001))

def test_cosh_num():
    assert(cosh(0.5) == pytest.approx(1.1276, 0.001))

def test_tanh_Rev():
    assert(tanh(Reverse(0.5)).value == pytest.approx(0.4621, 0.001))

def test_tanh_num():
    assert(tanh(0.5) == pytest.approx(0.4621, 0.001))

def test_sub_Rev():
    x = Reverse(2.0)
    assert((cos(x**2) - cos(x**2)) == Reverse(0.0))

def test_sqrt_pow():
    x = Reverse(4.0)
    print(sqrt(x**2).value)
    print(sqrt(x**2).gradient_value)
    assert(sqrt(x**2) == Reverse(4.0))

def test_tan():
    x = Reverse(2)
    f = tan(x)
    f.gradient_value = 1.0
    assert f.value == approx(np.tan(2))
    assert x.get_gradient() == approx(1 / np.cos(2) ** 2)

def test_cot():
    x = Reverse(5)
    f = cot(x)
    f.gradient_value = 1.0
    assert f.value == approx(1 / np.tan(5))
    assert x.get_gradient() == approx(-1 / np.sin(5) ** 2)

def test_sec():
    x = Reverse(2)
    f = sec(x)
    f.gradient_value = 1.0
    assert f.value == approx(1 / np.cos(2))
    assert x.get_gradient() == approx(np.tan(2) / np.cos(2))

def test_cosec():
    x = Reverse(-1)
    f = csc(x)
    f.gradient_value = 1.0
    assert f.value == approx(1 / np.sin(-1))
    assert x.get_gradient() == approx(-1 / np.tan(-1) / np.sin(-1))

# def test_other_trig_funcs():
#     x = Reverse(2)
#     f = sinh(x) + sinh(2)
#     f.gradient_value = 1.0
#     assert f.value == approx(2 * np.sinh(2))
#     assert x.get_gradient() == approx(np.cosh(2))

#     x = Reverse(2)
#     f = cosh(x) + cosh(2)
#     f.gradient_value = 1.0
#     assert f.value == approx(2 * np.cosh(2))
#     assert x.get_gradient() == approx(np.sinh(2))

#     x = Reverse(2)
#     f = tanh(x) + tanh(2)
#     f.gradient_value = 1.0
#     assert f.value == approx(2 * np.tanh(2))
#     assert x.get_gradient() == approx(
#         (np.cosh(2) ** 2 - np.sinh(2) ** 2) / np.cosh(2) ** 2
#     )

#     x = Reverse(2)
#     f = sech(x) + sech(2)
#     f.gradient_value = 1.0
#     assert f.value == approx(2 * 1 / np.cosh(2))
#     assert x.get_gradient() == approx((-1 / np.cosh(2)) * (np.sinh(2) / np.cosh(2)))

#     x = Reverse(2)
#     f = csch(x) + csch(2)
#     f.gradient_value = 1.0
#     assert f.value == approx(2 * 1 / np.sinh(2))
#     assert x.get_gradient() == approx((-1 / np.sinh(2)) * (np.cosh(2) / np.sinh(2)))

#     x = Reverse(2)
#     f = coth(x) + coth(2)
#     f.gradient_value = 1.0
#     assert f.value == approx(2 * (np.cosh(2) / np.sinh(2)))
#     assert x.get_gradient() == approx(-1 / (np.sinh(2) ** 2))

def test_find_gradient_vector_error_cases():
    # function attribute error
    func = ['3*2']
    vars_dict = {'x': 1}
    vector = rVector(func, vars_dict)
    assert vector.values['3*2'] == 6

    with raises(AttributeError): # variable attribute error
        func = ['3*x']
        vars_dict = {'2': 1}
        vector = rVector(func, vars_dict)

    with raises(ValueError):
        func = ['3*x']
        vars_dict = {'x': 'e'}
        vector = rVector(func, vars_dict)

    with raises(Exception):
        func = ['3x']
        vars_dict = {'x': 1}
        vector = rVector(func, vars_dict)
        
    with raises(Exception):
        func = ['3*x*y']
        vars_dict = {'x': 1}
        vector = rVector(func, vars_dict)

    with raises(TypeError):
        func = [2*3]
        vars_dict = {'x': 1}
        vector = rVector(func, vars_dict)

def test_vector():
    # Check for str
    func = ['x*2*y+y**3', '2*x**2*y', '3*y']
    vars_dict = {'x': 1, 'y': '2'}
    vector = rVector(func, vars_dict)
    assert str(vector) == "x=1\ny=2\nx*2*y+y**3=12.0  Df(x)=4.0  Df(y)=14.0  \n2*x**2*y=4.0  Df(x)=8.0  Df(y)=2.0  \n3*y=6.0  Df(x)=0  Df(y)=3"

    # Check for find_gradients()
    func = ['x*2*y+y**3', '2*x**2*y', '3*y']
    vars_dict = {'x': 1, 'y': 2}
    vector = rVector(func, vars_dict)
    vector.find_gradients(functions = ['2*x'], variables = {'x':1})
    assert vector.variables == {'x':1}
    assert vector.functions == ['2*x']

    # Check for get_gradients()
    func = ['x*2*y+y**3', '2*x**2*y', '3*y']
    vars_dict = {'x': 1, 'y': 2}
    vector = rVector(func, vars_dict)
    assert vector.get_gradients(func_num=0, var_name='x') == approx(4)
    assert vector.get_gradients(func_num=0) == {'x': 4.0, 'y': 14.0}
    assert vector.get_gradients(var_name='x') == [4.0, 8.0, 0]
    assert vector.get_gradients() == [{'x': 4.0, 'y': 14.0}, {'x': 8.0, 'y': 2.0}, {'x': 0, 'y': 3}]
