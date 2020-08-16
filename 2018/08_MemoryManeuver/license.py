# ======================================================================
# Memory Maneuver
#   Advent of Code 2018 Day 08 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         l i c e n s e . p y
# ======================================================================
"A solver for the Advent of Code 2018 Day 08 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import node
# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                License
# ======================================================================


class License(object):   # pylint: disable=R0902, R0205
    "Object for Memory Maneuver"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.head = None

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            numbers = list(map(int, text[0].split(' ')))
            self.head = node.from_numbers(numbers)

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 1. Return the solution for part one
        if self.head is None:
            return None
        return self.head.add_metadata_entries()


    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 1. Return the solution for part two
        if self.head is None:
            return None
        return self.head.value

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                        l i c e n s e . p y                     end
# ======================================================================
