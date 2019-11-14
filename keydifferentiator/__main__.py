# __main__.py

import keydifferentiator.diff as d

def main():
	while True:
		f = input("Input your function:   f(x) = ")
		x = input("What value of x would you like to evaluate at? Enter a number:   ")
		print("Evaluating f(x) = %s at x = %f..." % (f, float(x)))

		try: 
			result = d.diff(f, x)
			print("f(x) = %f, f'(x) = %f" % (result[0], result[1]))
		except:
			print("Cannot evaluate f(x) = %s at x = %d." % (f, float(x)))
			print("Hints: ")
			print("    - Use * for multiplication (e.g. 3*x, not 3x)")
			print("    - Use ** for exponentiation (e.g. 3**x, not 3^x)")

if __name__ == "__main__":
	main()

