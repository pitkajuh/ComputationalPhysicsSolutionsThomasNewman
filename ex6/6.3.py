# -*- coding: utf-8 -*-

# Calculate a value for the integral

# (a) Show that the probability distribution p(x) from which the sample points should be drawn
# is given by

# and derive a transformation formula for generating random numbers between zero and one
# from this distribution.

# (b) Using your formula, sample N = 1, 000, 000 random points and hence evaluate the
# integral. You should get a value around 0.84.

import random as rn
import numpy as np

def imp_integral(n):
    """Calculate integral with importance sampling
    Args:
        n (int): number of points
    Returns:
        float: integral of the function"""
    integral = 0

    for i in range (n):
        x=rn.random ()**2
        integral+=1/(1+np.exp (x))
    integral=integral/n*2
    return integral

# validation
integral = imp_integral(1000000)
print (integral)
print('Integral through importance sampling: {}'
      ''.format(integral))
assert abs(integral - 0.84) < 5e-2, 'bad integral value'
