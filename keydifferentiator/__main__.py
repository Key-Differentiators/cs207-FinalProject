# __main__.py

import re
import keydifferentiator.AD as ad
from keydifferentiator.Reverse import *
from keydifferentiator.unary import *

def diff_forward(f, x, method):
	if method == 'forward':
		eq = re.sub('x', 'ad.AD(x)', f)
	elif method == 'reverse':
		eq = re.sub('x', 'Reverse(x)', f)
	else:
		raise Exception
	eq = re.sub('x', str(x), eq)
	result = eval(eq)
	return (result.val, result.der)

def main():
	while True:
		f = input("Input a function of x, or enter q to quit:   f(x) = ")
		if f == 'q':
			break;
		x = input("What value of x would you like to evaluate at? Enter a number: ")
		method = input("Would you like to use forward or reverse mode? [forward] or [reverse]: ")
		print("Evaluating f(x) = %s at x = %f using %s mode..." % (f, float(x), method))

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
