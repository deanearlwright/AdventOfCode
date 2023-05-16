
# ======================================================================
# Monkey Map
#   Advent of Code 2022 Day 22 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         f a c e s . p y
# ======================================================================
"Faces for the Advent of Code 2022 Day 22 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from collections import namedtuple

# ----------------------------------------------------------------------
#                                                                  types
# ----------------------------------------------------------------------
Loc = namedtuple('Loc', 'col, row')
Face = namedtuple('Face', 'number, min_col, max_col, min_row, max_row')
Warp = namedtuple('Warp', 'num, dir')
WarpLoc = namedtuple('WarpLoc', 'from_face, to_face, facing')

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
MIN = -1    # Go to the minimum col/row for this face
SAME = 0    # Keep the same col/row
MAX = 1     # Go to the maximum col/row for this face
OFFSET = 2  # Same col/row but offset for new face
OFFREV = 3  # Offset but min/max reversed
OTHER = 4   # Switch row/col with offset
OTHREV = 5  # Switch row/col with reverse offset

N = '^'
S = 'v'
E = '>'
W = '<'

# ----------------------------------------------------------------------
# Part One Example                                             constants
# ----------------------------------------------------------------------
WARP_ONE = {N: Warp(5, N), S: Warp(4, S), E: Warp(1, E), W: Warp(1, W)}
WARP_TWO = {N: Warp(2, N), S: Warp(2, S), E: Warp(3, E), W: Warp(4, W)}
WARP_TRI = {N: Warp(3, N), S: Warp(3, S), E: Warp(4, E), W: Warp(2, W)}
WARP_FUR = {N: Warp(1, N), S: Warp(5, S), E: Warp(2, E), W: Warp(3, W)}
WARP_FIV = {N: Warp(4, N), S: Warp(1, S), E: Warp(6, E), W: Warp(6, W)}
WARP_SIX = {N: Warp(6, N), S: Warp(6, S), E: Warp(5, E), W: Warp(5, W)}
WARPS = [None, WARP_ONE, WARP_TWO, WARP_TRI, WARP_FUR, WARP_FIV, WARP_SIX]


# ----------------------------------------------------------------------
# Part One Puzzle Input                                        constants
# ----------------------------------------------------------------------
WARP_ONE_PI = {N: Warp(1, N), S: Warp(1, S), E: Warp(2, E), W: Warp(2, W)}
WARP_TWO_PI = {N: Warp(4, N), S: Warp(3, S), E: Warp(1, E), W: Warp(1, W)}
WARP_TRI_PI = {N: Warp(2, N), S: Warp(4, S), E: Warp(3, E), W: Warp(3, W)}
WARP_FUR_PI = {N: Warp(3, N), S: Warp(2, S), E: Warp(5, E), W: Warp(5, W)}
WARP_FIV_PI = {N: Warp(6, N), S: Warp(6, S), E: Warp(4, E), W: Warp(4, W)}
WARP_SIX_PI = {N: Warp(5, N), S: Warp(5, S), E: Warp(6, E), W: Warp(6, W)}
WARPS_PI = [None, WARP_ONE_PI, WARP_TWO_PI, WARP_TRI_PI,
            WARP_FUR_PI, WARP_FIV_PI, WARP_SIX_PI]

# ----------------------------------------------------------------------
# Part Two                                                     constants
# ----------------------------------------------------------------------
WARP_ONE_TWO = {N: Warp(2, S), S: Warp(4, S), E: Warp(6, W), W: Warp(3, S)}
WARP_TWO_TWO = {N: Warp(1, S), S: Warp(5, N), E: Warp(3, E), W: Warp(6, N)}
WARP_TRI_TWO = {N: Warp(1, E), S: Warp(5, E), E: Warp(4, E), W: Warp(2, W)}
WARP_FUR_TWO = {N: Warp(1, N), S: Warp(5, S), E: Warp(6, S), W: Warp(3, W)}
WARP_FIV_TWO = {N: Warp(4, N), S: Warp(2, N), E: Warp(6, E), W: Warp(3, N)}
WARP_SIX_TWO = {N: Warp(4, W), S: Warp(2, E), E: Warp(1, W), W: Warp(5, W)}
WARPS_TWO = [None, WARP_ONE_TWO, WARP_TWO_TWO, WARP_TRI_TWO,
             WARP_FUR_TWO, WARP_FIV_TWO, WARP_SIX_TWO]

