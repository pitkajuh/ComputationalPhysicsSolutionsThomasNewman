# -*- coding: utf-8 -*-

# Consider the equation x = 1 − e−cx , where c is a known parameter and x is unknown.
# This equation arises in a variety of situations, including the physics of contact processes,
# mathematical models of epidemics, and the theory of random graphs. Write function
# relaxation_solve(c,accuracy) that solves this equation for x using the relaxation
# method. Then use your function to solve x for values of c from 0.01 to 3 in steps of 0.01 .
# Calculate your solution to an accuracy of at least 10−6 . Make a plot of x as a function of c .
# You should see a clear transition from a regime in which x = 0 to a regime of nonzero x.
# This is another example of a phase transition. In physics this transition is known as the
# percolation transition; in epidemiology it is the epidemic threshold.

import numpy as np
import matplotlib.pyplot as plt
def relaxation_solve(c,accuracy):
    """ Solves equation x = 1 - e^(-cx) for x using the relaxation method.
    Args:
        c (float): value for c
        accuracy (float): target value for the error
    Returns
        float: value of x that satisfies x = 1 - e^(-cx)"""
    x = 0.0
    error=1
    x=1
    x_values=[]
    for i in c:
        x = 0.0
        error=1
        x=1
        while error>accuracy:
            x, x2=1-np.exp(-i*x), x
            error=abs ((x-x2)/(1-1/(i*np.exp(-i*x))))
        x_values.append (x)

    return x_values

# plotting
c_plot =  np.arange(0.01,3.01,0.01)
accuracy=1e-6

plt.plot (c_plot, relaxation_solve (c_plot, accuracy))
plt.xlabel('c')
plt.ylabel('Solution of $x=1-e^{-cx}$')
plt.show ()
