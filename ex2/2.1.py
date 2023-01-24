# -*- coding: utf-8 -*-

# In the folder for exercise 2 you will find a file called velocities.txt , which contains two
# columns of numbers, the first representing time t in seconds and the second the x-velocity
# in meters per second of a particle, measured once every second from time t = 0 to
# t = 100. The first few lines look like this:

# (a) Write a function that reads in the data and returns it as an array. Then, write another
# function that uses the trapezoidal rule to approximate the distance traveled by the particle in
# the x direction as a function of time.

# (b) Extend your program to make a graph that shows, on the same plot, both the original
# velocity curve and the distance traveled as a function of time.


import numpy as np
from matplotlib import pyplot as plt
import scipy

def read_velocity_data():
    """Reads and returns velocity data
    Returns:
        numpy array: data array of shape (101, 2)"""
    data = None

    data=np.loadtxt ("velocities.txt")

    return data

def distance_traveled(t,v):
    """Calculates the distance traveled using the trapezoidal rule
    Args:
        t (numpy array) : time (ordered t[i] < t[i+1])
        v (numpy array) : v[i] is the velocity at time t[i]
    Returns:
        numpy array: distance traveled at each time t[i]"""
    x = None

    N=len (t)
    width=(t[-1]-t[0])/N
    x1=0
    x=[]
    for i in range (N):
        x1+=0.5*(v[i-1]+v[i])*width
        x.append(x1)

    x=np.array (x)
    return x


# validation
data = read_velocity_data()

assert isinstance(data, np.ndarray), 'data not a numpy array'
assert data.shape == (101, 2), 'bad shape'
assert data.dtype == float, 'bad type'

assert abs(distance_traveled(np.array([0,1,3]),np.array([1,1,2]))[2] - 4.0) < 2e-7


# plotting
data = read_velocity_data()
plt.plot (data[:,0], data[:,1], label="velocity")

plt.plot (data[:,0],distance_traveled (data[:,0], data[:,1]), label="distance")
plt.legend ()
plt.xlabel('Time [s]')
plt.savefig ("1.jpg")
