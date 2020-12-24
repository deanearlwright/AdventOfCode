# ======================================================================
# Encoding Error
#   Advent of Code 2020 Day 09 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         c y p h e r . p y
# ======================================================================
"A solver for the Advent of Code 2020 Day 09 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
DEFAULT_SIZE = 25
MAX_WIDTH = 1000

# ======================================================================
#                                                                 Cypher
# ======================================================================


class Cypher(object):   # pylint: disable=R0902, R0205
    "Object for Encoding Error"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.numbers = None
        self.previous = None

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.numbers = []
            for line in text:
                self.numbers.append(int(line))

    def preamble(self, limit=DEFAULT_SIZE):
        "Populate the previous numbers"
        self.previous = []
        for _ in range(limit):
            self.previous.append(self.numbers.pop(0))
        assert len(self.previous) == limit

    def get_pair(self, total):
        "Get a pair of numbers that add to the total"
        for num in self.previous:
            num2 = total - num
            if num != num2 and num2 in self.previous:
                return num, num2
        return None, None

    def is_weak(self, number):
        pair = self.get_pair(number)
        # print("is_weak: %d %s %s" % (number, pair[0], pair[1]))
        if pair[0] is None:
            return True
        return False

    def find_first_weakness(self, limit=DEFAULT_SIZE):
        "Find the first weak number"
        self.preamble(limit=limit)
        for number in self.numbers:
            if self.is_weak(number):
                return number
            self.previous.pop(0)
            self.previous.append(number)
            assert len(self.previous) == limit
        return None

    def is_range(self, number, width, start):
        "Return True if the range adds up to the number"
        numbers = self.numbers[start:start + width]
        return number == sum(numbers)

    def min_max_range(self, width, start):
        "Return the min and max of the range"
        numbers = self.numbers[start:start + width]
        return min(numbers), max(numbers)

    def find_weak_range(self, verbose=False, limit=DEFAULT_SIZE):
        "Find the weak range"
        numbers = self.numbers.copy()
        weakness = self.find_first_weakness(limit=limit)
        self.numbers = numbers
        if verbose:
            print("Looking for %d" % weakness)
        for width in range(2, MAX_WIDTH):
            if verbose:
                print("Width = %d" % width)
            for start in range(len(self.numbers) - width):
                if self.is_range(weakness, width, start):
                    if verbose:
                        print("Start = %s, first = %d, last = %d" %
                              (start, self.numbers[start], self.numbers[start + width - 1]))
                    min_max = self.min_max_range(width, start)
                    return sum(min_max)
        return None

    def part_one(self, verbose=False, limit=DEFAULT_SIZE):
        "Returns the solution for part one"

        # 1. Return the solution for part one
        if limit == 0:
            limit = DEFAULT_SIZE
        return self.find_first_weakness(limit=limit)

    def part_two(self, verbose=False, limit=DEFAULT_SIZE):
        "Returns the solution for part two"

        # 1. Return the solution for part two
        if limit == 0:
            limit = DEFAULT_SIZE
        return self.find_weak_range(verbose=verbose, limit=limit)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      c y p h e r . p y                     end
# ======================================================================
