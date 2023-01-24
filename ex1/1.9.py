# -*- coding: utf-8 -*-

# Suppose we want to calculate the value of the integral

# The integrand looks like a semicircle of radius 1:

# and hence the value of the integral---the area under the curve---must be

# Alternatively, we can evaluate the integral on the computer by dividing the domain of
# integration into a large number N of slices of width h = 2/N each and then using the
# Riemann definition of the integral:

# We cannot in practice take the limit N → ∞, but we can make a reasonable approximation
# by just making N large.
# (a) Write a program to evaluate the integral above with N = 100 and compare the result
# with the exact value. The two will not agree very well, because N = 100 is not a sufficiently
# large number of slices.
# (b) Increase the value of N to get a more accurate value for the integral. If we require that
# the program runs in about one second or less, how accurate a value can you get?
# Evaluating integrals is a common task in computational physics calculations. We will study
# techniques for doing integrals in detail in the next chapter. As we will see, there are
# substantially quicker and more accurate methods than the simple one we have used here.

def semicircle_area(N=100):
    """Calculates the area of a semi circle with unit radius using
    the riemann definition of an integral
    Args:
        N (int): number of slices to compute area
    Retruns:
        float: area of the semi circle"""
    area = 0

    h=2/N

    for k in range (1, N, 1):
        xk=h*k-1
        yk=(1-xk**2)**0.5
        area+=yk*h

    print (area)

    return area


# validation
N = 3700000

import time
t = time.time()
area = semicircle_area(N)
print("Runtime = {} s\nArea with N {} = {} sq.m.\n"
      "Error = {} %".format((time.time() - t), N, area,
                               abs(area / 1.57079632679 - 1) * 100))

assert abs(area - 1.57079632679) < 1e-2, "error too large"
