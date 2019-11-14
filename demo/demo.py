# demo.py

#####      TO RUN      #####
## run 'python -m demo.demo'

from keydifferentiator import diff

# create a function to differentiate
f = '3 * x + 1'

# select a value to differentiate at
x = 1

# get the value and derivative of function f at value x as a tuple
value, derivative = diff.diff(f, x)

# print the result
print("Evaluated the function %s at %f" % (f, x))
print("f(x) = %f" % value)
print("f'(x) = %f" % derivative)
