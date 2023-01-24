# -*- coding: utf-8 -*-

# One of the most famous examples of the phenomenon of chaos is the logistic map, defined
# by the equation
# x′ = rx(1 − x).
# For a given value of the constant r you take a value of x --- say x = 1
#  2 --- and you feed it

#  into the right-hand side of this equation, which gives you a value of x′ . Then you take that
# value and feed it back in on the right-hand side again, which gives you another value, and
# so forth. This is a iterative map. You keep doing the same operation over and over on your
# value of x, and one of three things happens:
# 1. The value settles down to a fixed number and stays there. This is called a fixed point.
# For instance, x = 0 is always a fixed point of the logistic map. (You put x = 0 on the
# right-hand side and you get x′ = 0 on the left.)
# 2. It doesn't settle down to a single value, but it settles down into a periodic pattern,
# rotating around a set of values, such as say four values, repeating them in sequence
# over and over. This is called a limit cycle.
# 3. It goes crazy. It generates a seemingly random sequence of numbers that appear to
# have no rhyme or reason to them at all. This is deterministic chaos. "Chaos" because it
# really does look chaotic, and "deterministic" because even though the values look
# random, they're not. They're clearly entirely predictable, because they are given to you
# by one simple equation. The behavior is determined, although it may not look like it.
# Write a program that calculates and displays the behavior of the logistic map. Here's what
# you need to do. For a given value of r , start with x = 1
#  2 , and iterate the logistic map
# equation a thousand times. That will give it a chance to settle down to a fixed point or limit
# cycle if it's going to. Then run for another thousand iterations and plot the points (r, x) on a
# graph where the horizontal axis is r and the vertical axis is x. You can either use the plot
# function with the options "ko" or "k." to draw a graph with dots, one for each point,
# you can use the scatter function to draw a scatter plot (which always uses dots). Repeat
# the whole calculation for values of r from 1 to 4 in steps of 0.01, plotting the dots for all
# values of r on the same figure and then finally using the function show once to display the
# complete figure.
# Your program should generate a distinctive plot that looks like a tree bent over onto its side.
# This famous picture is called the Feigenbaum plot, after its discoverer Mitchell Feigenbaum,
# or sometimes the figtree plot, a play on the fact that it looks like a tree and Feigenbaum
# means "figtree" in German.


def logistic_map(r, x_init, n_settle, n_prod):
    """returns a list of values generated through the logistic map
    x' = r * x * (1 - x)
    Args:
    r (float): r value
    x_init (float): initial x value
    n_settle (int): number of values to make the map settle
    n_prod (int): number of values to include in the final map
    Returns:
    list: list of values generated through the logistic map"""
    map_values = []

    for i in range (n_settle):
        x_init=r*x_init*(1-x_init)
        map_values.append(x_init)

    return map_values

# validation
import numpy as np
l_map = logistic_map(2, 0.5, 1000, 1000)
assert np.all([abs(x - 0.5) < 1e-4 for x in l_map]) == True, "bad function"
assert len(l_map) == 1000, "len mismatch"

# plotting
from matplotlib import pyplot as plt
r = [x / 20 for x in range(20, 101)]  # 1, 1.05, 1.10, 1.15 ... 5

ab=[]
for i in range (len (r)):
    ab.append(logistic_map(r[i], 0.5, len (r), len (r)))

plt.plot (r, ab, color="r", label="a", )

plt.xlabel('r')
plt.ylabel('x')
plt.ylim ([0, 1])
plt.xlim ([1, 4])
plt.savefig ("1.6.jpg")
