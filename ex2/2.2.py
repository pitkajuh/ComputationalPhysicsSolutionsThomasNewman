# -*- coding: utf-8 -*-

# Our ability to resolve detail in astronomical observations is limited by the diffraction of light in
# our telescopes. Light from stars can be treated effectively as coming from a point source at
# infinity. When such light, with wavelength λ, passes through the circular aperture of a
# telescope (which we'll assume to have unit radius) and is focused by the telescope in the
# focal plane, it produces not a single dot, but a circular diffraction pattern consisting of central
# spot surrounded by a series of concentric rings. The intensity of the light in this diffraction
# pattern is given by

# where r is the distance in the focal plane from the center of the diffraction pattern,
# k = 2π/λ, and J1 (x) is a Bessel function. The Bessel functions Jm (x) are given by

# where m is a nonnegative integer and x ≥ 0.
# (a) Write a Python function J(m,x) that calculates the value of Jm (x) using Simpson's

# rule with N = 1000 points. Use your function in a program to make a plot, on a single
# graph, of the Bessel functions J0 , J1 , and J2 as a function of x from x = 0 to x = 20.

#            (b) Write a Python function I(r) that uses your Bessel function implementation to
# calculate the light intensity of the circular diffraction pattern of a point light source with
# λ = 500 nm. Then, make a plot of the diffraction pattern in a square region of the focal
# plane. Your picture should cover values of r from zero up to about 1 μm.
# Hint 1: You may find it useful to know that limx→0 J1 (x)/x = 1
#  2 .
# Hint 2: The central spot in the diffraction pattern is so bright that it may be difficult to see the
# rings around it on the computer screen. If you use imshow from pyplot you can give
# vmax as additional argument, i.e., plt.imshow(dp,vmax=0.005) . By lowering the
# vmax value, you can reduce the total range of values between the minimum and maximum
# brightness, and hence increase the sensitivity of the plot, making subtle details visible. For
# this exercise a value of vmax=0.005 appears to work well.


import numpy as np
import matplotlib.pyplot as plt

def func (theta, m, x):
    return np.cos (m*theta-x*np.sin (theta))

def J(m,x):
    """Calculates Bessel function values with Simpson's rule
    Args:
        m (int) : order m of the Bessel function
        x (float) : evaluation point x
    Returns:
        float: value of J_m(x)"""
    j = 0.0

    N = 1000 # number of sampled points

    lim_to=np.pi
    lim_from=0
    h=(lim_to-lim_from)/N
    simpson=func (lim_from, m, x)+func (lim_to, m, x)+4*func (lim_to-h, m, x)

    for i in range (1, int (N/2), 1):
        simpson+=4*func (lim_from+h*(2*i-1), m, x)+2*func (lim_to+2*i*h, m, x)

    j=h*simpson/(3*np.pi)

    return j

# plotting
x_plot = np.linspace(0,20,100)

plt.plot (x_plot, J (0,x_plot), label="$J_{0}$")
plt.plot (x_plot, J (1,x_plot), label="$J_{1}$")
plt.plot (x_plot, J (2,x_plot), label="$J_{2}$")
plt.legend ()
plt.xlabel('x')
plt.xlim ([0,20])
plt.savefig ("2.2.jpg")
plt.close ()

#validation
assert abs(J(0,0) - 1)  < 2e-7
assert abs(J(1,0) - 0)  < 2e-7
assert abs(J(2,170) + 0.055868957264523095) < 2e-7

def I(r):
    """Calculates the light intensity on the focal plane based on distance r
    Args:
        r (float) : distance on the focal plane
    Returns:
        float: Light intensity value"""
    i = 0.0

    # constants
    wavelength = 500e-9
    wavelength=0.5
    k=2*np.pi/wavelength

    i=(J (1, k*r)/(k*r))**2

    return i


x=np.linspace (-1, 1, 1000000).reshape ((1000, 1000))
y=np.linspace (-1, 1, 1000000).reshape ((1000, 1000))

x=np.linspace (-1, 1, 1000)
y=np.linspace (-1, 1, 1000)

x, y=np.meshgrid(x,y)

r=(x**2+y**2)**0.5
intensity=I (r)

plt.imshow (intensity, vmax=0.01)
plt.show ()
