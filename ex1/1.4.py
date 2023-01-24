# -*- coding: utf-8 -*-

# In condensed matter physics the Madelung constant gives the total electric potential felt by
# an atom in a solid. It depends on the charges on the other atoms nearby and their locations.
# Consider for instance solid sodium chloride---table salt. The sodium chloride crystal has
# atoms arranged on a cubic lattice, but with alternating sodium and chlorine atoms, the
# sodium ones having a single positive charge +e and the chlorine ones a single negative
# charge −e , where e is the charge on the electron. If we label each position on the lattice by
# three integer coordinates (i, j, k) , then the sodium atoms fall at positions where i + j + k is
# even, and the chlorine atoms at positions where i + j + k is odd.
# Consider a sodium atom at the origin, i = j = k = 0, and let us calculate the Madelung
# constant. If the spacing of atoms on the lattice is a, then the distance from the origin to the
# atom at position (i, j, k) is

# and the potential at the origin created by such an atom is

# with ε0 being the permittivity of the vacuum and the sign of the expression depending on
# whether i + j + k is even or odd. The total potential felt by the sodium atom is then the
# sum of this quantity over all other atoms. Let us assume a cubic box around the sodium at
# the origin, with L atoms in all directions. Then

# where M is the Madelung constant, at least approximately---technically the Madelung
# constant is the value of M when L → ∞, but one can get a good approximation just by
# using a large value of L .
# Write a program to calculate and print the Madelung constant for sodium chloride. Use as
# large a value of L as you can, while still having your program run in reasonable time---say
# in a minute or less.


def get_madelung_constant(L):
    """gets madelung constant
    Args:
        L (int): number of atoms in all directions
    Returns:
        float: madelungs constant"""
    M = 0

    i=-L
    j=-L
    k=-L

    val1=False
    val2=False
    val3=False
    tot=0
    tot2=0
    while tot<=(2*L)**3:
        if tot==(2*L)**tot3:

        if i==0 and j==0 and k==0:
            continue
        elif abs (i+j+k) % 2==0: 
            M+=(i**2+j**2+k**2)**(-0.5)
        else:
            M-=(i**2+j**2+k**2)**(-0.5)

    return M


# validation
import time
t = time.time()
M = get_madelung_constant(200)
print("Run time: {} s\n"
      "Madelung constant: {}".format(time.time() - t, M))
assert abs(M + 1.747565) < 1e-2, "wrong value"
