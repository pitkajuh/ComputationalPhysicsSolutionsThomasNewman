# -*- coding: utf-8 -*-

# We want to solve the following second-order differential equation:

# (a) Change the second-order equation into two first-order equations and write them down.

# (b) Write a program that solves these equations using the Leapfrog method. Solve from
# t = 0 to t = 50 in steps of h = 0.001 with initial condition x = 1 and dx/dt = 0 . Make a
# plot of your solution showing x as a function of t.

import matplotlib.pyplot as plt
import numpy as np

def leapfrog(f,r0,t0,tf,h):
    """ Solves the time evolution of r(t) for dr/dt = f(r,t)
        in the range [t0,tf] using Leapfrog method.
    Args:
        f (function): f(r,t) in dr/dt = f(r,t)
        r0 (numpy float array): initial value r(t0)
        t0 (float): start time
        tf (float): stop time
        h (float): time step. The length of the time interval tf-t0 should be a multiple of h.
    Returns
        numpy float array: [r(t0), r(t0+h), ..., r(tf)]"""
    r = None
    r=r0
    tp=np.arange (t0, tf+h, h)
    xp=[]
    for i in range(len(tp)):
        xp.append (r[0])
        rm=r+0.5*h*f (r, tp[i])
        a=h*f (rm, tp[i])
        r+=a

    r=xp
    return r


def f(r,t):
    """ definition of the two first-order equations
    Args:
        r (float array): [x,v]
        t (float array): time
    Returns
        numpy float array: [dx/dt, dv/dt]"""
    f_xv = np.empty(2,float)
    f_xv[0]=r[1]
    f_xv[1]=r[1]**2-r[0]-5

    return f_xv


t0 = 0.0  # start time
tf = 50.0 # final time
h = 0.001 # time step
x0 = 1.0  # initial x
dx0 = 0.0 # initial dx/dt
tp=np.arange (t0, tf+h, h)
# Solve the equations and plot the results
r0=np.array ([1.0, 0.0])
plt.plot (tp, leapfrog (f, r0, t0, tf, h))

plt.xlabel('t')
plt.ylabel('x')
plt.show ()

# validation
assert np.allclose(f(np.array([4.0,3.0]),10.0), [3.0,0.0], rtol=1e-5, atol=1e-5)

# defining equation dx/dt = x + x/t
def f_test(x,t):
    return x + x/t

leapfrog_test = leapfrog(f_test,np.array([1.5]),1.0,2.0,0.001)
print (leapfrog_test[-1] - 8.154845485377136)
assert len(leapfrog_test) == 1001

assert abs(leapfrog_test[-1] - 8.154845485377136) < 1e-2
