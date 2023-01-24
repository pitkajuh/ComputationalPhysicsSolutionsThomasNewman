# -*- coding: utf-8 -*-

# In units where all the constants are 1, the wavefunction of the n th energy level of the one-
# dimensional quantum harmonic oscillator, i.e., a spinless point particle in a quadratic
# potential well is given by

# for n = 0 ... ∞, where Hn (x) is the nth Hermite polynomial. Hermite polynomials satisfy a
# relation somewhat similar to that for the Fibonacci numbers, although more complex:

# The first two Hermite polynomials are H0 (x) = 1 and H1 (x) = 2x .
# (a) Write a function H(n,x) that calculates Hn (x) for given x and any integer n ≥ 0 .
# Then, use H(n,x) to implement function psi(n,x) that calculates the value of the n th
# harmonic oscillator wavefunction at point x. Use your function to make a plot that shows the
# wavefunctions for n = 0, 1, 2, 3 all on the same graph, in the range x = −4 to x = 4.
# Hint: There is a function factorial in the math package that calculates the factorial of
# an integer.

# (b) Make a separate plot of the wavefunction for n = 30 from x = −10 to x = 10. Hint: If
# your program takes too long to run in this case, then you're doing the calculation wrong; the
# program should take only a second or so to run.

# (c) The quantum uncertainty of a particle in the nth level of a quantum harmonic oscillator

# can be quantified by its root-mean-square position √< x2 >, where

# Write a function that evaluates this integral using Gaussian quadrature on 100 points and
# then calculates the uncertainty (i.e., the root-mean-square position of the particle) for a
# given value of n. The uncertainty for n = 5 should be in the vicinity of √< x2 > = 2.3.

def H(n,x):
    """Calculates Hermite polynomial H_n at x
    Args:
        n (int): Herimite polynomial order
        x (float): evaluation point
    Returns:
        float: Value H_n(x)"""
    h_n = 0.0
    if n==0:
        h_n=1
    elif n==1:
        h_n=2*x
    else:
        h_n=2*x*H (n-1, x)-2*(n-1)*H (n-2, x)

    return h_n

from math import factorial
def psi(n,x):
    """Calculates the value of the nth wavefunction at x
    Args:
        n (int): wavefunction order
        x (float): evaluation point
    Returns:
        float: Value psi_n(x)"""
    p = 0.0
    import numpy as np
    p=(1/(2**n*factorial (n)*(np.pi)**0.5)**0.5)*np.exp (-0.5*x**2)*H (n, x)

    return p

# plotting
import numpy as np
import matplotlib.pyplot as plt

x_plot = np.linspace(-4,4,100)
plt.plot (x_plot, psi (0, x_plot), label="$\Psi_{0}$")
plt.plot (x_plot, psi (1, x_plot), label="$\Psi_{1}$")
plt.plot (x_plot, psi (2, x_plot), label="$\Psi_{2}$")
plt.plot (x_plot, psi (3, x_plot), label="$\Psi_{3}$")
plt.xlim ([-4, 4])
plt.legend ()
plt.xlabel('x')
plt.savefig ("2.4.jpg")
plt.close ()
# validation


assert(abs(H(1,-10) - (-20)) < 2e-7)
assert(abs(H(5,0.5) - 41) < 2e-7)
assert(abs(psi(0,-4) - 0.0002519745490309146) < 2e-7)
assert(abs(psi(2,1) - 0.32214418255673755) < 2e-7)


# plotting
x_plot = np.linspace(-10,10,1000)
plt.plot (x_plot, psi (30, x_plot), label="$\Psi_{30}$")
plt.xlim ([-10, 10])
plt.legend ()
plt.xlabel('x')
plt.savefig ("2.4b.jpg")

def gaussxw(N):
    """ Calculate integration weights for Gaussian quadrature
    Args:
    N (int): number of samples
    Returns:
    numpy array: integration points
    numpy array: integration weights"""
    # Initial approximation to roots of the Legendre polynomial
    a = np.linspace(3,4*N-1,N)/(4*N+2)
    x = np.empty(N,float)
    for i in range(N):
        x[i] = np.cos(np.pi*a[i]+1/(8*N*N*np.tan(a[i])))
    # Find roots using Newton's method
    epsilon = 1e-15
    delta = 1.0
    while delta>epsilon:
        p0 = np.ones(N,float)
        p1 = np.copy(x)
        for k in range(1,N):
            p0,p1 = p1,((2*k+1)*x*p1-k*p0)/(k+1)
        dp = (N+1)*(p0-x*p1)/(1-x*x)
        dx = p1/dp
        x -= dx
        delta = max(abs(dx))

    # Calculate the weights
    w = 2*(N+1)*(N+1)/(N*N*(1-x*x)*dp*dp)
    return x,w



def gauss1(a, b, N, n):
    gauss_xw=gaussxw(N)
    x=gauss_xw[0]
    w=gauss_xw[1]
    xp=0.5*(x*(b-a)+b+a)
    wp=0.5*w*(b-a)
    return [xp, wp]

def integ (n, x):
    return x**2*psi (n, x)**2


def uncertainty(n):
    """Calculates the uncertainty <x^2> for the nth wavefunction
    Args:
        n (int): wavefunction order
    Returns:
        float: value of <x^2>"""
    u = 0.0
    a=-1
    b=1

    gauss=gauss1(a, b, 100, 5)
    xp=gauss[0]
    wp=gauss[1]
    x=xp/(1-xp**2)
    u=wp*integ (n, x)*(1+xp**2)/(1-xp**2)**2

    u=sum (u)
    u=u**0.5
    return u

# validation
u = uncertainty(5)
print (u)
print("Uncertainty (n=5): {}".format(u))
assert(abs(u - 2.3) < 1e-1)
