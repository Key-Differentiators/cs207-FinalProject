# interpreter.py

from keydifferentiator.AD import AD as ad
from keydifferentiator.AD import unary
from unary import *
import re

def interpreter():
	while True:
		f = input("Input your function:   f(x) = ")
		x = input("What value of x would you like to evaluate at? Enter a number:   ")
		print("Evaluating f(x) = %s at x = %d..." % (f, int(x)))
		f = re.sub('x', 'ad.AD(x)', f)
		f = re.sub('x', x, f)
		x = eval(f)
		print(x)
