# ======================================================================
# Timing is Everything
#   Advent of Code 2016 Day 15 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
#  based on
#   https://fangya.medium.com/chinese-remainder-theorem-with-python-a483de81fbb8
#   https://rosettacode.org/wiki/Chinese_remainder_theorem
# ======================================================================

# ======================================================================
#                            c r t . p y
# ======================================================================
"Chineese Remainder Theorem for the Advent of Code 2016 Day 15 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from functools import reduce

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                    CRT
# ======================================================================


def chinese_remainder(n, a):
    "Return the solution to a Chinese Remainder Theorem problem"
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    "Multiplicative Inverse"
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                           c r t . p y                          end
# ======================================================================
