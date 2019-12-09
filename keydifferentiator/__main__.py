# __main__.py

import re
import keydifferentiator.AD as ad
from keydifferentiator.Reverse import *
from keydifferentiator.unary import *

def diff(f, x):
	eq = re.sub('x', 'ad.AD(x)', f)
	eq = re.sub('x', str(x), eq)
	result = eval(eq)
	return (result.val, result.der)

def main():
	while True:
		f = input("Input a function of x, or enter q to quit:   f(x) = ")
		if f == 'q':
			break;
		x = input("What value of x would you like to evaluate at? Enter a number: ")
		print("Evaluating f(x) = %s at x = %f using %s mode..." % (f, float(x)))

		try: 
			result = diff(f, x, method)
			print("f(x) = %f, f'(x) = %f" % (result[0], result[1]))
		except:
			print("Cannot evaluate f(x) = %s at x = %d." % (f, float(x)))
			print("Hints: ")
			print("    - Use * for multiplication (e.g. 3*x, not 3x)")
			print("    - Use ** for exponentiation (e.g. 3**x, not 3^x)")

if __name__ == "__main__":
	main()
