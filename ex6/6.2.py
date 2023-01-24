# -*- coding: utf-8 -*-

# This exercise asks you to estimate the volume of a sphere of unit radius in ten dimensions
# using a Monte Carlo method. Consider the equivalent problem in two dimensions, the area
# of a circle of unit radius:

# The area of the circle, the shaded area above, is given by the integral

# where f(x, y) = 1 everywhere inside the circle and zero everywhere outside. In other
# words,

# So if we didn't already know the area of the circle, we could calculate it by Monte Carlo
# integration. We would generate a set of N random points (x, y) , where both x and y are in
# the range from −1 to~1. Then the two-dimensional version of Equation I ≃ N V

# Generalize this method to the ten-dimensional case and write a program to perform a Monte
# Carlo calculation of the volume of a sphere of unit radius in ten dimensions.
# If we had to do a ten-dimensional integral the traditional way, it would take a very long time.
# Even with only 100 points along each axis (which wouldn't give a very accurate result) we'd
# still have 10010 = 1020 points to sample, which is impossible on any computer. But using
# the Monte Carlo method we can get a pretty good result with a million points or so.

import numpy as np

def mc_sphere(n, dim):
    """
    Monte Carlo volume of multi-dimensional unit sphere
    Args:
        n (int): number of points
        dim (int): dimensions of the unit sphere
    Returns:
        float: the volume of the unit sphere
    """
    vol = 0 # volume of the sphere
    n1=0
    for i in range (n):
        val=np.linalg.norm (np.random.uniform (-1, 1, dim))
        if val<1:
            n1+=1

    vol=(2**dim)*n1/n

    return vol



# validation
vol = mc_sphere(500000, 10)
print('Volume of 10 dimensional sphere: {}'.format(vol))
assert abs(vol - 2.55016) < 5e-1, 'bad volume'
