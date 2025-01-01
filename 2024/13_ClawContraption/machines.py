
# ======================================================================
# Claw Contraption
#   Advent of Code 2024 Day 13 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         m a c h i n e s . p y
# ======================================================================
"A solver for the Advent of Code 2024 Day 13 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import machine

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                               Machines
# ======================================================================


class Machines(object):   # pylint: disable=R0902, R0205
    "Object for Claw Contraption"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.machines = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text()

    def _process_text(self):
        "Assign values from text"

        assert self.text is not None and len(self.text) > 0
        assert len(self.text) % 3 == 0

        # 1. Loop for every three lines of text
        for indx in range(0, len(self.text), 3):

            # 2. Create a machine
            claw = machine.Machine(text=self.text[indx:indx + 3], part2=self.part2)

            # 3. Save it
            self.machines.append(claw)

    def tokens(self):
        "Return the total tokens needed"
        return sum(mech.tokens() for mech in self.machines)

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. No solution if no text
        if self.text is None:
            return None

        # 2. Return the solution for part one
        return self.tokens()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. No solution if no text
        if self.text is None:
            return None

        # 2. Return the solution for part two
        return self.tokens()

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                      m a c h i n e s . p y                     end
# ======================================================================