# ----------------------------------------------------------------------
# Part Two Puzzle Input                                        constants
# ----------------------------------------------------------------------
WARP_ONE_PI2 = {N: Warp(6, N), S: Warp(3, W), E: Warp(4, W), W: Warp(2, W)}
WARP_TWO_PI2 = {N: Warp(6, E), S: Warp(3, S), E: Warp(1, E), W: Warp(5, E)}
WARP_TRI_PI2 = {N: Warp(2, N), S: Warp(4, S), E: Warp(1, N), W: Warp(5, S)}
WARP_FUR_PI2 = {N: Warp(3, N), S: Warp(6, W), E: Warp(1, W), W: Warp(5, W)}
WARP_FIV_PI2 = {N: Warp(3, E), S: Warp(6, S), E: Warp(4, E), W: Warp(2, E)}
WARP_SIX_PI2 = {N: Warp(5, N), S: Warp(1, S), E: Warp(4, N), W: Warp(2, S)}
WARPS_PI2 = [None, WARP_ONE_PI2, WARP_TWO_PI2, WARP_TRI_PI2,
             WARP_FUR_PI2, WARP_FIV_PI2, WARP_SIX_PI2]

# ----------------------------------------------------------------------
# Common direction location alterations                        constants
# ----------------------------------------------------------------------
ALTER = {N: {N: Loc(col=SAME, row=MAX),
             S: Loc(col=OFFREV, row=MIN),
             E: Loc(col=MIN, row=OTHER),
             W: Loc(col=MAX, row=OTHREV)},
         S: {N: Loc(col=OFFREV, row=MAX),
             S: Loc(col=SAME, row=MIN),
             E: Loc(col=MIN, row=OTHREV),
             W: Loc(col=MAX, row=OTHER)},
         E: {N: Loc(col=OTHER, row=MAX),
             S: Loc(col=OTHREV, row=MIN),
             E: Loc(col=MIN, row=SAME),
             W: Loc(col=MAX, row=OFFREV)},
         W: {N: Loc(col=OTHREV, row=MAX),
             S: Loc(col=OTHER, row=MIN),
             E: Loc(col=MIN, row=OFFREV),
             W: Loc(col=MAX, row=SAME)}
         }


# ======================================================================
#                                                                  Faces
# ======================================================================


