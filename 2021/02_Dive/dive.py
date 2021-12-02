# ======================================================================
# Dive
#   Advent of Code 2021 Day 02 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         d i v e . p y
# ======================================================================
"A solver for the Advent of Code 2021 Day 02 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                   Dive
# ======================================================================


class Dive(object):   # pylint: disable=R0902, R0205
    "Object for Dive"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.hor = 0
        self.depth = 0
        self.aim = 0

    def one_inst(self, inst):
        "Execute a single instruction"

        # 1. Decode the instruction
        action, number = inst.split()
        number = int(number)

        # 2. Execute the instruction
        if action == "forward":
            self.hor += number
            if self.part2:
                self.depth += self.aim * number
        elif action == "down":
            if self.part2:
                self.aim += number
            else:
                self.depth += number
        elif action == "up":
            if self.part2:
                self.aim -= number
            else:
                self.depth -= number

        # 3. Return pos * depth
        return self.hor * self.depth

    def all_inst(self):
        "Execute all instructions"

        # 1. Loop for all instructions
        for inst in self.text:

            # 2. Execute the instruction
            result = self.one_inst(inst)

        # 3. Return the result
        return result

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.all_inst()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.all_inst()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                          d i v e . p y                         end
# ======================================================================
