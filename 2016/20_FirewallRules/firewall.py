# ======================================================================
# Firewall Rules
#   Advent of Code 2016 Day 20 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         f i r e w a l l . p y
# ======================================================================
"A solver for the Advent of Code 2016 Day 20 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
IP_LOW = 0
IP_HIGH = 4294967295

# ======================================================================
#                                                               Firewall
# ======================================================================


class Firewall(object):   # pylint: disable=R0902, R0205
    "Object for Firewall Rules"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.ranges = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            for line in text:
                self.ranges.append([int(x) for x in line.split('-')])

        # 3. Sort the ranges
        self.ranges.sort()

    def lowest(self):
        "Find the lowest allowed external address"

        # 1. You have to start somewhere
        lowest = IP_LOW

        # 2. Loop for all of the sorted ranges
        for low_high in self.ranges:

            # 3. If our value is less than this range, we have a winner
            if lowest < low_high[0]:
                return lowest

            # 4. If the range excludes our value, try the next one
            if lowest < low_high[1]:
                lowest = low_high[1] + 1

        # 5. And the winner by default
        return lowest

    def count(self, highest=IP_HIGH):
        "Returns the number of external addresses allowed"

        # 1. You have to start somewhere
        result = 0
        lowest = IP_LOW

        # 2. Loop for all of the sorted ranges
        for low_high in self.ranges:

            # 3. If our value is less than this range, have some
            if lowest < low_high[0]:
                result += low_high[0] - lowest

            # 4. If the range excludes our value, try the next one
            if lowest < low_high[1]:
                lowest = low_high[1] + 1

        # 5. Is there anything at the high end?
        if lowest < highest:
            result += highest - lowest

        # 6. Return the count of unblocked addressess
        return result

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.lowest()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.count()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      f i r e w a l l . p y                     end
# ======================================================================
