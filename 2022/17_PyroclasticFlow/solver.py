
# ======================================================================
# Pyroclastic Flow
#   Advent of Code 2022 Day 17 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         s o l v e r . p y
# ======================================================================
"A solver for the Advent of Code 2022 Day 17 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import simulation

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
ROCKS = 2022
ROCKS_TWO = 1000000000000

# ======================================================================
#                                                                 Solver
# ======================================================================


class Solver(object):   # pylint: disable=R0902, R0205
    "Object for Pyroclastic Flow"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.simulation = None

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.simulation = simulation.Simulation(text=text, part2=part2)

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        if self.simulation:
            return self.simulation.run_for_n_rocks(ROCKS, verbose=verbose)
        return None

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        if self.simulation:
            return self.simulation.calculate_n_rocks(ROCKS_TWO, verbose=verbose)
        return None


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                        s o l v e r . p y                       end
# ======================================================================
