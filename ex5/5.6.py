# -*- coding: utf-8 -*-

# Consider a piano string of length L , initially at rest. At time t = 0 the string is struck by the
# piano hammer a distance d from the end of the string:

# The string vibrates as a result of being struck, except at the ends, x = 0 and x = L, where
# it is held fixed.
# This system can be described by the 1D wave equation

# We start by dividing the string into discrete points with spacing a. Then we replace the right-
# hand side of the equation with a discrete difference, see lecture, and derive a set of second-
# order differential equation, one for each grid point

# (b) Plot the solution at 2 ms, 83 ms and 100 ms. Make also an animation of the motion of
# the piano string. There are various ways how you can could do animations, which were
# introduce in the first lecture of this course. You can use FuncAnimation from the
# matplotlib package. You can also use the vpython package by, e.g., placing a small
# sphere at the location of each grid point on the string. Allow your animation to run for at least
# 100 ms.

# (c) When do numerical instabilities start to appear? The FTCS method worked well for the
# diffusion problem discussed in the lecture. Can you improve the numerical stability for the
# wave equation by making the step size smaller?

import numpy as np
import matplotlib.pyplot as plt

# global constants
L = 1.0 # length of the string


def FTCS_string(phi0,psi0,t0,tf,h):
    """ Solves the time evolution of phi(t) and psi(t) in the
        range [t0,tf] using FTCS method.
    Args:
        phi0 (numpy float array): initial phi(t0)
        psi0 (numpy float array): initial psi(t0)
        t0 (float): start time
        tf (float): stop time
        h (float): time step. The length of the time interval tf-t0 should be a multiple of h.
    Returns
        numpy float array: [phi(t0), phi(t0+h), ..., phi(tf)]
        numpy float array: [psi(t0), psi(t0+h), ..., psi(tf)]"""
    phi = None
    psi = None
    N=len (phi0)-1
    phi=np.zeros_like (phi0)

    x_val=np.linspace (0, L, N+1)
    psi=psi_initial (x_val)
    # constants
    a = L/(len(phi0)-1)
    v = 100.0

    t=0

    while t<=tf:
        phi[1:N]+=h*psi[1:N]
        psi[1:N]+=(h*v**2/(a**2))*(phi[2:N+1]+phi[0:N-1]-2*phi[1:N])
        t+=h

    print (np.shape (phi), np.shape (psi), np.mean (phi), np.mean (psi))
    return phi, psi


def psi_initial(x):
    """ Initial profile for psi
    Args:
        x (float): coordinate x
    Returns
        float: psi(x) at t=0"""
    psi0 = 0.0

    # constants
    d = 0.1
    sigma = 0.3
    C = 1.0
    psi0=(C*x*(L-x)/L**2)*np.exp (-(x-d)**2/(2*sigma**2))

    return psi0


N =  100 # number of grid points
t0 = 0.0 # start time (s)
tf = 0.1 # stop time (s)
h = 1e-6 # time step (s)

# Initial values
x = np.linspace(0.0,L,N)
phi0 = np.zeros(N,float)
psi0 = np.array([psi_initial(x_val) for x_val in x])

# Solving the time evolution for the string
phi, psi = FTCS_string(phi0,psi0,t0,tf,h)

from celluloid import Camera

fig = plt.figure()
camera = Camera(fig)
# t = np.linspace(0, 2 * np.pi, 128, endpoint=False)
for i in x:
    phi, psi = FTCS_string(phi0,psi0,t0,tf+i,h)
    plt.plot(x, phi, color='blue')
    camera.snap()
plt.show ()
animation = camera.animate()
animation.save('celluloid_subplots.gif', writer = 'imagemagick')
