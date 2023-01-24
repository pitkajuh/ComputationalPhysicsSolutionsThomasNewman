# -*- coding: utf-8 -*-

# Use the Verlet method to calculate the orbit of the Earth around the Sun. The differential
# equation obeyed by the earth is straightforward to derive. The force between the Sun, with
# mass M at the origin, and a earth of mass m with position vector r is GMm/r2 in direction
# −r/r (i.e., the direction towards the Sun), and hence Newton's second law tells us that

# Canceling the m and taking the x component we have

# and similarly for the other two coordinates. We can, however, throw out one of the
# coordinates because the earth stays in a single plane as it orbits. If we orient our axes so
# that this plane is perpendicular to the z-axis, we can forget about the z coordinate and we
# are left with just two second-order equations to solve:

# The orbit of the Earth is not perfectly circular, the planet being sometimes closer to and
# sometimes further from the Sun. When it is at its closest point, or "perihelion", it is moving
# precisely tangentially (i.e., perpendicular to the line between itself and the Sun) and it has
# distance 1.4710 × 1011 m from the Sun and linear velocity 3.0287 × 104 m s−1 .

# (b) Write a program to calculate the orbit of the Earth using the Verlet method with a time-
# step of h = 1 hour. Choose the perihelion as starting point, which translates to the initial
# conditions x = 1.4710 × 1011 m and y = 0 for the coordinates and vx = 0 and
# vy = 3.0287 × 104 m s−1 for the velocities. Make a plot of the orbit, showing 10 complete
# revolutions around the Sun. The orbit should be very slightly, but visibly, non-circular.

# (c) The gravitational potential energy of the Earth is −GMm/r , where
# m = 5.9722 × 1024 kg is the mass of the planet, and its kinetic energy is 1/2mv2 as usual.
# Modify your program to calculate both of these quantities at each step, along with their sum
# (which is the total energy), and make a plot showing all three as a function of time on the
# same axes. You should find that the potential and kinetic energies vary visibly during the
# course of an orbit, but the total energy remains constant.

# (d) Now plot the total energy alone without the others and you should be able to see a slight
# variation over the course of an orbit. However, Because you're using the Verlet method
# which conserves energy in the long term, the energy should always return to its starting
# value at the end of each complete orbit.

# (e) Calculate the earth orbit with the second-order Runge-Kutta method instead of the Verlet
# algorithm . Plot the total energy and compare it to the total energy from the Verlet algorithm.
# What is the major difference? Which method, second-order Runge-Kutta or Verlet, do you
# find more suitable for the investigated problem?

import numpy as np
import matplotlib.pyplot as plt

def verlet(f,r0,v0,t0,tf,h):
    """ Solves the time evolution of r(t) and v(t)=dr/dt for
        dv/dt = f(r,t) in the range [t0,tf] using Verlet method.
    Args:
        f (function): f(r,t) in dv/dt = f(r,t)
        r0 (numpy float array): initial value r(t0)
        v0 (numpy float array): initial value v(t0)
        t0 (float): start time
        tf (float): stop time
        h (float): time step. The length of the time interval tf-t0 should be a multiple of h.
    Returns
        numpy float array: [r(t0), r(t0+h), ..., r(tf)]
        numpy float array: [v(t0), v(t0+h), ..., v(tf)]"""
    r = None
    v = None
    t=0
    tp=np.arange (t0, tf+h, h)

    r=np.array ([r0[0], r0[1]])
    v=np.array ([v0[0], v0[1]])

    fm=h*f (r, t)/2
    vxm=v[0]+fm[0]
    vym=v[1]+fm[1]
    xp=[]
    yp=[]
    vxl=[]
    vyl=[]

    for i in tp:
        xp.append (r[0])
        yp.append (r[1])

        vxl.append (v[0])
        vyl.append (v[1])

        r[0]+=h*vxm
        r[1]+=h*vym

        k=h*f (r, t)

        v[0]=vxm+k[0]/2
        v[1]=vym+k[1]/2

        fm=h*f (r, t)/2

        vxm+=k[0]
        vym+=k[1]

    v=np.array ([vxl, vyl])
    r=np.array ([xp, yp])

    return r, v


# Global constants
G = 6.6738e-11
M = 1.9891e30
m = 5.9722e24


def f(r,t):
    """ definition of the equation dv/dt = f(r,t)
    Args:
        r (float array): [x,y]
        t (float array): time
    Returns
        numpy float array: [dv_x/dt, dv_y/dt]"""
    ret = None

    x=r[0]
    y=r[1]

    rsq=(x**2+y**2)**0.5
    ret=np.array ([-G*M*x/rsq**3, -G*M*y/rsq**3])

    return ret


