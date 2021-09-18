# ======================================================================
# Infinite Elves and Infinite Houses
#   Advent of Code 2015 Day 20 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         f e d e l f . p y
# ======================================================================
"A solver for the Advent of Code 2015 Day 20 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from collections import defaultdict

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                 Fedelf
# ======================================================================


class Fedelf(object):   # pylint: disable=R0902, R0205
    "Object for Infinite Elves and Infinite Houses"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.goal = 0

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.goal = int(text[0])

    def fast_deliver(self, verbose=False):

        # 1. Get a whole bunch of houses
        houses = defaultdict(int)

        # 2. Loop for an infinate number of elves
        for elf in range(1, self.goal):

            # 3. Deliver to all of the houses
            for house in range(elf, self.goal, elf):

                # 4. Deliver presents to this house
                houses[house] += elf * 10

            # 5. Have we got enough presents delivered?
            if houses[elf] >= self.goal:
                return elf

            # 6, Verbose ouput
            if verbose and 0 == elf % 1000:
                print(elf, houses[elf])

        # 7. Didn't work
        return None

    def slow_deliver(self, verbose=False):
        "Deliver presents until we reach a house with the goal"

        # 1. Loop for a infinate number of houses
        house = 0
        presents = 0
        while presents < self.goal:

            # 2. Advance to the next house
            house += 1
            presents = 0

            # 3. Loop for all of the elves
            for elf in range(1, house + 1):

                # 4. Will this elf make a delivery?  If so accumulate presents
                if 0 == house % elf:
                    presents += elf * 10

            # 5, Verbose ouput
            if verbose and 0 == house % 1000:
                print(house, presents)

        # 6. Return the house number
        return house

    def deliver2(self, verbose=False):

        # 1. Get a whole bunch of houses
        houses = defaultdict(int)

        # 2. Loop for an infinate number of elves
        for elf in range(1, self.goal):

            # 3. Deliver to 50 houses
            for house in range(elf, min(1 + 50 * elf, self.goal), elf):

                # 4. Deliver presents to this house
                houses[house] += elf * 11

            # 5. Have we got enough presents delivered?
            if houses[elf] >= self.goal:
                return elf

            # 6, Verbose ouput
            if verbose and 0 == elf % 1000:
                print(elf, houses[elf])

        # 7. Didn't work
        return None

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.fast_deliver(verbose=verbose)

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.deliver2(verbose=verbose)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                        f e d e l f . p y                       end
# ======================================================================
