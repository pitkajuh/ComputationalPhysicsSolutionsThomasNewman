# -*- coding: utf-8 -*-

# Modify your program from exercise 3.1 and introduce pivoting to solve the following equation

# and show that it can find the solution, even though Gaussian elimination without pivoting
# fails.

import numpy as np
def gaussian_elimination_pivoting(A,v):
    """ Gaussian elinmation with pivoting
    Args:
        A (2d numpy float array): NxN matrix
        v (1d numpy float array): length N vector
    Returns
        1d numpy float array: solution x to the secular equation  A*x=v"""
    x = None
    N=len (v)
    for m in range(N):
        for i in range(m+1,N):
            if A[m,m]<A[i,m]:
                A[[m,i],:]=A[[i,m],:]
                v[[m,i]]=v[[i,m]]

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



# validation
A_test = np.array([[0,3],[1,-1]],float)
v_test = np.array([2,1],float)
x_test = gaussian_elimination_pivoting(np.copy(A_test),np.copy(v_test))
print(x_test)
assert(abs(x_test[0]-5/3) < 1e-5)
assert(abs(x_test[1]-2/3) < 1e-5)

# solving the equation
A = np.array([[  0,  1,  4,  1 ],
              [  3,  4, -1, -1 ],
              [  1, -4,  1,  5 ],
              [  2, -2,  1,  3 ]], float)
v = np.array([-4, 3, 9, 7],float)
solution = gaussian_elimination_pivoting(A,v)

# printing
print("w = {}".format(solution[0]))
print("x = {}".format(solution[1]))
print("y = {}".format(solution[2]))
print("z = {}".format(solution[3]))
