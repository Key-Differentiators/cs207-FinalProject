# AD.py
import numpy as np

class AD():

    def __init__(self, val, der=[1.0]):
        """ Initializing an AD object taking with specific value and derivative(optional)

        INPUTS
        =======
        val: value of the AD object, an integer or a float
        der: derivative of the AD object, an integer, a float, or a list
             optional, if not specified, [1.0] is the default derivative

        EXAMPLES
        =========
        >>> x = AD(3)
        >>> print(x)
        AD(3, [1.])

        >>> x = AD(3, [1.0, 0.0])
        >>> y = AD(4, [0.0, 1.0])
        >>> print(y)
        AD(4, [0. 1.])
        """

        if isinstance(val, float) or isinstance(val, int):
            self.val = val
            if isinstance(der, np.ndarray):
                self.der = der
            else:
                if not isinstance(der, list):
                    der = [der]
                self.der = np.array(der)
        else:
            raise TypeError


    def __str__(self):
        return "AD("+str(self.val)+", "+str(self.der)+")"

    def get_jacobian(functions):
        """ Return the values and the Jacobian matrix of the vector of functions

        INPUTS
        =======
        self: an AD object
        functions: list of functions

        RETURNS
        ========
        vals: list of values of the functions
        ders: the Jacobian matrix of the list of functions
                an numpy array whose (i,j) entry is the partial derivative of unknown j regarding to function i

        EXAMPLES
        =========

        """
        if len(functions)>0:
            if all(isinstance(x, AD) for x in functions):
                vals = [functions[0].val]
                ders = functions[0].der.reshape(1,-1)
                dim  = functions[0].der.shape[0]
                for i in range(1,len(functions)):
                    if functions[i].der.shape[0] != dim:
                        raise Exception("Incorrect dimension")
                    vals.append(functions[i].val)
                    ders = np.append(ders, functions[i].der.reshape(1,-1), axis=0)
                return vals, ders
            else:
                raise TypeError
        else: raise Exception("Empty list of functions")



    def __add__(self, other):
        """ Addition of an AD object to an int, a float, or an AD object

        INPUTS
        =======
        self: original AD object
        other: int, float, or AD object to be added to self

        RETURNS
        ========
        result: AD object of adding other to self

        EXAMPLES
        =========
        >>> x = AD(3.0)
        >>> print(x+3)
        AD(6.0, [1.])

        >>> x = AD(3.0, [1.0,0.0])
        >>> y = AD(4.0, [0.0,1.0])
        >>> print(x+y)
        AD(7.0, [1. 1.])
        """
        try:
            return AD(self.val+other.val, self.der+other.der)
        except AttributeError:
            return AD(self.val+other, self.der)


    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        """  Subtraction of an int, a float, or an AD object from an AD object

        INPUTS
        =======
        self: original AD object
        other: int, float, or AD object to be subtracted from self

        RETURNS
        ========
        result: AD object of subtracting other from self

        EXAMPLES
        =========
        >>> x = AD(3.0)
        >>> print(x-1)
        AD(2.0, [1.])

        >>> a = AD(3.0)
        >>> b = AD(4.0)
        >>> print(a-b)
        AD(-1.0, [0.])

        """
        try:
            return AD(self.val-other.val, self.der-other.der)
        except AttributeError:
            return AD(self.val-other, self.der)

    def __rsub__(self, other):
        """ Subtraction of an AD object from an int, a float, or an AD object

        INPUTS
        =======
        self: AD object to be subtracted
        other: int, float, or AD object to be subtracted

        RETURNS
        ========
        result: AD object of subtracting self from other

        EXAMPLES
        =========
        >>> x = AD(3.0)
        >>> print(3-x)
        AD(0.0, [-1.])
        """
        try:
            return AD(other.val-self.val, other.der-self.der)
        except AttributeError:
            return AD(other-self.val, -self.der)

    def __mul__(self, other):
        """ Multiplication of an AD object by an int, a float, or an AD object

        INPUTS
        =======
        self: original AD object
        other: int, float, or AD object to be multiplied

        RETURNS
        ========
        result: AD object of multiplying self by other

        EXAMPLES
        =========
        >>> x = AD(3.0, [1.0,0.0])
        >>> y = AD(4.0, [0.0,1.0])
        >>> print(x*y)
        AD(12.0, [4. 3.])
        >>> print(x*2+y*1)
        AD(10.0, [2. 1.])
        """
        try:
            return AD(self.val*other.val, self.der*other.val+other.der*self.val)
        except AttributeError:
            return AD(self.val*other, self.der*other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        """ Division of an AD object by an int, a float, or an AD object

        INPUTS
        =======
        self: original AD object as the numerator
        other: int, float, or AD as the denominator

        RETURNS
        ========
        result: self divided by other

        EXAMPLES
        >>> x = AD(4.0, [1.0,0.0])
        >>> y = AD(1.0, [0.0,1.0])
        >>> print((2*y)/x)
        AD(0.5, [-0.125  0.5  ])
        """
        if isinstance(other, float) or isinstance(other, int):
            if other==0:
                raise Exception("Zero cannot be denominator")
            return AD(self.val/other, self.der/other)
        else:
            if other.val==0:
                raise Exception("Zero cannot be denominator")
            return AD(self.val/other.val, self.der/other.val-self.val/(other.val**2)*other.der)

    def __rtruediv__(self, other):
        """ Division of an int or a float by an AD object

        INPUTS
        =======
        self: AD object as the denominator
        other: int or float as the numerator

        RETURNS
        ========
        result: other divided by self

        EXAMPLES
        >>> x = AD(2.0, [1.0,0.0])
        >>> print(-4/x)
        AD(-2.0, [1. 0.])
        """
        return AD(other/self.val, -other*self.der/self.val**2)

    def __pow__(self, p):
        """ Power of an AD object

        INPUTS
        =======
        self: original AD object
        p: the power to be raised to

        RETURNS
        ========
        result: AD object that is power p of self

        EXAMPLES
        =========
        >>> x = AD(3.0, [1.])
        >>> print(x**3)
        AD(27.0, [27.])
        """
        if self.val==0:
            return AD(0, [0.0])        
        return AD(self.val**p, p*(self.val**(p-1))*self.der)

    def __rpow__(self, n):
        """ Power of n to an AD object

        INPUTS
        =======
        self: AD object, the wanted power
        n: base

        RETURNS
        ========
        result: power to self of n

        EXAMPLES
        >>> x = AD(2.0, [1.0])
        >>> print(3**x)
        AD(9.0, [9.8875106])
        """
        return AD(n**self.val, (n**self.val)*np.log(n)*self.der)

    def __eq__(self, other):
        """ Check if self and other are equal

        INPUTS
        =======
        self: AD object
        other: int, float, or AD object to compare

        RETURNS
        ========
        result: Boolean of whether self and other are equal

        EXAMPLES
        =========
        >>> x = AD(3.0)
        >>> y = 3.0
        >>> print(x==y)
        True

        >>> x = AD(3.0, [1.0,0.0])
        >>> y = AD(3.0, [0.0,1.0])
        >>> print(x==y)
        False
        """
        if not isinstance(other, AD):
            return self.val==other and all(self.der==np.array([1.0]))
        if self.val==other.val and all(self.der==other.der):
            return True
        else:
            return False

    def __ne__(self, other):
        """ Check if self and other are not equal

        INPUTS
        =======
        self: AD object
        other: int, float, or AD object to compare

        RETURNS
        ========
        result: Boolean of whether self and other are not equal

        EXAMPLES
        =========
        >>> x = AD(3.0)
        >>> y = 3.0
        >>> print(x!=y)
        False

        >>> x = AD(3.0, [1.0,0.0])
        >>> y = AD(3.0, [0.0,1.0])
        >>> print(x!=y)
        True
        """
        return not self.__eq__(other)

    def __neg__(self):
        """ Negation of an AD object

        INPUTS
        =======
        self: original AD object

        RETURNS
        ========
        result: negation of self

        EXAMPLES
        =========
        >>> x = AD(3.0)
        >>> print(-x)
        AD(-3.0, [-1.])
        """
        return AD(-self.val, -self.der)
