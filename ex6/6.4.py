# -*- coding: utf-8 -*-

# The Ising model is a theoretical model of a magnet. The magnetization of a magnetic
# material is made up of the combination of many small magnetic dipoles spread throughout
# the material. If these dipoles point in random directions then the overall magnetization of the
# system will be close to zero, but if they line up so that all or most of them point in the same
# direction then the system can acquire a macroscopic magnetic moment---it becomes
# magnetized. The Ising model is a model of this process in which the individual moments are
# represented by dipoles or "spins" arranged on a grid or lattice:

# In this case we are using a square lattice in two dimensions, although the model can be
# defined in principle for any lattice in any number of dimensions.

# The spins themselves, in this simple model, are restricted to point in only two directions, up
# and down. Mathematically the spins are represented by variables si = ±1 on the points of
# the lattice, +1 for up-pointing spins and −1 for down-pointing ones. Dipoles in real magnets
# can typically point in any spatial direction, not just up or down, but the Ising model, with its
# restriction to just the two directions, captures a lot of the important physics while being
# significantly simpler to understand.
# Another important feature of many magnetic materials is that the individual dipoles in the
# material may interact magnetically in such a way that it is energetically favorable for them to
# line up in the same direction. The magnetic potential energy due to the interaction of two
# dipoles is proportional to their dot product, but in the Ising model this simplifies to just the
# product si sj for spins on sites i and j of the lattice, since the spins are one-dimensional
# scalars, not vectors. Then the actual energy of interaction is −Jsi sj , where J is a positive
# interaction constant. The minus sign ensures that the interactions are ferromagnetic,
# meaning the energy is lower when dipoles are lined up. A ferromagnetic interaction implies
# that the material will magnetize if given the chance. (In some materials the interaction has
# the opposite sign so that the dipoles prefer to be antialigned. Such a material is said to be
# antiferromagnetic, but we will not look at the antiferromagnetic case here.)
# Normally it is assumed that spins interact only with those that are immediately adjacent to
# them on the lattice, which gives a total energy for the entire system equal to

# where the notation ⟨ij⟩ indicates a sum over pairs i, j that are adjacent on the lattice. On
# the square lattice we use in this exercise each spin has four adjacent neighbors with which it
# interacts.
# Write a program to perform a Markov chain Monte Carlo simulation of the Ising model on the
# square lattice for a system of 20 × 20 spins. You will need to set up variables to hold the
# value ±1 of the spin on each lattice site, probably using a two-dimensional integer array,
# and then take the following steps.
# (a) First write a function to calculate the total energy of the system, as given by the equation
# above. That is, for a given array of values of the spins, go through every pair of adjacent
# spins and add up the contributions si sj from all of them, then multiply by −J . Hint 1: Each
# unique pair of adjacent spins crops up only once in the sum. Thus there is a term −Js1 s2 if
# spins 1 and 2 are adjacent to one another, but you do not also need a term −Js2 s1 . Hint 2:
# To make your final program to run in a reasonable amount of time, you will find it helpful if
# you can work out a way to calculate the energy using Numpy's ability to do arithmetic with
# entire arrays at once. If you do the calculation step by step, your program will be significantly

# (b) Now use your function as the basis for a Metropolis-style simulation of the Ising model
# with J = 1 and temperature T = 1 in units where the Boltzmann constant kB is also~1.
# Initially set the spin variables randomly to ±1 , so that on average about a half of them are
# up and a half down, giving a total magnetization of roughly zero. Then choose a spin at
# random, flip it, and calculate the new energy after it is flipped, and hence also the change in
# energy as a result of the flip. Then decide whether to accept the flip using the Metropolis
# acceptance formula,

# (c) Now repeat the above process for many moves. Make a plot of the total magnetization
# M = ∑i si of the system as a function of time for a million Monte Carlo steps. You should
# see that the system develops a "spontaneous magnetization," a nonzero value of the overall
# magnetization. Hint: While you are working on your program, do shorter runs, of maybe ten
# thousand steps at a time. Once you have it working properly, do a longer run of a million
# steps to get the final results.

# (d) Run your program several times, in the previous cell itself, and observe the sign of the
# magnetization that develops, positive or negative. Describe what you find and give a brief
# explanation of what is happening.

import numpy as np

def ising_energy(array, J):
    """Calculates ising energy for array
    Args:
        array (nd array): 2D array with representing ising field
        J (float): interaction constant
    Returns:
        float: ising energy"""
    energy = 0  # energy (units)
    n=len (array)
    sumr=np.zeros([1, n], int)
    sumr=np.zeros([1, n])
    for i in range(0, n-1):
        sumr+=-J*array[i, :]*array[i+1, :]

    sumc=np.zeros(n, int)
    sumc=np.zeros(n)
    for i in range(0, n-1):
        sumc+=-J*array[:, i]*array[:, i+1]

    energy=np.sum(sumr[0])+np.sum(sumc)
    return energy



