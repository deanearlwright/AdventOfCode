
# ======================================================================
# Wait For It
#   Advent of Code 2023 Day 06 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         r a c e . p y
# ======================================================================
"Race for the Advent of Code 2023 Day 06 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from boat import Boat

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                   Race
# ======================================================================


class Race(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Wait For It"

    def __init__(self, num=0, time=0, distance=0, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.num = num
        self.time = time
        self.distance = distance

    def number_of_ways(self):
        "Return the number of ways to win the race"

        # 1. Create a boat
        my_boat = Boat(part2=self.part2)

        # 2. Return the number of ways to win
        return my_boat.number_of_ways(time=self.time, distance=self.distance)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------

if __name__ == '__main__':
    pass

# ======================================================================
# end                          r a c e . p y                         end
# ======================================================================
