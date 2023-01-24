# -*- coding: utf-8 -*-

# The Catalan numbers Cn are a sequence of integers 1, 1, 2, 5, 14, 42, 132 ... that play an
# important role in quantum mechanics and the theory of disordered systems. (They were
# central to Eugene Wigner's proof of the so-called semicircle law.) They are given by

# Write a program that prints in increasing order all Catalan numbers less than or equal to one
# billion.


def get_catalan_nos():
    """ gets catalan numbers upto 1 billion
    Returns:
        list: list of catalan numbers upto 1 billion"""
    cat_nos = []

    n=0
    C_n=1
    cat_nos.append (C_n)
    while C_n<=1e7:
        C_n=((4*n+2)/(n+2))*C_n
        cat_nos.append (C_n)
        n+=1

    return cat_nos



# validation
cat_nos = get_catalan_nos()
assert cat_nos[0] == 1
assert cat_nos[1] == 1
assert cat_nos[2] == 2
assert cat_nos[3] == 5
assert cat_nos[-1] <= 1e9
