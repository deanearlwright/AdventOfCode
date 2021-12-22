# ======================================================================
# Dirac Dice
#   Advent of Code 2021 Day 21 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         d i e . p y
# ======================================================================
"Die for the Advent of Code 2021 Day 21 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
SIDES = 100
# ======================================================================
#                                                                    Die
# ======================================================================


class Die(object):   # pylint: disable=R0902, R0205
    "Object for Dirac Dice"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.rolled = 0
        self.sides = SIDES
        self.last = 0

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.sides = int(text)

    def roll(self):
        "Roll them bones"

        # 1. Part 1: Roll a deterministic die
        if not self.part2:
            self.rolled += 1
            self.last += 1
            if self.last > SIDES:
                self.last = 1
            return self.last

        # 2. Part 2:
        return None


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                           d i e . p y                          end
# ======================================================================
