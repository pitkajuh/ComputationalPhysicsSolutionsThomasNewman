# -*- coding: utf-8 -*-

# Debye's theory of solids gives the heat capacity of a solid at temperature T to be

# where V is the volume of the solid, ρ is the number density of atoms, kB is Boltzmann's
# constant, and θD is the so-called \defn{Debye temperature}, a property of solids that
# depends on their density and speed of sound.
# (a) Write a function for calculating the Gaussian quadrature integral of an arbitrary integrand
# over a given range (a, b). Code for generating the Gaussian quadrature integration points
# and weights is given below.

# (b) Now, consider a sample consisting of 1000 cubic centimeters of solid aluminum, which
# has a number density of ρ = 6.022 × 1028 m−3 and a Debye temperature of θD = 428 K.
# Write a function cv(T) that calculates CV for the sample at a given temperature using
# your integration function. Use cv(T) to make a graph of the heat capacity as a function of
# temperature from T = 5 K to T = 500 K.

import numpy as np
import matplotlib.pyplot as plt

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

def integ (x):
    return x**4*np.exp (x)/(np.exp (x)-1)**2


def gaussian_quadrature_integral(f, a, b, N):
    """Calculate integral using Gaussian quadrature
    Args:
    f (function): integrand function
    a (float): lower limit of the integration range
    b (float): upper limit of the integration range
    N (int): number of samples
    Returns:
    float: integral value"""
    i = 0.0

    gauss_xw=gaussxw(N)
    x=gauss_xw[0]
    w=gauss_xw[1]

    xp=0.5*(x*(b-a)+b+a)
    wp=0.5*w*(b-a)

    xp=0.5*(b-a)*x+0.5*(b+a)
    wp=0.5*(b-a)*w


    i=0
    for k in range(N):
        i+=wp[k]*integ(xp[k])

    return i



def heat_cap_of_solid_Cv(V, rho, theta, T, I):
    k=1.380649e-23 # Boltzmann constant in J/K
    return 9*V*rho*k*(T/theta)**3*I

def cv(T):
    """Computes the heat capacity using Gaussian quadrature integration
    Args:
    T (float): temperature in K
    Returns:
    float: heat capacity"""
    c = 0.0
    # constants
    kB = 1.38065e-23
    # Boltzmann's constant
    # system parameters
    V = 0.001
    # Volume in cubic meters
    rho = 6.022e28
    # Number density
    theta_d = 428
    # Debye temperature

    N = 50

    # Number of Gaussian quadrature samples

    a=0
    b=theta_d/T

    I=gaussian_quadrature_integral(integ, a, b, N)
    c=heat_cap_of_solid_Cv(V, rho, theta_d, T, I)

    return c


# # plotting
T_plot = np.linspace(5,500,100)

T1=5
T2=500

CV=[]
for i in T_plot:
    CV.append (cv (i))
CV=np.array (CV)

plt.plot (T_plot, CV)
plt.xlabel('Temperature (K)')
plt.ylabel('$C_V$ (J/K)')
plt.savefig ("2.3.jpg")
