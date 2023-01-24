# -*- coding: utf-8 -*-

# The Lotka-Volterra equations are a mathematical model of predator-prey interactions
# between biological species. Let two variables x and y be proportional to the size of the
# populations of two species, traditionally called "rabbits" (the prey) and "foxes'' (the
# predators). You could think of x and y as being the population in thousands, say, so that
# x = 2 means there are 2000 rabbits. Strictly the only allowed values of x and y would then
# be multiples of 0.001, since you can only have whole numbers of rabbits or foxes. But 0.001
# is a pretty close spacing of values, so it's a decent approximation to treat x and y as
# continuous real numbers so long as neither gets very close to zero.
# In the Lotka-Volterra model the rabbits reproduce at a rate proportional to their population,
# but are eaten by the foxes at a rate proportional to both their own population and the
# population of foxes:

# where α and β are constants. At the same time the foxes reproduce at a rate proportional
# the rate at which they eat rabbits - because they need food to grow and reproduce - but also
# die of old age at a rate proportional to their own population:

# where γ and δ are also constants.
# (a) Write a program to solve these equations using the fourth-order Runge-Kutta method for
# the case α = 1, β = γ = 0.5 , and δ = 2 , starting from the initial condition x = y = 2.
# Make a graph showing both x and y as a function of time on the same axes from t = 0 to
# t = 20 .

import numpy as np
import matplotlib.pyplot as plt

def f_lotka_volterra(r,t):
    """ definition of the Lotka-Volterra equations
    Args:
        r (numpy float array): [x,y]
        t (numpy float array): time
    Returns
        numpy float array: [dx/dt,dy/dt]"""
    f_lv = np.empty(2,float)
    # constants
    alpha = 1.0
    beta = gamma = 0.5
    delta = 2.0
    x=r[0]
    y=r[1]
    f_lv[0]=alpha*x-beta*x*y
    f_lv[1]=gamma*x*y-delta*y

    return f_lv


r0 = np.array([2.0,2.0]) # initial population sizes
t0 = 0.0  # start time
tf = 20.0 # final time
h = 0.01  # time step
xp=[]
yp=[]

tp=np.arange (t0, tf, h)
# Solve the equations and plot the populations
for t in tp:
    xp.append (r0[0])
    yp.append (r0[1])
    k1=h*f_lotka_volterra (r0, t)
    k2=h*f_lotka_volterra (r0+0.5*k1, t+0.5*h)
    k3=h*f_lotka_volterra (r0+0.5*k2, t+0.5*h)
    k4=h*f_lotka_volterra (r0+k3, t+h)
    r0+=(k1+2*k2+2*k3+k4)/6

print (np.shape (xp), np.shape (yp), np.shape (tp))
plt.plot (tp, yp, label="foxes")
plt.plot (tp, xp, label="rabbits")
plt.legend ()
plt.xlabel('Time')
plt.ylabel('Population/1000')
plt.show ()

# validation
assert np.allclose(f_lotka_volterra(np.array([3.0,1.0]),5.0), [1.5,-0.5], rtol=1e-5, atol=1e-5)
