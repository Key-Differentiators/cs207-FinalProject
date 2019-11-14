# diff.py

import re
import keydifferentiator.AD as ad
from keydifferentiator.unary import *

def diff(f, x):
	eq = re.sub('x', 'ad.AD(x)', f)
	eq = re.sub('x', str(x), eq)
	result = eval(eq)
	return (result.val, result.der)