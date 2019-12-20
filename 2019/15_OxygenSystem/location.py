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

DIR_LETTER = {
    DIR_N: '^',
    DIR_S: 'v',
    DIR_W: '<',
    DIR_E: '>'
}

REV_DIR = {
    DIR_N: DIR_S,
    DIR_S: DIR_N,
    DIR_W: DIR_E,
    DIR_E: DIR_W
}

IS_WALL = '#'
IS_BACK = '<'
IS_FWD = '>'
IS_OXYGEN = 'O'
IS_VALUES = set([IS_WALL, IS_BACK, IS_FWD, IS_OXYGEN])

# ======================================================================
#                                                               Location
# ======================================================================


class Location():
    """Object representing a location in the space ship"""

    def __init__(self, loc=(0, 0)):

        # 1. Set the initial values
        self.loc = loc
        self.dirs = {DIR_N: None,
                     DIR_S: None,
                     DIR_W: None,
                     DIR_E: None}
        self.dist = 0
        self.o_time = None

    def __str__(self):
        return "loc: (%d,%d) N:%s, S:%s, W:%s, E:%s" % (
            self.loc[0], self.loc[1],
            self.dirs[DIR_N], self.dirs[DIR_S],
            self.dirs[DIR_W], self.dirs[DIR_E])

    def set_dir(self, direction, value):
        "Set the value for a direction"

        # 0. Preconditions
        assert direction in DIRS
        assert value in IS_VALUES
        assert self.dirs[direction] is None

        # 1. Set the value
        self.dirs[direction] = value

    def set_wall(self, direction):
        "Set direction as leading to a wall"

        # 0. Preconditions
        assert direction in DIRS
        assert self.dirs[direction] is None

        # 1. Set the value
        self.dirs[direction] = IS_WALL

    def set_back(self, direction):
        "Set direction as leading to the origin"

        # 0. Preconditions
        assert direction in DIRS
        assert self.dirs[direction] is None

        # 1. Set the value
        self.dirs[REV_DIR[direction]] = IS_BACK

    def unknown(self):
        "Return the unknown directions"
        return [key for key, item in self.dirs.items() if item is None]

    def back(self):
        "Return the reverse direction"
        return [key for key, item in self.dirs.items() if item == IS_BACK][0]

    def exits_at(self):
        "Return the direction of the exits"
        return [key for key, item in self.dirs.items() if item is not None and item != IS_WALL]

    def oxygen_at(self):
        "Return when oxygen reached this location (if ever)"
        return self.o_time

    def set_oxygen_time(self, o_time):
        "Set when oxygen reached this location"
        self.o_time = o_time

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                     l o c a t i o n  . p y                     end
# ======================================================================
