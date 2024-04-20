
# ======================================================================
# Clumsy Crucible
#   Advent of Code 2023 Day 17 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         b l o c k s . p y
# ======================================================================
"Blocks for the Advent of Code 2023 Day 17 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                 Blocks
# ======================================================================


class Blocks(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Clumsy Crucible"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.rows = 0
        self.cols = 0

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.rows = len(self.text)
            self.cols = len(self.text[0])
            assert self.cols == len(self.text[-1])

    def heat_loss(self, loc):
        "Return the heat loss at the designated location"

        # 0. Precondition axioms
        assert self.text is not None and len(self.text) > 0
        assert 0 <= loc[0] < self.rows
        assert 0 <= loc[1] < self.cols

        # 1. Return the heat loss for the block as an integer
        return int(self.text[loc[0]][loc[1]])

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                        b l o c k s . p y                       end
# ======================================================================
