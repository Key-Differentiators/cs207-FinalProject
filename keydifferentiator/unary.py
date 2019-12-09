# unary.py

import numpy as np
import math
import keydifferentiator.AD as ad

def exp(x):
    """ Calculate the exponential of the input AD object, integer, or float
    
    INPUTS
    =======
    x: input value, an AD object, int, or flot
    
    RETURNS
    ========
    result: exponential of x

    EXAMPLES
    =========
    >>> x = ad.AD(2.0, [1.0,0.0])
    >>> y = ad.AD(3.0, [0.0,1.0])
    >>> print(exp(x))
    AD(7.38905609893065, [7.3890561 0.       ])
    >>> print(exp(x*y))
    AD(403.4287934927351, [1210.28638048  806.85758699])
    """
    try:
        return ad.AD(np.exp(x.val), np.exp(x.val)*x.der)
    except AttributeError:
        return np.exp(x)

def ln(x):
    """ Calculate the natural base logarithm of the input AD object, integer, or float
    
    INPUTS
    =======
    x: input value, an AD object, int, or float
    
    RETURNS
    ========
    result: natural logarithm of x
    
    EXAMPLES
    =========
    >>> x = ad.AD(2.0, [1.0,0.0])
    >>> y = ad.AD(3.0, [0.0,1.0])
    >>> print(ln(x*y))
    AD(1.791759469228055, [0.5        0.33333333])
    """
    try:
        return ad.AD(np.log(x.val), x.der/x.val)
    except AttributeError:
        return np.log(x)

def log(x, base):
    """ Calculate the logarithm of an AD object, integer, or float of given base
    
    INPUTS
    =======
    x: the AD object, int, or float
    base: logarithm base
    
    RETURNS
    ========
    result: given base logarithm of x
    
    EXAMPLES
    =========
    >>> x = ad.AD(4.0)
    >>> print(log(x,2))
    AD(2.0, [0.36067376])
    """
    try:
        return ad.AD(math.log(x.val, base), x.der/(x.val*np.log(base)))
    except AttributeError:
        return math.log(x,base)

def logistic(x):
    """ Return the logistic of an AD object, integer, or float

    INPUTS
    =======
    x: the AD object, int, or float

    RETURNS
    ========
    result: 1/(1+e^(-x))

    EXAMPLES
    =========
    >>> x = ad.AD(4.0)
    >>> print(logistic(x))
    AD(0.9820137900379085, [0.0183095])
    """
    try:
        return ad.AD(1/(1+np.exp(-x.val)), np.exp(-x.val)*x.der/(1+np.exp(-x.val)**2))
    except AttributeError:
        return 1/(1+np.exp(-x))

def sqrt(x):
    """ Calculate the square root of the input AD object, integer, or float
    
    INPUTS
    =======
    x: input value, an AD object, int, or float
    
    RETURNS
    ========
    result: square root of x
    
    EXAMPLES
    =========
    >>> x = ad.AD(2.0, [1.0,0.0])
    >>> y = ad.AD(3.0, [0.0,1.0])
    >>> print(sqrt(x*y))
    AD(2.449489742783178, [0.61237244 0.40824829])
    """
    return x**(1/2)

def sin(x):
    """ Calculate sine of the input AD object, integer, or float
    
    INPUTS
    =======
    x: input value, an AD object, int, or float
    
    RETURNS
    ========
    result: sine of x
    
    EXAMPLES
    =========
    >>> x = ad.AD(2.0, [1.0,0.0])
    >>> y = ad.AD(3.0, [0.0,1.0])
    >>> print(sin(x*y))
    AD(-0.27941549819892586, [2.88051086 1.92034057])
    """
    try:
        return ad.AD(np.sin(x.val), x.der*np.cos(x.val))
    except AttributeError:
        return np.sin(x)

def cos(x):
    """ Calculate cosine of the input AD object, integer, or float
    
    INPUTS
    =======
    x: input value, an AD object, int, or float
    
    RETURNS
    ========
    result: cosine of x
    
    EXAMPLES
    =========
    >>> x = ad.AD(2.0, [1.0,0.0])
    >>> y = ad.AD(3.0, [0.0,1.0])
    >>> print(cos(x*y))
    AD(0.9601702866503661, [0.83824649 0.558831  ])
    """
    try:
        return ad.AD(np.cos(x.val), -x.der*np.sin(x.val))
    except AttributeError:
        return np.cos(x)