t0 = 0.0                 # start time
tf = 3600*24*365.25*10   # end time (s), 10 years
h = 3600.0               # step of 1h

x0 = 1.4710e11 # initial x position (m)
y0 = 0.0       # initial y position (m)
vx0 = 0.0      # initial x velocity (m/s)
vy0 = 3.0287e4 # initial y velocity (m/s)

v0=np.array ([vx0, vy0])
r0=np.array ([x0, y0])

pl=verlet(f,r0,v0,t0,tf,h)
# Solve the orbit using verlet and plot the results

plt.plot (pl[0][0], pl[0][1])
plt.xlabel('x')
plt.ylabel('y')
plt.close ()

def f_test(r,t):
    return np.array([0.0,-9.81])

verlet_test = verlet(f_test, np.array([0.0,0.0]), np.array([10.0,10.0]), 0.0, 2.0, 0.01)
verlet_test_r = verlet_test[0]
verlet_test_v = verlet_test[1]
print ("verlet_test_r", len (verlet_test_r), len (verlet_test_r))
assert len(verlet_test_r) == 201
assert len(verlet_test_v) == 201
print (abs(np.sum(verlet_test_v[-1]**2)**0.5 - 13.8714))
assert abs(np.sum(verlet_test_v[-1]**2)**0.5 - 13.8714) < 1e-2

def V(r):
    """ Potential energy of the Earth
    Args:
        r (float array): [x,y]
    Returns
        float: Potential energy in J"""
    v = 0.0
    v=-G*M*m/(r[0]**2+r[1]**2)**0.5
    return v


def T(v):
    """ Kinetic energy of the Earth
    Args:
        v (float array): [v_x,v_y]
    Returns
        float: Kinetic energy in J"""
    t = 0.0
    t=0.5*m*((v[0]**2+v[1]**2)**0.5)**2

    return t


# Plot the energies
t_plot = np.arange(t0,tf+h,h)
plt.plot (t_plot, V ([pl[0][0], pl[0][1]]), label="Potential")
plt.plot (t_plot, T ([pl[1][0], pl[1][1]]), label="Kinetic")
plt.legend ()
plt.xlabel('Time (s)')
plt.ylabel('Energy (J)')
plt.close ()

# Plot the total energy
plt.plot (t_plot, V ([pl[0][0], pl[0][1]])+T ([pl[1][0], pl[1][1]]), label="Total Energy")
plt.legend ()
plt.xlabel('Time (s)')
plt.ylabel('Energy (J)')
plt.close ()


def rk2(g,r0,t0,tf,h):
    """ Solves the time evolution of r(t) for dr/dt = f(r,t)
        in the range [t0,tf] using the 2nd-order Runge-Kutta method.
    Args:
        f (function): f(r,t) in dr/dt = f(r,t)
        r0 (numpy float array): initial value of r
        t0 (float): start time
        tf (float): stop time
        h (float): time step. The length of the time interval tf-t0 should be a multiple of h.
    Returns
        numpy float array: [r(t0), r(t0+h), ..., r(tf)]"""
    r = None
    tp=np.arange (t0, tf+h, h)
    xp=[]
    for i in tp:
        xp.append (r0)
        k1=h*g (r0, i)
        k2=h*g (r0+0.5*k1, i+0.5*h)
        r0+=k2

    r=np.array(xp)
    return r



def g(r,t):
    """ definition of the four first-order equations
    Args:
        r (numpy float array): array of variables [x, y, v_x, v_y]
        t (float): time
    Returns
        numpy float array: [dx/dt, dy/dt, dv_x/dt, dv_y/dt]"""
    ret = np.empty(4,float)

    x=r[0]
    y=r[1]
    rsq=(x**2+y**2)**0.5
    ret[0]=r[2]
    ret[1]=r[3]
    ret[2]=-G*M*x/rsq**3
    ret[3]=-G*M*y/rsq**3

    return ret

plt.close ()

r0=np.array ([x0, y0, vx0, vy0])
rk22=rk2 (g, r0, t0, tf, h)

print (rk22[0][0], rk22[:, 0][0])
print (rk22[0][-1], rk22[:, -1][0])

r=np.array ([rk22[:, 0], rk22[:, 1]])
v=np.array ([rk22[:, 2], rk22[:, 3]])

plt.plot (t_plot, T ([rk22[:, 2], rk22[:, 3]])+V ([rk22[:, 0], rk22[:, 1]]), label="Total energy, RK2")
plt.legend ()
plt.xlabel('Time (s)')
plt.ylabel('Energy (J)')

# defining equation dx/dt = x + x/t
def f_test(x,t):
    return x + x/t

rk2_test = rk2(f_test,np.array([1.5]),1.0,2.0,0.001)
