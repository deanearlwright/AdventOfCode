# ======================================================================
# Chronal Classification
#   Advent of Code 2018 Day 16 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         d e v i c e . p y
# ======================================================================
"A solver for the Advent of Code 2018 Day 16 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import observations

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

INSTRUCTION_NAMES = ['addr', 'addi',
                     'mulr', 'muli',
                     'barr', 'bari',
                     'borr', 'bori',
                     'setr', 'seti',
                     'gtir', 'gtri', 'gtrr',
                     'eqir', 'eqri', 'eqrr']

# ======================================================================
#                                                                 Device
# ======================================================================


class Device(object):   # pylint: disable=R0902, R0205
    "Object for Chronal Classification"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.obs = None
        self.program = None

        # 2. Process text (if any)
        if text is not None:
            self.obs = observations.Observations(text=text)

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 1. Return the solution for part one
        return None


    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 1. Return the solution for part two
        return None

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         d e v i c e . p y                      end
# ======================================================================
