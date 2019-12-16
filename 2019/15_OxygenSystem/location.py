# ======================================================================
# Oxygen System
#   Advent of Code 2019 Day 15 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                           l o c a t i o n . p y
# ======================================================================
"A ship location for Oxygen System problem Advent of Code 2019 Day 15"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
DIR_N = 'N'
DIR_S = 'S'
DIR_W = 'W'
DIR_E = 'E'
DIRS = set([DIR_N, DIR_S, DIR_W, DIR_E])

IS_WALL = '#'
IS_BACK = '.'
IS_OXYGEN = 'O'
IS_VALUES = set([IS_WALL, IS_BACK, IS_OXYGEN])

# ======================================================================
#                                                               Location
# ======================================================================


class Location():
    """Object representing a location in the space ship"""

    def __init__(self, loc=(0, 0)):

        # 1. Set the initial values
        self.loc = loc
        self.directions = {DIR_N: None,
                           DIR_S: None,
                           DIR_W: None,
                           DIR_E: None}

    def __str__(self):
        return "???"

    def set_dir(self, direction, value):
        "Return the value for a direction"

        # 0. Preconditions
        assert direction in DIRS
        assert values in IS_VALUES
        assert self.directions is None

        # 1. Set the value
        self.directions[direction] = value

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                     l o c a t i o n  . p y                     end
# ======================================================================
