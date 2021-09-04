# ======================================================================
# No Such Thing as Too Much
#   Advent of Code 2015 Day 17 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         e g g n o g . p y
# ======================================================================
"A solver for the Advent of Code 2015 Day 17 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import itertools

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EGGNOG_AMOUNT = 150

# ======================================================================
#                                                                 Eggnog
# ======================================================================


class Eggnog(object):   # pylint: disable=R0902, R0205
    "Object for No Such Thing as Too Much"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.containers = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            for line in self.text:
                self.containers.append(int(line))

    def num_combos(self, amount=EGGNOG_AMOUNT):
        "Returns the number of combinations of containers"

        # 1. Start with nothing
        result = 0

        # 2. Loop for the number of containers
        for number in range(1, len(self.containers)):

            # 3. Loop for all combinations of that number of containers
            for kntrs in itertools.combinations(self.containers, number):

                # 4. The they exactly hold the amount we want, increment the count
                if sum(kntrs) == amount:
                    result += 1

            # 5. For part two, use only the minimum number of containers
            if self.part2 and result > 0:
                break

        # 6. Return the number of combinations
        return result

    def part_one(self, verbose=False, limit=0, amount=EGGNOG_AMOUNT):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.num_combos(amount=amount)

    def part_two(self, verbose=False, limit=0, amount=EGGNOG_AMOUNT):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.num_combos(amount=amount)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                        e g g n o g . p y                       end
# ======================================================================
