# ======================================================================
# Set and Forget
#   Advent of Code 2019 Day 17 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                              a i i . p y
# ======================================================================
"Lights and action for Set and Forget problem for AoC 2019 Day 17"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import intcode

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
SCAFFOLD = 35
OPENSPACE = 46
NEWLINE = 10

# ======================================================================
#                                                                  ASCII
# ======================================================================


class AII():
    """Object representing a external cameras and vacum robot control"""

    def __init__(self, text=None):

        # 1. Set the initial values
        self.computer = intcode.IntCode(text=text)
        self.ext_map = []
        self.dust = -1

    def __str__(self):
        return ''.join([chr(_) for _ in self.ext_map])

    def get_map(self, watch=False):
        "Run the ascii program until it stops"

        # 1. Run the computer until it stops
        result = self.computer.run(watch=watch)

        # 2. Ouput is the external map
        self.ext_map = self.computer.outputs()

        # 3. Return the reason for the machine stopping
        return result

    def get_dust(self, watch=False, movement=None):
        "Run the ascii program until it stops"

        # 1. Run the computer until it stops
        self.computer.alter(0, 2)
        result = self.computer.run(watch=watch, inp=movement)

        # 2. Ouput is the how much dust
        self.dust = self.computer.outputs()

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
