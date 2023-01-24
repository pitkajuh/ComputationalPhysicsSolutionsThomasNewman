# -*- coding: utf-8 -*-

# LU decomposition with partial pivoting is the most widely used method for the solution of
# simultaneous equations in practice. Write your own program to solve simultaneous
# equations using LU decomposition.
# (a) Write a Python function that calculates the LU decomposition of a matrix. The calculation
# is the same as that for Gaussian elimination, except that at each step of the calculation you
# need to extract the appropriate elements of the matrix and assemble them to form the lower
# diagonal matrix L. Test your function by calculating the LU decomposition of the following
# matrix

# Write a function that performs a double backsubstitution as described in the lecture and
# use it in function solve_LU(A,v) 

# Solve the same equation using the function solve from the numpy package ( linalg
# module) and verify that you get the same answer either way.

# (c) Include partial pivoting in the LU decomposition. Partial pivoting works in the same way
# for LU decomposition as it does for Gaussian elimination, swapping rows to get the largest
# diagonal element as in Exercise 3.2, but the extension to LU decomposition requires two
# additional steps. First, every time you swap two rows you also have to swap the same rows
# in the matrix L . Second, when you use your LU decomposition to solve a set of equations
# Ax = v you will also need to perform the same sequence of swaps on the vector v on the
# right-hand side. This means you need to record the swaps as you are doing the
# decomposition so that you can recreate them later. The simplest way to do this is to set up a
# list or array in which the value of the ith element records the row you swapped with on the
# ith step of the process. For instance, if you swapped the first row with the second then the
# second with the fourth, the first two elements of the list would be 2 and 4. Solving a set of
# equations for given v involves first performing the required sequence of swaps on the
# elements of v then performing a double backsubstitution as usual.
# Write function LUP(A) to perform LU decomposition with partial pivoting. The function
# should return the matrices L and U for the LU decomposition of the swapped matrix, plus a
# list of the swaps made. Then write function solve_LUP(A,v) for solving equations of the
# form Ax = v using LU decomposition with pivoting. Test your program on the example from
# Exercise 3.2, which cannot be solved without pivoting because of the zero in the first
# element of the matrix. Check your results against a solution of the same equations using the
# solve function from numpy .

import numpy as np
def LU(A):
    """ Performs LU decomposition of matrix A.
        Resulting matrices L and U satisfy L[i,j>i] = U[i,j<i] = 0 and L*U = A.
    Args:
        A (2d numpy float array): square matrix
    Returns
        2d numpy float array: matrix L
        2d numpy float array: matrix U"""
    L = None
    U = None
    N=len (A)

    print (np.shape (A))

    L=np.zeros([N, N], float)
    U=np.zeros([N, N], float)

    for j in range(N):
        L[j, j]=1
        for i in range(j+1):
            sum1=0
            for k in range (i):
                sum1+=L[i, k]*U[k, j]
            U[i, j]=A[i, j]-sum1
        for i in range(j, N):
            sum2=0
            for k in range (i):
                sum2+=L[i, k]*U[k, j]
            L[i, j]=A[i, j]-sum2
            L[i, j]/=U[j, j]

    return L,U



# validation
A = np.array([[  2,  1,   4,   1 ],
              [  3,  4,  -1,  -1 ],
              [  1, -4,   1,   5 ],
              [  2, -2,   1,   3 ]], float)
L,U = LU(np.copy(A))
LxU = L @ U
print('A =', np.array2string(A, prefix='A = '),end="\n\n")
print('L =', np.array2string(L, prefix='L = '),end="\n\n")
print('U =', np.array2string(U, prefix='U = '),end="\n\n")
print('LU =', np.array2string(LxU, prefix='LU = '))
