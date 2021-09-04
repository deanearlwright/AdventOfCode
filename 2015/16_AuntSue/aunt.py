# ======================================================================
# Aunt Sue
#   Advent of Code 2015 Day 16 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         a u n t . p y
# ======================================================================
"Aunt for the Advent of Code 2015 Day 16 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import re

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
RE_AUNT = re.compile("Sue ([0-9]+): ([a-z]+): ([0-9]+), ([a-z]+): ([0-9]+), ([a-z]+): ([0-9]+)")
# ======================================================================
#                                                                   Aunt
# ======================================================================


class Aunt(object):   # pylint: disable=R0902, R0205
    "Object for Aunt Sue"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.number = 0
        self.attributes = {}

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            match = RE_AUNT.match(text)
            if not match:
                print("Unable to parse", text)
            else:
                num, att1, val1, att2, val2, att3, val3 = match.groups()
                self.number = int(num)
                self.attributes[att1] = int(val1)
                self.attributes[att2] = int(val2)
                self.attributes[att3] = int(val3)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                          a u n t . p y                         end
# ======================================================================
