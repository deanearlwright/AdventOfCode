# ======================================================================
# Binary Boarding
#   Advent of Code 2020 Day 05 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         b p a s s . p y
# ======================================================================
"A Boarding Pass for the Advent of Code 2020 Day 05 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                  Bpass
# ======================================================================


class Bpass(object):   # pylint: disable=R0902, R0205
    "Boarding Pass Object for Binary Boarding"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.row = None
        self.column = None
        self.seat = None

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.set_rcs()

    def set_rcs(self):
        "Set the row, column, and seat ID based on the boarding pass"

        # 1. Convert to binary digits
        assert len(self.text) == 10
        digits = self.text.replace('F', '0').replace('B', '1')
        digits = digits.replace('L', '0').replace('R', '1')

        # 2. Calculate the row, column and seat
        self.row = int(digits[0:7], 2)
        self.column = int(digits[7:], 2)
        self.seat = self.row * 8 + self.column

        # 3. A simple check
        # print("text=%s, digits=%s, row=%d, col=%d, seat=%d, int=%d" %
        #        (self.text, digits, self.row, self.column, self.seat, int(digits, 2)))
        assert self.seat == int(digits, 2)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      p h o n e . p y                     end
# ======================================================================
