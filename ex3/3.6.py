# -*- coding: utf-8 -*-

# Consider the sixth-order polynomial

# There is no general formula for the roots of a sixth-order polynomial, but one can find them
# easily enough using a computer.
# (a) Make a plot of P (x) from x = 0 to x = 1 and by inspecting it find rough values for the
# six roots of the polynomial, that is, the points at which P (x) = 0.

# (b) Implement newton_root() that finds a root of a function using Newton's method.
# Then, write function find_P_roots() that finds all six roots of P (x).

import numpy as np
import matplotlib.pyplot as plt
def P(x):
    return 924*x**6 - 2772*x**5 + 3150*x**4 - 1680*x**3 + 420*x**2 - 42*x + 1

# plotting
x=np.linspace (0, 1, 100)
# raise NotImplementedError()
plt.plot (x, P (x))
plt.xlabel('x')
plt.ylabel('y')
# plt.show ()


def df1(x):
    return 5544*x**5-13860*x**4+12600*x**3-5040*x**2+840*x-42


def newton_root(f, df, x_init, accuracy):
    """ Newton's method. Finds a root of function f.
    Args:
        f (function): the function
        df (function): derivative of f
        x_init (float): initial guess for the root
        accuracy (float): target value for the error
    Returns
        float: value of the root"""
    x = 0.0
    x=x_init
    delta=f (x_init)/df (x_init)

    while abs (delta)>accuracy:
        delta=f (x)/df (x)
        x-=delta

    return x


def find_P_roots():
    """ Finds all roots of P(x) using Newton's method
    Returns
        numpy float array: values of the roots"""
    roots = None
    roots_guess=[0.05, 0.2, 0.4, 0.6, 0.8, 0.95]
    acc=1e-10
    roots=[]
    for i in roots_guess:
        root=newton_root (P, df1, i, acc)
        roots.append (root)
    roots=np.array (roots)
    print (roots)
    return roots




# validation
def g(x): return np.sin(x)
def gd(x): return np.cos(x)
root = newton_root(g,gd,3,1e-11)
assert abs(root-np.pi) < 1e-5
assert abs(g(root)) < 1e-10

# Finding the roots of P(x)
roots = find_P_roots()
value_at_roots = P(roots)
for root, value in zip(roots,value_at_roots):
    print("x = {:.16f}, P(x) = {:.16f}".format(root, value))
