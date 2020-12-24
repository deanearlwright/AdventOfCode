# ======================================================================
# Report Repair
#   Advent of Code 2020 Day 01 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         r e p o r t . p y
# ======================================================================
"A solver for the Advent of Code 2020 Day 01 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                 Report
# ======================================================================


class Report(object):   # pylint: disable=R0902, R0205
    "Object for Report Repair"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.numbers = set()

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            for number in text:
                self.numbers.add(int(number))

    def get_pair(self, total):
        "Get a pair of numbers that add to the total"
        for num in self.numbers:
            if (total - num) in self.numbers:
                return num, total - num
        return None, None

    def get_trio(self, total):
        "Get a trio of numbers that add to the total"
        for num in self.numbers:
            pair = self.get_pair(total - num)
            if pair[0] is not None:
                return [num, pair[0], pair[1]]
        return None, None, None

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 1. Return the solution for part one
        numbers = self.get_pair(2020)
        return numbers[0] * numbers[1]

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 1. Return the solution for part two
        numbers = self.get_trio(2020)
        return numbers[0] * numbers[1] * numbers[2]


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         r e p o r t . p y                      end
# ======================================================================
