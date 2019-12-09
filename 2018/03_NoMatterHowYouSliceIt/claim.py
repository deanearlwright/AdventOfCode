# ======================================================================
# No Matter How You Slice It
#   Advent of Code 2018 Day 03 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                             c l a i m . p y
# ======================================================================
"Claim for No Matter How You Slice It problem of Advent of Code 2018-03"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import re

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
PARSE = re.compile(r'^#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)$')

# ======================================================================
#                                                                  Claim
# ======================================================================


class Claim():
    """Object representing a single fabric claim"""

    def __init__(self,                          # pylint: disable=R0913
                 number=0,
                 left=0,
                 top=0,
                 width=1,
                 height=1,
                 text=None):

        # 1. Set the values
        self.number = number
        self.left = left
        self.top = top
        self.width = width
        self.height = height

        # 2. If there is text, decode and save those values
        if text:
            parse = PARSE.match(text)
            self.number = int(parse.group(1))
            self.left = int(parse.group(2))
            self.top = int(parse.group(3))
            self.width = int(parse.group(4))
            self.height = int(parse.group(5))

        # 3. Compute bottom and right
        self.right = self.left + self.width
        if self.width:
            self.right -= 1
        self.bottom = self.top + self.height
        if self.height:
            self.bottom -= 1

    def does_overlap(self, other):
        "Does this claim overlap with the other claim?"

        # 0. Preconditions
        assert other is not None
        assert isinstance(other, Claim)

        # 1. Check column displacements
        if self.right < other.left or self.left > other.right:
            # print("not column %s %d | %s %d" % (str(self), self.right, str(other), other.right))
            return False

        # 2. Check row displacement
        if self.bottom < other.top or self.top > other.bottom:
            # print("not row %s %d | %s %d" % (str(self), self.bottom, str(other), other.bottom))
            return False

        # 3. We do indeed overlap
        return True

    def __str__(self):
        return "#%d @ %d,%d: %dx%d" % (self.number,
                                       self.left,
                                       self.top,
                                       self.width,
                                       self.height)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                        c l a i m . p y                         end
# ======================================================================
