# -*- coding: utf-8 -*-
"""
Created: 16.01.2022 12:31

Author: jp
"""

# from numpy import array from pylab import loadtxt, plot, show, xlabel, ylabel, title,legend
import numpy as np
import matplotlib.pyplot as plt
values = np.loadtxt("velocities.txt", float)
time = (values[:, 0]).astype(int)
# time values in float, using astypr to convert them into integer
velocity = values[:, 1] # velocity values
function = dict(zip(time, velocity))
N = len(time) - 1 # step size
a = time[0]
#x_initial
b = time[-1]
#x_final
h = (b - a) // N
#difference between each step
S = 0
for k in range(1, N):
    S += function[a + k * h]
total_distance = h * (1/2 * (function[a] + function[b]) + S)
#the integral value of the velocity
distance = [0]
#the initial value
for k in range(N):
    d = 1/2 * h * (function[a + k*h] + function[a + (k+1) * h])
    distance.append(distance[-1] + d)

plt.plot(time, distance, "g--", label = "position")
plt.plot(time, velocity, "b-", label= "velocity")
plt.legend(loc='upper left')
plt.xlabel("Time(s)")
plt.title("Velocity vs Time and Distance vs Time")
plt.show()
