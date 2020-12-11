# ======================================================================
# Adapter Array
#   Advent of Code 2020 Day 10 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         j o l t s . p y
# ======================================================================
"A solver for the Advent of Code 2020 Day 10 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from collections import Counter
from collections import defaultdict

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                  Jolts
# ======================================================================


class Jolts(object):   # pylint: disable=R0902, R0205
    "Object for Adapter Array"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.adapters = []
        self.ordered = []
        self.start = 0
        self.device = None

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            for line in text:
                self.adapters.append(int(line))
            self.device = 3 + max(self.adapters)
            self.ordered = self.adapters.copy()
            self.ordered.sort()

    def get_differences(self):
        "Get adapter volt differences"

        # 1. Start with no counts and jolts at zero
        result = Counter()
        jolts = self.start

        # 2. Loop through the adaptors in sorted order
        for adapter in self.ordered:

            # 3. Determine the adapter difference and record it
            diff = adapter - jolts
            result[diff] += 1
            # print('jolts = %d, adapter=%d, diff=%d' % (jolts, adapter, diff))

            # 4. Now at the level of the adapter
            jolts = adapter

        # 5. Remember that the device is also an adaptor
        diff = self.device - jolts
        result[diff] += 1

        # 6. Return all of the jolt differences
        # print(result)
        return result

    def get_part_one_differences(self):
        "Return the number for part one"
        differences = self.get_differences()
        return differences[1] * differences[3]

    def how_many_ways(self):
        "Compute the number of ways to get to each possible value"

        # 1. Start with one way to get to zero
        ways = defaultdict(int)
        ways[self.start] = 1

        # 2. Loop through the adaptors in sorted order
        for adaptor in self.ordered:

            # 3. The number of ways to get to an adaptor value is the number of ways
            #    to get to the three values below it (some might loop around to zero value)
            ways[adaptor] = ways[adaptor - 1] + ways[adaptor - 2] + ways[adaptor - 3]

        # 4. Remember that the device is also an adaptor
        ways[self.device] = ways[self.device - 1] + ways[self.device - 2] + ways[self.device - 3]

        # 5. Return the number of ways to reach the device
        return ways[self.device]

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 1. Return the solution for part one
        return self.get_part_one_differences()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 1. Return the solution for part two
        return self.how_many_ways()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         j o l t s . p y                        end
# ======================================================================
