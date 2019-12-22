# ======================================================================
# Springdroid Adventure
#   Advent of Code 2019 Day 21 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                              d r o i d . p y
# ======================================================================
"Droid for the Springdroid Adventure problem for AoC 2019 Day 21"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import intcode

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
DROID = '@'
HULL = '#'
SPACE = '.'
NEWLINE = '\n'

# ======================================================================
#                                                                  Droid
# ======================================================================


class Droid():
    """Object representing a external cameras and vacum robot control"""

    def __init__(self, text=None):

        # 1. Set the initial values
        self.computer = intcode.IntCode(text=text)
        self.last_moments = []
        self.damage = None

    def __str__(self):
        return ''.join([chr(_) for _ in self.last_moments if _ < 128])


    def get_damage(self, watch=False, prog=None):
        "Run the droid program until it stops"

        # 1. Run the computer until it stops
        result = self.computer.run(watch=watch, inp=prog)

        # 2. Output is the how much damage or last_moments
        outputs = self.computer.outputs()
        if outputs[-1] > 127:
            self.damage = outputs.pop()
        self.last_moments = outputs

        # 3. Return the reason for the machine stopping
        return result


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                           a i i . p y                          end
# ======================================================================
