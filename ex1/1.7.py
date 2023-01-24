# -*- coding: utf-8 -*-

# It's a common situation in physics that an experiment produces data that lies roughly on a
# straight line, like the dots in this figure:

# The solid line here represents the underlying straight-line form, which we usually don't know,
# and the points representing the measured data lie roughly along the line but don't fall exactly
# on it, typically because of measurement error.
# The straight line can be represented in the familiar form y = mx + c and a frequent
# question is what the appropriate values of the slope m and intercept c are that correspond
# to the measured data. Since the data don't fall perfectly on a straight line, there is no perfect
# answer to such a question, but we can find the straight line that gives the best compromise
# fit to the data. The standard technique for doing this is the method of least squares.
# Suppose we make some guess about the parameters m and c for the straight line. We then
# calculate the vertical distances between the data points and that line, as represented by the
# short vertical lines in the figure, then we calculate the sum of the squares of those
# distances, which we denote χ 2 . If we have N data points with coordinates (xi , yi ), then χ 2
# is given by

# The solid line here represents the underlying straight-line form, which we usually don't know,
# and the points representing the measured data lie roughly along the line but don't fall exactly
# on it, typically because of measurement error.
# The straight line can be represented in the familiar form y = mx + c and a frequent
# question is what the appropriate values of the slope m and intercept c are that correspond
# to the measured data. Since the data don't fall perfectly on a straight line, there is no perfect
# answer to such a question, but we can find the straight line that gives the best compromise
# fit to the data. The standard technique for doing this is the method of least squares.
# Suppose we make some guess about the parameters m and c for the straight line. We then
# calculate the vertical distances between the data points and that line, as represented by the
# short vertical lines in the figure, then we calculate the sum of the squares of those
# distances, which we denote χ 2 . If we have N data points with coordinates (xi , yi ), then χ 2
# is given by

# These are the equations for the least-squares fit of a straight line to N data points. They tell
# you the values of m and c for the line that best fits the given data.
# (a) In the folder that you obtained this notebook you will find a file called millikan.txt .
# The file contains two columns of numbers, giving the x and y coordinates of a set of data
# points. Write a program to read these data points and make a graph with one dot or circle
# for each point.
# (b) Add code to your program, before the part that makes the graph, to calculate the
# quantities Ex , Ey , Exx , and Exy defined above, and from them calculate and print out the
# slope m and intercept c of the best-fit line.
# (c) Now write code that goes through each of the data points in turn and evaluates the
# quantity mxi + c using the values of m and c that you calculated. Store these values in a
# new array or list, and then graph this new array, as a solid line, on the same plot as the
# original data. You should end up with a plot of the data points plus a straight line that runs
# through them.
# (d) The data in the file millikan.txt are taken from a historic experiment by Robert
# Millikan that measured the photoelectric effect. When light of an appropriate wavelength is
# shone on the surface of a metal, the photons in the light can strike conduction electrons in
# the metal and, sometimes, eject them from the surface into the free space above. The
# energy of an ejected electron is equal to the energy of the photon that struck it minus a
# small amount φ called the work function of the surface, which represents the energy
# needed to remove an electron from the surface. The energy of a photon is hν, where h is
# Planck's constant and ν is the frequency of the light, and we can measure the energy of an
# ejected electron by measuring the voltage V that is just sufficient to stop the electron
# moving. Then the voltage, frequency, and work function are related by the equation

# where e is the charge on the electron. This equation was first given by Albert Einstein in
# 1905.
# The data in the file millikan.txt represent frequencies ν in hertz (first column) and
# voltages V in volts (second column) from photoelectric measurements of this kind. Using
# the equation above and the program you wrote, and given that the charge on the electron is
# 1.602 × 10−19 C, calculate from Millikan's experimental data a value for Planck's constant.
# Compare your value with the accepted value of the constant, which you can find in books or
# on-line. You should get a result within a couple of percent of the accepted value.
# This calculation is essentially the same as the one that Millikan himself used to determine of
# the value of Planck's constant, although, lacking a computer, he fitted his straight line to the
# data by eye. In part for this work, Millikan was awarded the Nobel prize in physics in 1923.


# data fitting
def fit(x, y):
    """Fits straight line to the data
    Args:
        x (list): list of x values
        y (list): list of y values
    Returns
        float: m slope of the line fit
        float: c constant of the line fit"""
    m, c = 0, 0

    import numpy as np

    x=np.array (x)
    y=np.array (y)
    N=len (x)
    Ex=(1/N)*np.sum (x)
    Ey=(1/N)*np.sum (y)
    Exx=(1/N)*np.sum (x**2)
    Exy=(1/N)*np.sum (x*y)

    m=(Exy-Ex*Ey)/(Exx-Ex**2)
    c=(Exx*Ey-Ex*Exy)/(Exx-Ex**2)

    return m, c

# validation
m, c = fit([0, 1], [0, 1])
assert m == 1, "bad fit"
assert c == 0, "bad fit"

import numpy as np
import matplotlib.pyplot as plt

data=np.loadtxt ("millikan.txt")
x=data[:,0]
y=data[:,1]

a=fit(x, y)

plt.plot (x, y, "ro")
plt.plot (x, a[0]*x+a[1])
plt.savefig ("7.jpg")

def get_plank_const(filename):
    """returns planks constant from millikan experiment
    Args:
        filename (str): name of file with millikan data
    Returns:
        float: plank's constant"""
    # constants
    m = 0 # slope of fit, h/e
    c = 0 # fitting constant, \phi, work funtion
    e = 1.602e-19 # charge on electron

    data=np.loadtxt ("millikan.txt")
    x=data[:,0]
    y=data[:,1]
    a=fit(x, y)
    m=a[0]
    c=a[1]

    return m * e

h = get_plank_const('millikan.txt')
print("plank's constant calculated = {} m^2Kg/s\n"
      "plank's constant = 6.626068e-34 m^2Kg/s".format(h))
assert abs(h - 6.626068e-34) < 1e-35, "error too large"
