# -*- coding: utf-8 -*-

# A well-known quantum mechanics problem involves a particle of mass m that encounters a
# one-dimensional potential step, like this:

# The particle with initial kinetic energy E and wavevector k1 = √2mE /ħ enters from the
# left and encounters a sudden jump in potential energy of height V at position x = 0 . By
# solving the Schroedinger equation, one can show that when E > V the particle may either
# (a) pass the step, in which case it has a lower kinetic energy of E − V on the other side

# and a correspondingly smaller wavevector of k2 = √2m(E − V ) /ħ, or (b) it may be
# reflected, keeping all of its kinetic energy and an unchanged wavevector but moving in the
# opposite direction. The probabilities T and R for transmission and reflection are given by

# Suppose we have a particle with mass equal to the electron mass m = 9.11 × 10−31 kg
# and energy 10 eV encountering a potential step of height 9 eV. Write a Python program to
# compute and print out the transmission and reflection probabilities using the formulas
# above.


def get_tnr_prob(m, e, v):
    """get transmission and reflection probabilities
    Args:
        m (float): mass of the object in Kg
        e (float): energy of the object in eV
        v (float): height of the potential step in eV

    Retruns:
        float: transmission values
        float: reflection values
    """
    # constants
    hbar = 6.58211956e-16  # eVs
    t, r = 0, 0

    k1=(2*m*e)**0.5/hbar
    k2=(2*m*(e-v))**0.5/hbar

    t=(4*k1*k2)/(k1+k2)**2
    r=((k1-k2)/(k1+k2))**2

    return t, r



# validation
t, r = get_tnr_prob(8e-30, 20, 15)

# ex
m = 9.11e-31  # Kg
e = 10  # eV
v = 9  # eV
t, r = get_tnr_prob(m, e, v)
print("With: M {} Kg, E {} eV, and V {} eV\n"
      "Transmission probability: {}\n"
      "Reflection probability: {}".format(m, e, v, t, r))