# validate
array = np.array([[ 1,  1, -1,  1],
                  [ 1, -1, -1,  1],
                  [-1,  1,  1, -1],
                  [ 1, -1,  1,  1]])
energy = ising_energy(array, 1)
assert energy == 8, 'bad energy'
# wall time check
import time
# random large ising field
array = np.random.randint(0, 2, (1000, 1000)) * 2 - 1
t0 = time.time()
energy = ising_energy(array, 1)
wall_time = time.time() - t0
print('wall time for 1000x1000 field: {} s'.format(wall_time))
assert wall_time < 5e-2, ('needs further optimising, bring wall time below 0.05 s')

def accept_or_not(deltaE, kbt):
    # spin_flipped=False # makes sure that spin is flipped only once, without it the spin would be reverted back to its original value
    beta=1/kbt
    accept_or_not2=0
    rnd_test_nr=np.random.randint(0, 100)/100
    if deltaE<=0:
        accept_or_not2=1
    else:
        accept_or_no2t=np.exp(-beta*deltaE)

    if rnd_test_nr<accept_or_not2:
        print ("flips")
        return True
    else:
        print ("does not flip")
        no_flip=True
        return False

def flip(array, flip_ind, j=1, kbt=10):
    """flips a spin if accepted using metropolis formula
    Args:
        array (nd array): the ising field
        flip_ind (list): index (as a list [x, y]) to be flipped
        j (float): interaction energy
        kbt (float): k_b * T
    Returns:
        nd array: the ising field with flipped spin, if accepted, or
            the same field otherwise."""

    array_old=array
    array_new=array

    Ei=ising_energy(array_old, j)
    ind1=flip_ind[0]
    ind2=flip_ind[1]
    spin_before=array[ind1, ind2]

    spin_flipped=False # makes sure that spin is flipped only once, without it the spin would be reverted back to its original value
    if array_new[ind1, ind2]==1 and spin_flipped==False:
        array_new[ind1, ind2]=-1
        print ("change 1 to ", array_new[ind1, ind2])
        spin_flipped=True

    if array_new[ind1, ind2]==-1 and spin_flipped==False:
        array_new[ind1, ind2]=1
        print ("change -1 to ", array_new[ind1, ind2])
        spin_flipped=True

    Ej=ising_energy(array_new, j)
    deltaE=Ej-Ei
    no_flip=False

    a=accept_or_not(deltaE, kbt)
    print ("bool on", a)
    if a==True:
        print ("accept new")
        array=array_new
        print (array[ind1, ind2])
        return array

    if a==False:
        print ("reject new, spin before", spin_before)
        array[ind1, ind2]=spin_before # return spin to its original value
        print (array[ind1, ind2])
        return array

    print ("dd")
    return array

# initialise random array with zero magnetisation.
N=100
array=np.empty ([N, N])
spins=[-1, 1]
for i in range (np.shape (array)[0]):
    for j in range (np.shape (array)[1]):
        spin=np.random.randint(0, 2, dtype=int)
        array[i, j]=spins[spin]

# choose an index, [x, y], at random
random_index=np.random.randint(0, N, size=2)
# get flipped array if it is flipped
# validation
array = np.array([[ 1,  1, -1,  1],
                  [ 1, -1, -1,  1],
                  [-1,  1,  1, -1],
                  [ 1, -1,  -1,  1]])
array = flip(array.copy(), [2, 2], j=1, kbt=10)
print ('should flip')
assert array[2, 2] == -1, "should flip"
print ("flips")
print ("########################################")
print ('should not flip')
array = flip(array, [2, 2], j=1, kbt=1e-9)
assert array[2, 2] == -1, "shouldn't flip"
print ('does not flip')
##################################################

def monte_carlo(array, n, j, kbt):
    """perform monte carlo for n steps
    Args:
        array (nd array): initial ising field
        n (int): number of steps
        j (float): interaction energy
        kbt (float): k_b * T
    Returns:
        nd array: array of size n with magnetisation at each step"""
    array = np.array(array)  # making sure its a np array
    if np.any(np.logical_and(array != 1, array != -1)):
        raise ValueError('bad ising array')

    magnetisation = np.zeros(n)
    for ii in range (n):
        ind=np.random.randint(0, np.shape (array)[0], size=2)
        array=flip (array, ind, j, kbt)

    return magnetisation
kbt=1
n=1
monte_carlo(array, n, j, kbt)
