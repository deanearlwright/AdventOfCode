
# ======================================================================
# Wait For It
#   Advent of Code 2023 Day 06 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         s o l v e r . p y
# ======================================================================
"A solver for the Advent of Code 2023 Day 06 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from math import prod
from race import Race

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                 Solver
# ======================================================================


class Solver(object):   # pylint: disable=R0902, R0205
    "Object for Wait For It"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.races = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:

            # 3. Part 2 needs to remove spaces
            if self.part2:
                for indx, line in enumerate(text):
                    text[indx] = line.replace(' ', '')

            # 4. Ok, now we can process the text
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        assert text is not None and len(text) == 2

        # 1. Check the input
        assert text[0].startswith("Time:")
        assert text[1].startswith("Distance:")

        # 2. Get the numbers from the input lines
        times = [int(x) for x in text[0].split(":")[1].split()]
        dists = [int(x) for x in text[1].split(":")[1].split()]
        assert len(times) == len(dists)

        # 3. Loop over the input, creating and saving races
        for indx, time in enumerate(times):
            a_race = Race(num=1 + indx, time=time, distance=dists[indx],
                          part2=self.part2)
            self.races.append(a_race)

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        if self.text:
            return prod([r.number_of_ways() for r in self.races])
        return None

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        if self.text:
            return prod([r.number_of_ways() for r in self.races])
        return None

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                      s o l v e r . p y                     end
# ======================================================================
