# ======================================================================
# I Was Told There Would Be No Math
#   Advent of Code 2015 Day 02 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                             n o m a t h . p y
# ======================================================================
"A solver for the Advent of Code 2015 Day 02 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import present

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                 NoMath
# ======================================================================


class NoMath(object):   # pylint: disable=R0902, R0205
    "Object for I Was Told There Would Be No Math"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.presents = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            for line in text:
                line = line.strip()
                if not line or len(line) == 0:
                    continue
                self.presents.append(present.Present(text=line))

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 1. Start with nothing
        result = 0

        # 2. Loop for all presents
        for pres in self.presents:

            #  3. Add it the wrapping paper for this present
            result += pres.paper()

        # 4. Return the solution for part one
        return result

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 1. Start with nothing
        result = 0

        # 2. Loop for all presents
        for pres in self.presents:

            #  3. Add it the ribbon for this present
            result += pres.ribbon()

        # 4. Return the solution for part two
        return result


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         n o m a t h . p y                      end
# ======================================================================
