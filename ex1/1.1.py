# -*- coding: utf-8 -*-

# A ball is dropped from a tower of height h with initial velocity zero. Write a program that asks
# the user to enter the height in meters of the tower and then calculates and prints the time
# the ball takes until it hits the ground, ignoring air resistance. Use your program to calculate
# the time for a ball dropped from a 100 m high tower.


def time_from_h(s):
    """calculates time taken for a mass dropped from height
    s to hit the ground
    Args:
        s (float): height in meters
    Returns:
        float: time to reach the ground"""
    # constants
    a = 9.8  # acceleration due to gravity (m/s^2)
    t = 0  # time (s)
    h=input ("Enter height: ") # asks to input height
    h=float (h) # changes input from string to float

    t=(2*h/a)**0.5 # calculates the time

    return t



# validation
assert time_from_h(0) == 0.0
assert abs(time_from_h(10) - 1.4285714) < 1e-4
print("Time for a ball dropped from 100m high tower: {} s"
      "".format(time_from_h(100)))
