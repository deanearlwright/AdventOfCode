# ======================================================================
# Toboggan Trajectory
#   Advent of Code 2020 Day 03 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         t o b o g g a n . p y
# ======================================================================
"A solver for the Advent of Code 2020 Day 03 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import math
import trees

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
SLOPES = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]

# ======================================================================
#                                                               Toboggan
# ======================================================================


class Toboggan(object):   # pylint: disable=R0902, R0205
    "Object for Toboggan Trajectory"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.loc = (0, 0)
        self.delta = (3, 1)
        self.trees = None

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.trees = trees.Trees(text=text, part2=part2)

    def move(self):
        "Move the toboggan"
        new_loc = (self.loc[0] + self.delta[0], self.loc[1] + self.delta[1])
        self.loc = new_loc

    def impacts(self):
        "Count the number of trees we hit"

        result = 0
        while self.trees.is_last(self.loc) == False:
            result += self.trees.is_tree(self.loc)
            self.move()
        result += self.trees.is_tree(self.loc)
        return result

    def slopes(self):
        "Return product of tree encountered for various slopes"
        result = []
        for slope in SLOPES:
            self.loc = (0, 0)
            self.delta = slope
            result.append(self.impacts())
        return math.prod(result)

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 1. Return the solution for part one
        return self.impacts()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 1. Return the solution for part two
        return self.slopes()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      t o b o g g a n . p y                     end
# ======================================================================
