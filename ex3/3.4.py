# -*- coding: utf-8 -*-

# In this exercise you will write a program to calculate the eigenvalues and eigenvectors of a
# real symmetric matrix using the QR algorithm. The first challenge is to write a program that
# finds the QR decomposition of a matrix. Then you will use that decomposition to find the
# eigenvalues.

# As described above, the QR decomposition expresses a real square matrix A in the form
# A = QR , where Q is an orthogonal matrix and R is an upper-triangular matrix. Given an
# N × N matrix A we can compute the QR decomposition as follows.

# (b) Write a Python function that takes as its argument a real square matrix A and returns
# the two matrices Q and R that form its QR decomposition. As a test case, try out your
# function on the matrix below and check the results by multiplying Q and R together to
# recover the original matrix A again.

# (c) Using QR() , write a function for calculating the eigenvalues and eigenvectors of a real
# symmetric matrix. Continue the calculation until the magnitude of every off-diagonal element
# of the matrix is smaller than 10−6 . When your are done the diagonal elements of A contain
# the eigenvalues and the columns of V contain the eigenvectors. Test your program on the
# example matrix above. You should find that the eigenvalues are 1, 21 , −3, and −8 .

import numpy as np

def QR(A):
    """ Performs QR decomposition of matrix A.
    Args:
        A (2d numpy float array): square matrix
    Returns
        2d numpy float array: matrix Q
        2d numpy float array: matrix R"""
    Q = None
    R = None
    N=len (A)
    Q=np.zeros((N, N))
    R=np.zeros((N, N))

    for x in range (0, N, 1):
        append=0
        ai=A[:,x]
        ui=np.copy(ai)
        if x==0:
            R[0, 0]=np.linalg.norm(ui)
        for j in range(0, x, 1):
            qi=Q[:, j]
            dot=qi.dot(A[:, x])
            R[j, x]=dot
            append=dot*qi
            ui-=append
            if j==x-1:
                R[j+1, j+1]=np.linalg.norm(ui)
        qi=ui/np.linalg.norm(ui)
        Q[:, x]=qi

    return Q,R


# validation
A = np.array([[  1,  4,   8,   4 ],
              [  4,  2,   3,   7 ],
              [  8,  3,   6,   9 ],
              [  4,  7,   9,   2 ]], float)
Q,R = QR(A)
QxR = Q @ R

print('A =', np.array2string(A, prefix='A = '),end="\n\n")
print('Q =', np.array2string(Q, prefix='Q = '),end="\n\n")
print('R =', np.array2string(R, prefix='R = '),end="\n\n")
print('QR =', np.array2string(QxR, prefix='QR = '))


def eigen(A):
    """ Finds eigenvalues and eigenvectors of matrix A using QR decomposition.
    Args:
        A (2d numpy float array): square matrix
    Returns
        1D numpy float array: eigenvalues
        2D numpy float array: eigenvectors (matrix V)"""
    eigenvalues = None
    V = None
    N=len (A)
    error=10e-6
    V=np.identity(N)

    threshold=False

    while (threshold==False):

        Q=QR (A)[0]
        R=QR (A)[1]
        A=R.dot(Q)
        V=V.dot(Q)

        for i in range(0, N):
            for j in range(0, N):
                if i!=j:
                    if A[i, j]>error:
                        break
            else:
                threshold=True
                continue
            break

    return A, V


# validation
A = np.array([[  1,  4,   8,   4 ],
              [  4,  2,   3,   7 ],
              [  8,  3,   6,   9 ],
              [  4,  7,   9,   2 ]], float)

eigenvalues, eigenvectors = eigen(np.copy(A))

print("Eigenvalues of A are: ",eigenvalues)
