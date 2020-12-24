# ======================================================================
# Rain Risk
#   Advent of Code 2020 Day 12 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         n a v i g a t i o n . p y
# ======================================================================
"A solver for the Advent of Code 2020 Day 12 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import ferry

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                             Navigation
# ======================================================================


class Navigation(object):   # pylint: disable=R0902, R0205
    "Object for Rain Risk"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.ferry = ferry.Ferry(part2=part2)

    def execute(self):
        "Execute a series of instruction and return distance"
        for instruction in self.text:
            self.ferry.execute(instruction)
        return self.ferry.manhattan()

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 1. Return the solution for part one
        return self.execute()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 1. Return the solution for part two
        return self.execute()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    n a v i g a t i o n . p y                   end
# ======================================================================
