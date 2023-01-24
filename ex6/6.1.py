# -*- coding: utf-8 -*-

# (a) Write a program to evaluate the integral in Equation 

#  using the
# Monte Carlo Integration method with 10 000 points. Also evaluate the error on your
# estimate.
# (b) Now estimate the integral again using the mean value method with 10 000 points. Also
# evaluate the error.
# You should find that the error is somewhat smaller using the mean value method.

import numpy as np
import random as rn

def f (x):
    return np.sin (1/(x*(2-x)))**2
lim0=0
lim1=2
lm=lim1-lim0
def mc_integration(n):
    """
    derive Monte Carlo integral of the function
    Args:
        n (int): number of points
    Returns:
        float: the integral value
        float: the error on the estimate
    """
    integral = 0  # the integral value
    err = 0
    # recall form the lecture that the area is bounded
    # 2 units in x and 1 unit in y, from the plot of the function.
    count=0
    for i in range (n):
        x=2*rn.random ()
        y=rn.random ()
        if y<f (x):
            count+=1
    integral=2*count/n
    # raise NotImplementedError()
    var=(n*integral/lm)*(1-integral/n)
    err=(lm/n)*(var)**0.5
    # err=((integral*(lm-integral))/n)**0.5
    return integral, err

def mvt_integration(n):
    """derive Mean Value integral of the function
    Args:
        n (int): number of points
    Returns:
        float: the integral value
        float: the error on the estimate"""
    integral = 0  # the integral value
    err = 0
    # recall form the lecture that the area is bounded
    # 2 units in x and 1 unit in y, from the plot of the function.
    int2=0
    for i in range (n):
        x=2*rn.random ()
        integral+=(lm/n)*f (x)
        int2+=integral**2
    var=int2/n-(integral/n)**2
    err=lm*(var/n)**0.5

    return integral, err


# validation
mc_I, mc_E = mc_integration(10000)
print('Integral through Monte Carlo method: {} +-{}'
      ''.format(mc_I, mc_E))
assert abs(mc_I - 1.4514) < 3e-2, 'Monte Carlo integral bad'


mvt_I, mvt_E = mvt_integration(10000)
print('Integral through mean value method: {} +-{}'
      ''.format(mvt_I, mvt_E))
assert abs(mvt_I - 1.4514) < 3e-2, 'Mean value integral bad'
assert mvt_E < mc_E, 'MVT error should be less than MC error'
