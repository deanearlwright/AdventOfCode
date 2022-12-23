
# ======================================================================
# Beacon Exclusion Zone
#   Advent of Code 2022 Day 15 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         s o l v e r . p y
# ======================================================================
"A solver for the Advent of Code 2022 Day 15 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import device

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
PART1_ROW = 2000000
PART2_ROW = 4000000

# ======================================================================
#                                                                 Solver
# ======================================================================


class Solver(object):   # pylint: disable=R0902, R0205
    "Object for Beacon Exclusion Zone"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.device = None

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.device = device.Device(text=text, part2=part2)

    def part_one(self, verbose=False, limit=0, row=PART1_ROW):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        if self.device:
            return self.device.count_not_beacons_row(row=row)
        return None

    def part_two(self, verbose=False, limit=0, row=PART2_ROW):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        if self.device:
            return self.device.tuning_frequency(row=row)
        return None

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                      s o l v e r . p y                     end
# ======================================================================
