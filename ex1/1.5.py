# -*- coding: utf-8 -*-

# A useful feature of user-defined functions is recursion, the ability of a function to call itself.
# For example, consider the following definition of the factorial n! of a positive integer n:

# This constitutes a complete definition of the factorial which allows us to calculate the value
# of n! for any positive integer. We can employ this definition directly to create a Python
# function for factorials, like this:

# Note how, if n is not equal to 1, the function calls itself to calculate the factorial of n − 1.
# This is recursion. If we now say print(factorial(5)) the computer will correctly print
# the answer 120.
# (a) We encountered the Catalan numbers Cn previously in Exercise 1.3. With just a little
# rearrangement, the definition 

# Write a Python function, using recursion, that calculates Cn . Use your function to calculate
# and print C100 .
# (b) Euclid showed that the greatest common divisor g(m, n) of two nonnegative integers m
# and n satisfies

# Write a Python function g(m,n) that employs recursion to calculate the greatest common
# divisor of m and n using this formula. Use your function to calculate and print the greatest
# common divisor of 108 and 192.
# Comparing the calculation of the Catalan numbers in part (a) above with that of Exercise
# 1.3, we see that it's possible to do the calculation two ways, either directly or using
# recursion. In most cases, if a quantity can be calculated without recursion, then it will be


# faster to do so, and we normally recommend taking this route if possible. There are some
# calculations, however, that are essentially impossible (or at least much more difficult) without
# recursion. We will see some examples later in this book.


def get_catalan_n(n):
    """ gets nth catalan number with recursion
    Args:
        n (int): the index of catalan number needed
    Returns:
        int: nth catalan number
    Raises:
        AssertionError: if n is not integer"""
    cn = 1
    assert isinstance(n, int), "n should be int"

    if n==0:
        return 1
    else:
        return ((4*n-2)/(n+1))*get_catalan_n (n-1)

    raise NotImplementedError()
    return cn


# validation
# catalan numbers
c100 = get_catalan_n(100)
assert get_catalan_n(0) == 1, "bad get_catalan_n func"
assert get_catalan_n(1) == 1, "bad get_catalan_n func"
assert get_catalan_n(2) == 2, "bad get_catalan_n func"
assert get_catalan_n(20) == 6564120420, "bad get_catalan_n func"
print("100th catalan number = {}".format(c100))


def get_gcd(m, n):
    """gets greatest common divisor of two non negative integers
    Args:
        m (int): first integer
        n (int): second integer
    Returns:
        int: greatest common divisor of m and n
    Raises:
        AssertionError: if m or n are not non negative integers"""
    gcd = 0

    # YOUR CODE HERE

    if n==0:
        return m
    else:
        return get_gcd (n, m % n)

    return gcd



# gcd
assert get_gcd(2, 0) == 2, "bad get_gcd func"
assert get_gcd(2, 10) == 2, "bad get_gcd func"
assert get_gcd(12, 16) == 4, "bad get_gcd func"
print("gcd of {} and {} = {}".format(108, 192, get_gcd(108, 192)))
