# -*- coding: utf-8 -*-

# Consider the following circuit of resistors:

# All the resistors have the same resistance R. The power rail at the top is at voltage
# V+ = 5 V. What are the other four voltages, V1 to V4 ?
# To answer this question we use Ohm's law and the Kirchhoff current law, which says that the
# total net current flow out of (or into) any junction in a circuit must be zero. Thus for the
# junction at voltage V1 , for instance, we have

# (b) Write function gaussian_elimination(A,v) that solves equations of the form
# Ax = v for x using Gaussian elimination. Then write the system of equations for the
# voltages in matrix form and apply Gaussian elimination to find the voltage values.

import numpy as np
def gaussian_elimination(A,v):
    """ Gaussian elimination with backsubstitution
    Args:
        A (2d numpy float array): NxN matrix
        v (1d numpy float array): length N vector
    Returns
        1d numpy float array: solution x to the secular equation  A*x=v"""
    x = None
    N=len (v)
    for m in range(N):

        div=A[m,m]
        A[m,:]/=div
        v[m]/=div

        for i in range(m+1,N):
            mult=A[i,m]
            A[i,:]-=mult*A[m,:]
            v[i]-=mult*v[m]

    x=np.empty(N,float)
    for m in range(N-1,-1,-1):
        x[m]=v[m]
        for i in range(m+1,N):
            x[m]-=A[m,i]*x[i]

    return x

def solve_voltages():
    """ Solves the voltages of the circuit
    Returns
        1d numpy float array: the 4 voltages as an array [V_1, V_2, V_3, V_4]"""
    voltages = None
    A=np.array([[4, -1, -1, -1], [-1, 3, 0, -1 ], [-1, 0, 3, -1 ],[-1, -1, 0, 4]], float)
    v=np.array([5, 0, 5, 0],float)
    voltages=gaussian_elimination (A, v)

    return voltages

# validation
A = np.array([[1,1],[1,-1]],float)
v = np.array([2,0],float)
x = gaussian_elimination(A,v)
assert(abs(x[0]-1.0) < 1e-5)
assert(abs(x[1]-1.0) < 1e-5)

# Solving the voltages
voltages = solve_voltages()
print('V_1 = {} V'.format(voltages[0]))
print('V_2 = {} V'.format(voltages[1]))
print('V_3 = {} V'.format(voltages[2]))
print('V_4 = {} V'.format(voltages[3]))