class Faces(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Monkey Map"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.edge_len = 1
        self.faces = []
        self.face_warp = WARPS
        if self.part2:
            self.face_warp = WARPS_TWO

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.edge_len = int(text)

            # 3. And add the face information
            self.faces.append(None)
            if self.edge_len == 4:
                self.faces_example()
            else:
                self.faces_input()

        # 4. Set Warp tables for actual puzzle input
        if self.edge_len > 4:
            self.face_warp = WARPS_PI
            if self.part2:
                self.face_warp = WARPS_PI2

    def faces_example(self):
        "Construct the faces for the example"

        self.faces.append(Face(number=1,
                               min_col=1 + 2 * self.edge_len,
                               max_col=3 * self.edge_len,
                               min_row=1,
                               max_row=self.edge_len))
        self.faces.append(Face(number=2,
                               min_col=1,
                               max_col=self.edge_len,
                               min_row=1 + self.edge_len,
                               max_row=2 * self.edge_len))
        self.faces.append(Face(number=3,
                               min_col=1 + self.edge_len,
                               max_col=2 * self.edge_len,
                               min_row=1 + self.edge_len,
                               max_row=2 * self.edge_len))
        self.faces.append(Face(number=4,
                               min_col=1 + 2 * self.edge_len,
                               max_col=3 * self.edge_len,
                               min_row=1 + self.edge_len,
                               max_row=2 * self.edge_len))
        self.faces.append(Face(number=5,
                               min_col=1 + 2 * self.edge_len,
                               max_col=3 * self.edge_len,
                               min_row=1 + 2 * self.edge_len,
                               max_row=3 * self.edge_len))
        self.faces.append(Face(number=6,
                               min_col=1 + 3 * self.edge_len,
                               max_col=4 * self.edge_len,
                               min_row=1 + 2 * self.edge_len,
                               max_row=3 * self.edge_len))

    def faces_input(self):
        "Construct the faces for the actual puzzle input"

        self.faces.append(Face(number=1,
                               min_col=1 + 2 * self.edge_len,
                               max_col=3 * self.edge_len,
                               min_row=1,
                               max_row=self.edge_len))
        self.faces.append(Face(number=2,
                               min_col=1 + self.edge_len,
                               max_col=2 * self.edge_len,
                               min_row=1,
                               max_row=self.edge_len))
        self.faces.append(Face(number=3,
                               min_col=1 + self.edge_len,
                               max_col=2 * self.edge_len,
                               min_row=1 + self.edge_len,
                               max_row=2 * self.edge_len))
        self.faces.append(Face(number=4,
                               min_col=1 + self.edge_len,
                               max_col=2 * self.edge_len,
                               min_row=1 + 2 * self.edge_len,
                               max_row=3 * self.edge_len))
        self.faces.append(Face(number=5,
                               min_col=1,
                               max_col=self.edge_len,
                               min_row=1 + 2 * self.edge_len,
                               max_row=3 * self.edge_len))
        self.faces.append(Face(number=6,
                               min_col=1,
                               max_col=self.edge_len,
                               min_row=1 + 3 * self.edge_len,
                               max_row=4 * self.edge_len))

    def on_face(self, loc):
        "Return the number of the face of the location"

        # 1. Loop for all the faces
        for face_info in self.faces:
            if face_info is None:
                continue

            # 2. If the location within the bounds of the face ...
            if (loc.col >= face_info.min_col
                and loc.col <= face_info.max_col
                and loc.row >= face_info.min_row
                    and loc.row <= face_info.max_row):

                # 3. ... return face number!
                return face_info.number

        # 4. Now that is a bit strange
        return 0

    def warp_to(self, loc, facing):
        "Return new location and facing after warpping"

        # 1. What face are we on now?
        loc_face = self.on_face(loc)

        # 2. What face will we be on?
        new_face, new_facing = self.face_warp[loc_face][facing]

        # 3. Determine the new location
        new_loc = self.alter_loc(loc, loc_face, new_face, facing, new_facing)

        # 4. Return the new location and facing
        return new_loc, new_facing

    def relative_loc(self, face, loc):
        "Return the relative location on the face"

        return Loc(col=loc.col - self.faces[face].min_col,
                   row=loc.row - self.faces[face].min_row)

    def alter_loc(self, loc, old_face, new_face, old_facing, new_facing): # pylint: disable=R0912, R0913
        "Determine the warped location using new improved ALTER table"

        # 1. Get the min and maximums of the new face
        new_info = self.faces[new_face]

        # 2. Get the location change info
        loc_info = ALTER[old_facing][new_facing]
        if loc_info.col == loc_info.row:
            print(f"Unknown Alter: loc={loc}, old={old_facing}, new={new_facing}")
            return loc

        # 3. Start with the old location
        new_loc = loc
        rel_loc = self.relative_loc(old_face, loc)

        # 4. Adjust column
        if loc_info.col == MIN:
            new_loc = Loc(col=new_info.min_col, row=new_loc.row)
        elif loc_info.col == SAME:
            new_loc = Loc(col=new_info.min_col + rel_loc.col, row=new_loc.row)
        elif loc_info.col == MAX:
            new_loc = Loc(col=new_info.max_col, row=new_loc.row)
        elif loc_info.col == OFFSET:
            new_loc = Loc(col=new_info.min_col + rel_loc.col, row=new_loc.row)
        elif loc_info.col == OFFREV:
            new_loc = Loc(col=new_info.max_col - rel_loc.col, row=new_loc.row)
        elif loc_info.col == OTHER:
            new_loc = Loc(col=new_info.min_col + rel_loc.row, row=new_loc.row)
        elif loc_info.col == OTHREV:
            new_loc = Loc(col=new_info.max_col - rel_loc.row, row=new_loc.row)

        # 5. Adjust row
        if loc_info.row == MIN:
            new_loc = Loc(col=new_loc.col, row=new_info.min_row)
        elif loc_info.row == SAME:
            new_loc = Loc(col=new_loc.col, row=new_info.min_row + rel_loc.row)
        elif loc_info.row == MAX:
            new_loc = Loc(col=new_loc.col, row=new_info.max_row)
        elif loc_info.row == OFFSET:
            new_loc = Loc(col=new_loc.col, row=new_info.min_row + rel_loc.row)
        elif loc_info.row == OFFREV:
            new_loc = Loc(col=new_loc.col, row=new_info.max_row - rel_loc.row)
        elif loc_info.row == OTHER:
            new_loc = Loc(col=new_loc.col, row=new_info.min_row + rel_loc.col)
        elif loc_info.row == OTHREV:
            new_loc = Loc(col=new_loc.col, row=new_info.max_row - rel_loc.col)

        # 6. Return the new location
        return new_loc

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass


# ======================================================================
# end                         f a c e s . p y                        end
# ======================================================================
