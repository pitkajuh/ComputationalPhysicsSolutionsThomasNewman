# -*- coding: utf-8 -*-

# Chemical kinetics or reaction kinetics investigates the speed of a chemical reaction, i.e.,
# how fast the concentration of a reactant changes with time. The reactions are due to
# collisions of the the reactant species. The frequency with which the molecules or ions collide
# depends - next to theromodynamic variables such as the temperature - on their
# concentrations. Lets consider the thermical decomposition of dimethlyether

# This is an reaction of the type

# Since we have only one reactant, the reaction rate will depend only on the concentration cA
# of A. This is a so-called 1st order reaction. The differential equation for a 1st order reaction
# is

# where k is the reaction rate coefficient, which depends on the temperature, the activation
# energy of the reaction and other factors.
# (a) Solve this equation i) analytically and write a program to solve with ii) the Euler method
# and iii) the 4th-order Runge-Kutta (RK4) method. Assume that the concentration of A is
# cA = 1 mol/l at t = 0 and that k = 2.0 min−1 . For the Euler method and RK4 method
# use a step size of h = 0.1 min . Plot cA (t) for t = 0 to t = 1 min using the analytic, Euler

# (b) Repeat the Euler and RK4 calculations for step sizes
# h = 0.2, 0.1, 0.05, 0.02, 0.01, 0.005, 0.002, 0.001, 0.0005 min . Calculate the errors with
# respect to the analytic solution after 1 min, i.e., calculate

# (c) Investigate the convergence properties of the Euler and RK4 solver with respect to h
# further: Determine from your calculations in 5.1.b the scaling of the error (hn ) by power-
# law fits. Do the obtained exponents n match the theoretical predictions? Replot the errors
# from 5.1.b with the fitted error curves. Hint: If you use a log-scale for the axes, you can
# perform a simple linear fit to get the exponents n.

# imports
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation


def analytic(t,c0):
    """ Analytic solution c_A(t)
    Args:
        t (float): time
        c0 (float): initial value c(t=0)
    Returns
        float: c(t)"""
    c = 0.0

    #constants
    k = 2.0

    c=c0*np.exp (-k*t)

    return c

def euler(f,x0,t0,tf,h):
    """ Solves the time evolution of x(t) for dx/dt = f(x,t)
        in the range [t0,tf] using Euler's method.
    Args:
        f (function): f(x,t) in dx/dt = f(x,t)
        x0 (float or numpy float array): initial value x(t0)
        t0 (float): start time
        tf (float): stop time
        h (float): time step. The length of the time interval tf-t0 should be a multiple of h.
    Returns
        numpy float array: [x(t0), x(t0+h), ..., x(tf)]"""
    x = None
    x=[]
    tp=np.arange (t0, tf+h, h)

    for i in tp:
        x.append (x0)
        x0+=h*f (x0, i)
    x=np.array (x)
    return x


def rk4(f,x0,t0,tf,h):
    """ Solves the time evolution of x(t) for dx/dt = f(x,t)
        in the range [t0,tf] using the 4th order Runge-Kutta method.
    Args:
        f (function): f(x,t) in dx/dt = f(x,t)
        x0 (float or numpy float array): initial value x(t0)
        t0 (float): start time
        tf (float): stop time
        h (float): time step. The length of the time interval tf-t0 should be a multiple of h.
    Returns
        numpy float array: [x(t0), x(t0+h), ..., x(tf)]"""
    x = None
    tp=np.arange (t0, tf+h, h)
    x=[]

    for i in tp:
        x.append (x0)
        k1=h*f (x0, i)
        k2=h*f (x0+0.5*k1, i+0.5*h)
        k3=h*f (x0+0.5*k2, i+0.5*h)
        k4=h*f (x0+k3, i+h)
        x0+=(k1+2*k2+2*k3+k4)/6

    x=np.array (x)
    return x


def f(c,t):
    """ Definition of equation dc/dt = f(c,t) = -k*c
    Args:
        c (float): concentration of A
        t (float): time
    Returns
        float: dc/dt"""
    k = 2.0
    return -k*c

c0 = 1.0 # initial concentration of A at t=0
t0 = 0.0 # initial time (min)
tf = 1.0 # final time (min)
h = 0.1  # time step (min)

tp=np.arange (t0, tf+h, h)
x0=1


# # Solve the time evolution with the three methods and plot the results
plt.plot (tp, analytic (tp, x0), label="analytical")
plt.plot (tp, euler (f, x0, t0, tf, h), label="euler")
plt.scatter (tp, rk4 (f, x0, t0, tf, h), label="rk4")
plt.legend ()

plt.xlabel('t (min)')
plt.ylabel('$c_A$ (mol/l)')
plt.close ()


# validation
assert abs(analytic(1.5,1.0) - 0.049787068367863944) < 1e-5

# defining equation dx/dt = x + x/t
def f_test(x,t):
    return x + x/t

euler_test = euler(f_test,1.5,1.0,2.0,0.001)
print (len (euler_test), euler_test[-1])
assert len(euler_test) == 1001
assert abs(euler_test[-1] - 8.154845485377136) < 2e-2

rk4_test = rk4(f_test,1.5,1.0,2.0,0.001)
assert len(rk4_test) == 1001
assert abs(rk4_test[-1] - 8.154845485377136) < 1e-5

h_points = [0.2,0.1,0.05,0.02,0.01,0.005,0.002,0.001,0.0005]

c0 = 1.0 # initial concentration of A at t=0
t0 = 0.0 # initial time (min)
tf = 1.0 # final time (min)

# Calculate the errors and plot the results
err_euler=[]
err_rk4=[]
asd=[]

for i in h_points:
    an=analytic (tp, x0)[-1]
    eul=euler (f, x0, t0, tf, i)[-1]
    rkk4=rk4 (f, x0, t0, tf, i)[-1]
    err_euler.append (abs (an-eul))
    err_rk4.append (abs (an-rkk4))

from sklearn.linear_model import LinearRegression
model1 = LinearRegression()
model1.fit(h_points, err_euler)
model1 = LinearRegression().fit(h_points, err_euler)

plt.plot (h_points, err_euler, "o", label="Euler error")
plt.plot (h_points, err_rk4, "o", label="rk4 error")
plt.ylabel ("Error")
plt.xlabel ("Step size")
plt.xscale ("log")
plt.yscale ("log")
plt.legend ()
plt.show ()
