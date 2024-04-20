
# ======================================================================
# The Floor Will Be Lava
#   Advent of Code 2023 Day 16 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         t i l e . p y
# ======================================================================
"Tile for the Advent of Code 2023 Day 16 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EMPTY = "."
LEFT = "/"
RIGHT = "\\"
FLAT = "-"
VERT = "|"
CHARS = frozenset([EMPTY, LEFT, RIGHT, FLAT, VERT])

NORTH = "^"
SOUTH = "v"
EAST = ">"
WEST = "<"
DIRS = frozenset([NORTH, SOUTH, EAST, WEST])

DELTA = {
    NORTH: (-1, 0),
    SOUTH: (1, 0),
    EAST: (0, 1),
    WEST: (0, -1),
}

NEXT = {
    NORTH: {
        EMPTY: [NORTH],
        LEFT: [EAST],
        RIGHT: [WEST],
        FLAT: [EAST, WEST],
        VERT: [NORTH],
    },
    SOUTH: {
        EMPTY: [SOUTH],
        LEFT: [WEST],
        RIGHT: [EAST],
        FLAT: [EAST, WEST],
        VERT: [SOUTH],
    },
    EAST: {
        EMPTY: [EAST],
        LEFT: [NORTH],
        RIGHT: [SOUTH],
        FLAT: [EAST],
        VERT: [NORTH, SOUTH],
    },
    WEST: {
        EMPTY: [WEST],
        LEFT: [SOUTH],
        RIGHT: [NORTH],
        FLAT: [WEST],
        VERT: [NORTH, SOUTH],
    },
}
# ======================================================================
#                                                                   Tile
# ======================================================================


class Tile(object):   # pylint: disable=R0902, R0903, R0205
    "Object for The Floor Will Be Lava"

    def __init__(self, row=0, col=0, char=EMPTY):

        # 0. Precondition axioms
        assert 0 <= row
        assert 0 <= col
        assert char in CHARS

        # 1. Set the initial values
        self.row = row
        self.col = col
        self.char = char
        self.activated = False
        self.directions = set()

    def reset(self):
        "Reset to the initial state"
        self.activated = False
        self.directions = set()

    def entered(self, direction):
        "A beam enters from the given direction, return new directions"

        # 0. Precondition axioms
        assert direction in DIRS

        # 1. We are activated
        self.activated = True

        # 2. Have we had light come from this direction before?
        if direction in self.directions:
            return []

        # 3. Now we have
        self.directions.add(direction)

        # 4. Return the new direction(s)
        return NEXT[direction][self.char]

    def next(self, direction):
        "Return the next location if going in the given direction"

        # 0. Precondition axioms
        assert direction in DIRS

        # 1. Get the change in location
        delta = DELTA[direction]

        # 2. Return the new location (row, col)
        return (self.row + delta[0], self.col + delta[1])

    def is_activated(self):
        "Return the activation state (False or True)"
        return self.activated

    def energized(self):
        "Return the energized state (0 or 1)"
        if self.activated:
            return 1
        return 0

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                          t i l e . p y                         end
# ======================================================================
