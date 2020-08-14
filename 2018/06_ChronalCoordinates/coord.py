# ======================================================================
# Chronal Coordinates
#   Advent of Code 2018 Day 06 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         c o o r d . p y
# ======================================================================
"A solver for the Advent of Code 2018 Day 06 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
X_MULT = 1000;

# ======================================================================
#                                                                  Coord
# ======================================================================


class Coord(object):   # pylint: disable=R0902, R0205
    "Object for Chronal Coordinates"

    def __init__(self, x=None, y=None):

        # 1. Set the initial values
        self.x = x
        self.y = y
        self.isInfinite = None;
        self.minX = None
        self.maxX = None
        self.minY = None
        self.maxY = None
        self.area = None
        self.closest = None

    def distance(self, x, y):
        # 1. Determine distance from given location
        return abs(self.x - x) + abs(self.y - y)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         c o o r d . p y                        end
# ======================================================================
