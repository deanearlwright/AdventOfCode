# ======================================================================
# Toboggan Trajectory
#   Advent of Code 2020 Day 03 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                           t r e e s . p y
# ======================================================================
"An arboreal matrix for the Advent of Code 2020 Day 03 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
TREE = '#'
SPACE = '.'

# ======================================================================
#                                                                    Map
# ======================================================================


class Trees(object):   # pylint: disable=R0902, R0205
    "Tree locations Object for Toboggan Trajectory"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.trees = None
        self.rows = 0
        self.cols = 0

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.trees = text
            self.rows = len(text)
            self.cols = len(text[0])
            assert self.cols == len(text[-1])

    def is_tree(self, loc):
        "Returns True if there is a tree at that location"
        col, row = loc
        if row >= self.rows:
            return False
        col = col % self.cols
        if self.trees[row][col] == TREE:
            return True
        return False

    def is_last(self, loc):
        "Returns True if location is on the last row (or lower)"
        if loc[1] >= self.rows - 1:
            return True
        return False


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         t r e e s . p y                        end
# ======================================================================
