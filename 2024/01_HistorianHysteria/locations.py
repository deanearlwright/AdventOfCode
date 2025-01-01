
# ======================================================================
# Historian Hysteria
#   Advent of Code 2024 Day 01 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         l o c a t i o n s . p y
# ======================================================================
"A solver for the Advent of Code 2024 Day 01 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from collections import Counter

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                                utility
# ----------------------------------------------------------------------


def distance(left, right):
    "Compute the distance between the two numbers"
    return abs(left - right)


def simulatity(left, right):
    "Compute the simulatitiy between the two numbers"
    return left * right

# ======================================================================
#                                                              Locations
# ======================================================================


class Locations(object):   # pylint: disable=R0902, R0205
    "Object for Historian Hysteria"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.left = []
        self.right = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        assert text is not None and len(text) > 0

        # 1. Loop for the lines of text
        for line in text:

            # 2. Split the line into left and right
            left, right = line.split()

            # 3. Append to the appropoate list
            self.left.append(int(left))
            self.right.append(int(right))

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Start with nothing
        result = 0

        # 2. Sort the two lists
        left = sorted(self.left)
        right = sorted(self.right)

        # 3. Loop over the numbers in the list
        for lll, rrr in zip(left, right, strict=True):

            # 4. Add the distance to the result
            result += distance(lll, rrr)

        # 5. Return the solution for part one
        return result

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Start with nothing
        result = 0

        # 2. Get counts for the right hand list
        counts = Counter(self.right)

        # 3. Loop for all of the numbers in the left hand list
        for left in self.left:

            # 4. Accumulate the similarity score
            result += simulatity(left, counts[left])

        # 5. Return the solution for part two
        return result

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                     l o c a t i o n s . p y                    end
# ======================================================================
