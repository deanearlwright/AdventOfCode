# ======================================================================
# Passport Processing
#   Advent of Code 2020 Day 04 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         s c a n n e r . p y
# ======================================================================
"A solver for the Advent of Code 2020 Day 04 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import passport

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                Scanner
# ======================================================================


class Scanner(object):   # pylint: disable=R0902, R0205
    "Object for Passport Processing"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.passports = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            for line in text:
                self.passports.append(passport.Passport(text=line, part2=part2))

    def count_valid(self):
        "Count the number of valid passports"
        result = 0
        for passport in self.passports:
            if passport.is_valid():
                result += 1
        return result

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 1. Return the solution for part one
        return self.count_valid()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 1. Return the solution for part two
        return self.count_valid()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                       s c a n n e r . p y                      end
# ======================================================================
