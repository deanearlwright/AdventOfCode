
# ======================================================================
# Monkey Map
#   Advent of Code 2022 Day 22 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                           b o a r d . p y
# ======================================================================
"Map for the Advent of Code 2022 Day 22 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import faces

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
SPACE = ' '
WALL = '#'
TILE = '.'
WARP = '@'
STOP = frozenset([WALL, TILE])

WARPPED = {
    '>': (0, 1),
    '<': (-1, 1),
    '^': (1, -1),
    'v': (1, 0),
}

# ======================================================================
#                                                                  Board
# ======================================================================


class Board(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Monkey Map"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.rows = []
        self.faces = None

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.rows.append(WARP)
            self.rows.extend(text)
            self.rows.append(WARP)
            self.make_square()
            self.make_faces()

    def make_square(self):
        "Warping is easier if the end of the rows are filled in"

        # 1. Find the length of the longest row
        longest = 0
        for row in self.rows:
            if len(row) > longest:
                longest = len(row)

        # 2. Right pad all rows to that length
        for indx, row in enumerate(self.rows):
            self.rows[indx] = "".join([WARP,
                                       row.ljust(longest, WARP),
                                       WARP])
            self.rows[indx] = self.rows[indx].replace(SPACE, WARP)

    def make_faces(self):
        "Create the faces for improved warpping"

        # 1. Determine the length of the edges
        if len(self.rows) > 50:
            edge_len = 50
        else:
            edge_len = 4

        # 2. Construct the faces
        self.faces = faces.Faces(text=str(edge_len), part2=self.part2)

    def find_start(self):
        "Return the starting location"

        # 1. If we don't have any rows, there is no start
        if len(self.rows) == 0:
            return (0, 0)

        # 1. The is the first period in the first row
        return (self.rows[1].find(TILE), 1)

    def at_loc(self, loc):
        "What is at that location"

        # 1. What is at that location
        what = self.rows[loc[1]][loc[0]]

        # 2. Else return what ever is there
        return what

    def warp(self, loc, facing):
        "Return a warped location"

        return self.faces.warp_to(faces.Loc(col=loc[0], row=loc[1]), facing)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         b o a r d . p y                        end
# ======================================================================
