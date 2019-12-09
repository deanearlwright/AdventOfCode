# ======================================================================
# No Matter How You Slice It
#   Advent of Code 2018 Day 03 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                               r o w . p y
# ======================================================================
"Row for No Matter How You Slice It problem of Advent of Code 2018-03"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from collections import Counter
from claim import Claim

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                    Row
# ======================================================================


class Row():
    """Object representing a single row of fabric"""

    def __init__(self, number=0):

        # 1. Set the values
        self.number = number
        self.counts = Counter()

    def add_claim(self, claim):
        "Add claim against this row of fabric"

        # 0. Preconditions
        assert claim is not None
        assert isinstance(claim, Claim)

        # 1. Might not have much to do
        if claim.bottom < self.number or claim.top > self.number:
            return

        # 2. Make claims to squares in this row
        self.counts.update(range(claim.left, claim.right - 1))

    def claimed(self):
        "Return the number of squares claimed in the row"

        return len(self.counts)

    def overlap(self):
        "Return the number of squares with overlapping claims"

        return sum([s for s, n in self.counts.items() if n > 1])


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                          r o w . p y                           end
# ======================================================================
