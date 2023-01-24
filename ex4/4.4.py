# -*- coding: utf-8 -*-

# You've probably seen it on TV, in one of those crime drama shows. They have a blurry
# photo of a crime scene and they click a few buttons on the computer and magically the
# photo becomes sharp and clear, so you can make out someone's face, or some lettering on
# a sign. Surely (like almost everything else on such TV shows) this is just science fiction?
# Actually, no. It's not. It's real and in this exercise you'll write a program that does it.
# When a photo is blurred each point on the photo gets smeared out according to some
# "smearing distribution," which is technically called a point spread function. We can represent
# this smearing mathematically as follows. For simplicity let's assume we're working with a
# black and white photograph, so that the picture can be represented by a single function
# a(x, y) which tells you the brightness at each point (x, y) . And let us denote the point
# spread function by f(x, y). This means that a single bright dot at the origin ends up
# appearing as f(x, y) instead. If f(x, y) is a broad function then the picture is badly blurred.
# If it is a narrow peak then the picture is relatively sharp.
# In general the brightness b(x, y) of the blurred photo at point (x, y) is given by

# where K × L is the dimension of the picture. This equation is called the convolution of the
# picture with the point spread function.
# Working with two-dimensional functions can get complicated, so to get the idea of how the
# math works, let's switch temporarily to a one-dimensional equivalent of our problem. Once
# we work out the details in 1D we'll return to the 2D version. The one-dimensional version of
# the convolution above would be

# (a) In the folder that you obtained this notebook you will find a file called blur.txt that
# contains a grid of values representing brightness on a black-and-white photo---a badly out-
# of-focus one that has been deliberately blurred using a Gaussian point spread function of
# width σ = 25 . Write a program that reads the grid of values into a two-dimensional array of
# real numbers and then draws the values on the screen of the computer as a density plot.

# (b) Write another program that creates an array, of the same size as the photo, containing a
# grid of samples drawn from the Gaussian~f(x, y) above with σ = 25 . Make a density plot
# of these values on the screen too, so that you get a visualization of your point spread
# function. Remember that the point spread function is periodic (along both axes), which
# means that the values for negative x and y are repeated at the end of the interval. Since the
# Gaussian is centered on the origin, this means there should be bright patches in each of the
# four corners of your picture, something like this:

# (c) Combine your two programs and add Fourier transforms using the functions rfft2
# and irfft2 from numpy.fft , to make a program that does the following:
# i) Calculates Fourier transform of both, photo and point spread function
# ii) Divides one by the other
# iii) Performs an inverse transform to get the unblurred photo
# iv) Displays the unblurred photo on the screen
# When you are done, you should be able to make out the scene in the photo, although
# probably it will still not be perfectly sharp.
# Hint: One thing you'll need to deal with is what happens when the Fourier transform of the
# point spread function is zero, or close to zero. In that case if you divide by it you'll get an
# error (because you can't divide by zero) or just a very large number (because you're dividing
# by something small). A workable compromise is that if a value in the Fourier transform of the
# point spread function is smaller than a certain amount ε you don't divide by it---just leave
# that coefficient alone. The value of ε is not very critical but a reasonable value seems to be
# 10−3 .

# (d) Bearing in mind this last point about zeros in the Fourier transform, what is it that limits
# our ability to deblur a photo? Why can we not perfectly unblur any photo and make it
# completely sharp?
# We have seen this process in action here for a normal snapshot, but it is also used in many
# physics applications where one takes photos. For instance, it is used in astronomy to
# enhance photos taken by telescopes. It was famously used with images from the Hubble
# Space Telescope after it was realized that the telescope's main mirror had a serious
# manufacturing flaw and was returning blurry photos---scientists managed to partially correct
# the blurring using Fourier transform techniques.


import numpy as np
import matplotlib.pyplot as plt

def read_2D_data(filename):
    """Reads 2D data

    Args:
        filename (str): name of the file

    Returns:
        numpy array: the data"""

    data = None
    data=np.loadtxt (filename)

    return data

data = read_2D_data('blur.txt')

def gauss(x, y, sigma):
    return np.exp(-(x**2+y**2)/(2*sigma**2))

def get_point_spread_function(data, sigma):
    """Retruns a gaussian point spread function

    Args:
        data (numpy array): the photo array to get the size of the spread function
        sigma (float): sigma of gaussian

    Returns:
        numpy array: the point spread function"""
    spread = np.zeros_like(data)

    for i in range (data.shape[0]):
        for j in range (data.shape[1]):
            spread[i, j]+=gauss (i, j, sigma)
            spread[-i, j]+=gauss (i, j, sigma)
            spread[i, -j]+=gauss (i, j, sigma)
            spread[-i, -j]+=gauss (i, j, sigma)

    # raise NotImplementedError()

    return spread

point_func = get_point_spread_function(data, 25)

def deconvolve(data, point_function):
    """Deconvolves point_function from the data

    Args:
        data (numpy array): the 2D data to deconvolve
        point_dunction (numpy array): the point function

    Returns:
        numpy array: Deconvolved array"""

    print (np.shape (data))
    deconv_data = np.zeros_like(data, complex)
    epsilon = 1e-3

    data = read_2D_data('blur.txt')
    blur=np.fft.rfft2 (data)
    pt_fn = get_point_spread_function(data, 25)
    pfunc=np.fft.rfft2 (pt_fn)
    N=len (pfunc)
    print (len (pfunc), len (blur))

    for x in range (N):
        for y in range (N//2+1):
            if pfunc[x][y]<epsilon:
                deconv_data[x][y]=blur[x, y]
            else:
                deconv_data[x][y]=blur[x, y]/pfunc[x, y]

    deconv_data=np.fft.irfft2 (deconv_data)
    print (np.shape (deconv_data))
    return deconv_data

data = read_2D_data('blur.txt')
# try different values of sigma to get the best deconvolution without artefacts
point_func = get_point_spread_function(data, 20)
deconc_data = deconvolve(data, point_func)

# plotting
plt.imshow (deconc_data)
plt.show ()
