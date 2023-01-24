# -*- coding: utf-8 -*-

# Write a function that calculates the central difference of a function at point x. Then, use your
# function to plot the numerical derivative of

# in the range −2 ≤ x ≤ 2. To validate your result, derive the analytical formula for the
# derivative and draw it in the same plot. It may help to plot the exact answer as a line and the
# numerical one as dots. Hint: In Python the tanh function is found in both the math and
# numpy packages as tanh . The numpy version of this and other common mathematical
# functions may be more accurate and better performing than their math versions, as
# numpy is better funded and maintained.

def central_difference(f, x, h):
    """Calculates the central difference of function f at x
    Args:
    f (function): function to be differentiated
    x (float): evaluation point
    h (float): difference
    Returns:
    float: central difference value
    """
    import numpy as np
    import matplotlib.pyplot as plt

    d = 0.0

    d=(f (x+(h/2))-f (x-(h/2)))/h
    return d

import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return 1+0.5*np.tanh(2*x)

# plotting
x_plot = np.linspace(-2,2,100)
h=0.01

plt.plot (x_plot, (1/np.cosh(2*x_plot))**2, label="analytical")
plt.scatter (x_plot, central_difference (f, x_plot, h), label="numerical", color="r")
plt.legend ()
plt.savefig ("2.5.jpg")