def tan(x):
    """ Calculate tangent of the input AD object, integer, or float
    
    INPUTS
    =======
    x: input value, an AD object, int, or float
    
    RETURNS
    ========
    result: tangent of x
    
    EXAMPLES
    =========
    >>> x = ad.AD(2.0)
    >>> print(tan(x))
    AD(-2.185039863261519, [5.7743992])
    """
    return sin(x)/cos(x)

def arcsin(x):
    """ Calculate inverse sine of the input AD object, integer, or float
    
    INPUTS
    =======
    x: input value, an AD object, int, or float
    
    RETURNS
    ========
    result: inverse sine of x
    
    EXAMPLES
    =========
    >>> x = ad.AD(0.5)
    >>> print(arcsin(x))
    AD(0.5235987755982988, [1.15470054])
    """
    try:
        if x.val<=-1 or x.val>=1:
            raise Exception("X out of domain")
        return ad.AD(np.arcsin(x.val), x.der/np.sqrt(1-x.val**2))
    except AttributeError:
        return np.arcsin(x)

def arccos(x):
    """ Calculate inverse cosine of the input AD object, integer, or float
    
    INPUTS
    =======
    x: input value, an AD object, int, or float
    
    RETURNS
    ========
    result: inverse cosine of x
    
    EXAMPLES
    =========
    >>> x = ad.AD(0.5)
    >>> print(arccos(x))
    AD(1.0471975511965976, [-1.15470054])
    """
    try:
        if x.val<=-1 or x.val>=1:
            raise Exception("X out of domain")
        return ad.AD(np.arccos(x.val), -x.der/np.sqrt(1-x.val**2))
    except AttributeError:
        return np.arccos(x)

def arctan(x):
    """ Calculate inverse tangent of the input AD object, integer, or float
    
    INPUTS
    =======
    x: input value, an AD object, int, or float
    
    RETURNS
    ========
    result: inverse tangent of x
    
    EXAMPLES
    =========
    >>> x = ad.AD(2)
    >>> print(arctan(x))
    AD(1.1071487177940906, [0.2])
    """
    try:
        return ad.AD(np.arctan(x.val), x.der/(1+x.val**2))
    except AttributeError:
        return np.arctan(x)

def sinh(x):
    """ Calculate hyperbolic sine of the input AD object, integer, or float
    
    INPUTS
    =======
    x: input value, an AD object, int, or float
    
    RETURNS
    ========
    result: hyperbolic sine of x
    
    EXAMPLES
    =========
    >>> x = ad.AD(2.0, [1.0,0.0])
    >>> y = ad.AD(3.0, [0.0,1.0])
    >>> print(sinh(x+y))
    AD(74.20321057778875, [74.20994852 74.20994852])
    """
    try:
        return ad.AD(np.sinh(x.val), x.der*np.cosh(x.val))
    except AttributeError:
        return np.sinh(x)

def cosh(x):
    """ Calculate hyperbolic cosine of the input AD object, integer, or float
    
    INPUTS
    =======
    x: input value, an AD object, int, or float
    
    RETURNS
    ========
    result: hyperbolic cosine of x
    
    EXAMPLES
    =========
    >>> x = ad.AD(2.0, [1.0,0.0])
    >>> y = ad.AD(3.0, [0.0,1.0])
    >>> print(cosh(x*y))
    AD(201.7156361224559, [605.13947211 403.42631474])
    """
    try:
        return ad.AD(np.cosh(x.val), x.der*np.sinh(x.val))
    except AttributeError:
        return np.cosh(x)

def tanh(x):
    """ Calculate hyperbolic tangent of the input AD object, integer, or float
    
    INPUTS
    =======
    x: input value, an AD object, int, or float
    
    RETURNS
    ========
    result: hyperbolic tangent of x
    
    EXAMPLES
    =========
    >>> x = ad.AD(2.0, [1.0,0.0])
    >>> print(tanh(x))
    AD(0.9640275800758169, [0.07065082 0.        ])
    """
    try:
        return ad.AD(np.tanh(x.val), x.der/np.cosh(x.val)**2)
    except AttributeError:
        return np.tanh(x)
