# -*- coding: utf-8 -*-

# Exercise 4.2 looked at data representing the variation of the Dow Jones Industrial Average,
# colloquially called "the Dow," over time. The particular time period studied in that exercise

# was special in one sense: the value of the Dow at the end of the period was almost the
# same as at the start, so the function was, roughly speaking, periodic. In the folder that you
# obtained this notebook there is another file called dow2.txt , which also contains data on
# the Dow but for a different time period, from 2004 until 2008. Over this period the value
# changed considerably from a starting level around 9000 to a final level around 14000.
# (a) Write a program in which you read the data in the file dow2.txt and plot it on a graph.
# Then smooth the data by calculating its Fourier transform, setting all but the first 2% of the
# coefficients to zero, and inverting the transform again, plotting the result on the same graph
# as the original data. You should see that the data are smoothed, but now there will be an
# additional artifact. At the beginning and end of the plot you should see large deviations away
# from the true smoothed function. These occur because the function is required to be
# periodic---its last value must be the same as its first---so it needs to deviate substantially
# from the correct value to make the two ends of the function meet. In some situations
# (including this one) this behavior is unsatisfactory. If we want to use the Fourier transform
# for smoothing, we would certainly prefer that it not introduce artifacts of this kind.

# (b) Modify your program to repeat the same analysis using discrete cosine transforms. You
# can use the functions from dcst.py (in the folder that you obtained this notebook) to
# perform the transforms if you wish. Again discard all but the first 2% of the coefficients,
# invert the transform, and plot the result. You should see a significant improvement, with less
# distortion of the function at the ends of the interval. This occurs because the cosine
# transform does not force the value of the function to be the same at both ends.
# It is because of the artifacts introduced by the strict periodicity of the DFT that the cosine
# transform is favored for many technological applications, such as audio compression. The
# artifacts can degrade the sound quality of compressed audio and the cosine transform
# generally gives better results.
# The cosine transform is not wholly free of artifacts itself however. It's true it does not force
# the function to be periodic, but it does force the gradient to be zero at the ends of the
# interval (which the ordinary Fourier transform does not). You may be able to see this in your
# calculations for part (b) above. Look closely at the smoothed function and you should see
# that its slope is flat at the beginning and end of the interval. The distortion of the function
# introduced is less than the distortion in part (a), but it's there all the same. To reduce this
# effect, audio compression schemes often use overlapped cosine transforms, in which
# transforms are performed on overlapping blocks of samples, so that the portions at the ends
# of blocks, where the worst artifacts lie, need not be used.

import numpy as np
import matplotlib.pyplot as plt
import funcs as f

# use already made functions in 4.2

data=f.read_dow_data ("dow2.txt")
plt.plot (data)

dft_data = f.dft_numpy(data)
dft_data_trimmed = f.data_trim(dft_data, 2)
data_idft = f.idft_numpy(dft_data_trimmed)
plt.plot (data_idft)

plt.xlabel('days')
plt.ylabel('DOW closing values')
plt.show ()

# use already made functions in 4.2 and dcst.py
from dcst import dct, idct

# plotting
plt.plot (data)
dft_data = dct(data)
dft_data_trimmed = f.data_trim(dft_data, 2)
data_idct = idct(dft_data_trimmed)
plt.plot (data_idct)

plt.xlabel('days')
plt.ylabel('DOW closing values')
plt.show ()
