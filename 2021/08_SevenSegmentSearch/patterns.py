# ======================================================================
# Seven Segment Search
#   Advent of Code 2021 Day 08 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         p a t t e r n s . p y
# ======================================================================
"A solver for the Advent of Code 2021 Day 08 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import pattern

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                               Patterns
# ======================================================================


class Patterns(object):   # pylint: disable=R0902, R0205
    "Object for Seven Segment Search"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.patterns = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            for line in text:
                self.patterns.append(pattern.Pattern(text=line, part2=part2))

    def one_four_seven_eight(self):
        "Return the number of those values"

        # 1. Start with nothing
        result = 0

        # 2. Loop for the values
        for ptrn in self.patterns:

            # 3. Increment the result by the number of desired digits
            result += ptrn.one_four_seven_eight()

        # 4. Return the count of the desired digits
        return result

    def total_values(self):
        "Return the number of those values"

        # 1. Start with nothing
        result = 0

        # 2. Loop for the values
        for ptrn in self.patterns:

            # 3. Increment the result by the pattern's value
            result += ptrn.value()

        # 4. Return the sum of the values
        return result

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.one_four_seven_eight()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.total_values()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      p a t t e r n s . p y                     end
# ======================================================================
