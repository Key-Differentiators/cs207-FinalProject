# interpreter.py

from keydifferentiator import AD as ad
from keydifferentiator.unary import *
import re

def main():
	while True:
		f = input("Input your function:   f(x) = ")
		x = input("What value of x would you like to evaluate at? Enter a number:   ")
		print("Evaluating f(x) = %s at x = %f..." % (f, float(x)))
		eq = re.sub('x', 'ad.AD(x)', f)
		eq = re.sub('x', x, eq)
		try: 
			x = eval(eq)
			print(x)
		except:
			print("Cannot evaluate f(x) = %s at x = %d." % (f, float(x)))
			print("Hints: ")
			print("    - Use * for multiplication (e.g. 3*x, not 3x)")
			print("    - Use ** for exponentiation (e.g. 3**x, not 3^x)")

if __name__ == "__main__":
	main()