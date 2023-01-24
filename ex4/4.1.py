# -*- coding: utf-8 -*-

# In the folder that you obtained this notebook there is a file called sunspots.txt , which
# contains the observed number of sunspots on the Sun for each month since January 1749.
# The file contains two columns of numbers, the first representing the month and the second
# being the sunspot number.
# (a) Write a program that reads the data in the file and makes a graph of sunspots as a
# function of time. You should see that the number of sunspots has fluctuated on a regular
# cycle for as long as observations have been recorded. Make an estimate of the length of the
# cycle in months.

# (b) Modify your program to calculate the Fourier transform of the sunspot data and then
# make a graph of the magnitude squared |ck |2 of the Fourier coefficients as a function of
# k ---also called the power spectrum of the sunspot signal. You should see that there is a
# noticeable peak in the power spectrum at a nonzero value of~k. The appearance of this
# peak tells us that there is one frequency in the Fourier series that has a higher amplitude
# than the others around it---meaning that there is a large sine-wave term with this frequency,
# which corresponds to the periodic wave you can see in the original data.

# (c) Find the approximate value of k to which the peak corresponds. What is the period of the
# sine wave with this value of k? You should find that the period corresponds roughly to the
# length of the cycle that you estimated in part~(a).
# This kind of Fourier analysis is a sensitive method for detecting periodicity in signals. Even
# in cases where it is not clear to the eye that there is a periodic component to a signal, it may
# still be possible to find one using a Fourier transform.

import numpy as np
from matplotlib import pyplot as plt

def read_sunspot_data(filename):
    """Reads and returns sunspot data

    Args:
        filename (str): name of the file

    Returns:
        numpy array: the data"""

    data = None
    data=np.loadtxt (filename)

    return data

data = read_sunspot_data('sunspots.txt')[:, :]
# plotting
plt.plot (data[:, 0], data[:, 1])
plt.xlabel('time (months)')
plt.ylabel('sunspot (#)')
plt.close ()
plt.show ()

# validation
fn = read_sunspot_data('sunspots.txt')
assert isinstance(fn, np.ndarray), 'bad function'
assert fn.shape == (3143, 2), 'bad shape'
assert fn.dtype == float, 'bad type'


def discrete_fourier_transform(y):
    """Calculates coefficient of the discrete trasnform of 1D y

    Args:
        y (numpy array): 1D data

    Returns:
        numpy array: 1D array of coefficients after fourier transform"""
    # coefficients
    c = None

    N=len (y)
    c=np.zeros (N//2+1, complex)
    for k in range (N//2+1):
        for n in range (N):
            c[k]+=y[n]*np.exp (2j*np.pi*k*n/N)

    return c

# validation
n = 10
fn = np.sin(np.arange(n))
dft = discrete_fourier_transform(fn)
c_k2 = np.abs(dft)**2
assert abs(c_k2[0] - 3.82284412) <= 1e-4, 'bad function'
assert abs(c_k2[1] - 10.28600735) <= 1e-4, 'bad function'

fft_data = discrete_fourier_transform(data[:, 1])

#plotting
print (np.shape(c_k2), np.shape(fft_data))
plt.plot (abs(fft_data))

plt.xlabel('k')
plt.ylabel('$c_k^2$')
plt.show ()
