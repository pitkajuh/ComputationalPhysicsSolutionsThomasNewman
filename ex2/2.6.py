# -*- coding: utf-8 -*-

# When light strikes a surface, the amount falling per unit area depends not only on the
# intensity of the light, but also on the angle of incidence. If the light makes an angle θ to the
# normal, it only "sees" cos θ of area per unit of the actual area on the surface:

# So the intensity of illumination is a cos θ, if a is the raw intensity of the light. This simple
# physical law is a central element of 3D computer graphics. It allows us to calculate how light
# falls on three-dimensional objects and hence how they will look when illuminated from
# various angles.
# Suppose, for instance, that we are looking down on the Earth from above and we see
# mountains. We know the height of the mountains w(x, y) as a function of position in the
# plane, so the equation for the Earth's surface is simply z = w(x, y), or equivalently
# w(x, y) − z = 0 , and the normal vector v ⃗ to the surface is given by the gradient of
# w(x, y) − z thus:
  
# Now suppose we have light coming in represented by a vector a ⃗ with magnitude equal to
# the intensity of the light. Then the dot product of the vectors a ⃗ and v ⃗ is
# a ⃗ ⋅ v ⃗ = |a ⃗| |v ⃗| cos θ,
# where θ is the angle between the vectors. Thus the intensity of illumination of the surface of
# the mountains is

# Let's take a simple case where the light is shining horizontally with unit intensity, along a line
# an angle φ counter-clockwise from the east-west axis, so that a ⃗ = (cos φ, sin φ, 0). Then
# our intensity of illumination simplifies to

# If we can calculate the derivatives of the height w(x, y) and we know φ we can calculate
# the intensity at any point.
# (a) In the folder of exercise 2 you'll find a file called altitude.txt , which contains the
# altitude w(x, y) in meters above sea level (or depth below sea level) of the surface of the
# Earth, measured on a grid of points (x, y). The data in the file are in the following
# row/column format

# Write a function that reads an altitude data file and returns the data as an array. Then write
# another function that calculates the derivatives ∂w/∂x and ∂w/∂y at each grid point. Using
# multiline comment blocks and inline comments, explain what method you used to calculate

# (b) Now, using the values for the derivatives, calculate the intensity at each grid point, with
# φ = 135∘ , and make a density plot of the resulting values in which the brightness of each
# dot depends on the corresponding intensity value. If you get it working right, the plot should
# look like a relief map of the world; you should be able to see the continents and mountain
# ranges in 3D. (Common problems include a map that is upside-down or sideways, or a relief
# map that is "inside-out", meaning the high regions look low and vice versa. Work on your
# program until you get a map that looks right to you.)

# (c) There is another file in the resources called stm.txt , which contains a grid of values
# from scanning tunneling microscope measurements of the (111) surface of silicon. A
# scanning tunneling microscope (STM) is a device that measures the shape of surfaces at
# the atomic level by tracking a sharp tip over the surface and measuring quantum tunneling
# current as a function of position. The end result is a grid of values that represent the height
# of the surface as a function of position and the data in the file stm.txt contain just such
# a grid of values. Modify the program you just wrote to visualize the STM data and hence
# create a 3D picture of what the silicon surface looks like. The value of h for the derivatives in
# this case is around h = 2.5 (in arbitrary units).



def read_altitude_data(filename):
    """Reads and returns altitude data
    Args:
    filename (str): name of the data file
    Returns:
    numpy array: the data"""
    data = None
    import numpy as np
    import matplotlib.pyplot as plt
    data=np.loadtxt (filename)
    return data

def calc_derivatives(w,h):
    """Calculates derivatives of height
    Args:
    w (numpy array): 2D numpy array
    h (float): difference
    Returns:
    numpy array: dw/dx at each grid
    numpy array: dw/dy at each grid
    dx = None
    dy = None
    map w with regards to x and y
    height map
    point in w
    point in w"""

    import numpy as np
    import matplotlib.pyplot as plt

    x=w[:,0]
    y=w[1,:]

    dx=np.empty ((len(x), len(2*y)))
    dy=np.empty ((len(x), len(2*y)))

    for i in range (1, len (x)-1, 1):
            for j in range (1, len (y)-1, 1):
                dx[i, j]=(w[i+1, j]-w[i-1, j])/(2*h)
                dy[i, j]=(w[i, j+1]-w[i, j-1])/(2*h)

    return dx,dy


def calc_intensity(dx,dy,phi):
    """Calculates the lighting intensity
    Args:
    dx (numpy array): 2D array of dw/dx values
    dy (numpy array): 2D array of dw/dy values
    phi (float): angle of the incoming light in radians
    Returns:
    numpy array: lighting intensity at each grid point"""
    I = None
    import numpy as np
    import matplotlib.pyplot as plt
    I=(1/(dx**2+dy**2+1)**0.5)*(np.cos (phi)*dx+np.sin (phi)*dy)

    return I


# plotting
import numpy as np
import matplotlib.pyplot as plt
w = read_altitude_data("altitude.txt")
phi = 135*np.pi/180
h = 30000
d=calc_derivatives (w, h)

plt.imshow (calc_intensity (d[0], d[1], phi))
plt.savefig ("2.6b.jpg")
ptl.close

# plotting
w = read_altitude_data("stm.txt")
h = 2.5
d=calc_derivatives (w, h)
plt.imshow (calc_intensity (d[0], d[1], phi))
plt.savefig ("2.6c.jpg")
# raise NotImplementedError()
