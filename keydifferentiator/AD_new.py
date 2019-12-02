# AD.py

class AD():

    def __init__(self, val, der=[1.0]):
        """ # todo: write introduction

        INPUTS
        =======
        val: 
        der: 

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
            self.der = np.array(der)
        # todo
        # input is vector of functions/AD objects, derivative should be set to the jacobian
        # else:

    def __str__(self):
        return "AD("+str(self.val)+", "+str(self.der)+")"
        # todo
        # may need another case when input is vector of functions

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
        # todo
        pass

    def __rtruediv__(self, other):
        # todo
        pass

    def __pow__(self, other):
        # todo
        pass

    def __rpow__(self, other):
        # todo
        pass

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
