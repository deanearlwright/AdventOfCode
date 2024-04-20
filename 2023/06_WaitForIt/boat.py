
# ======================================================================
# Wait For It
#   Advent of Code 2023 Day 06 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         b o a t . p y
# ======================================================================
"Boat for the Advent of Code 2023 Day 06 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import math

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                   Boat
# ======================================================================


class Boat(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Wait For It"

    def __init__(self, part2=False):

        # 1. Set the initial values
        self.part2 = part2

    def race(self, hold=0, time=0):
        "Run a race, returns distance traveled"

        return (time - hold) * hold

    def min_hold(self, time=0, distance=0):
        "Return the minimum time needed to hold the button to win"

        # 1. Discriminant from quadratic equation
        discriminant = math.sqrt(time * time - 4 * distance)

        # 2. Determine the minimum hold time
        min_hold = (time - discriminant) / 2.0
        min_ceil = math.ceil(min_hold)

        # 3, Return the minimum hold time
        if min_hold == min_ceil:
            return 1 + min_ceil
        return min_ceil

    def max_hold(self, time=0, distance=0):
        "Return the maximum time you can hold the button and win"

        # 1. Discriminant from quadratic equation
        discriminant = math.sqrt(time * time - 4 * distance)

        # 2. Determin the maximum hold time
        max_hold = (time + discriminant) / 2.0
        max_floor = math.floor(max_hold)

        # 3. Return the maximum hold
        if max_hold == max_floor:
            return max_floor - 1
        return max_floor

    def number_of_ways(self, time=0, distance=0):
        "Return the number of milliseconds you hold the button and win"

        return (1 + self.max_hold(time=time, distance=distance) -
                self.min_hold(time=time, distance=distance))

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                      b o a t . p y                     end
# ======================================================================
