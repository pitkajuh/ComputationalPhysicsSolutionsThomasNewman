# -*- coding: utf-8 -*-

# Write a program to calculate and print the factorial of a number entered by the user. Write
# your program so that it calculates the factorial using integer variables, not floating-point
# ones. Use your program to calculate the factorial of 200.
# Now modify your program to use floating-point variables instead and again calculate the
# factorial of 200. What do you find? Explain.

def factorial_int(n):
    """factorial of a number with integer variables
    Args:
        n (int): number to calculate factorial of
    Returns:
        int: the factorial of n"""

    if n==1:
        return 1
    else:
        return n*factorial_int(n-1)

    return fact_n

def factorial_float(n):
    """factorial of a number with floating variables
    Args:
        n (float): number to calculate factorial of
    Returns:
        int: the factorial of n"""

    n=float (n)
    if n==1:
        return 1
    else:
        return n*factorial_int(n-1)

    return fact_n

# validation
print("Factorial of {}\nWith int variables: {}\nWith float variables: {}"
      "".format(200, factorial_int(200), factorial_float(200)))
assert factorial_float(4) == 24
assert factorial_int(4) == 24
assert isinstance(factorial_int(0), int)
assert isinstance(factorial_float(0), float)
