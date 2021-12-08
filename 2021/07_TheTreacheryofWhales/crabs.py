# ======================================================================
# The Treachery of Whales
#   Advent of Code 2021 Day 07 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         c r a b s . p y
# ======================================================================
"A solver for the Advent of Code 2021 Day 07 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import statistics

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                  Crabs
# ======================================================================


class Crabs(object):   # pylint: disable=R0902, R0205
    "Object for The Treachery of Whales"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.crabs = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.crabs = [int(x) for x in text[0].split(',')]

    def align_median(self):
        "Align the crabs using a miminum amount of fuel"

        # 1. Go to the medium
        here = int(statistics.median(self.crabs))

        # 2. Determine the amount of fuel needed
        return self.need(here)

    def align_search(self):
        "Align the crabs using a miminum amount of fuel"

        # 1. Assume nothing is best
        least_fuel = self.need(0)

        # 2. Possible locations
        for loc in range(max(self.crabs)):

            # 3. Determine the fuel cost to align here
            fuel = self.need(loc)

            # 4. Is this a better place?
            if fuel < least_fuel:
                least_fuel = fuel

        # 5. Return the least fuel
        return least_fuel

    def need(self, where):
        "Return the amount of fuel needed to move here"

        # 1. Start with nothing
        result = 0

        # 2. Loop for all of the crabs
        for crab in self.crabs:

            # 3. Accumulate the fuel
            result += self.cost(crab, where)

        # 4. Return the total fuel needed
        return result

    def cost(self, here, there):
        "Determine cost from here to there"

        diff = abs(here - there)
        if self.part2:
            return (diff * (diff + 1)) // 2
        return diff

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.align_median()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.align_search()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         c r a b s . p y                        end
# ======================================================================
