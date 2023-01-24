# -*- coding: utf-8 -*-
"""
Created: 26.01.2022 16:23

Author: jp
"""

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
    # raise NotImplementedError()
    return data

# data = read_dow_data('dow.txt')
# # plotting
# plt.plot (data)
# # raise NotImplementedError()
# plt.xlabel('days')
# plt.ylabel('closing value')
# # plt.show ()
# # plt.savefig("4.2-1.jpg")


# fn = read_dow_data('dow.txt')
# assert isinstance(fn, np.ndarray), 'bad function'
# assert fn.shape == (1024,), 'bad function'
# assert fn.dtype == float, 'bad function'




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
    # raise NotImplementedError()
    return dft

# # compute dft,
# dft_data = dft_numpy(data)

# # validation
# n = 10
# fn = np.sin(np.arange(n))
# dft = dft_numpy(fn)
# c_k2 = np.abs(dft)**2
# assert abs(c_k2[0] - 3.82284412) <= 1e-4, 'bad function'
# assert abs(c_k2[1] - 10.28600735) <= 1e-4, 'bad function'


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

    # first=np.zeros (int(len (y)*x/100))
    # y=y[int (len (y)-len (y)*x/100):-1]
    partc_out=[]
    # print ("ln (y)=", len (y), "x=", x, "maara", len (y)*x//100-1)
    for i in range(len(y)):
        # print (i, int(len (y)*x/100))
        # if i==int(len (y)*x/100)-1:
        if i<=len (y)*x//100-1:
            partc_out.append (y[i])
        else:
            partc_out.append (0)
    # first[0:x/100]=np.copy (y[0:x/100])
    partc_out=np.array (partc_out)

    # y[len (y)//100:]=0
    # partc_out1=y

    # if partc_out1==partc_out:
    #     print ("1")

    # print ("asd",np.shape (partc_out))
    # raise NotImplementedError()
    # print ("ln out", np.shape (partc_out), np.shape (y))
    # print (y[10:])
    # print (partc_out[10:])
    return partc_out

# dft_data_trimmed = data_trim(dft_data, 10)


# a = np.arange(1, 11)
# a_trimmed = data_trim(a, 30)


# #validation
# a = np.arange(1, 11)
# a_trimmed = data_trim(a, 10)
# # print ("a", a, a_trimmed)




# assert len(a_trimmed) == len(a), 'bad function'
# for i in range(1, 10):
#     # print ("i", i, "on", len(np.where(data_trim(a, i*10)==0)[0]), "pit ol", 10 - i, "arvo", data_trim(a, i*10))
#     assert len(np.where(data_trim(a, i*10)==0)[0]) == 10 - i, 'bad function'



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
    # print ("ln", np.shape (idft), np.shape (y))
    # raise NotImplementedError()
    return idft

# # compute idft
# data_idft = idft_numpy(dft_data_trimmed)

# # plotting
# plt.plot (data_idft)

# # raise NotImplementedError()
# plt.xlabel('days')
# plt.ylabel('closing value')
# # plt.show ()

# # validation
# n = 10
# fn = np.sin(np.arange(n))
# dft = dft_numpy(fn)
# fn_idft = idft_numpy(dft)
# assert np.mean(np.abs(fn - fn_idft)) <= 1e-4, 'bad function'






# # get trimmed data
# dft_data = dft_numpy(data)
# dft_data_trimmed = data_trim(dft_data, 2)
# data_idft = idft_numpy(dft_data_trimmed)
# # raise NotImplementedError()
# # plotting
# # data = read_dow_data('dow.txt')
# # plt.plot (data)
# plt.plot (data_idft)
# # raise NotImplementedError()
# plt.xlabel('days')
# plt.ylabel('closing value')
# plt.show ()
