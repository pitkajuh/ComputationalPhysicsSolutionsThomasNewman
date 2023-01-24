# -*- coding: utf-8 -*-

# In the folder that you obtained this notebook you'll find a file called dow.txt . It contains
# the daily closing value for each business day from late 2006 until the end of 2010 of the
# Dow Jones Industrial Average, which is a measure of average prices on the US stock
# market.
# Write a program to do the following:
# (a) Read in the data from dow.txt and plot them on a graph.

# (b) Calculate the coefficients of the discrete Fourier transform of the data using the function
# rfft from numpy.fft , which produces an array of 1
#  2 N + 1 complex numbers.

# (c) Now set all but the first 10% of the elements of this array to zero (i.e.,~set the last 90% to
# zero but keep the values of the first 10%).

# (d) Calculate the inverse Fourier transform of the resulting array, zeros and all, using the
# function \verb|irfft|, and plot it on the same graph as the original data. You may need to vary
# the colors of the two curves to make sure they both show up on the graph. Comment on what you see. What is happening when you set the Fourier coefficients to zero?

import numpy as np
from matplotlib import pyplot as plt

def read_dow_data(filename):
    """read dow data from filename

    Args:
        filename (str): name of the file

    Returns:
        numpy array: dow data"""
    data = None
    data=np.loadtxt (filename)

    return data

data = read_dow_data('dow.txt')
# plotting
plt.plot (data)
plt.xlabel('days')
plt.ylabel('closing value')

fn = read_dow_data('dow.txt')
assert isinstance(fn, np.ndarray), 'bad function'
assert fn.shape == (1024,), 'bad function'
assert fn.dtype == float, 'bad function'

def dft_numpy(y):
    """Perform numpy rfft

    Args:
        y (array): input data
    Returns:
        numpy array: dft of data
    """
    dft = None
    # modifications on y should not change incomming data too
    y = np.copy(y)
    dft=np.fft.rfft (y)
    return dft

# compute dft,
dft_data = dft_numpy(data)

# validation
n = 10
fn = np.sin(np.arange(n))
dft = dft_numpy(fn)
c_k2 = np.abs(dft)**2
assert abs(c_k2[0] - 3.82284412) <= 1e-4, 'bad function'
assert abs(c_k2[1] - 10.28600735) <= 1e-4, 'bad function'


def data_trim(y, x):
    """trim data, by making all but first x% elements to zero
    Args:
    y (numpy array): fft data
    x (float): percentage of first elements to be the same
    Returns:
    numpy array: trimmed data
    """
    partc_out = None
    # modifications on y should not change incomming data too
    y = np.copy(y)
    partc_out=[]

    for i in range(len(y)):
        if i<=len (y)*x//100-1:
            partc_out.append (y[i])
        else:
            partc_out.append (0)

    partc_out=np.array (partc_out)

    return partc_out

dft_data_trimmed = data_trim(dft_data, 10)


a = np.arange(1, 11)
a_trimmed = data_trim(a, 30)


#validation
a = np.arange(1, 11)
a_trimmed = data_trim(a, 10)

assert len(a_trimmed) == len(a), 'bad function'
for i in range(1, 10):
    assert len(np.where(data_trim(a, i*10)==0)[0]) == 10 - i, 'bad function'



def idft_numpy(y):
    """Perform numpy irfft
    Args:
    y (array): input data
    Returns:
    numpy array: dft of data
    """
    idft = None
    # modifications on y should not change incomming data too
    y = np.copy(y)
    idft=np.fft.irfft (y)
    return idft

# compute idft
data_idft = idft_numpy(dft_data_trimmed)

# plotting
plt.plot (data_idft)

# raise NotImplementedError()
plt.xlabel('days')
plt.ylabel('closing value')

# validation
n = 10
fn = np.sin(np.arange(n))
dft = dft_numpy(fn)
fn_idft = idft_numpy(dft)
assert np.mean(np.abs(fn - fn_idft)) <= 1e-4, 'bad function'

# get trimmed data
dft_data = dft_numpy(data)
dft_data_trimmed = data_trim(dft_data, 2)
data_idft = idft_numpy(dft_data_trimmed)

plt.plot (data_idft)
plt.xlabel('days')
plt.ylabel('closing value')
plt.show ()
