# -*- coding: utf-8 -*-

# As a more complex example of the use of the relaxation method, let us consider the solution
# of the Poisson equation of electrostatics

# which governs the electric potential in the presence of a charge density ρ. Here ε0 is the
# permittivity of empty space (and we are assuming that we are in empty space). Let us
# consider this equation in two dimensions, for simplicity, in a square box 1 m along each
# side. All the walls of the box will be at voltage zero, but there will be two square charge in
# the box, one positive, one negative, as depicted below.

# The two charges are each 20 cm on a side and 20 cm from the walls of the box and have
# the charge density ρ = ±1 Cm−2 .
# To solve this problem using the relaxation method we proceed similar as in the example in
# the lecture and rewrite the Poisson equation as

import numpy as np
import matplotlib.pyplot as plt

# Global constants
L = 1.0 # Length of box in meters

def rho_matrix(N):
    """ Constructs the charge density matrix:
        [[rho(0,0)  rho(0,a)  rho(0,2a)  ... rho(0,L) ]
         [rho(a,0)  rho(a,a)  rho(a,2a)  ... rho(a,L) ]
         [rho(2a,0) rho(2a,a) rho(2a,2a) ... rho(2a,L)]
         [                    ...                     ]
         [rho(L,0)  rho(L,a)  rho(L,2a)  ... rho(L,L) ]]
    Args:
        N (float): grid size
    Returns
        numpy float array: NxN charge density matrix"""
    rho = None
    rho=np.zeros ([N+1, N+1])

    # constants
    rho0 = 1.0  # Charge density of charges
    a = L/(N-1) # grid spacing

    val=20

    for i in range (N+1):
        for j in range (N+1):
            if val<i<2*val and 3*val<j<4*val:
                rho[i, j]=rho0
            elif 3*val<i<4*val and val<j<2*val:
                rho[i, j]=-rho0
            else:
                rho[i, j]=0

    return rho


def relax_phi(rho, tolerance):
    """ Solves the potential matrix based on the charge density matrix
        using the relaxation method.
    Args:
        rho (numpy float array): charge density matrix
        tolerance (float): maximum potential change at any grid point
    Returns
        numpy float array: potential matrix of the same shape as rho"""
    phi = None
    phi=np.zeros_like (rho)
    N=rho.shape[0]
    # constants
    e0 = 1.0               # Permittivity
    a = L/(rho.shape[0]-1) # Grid spacing

    delta=3*tolerance#1
    while delta>tolerance:
        delta=0.0
        for i in range (N-1):
            for j in range (N-1):

                if not i==N and not j==N:
                    phi_prev=phi[i, j]
                    phi_next=(phi[i+1, j]+phi[i-1, j]+phi[i, j+1]+phi[i, j-1] \
                                 +a**2/4*rho[i, j])/4
                    phi[i, j]=phi_next

                    if delta>=np.max (abs (phi_next-phi_prev)):
                        delta=delta
                    else:
                        delta=np.max (abs (phi_next-phi_prev))

    return phi



# validation
N = 101 # Number of grid points

rho = rho_matrix(N)

# # plotting the charge density
p = plt.imshow(rho)
cbar = plt.colorbar(p)
cbar.set_label(r"$\rho$ (C/m^2)")
plt.show ()
# Solving the potential
phi = relax_phi(rho,1e-6)

# plotting the potential
plt.figure()
p = plt.imshow(phi)
cbar = plt.colorbar(p)
cbar.set_label(r"$\phi$ (C)")
plt.show ()
