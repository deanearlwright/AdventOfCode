# ======================================================================
# Let It Snow
#   Advent of Code 2015 Day 25 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         c o d e s . p y
# ======================================================================
"A solver for the Advent of Code 2015 Day 25 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import re
import sys

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
RE_INPUT = re.compile(" row ([0-9]+), column ([0-9]+).")

FIRST_CODE = 20151125
MULTIPLY_BY = 252533
REMAINDER_OF = 33554393

# ======================================================================
#                                                                  Codes
# ======================================================================


class Codes(object):   # pylint: disable=R0902, R0205
    "Object for Let It Snow"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.row = 0
        self.col = 0

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            match = RE_INPUT.search(text[0])
            if match:
                self.row = int(match.group(1))
                self.col = int(match.group(2))
                sys.setrecursionlimit(max(1000, self.row + 10))

    @staticmethod
    def next_code(number):
        "Return the next code in the sequence"
        return (number * MULTIPLY_BY) % REMAINDER_OF

    @staticmethod
    def first_order(row):
        "Return the order of the first column of the row"

        # 1. Base case
        if row <= 1:
            return row

        # 2. Recurse to get the answer
        return row - 1 + Codes.first_order(row - 1)

    @staticmethod
    def order(row, col):
        "Return the order of the specifed row and column"

        # 1. Get the order of the first column
        result = Codes.first_order(row)
        if col < 1:
            return result

        # 2. Initially the offset is the row number plus one
        offset = row + 1

        # 3. Loop until we reach the column
        for _ in range(col - 1):

            # 4. Add in the ever increasing offset
            result += offset
            offset += 1

        # 5. Return the code offset
        return result

    @staticmethod
    def code(row, col):
        "Return the code at the specifed row and column"

        # 1. Get the order of the specified row and column
        order_rc = Codes.order(row, col)

        # 2. Start with the initial code
        result = FIRST_CODE

        # 3. Loop generating codes
        for _ in range(order_rc - 1):

            # 4, Generate the next code
            result = Codes.next_code(result)

        # 5. Return the final code generated
        return result

    def my_code(self):
        "Return the code for the row and column"

        # 1. Get the order of the
        return Codes.code(self.row, self.col)

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.my_code()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return None


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         c o d e s . p y                        end
# ======================================================================
