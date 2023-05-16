
# ======================================================================
# Pyroclastic Flow
#   Advent of Code 2022 Day 17 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         c h a m b e r . p y
# ======================================================================
"Chamber for the Advent of Code 2022 Day 17 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
CORNER = '+'
SIDE = '|'
BOTTOM = '-'
ROCK = '#'
MOVING = '@'
SPACE = '.'
LEFT = '<'
RIGHT = '>'
SIDEWAYS = {'>': 1, '<': -1}
CLEAR_BELOW = frozenset([MOVING, SPACE])

# ======================================================================
#                                                                Chamber
# ======================================================================


class Chamber(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Pyroclastic Flow"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.width = 0
        self.rows = []
        self.falling = None
        self.empty = None
        self.rocks = 0

        # 2. Process text (if any)
        if text is not None and len(text) > 0:

            # 3. Set the chamber width
            self.width = int(text)
            self.empty = ''.join([SIDE, ''.ljust(self.width, SPACE), SIDE])

            # 4. Add the bottom
            self.rows.append(''.join([CORNER, BOTTOM.ljust(self.width, BOTTOM), CORNER]))

    def add_rock(self, rock):
        "Add a falling rock"

        # 1. Get the highest current rock (or bottom)
        highest = self.get_highest()

        # 2. Set the rock locations
        rock.loc = (3, highest + 4)

        # 3. Save the rock
        self.falling = rock

        # 4. Get space for the rock
        rock_top = self.falling.loc[1] + self.falling.height - 1
        while rock_top >= len(self.rows):
            self.rows.append(self.empty)

        # 5. Draw the rock
        self.draw_rock()

    def draw_rock(self, char=MOVING):
        "Draw the rock in the chamber"

        # 1 Determine the top row of the rock
        rock_top = self.falling.loc[1] + self.falling.height - 1

        # 2. Loop for the rows in the rock's shapeape to the chamber
        for shape_row, shape in enumerate(self.falling.shape):

            # 3. Get the current row
            chamber_row = list(self.rows[rock_top - shape_row])

            # 4. Loop for the characters of the shape
            for shape_col, piece in enumerate(shape):

                # 5. If rock (and not just empty space), draw the piece
                if piece == ROCK:
                    chamber_row[shape_col + self.falling.loc[0]] = char

            # 6. Save the updated chamber row
            self.rows[rock_top - shape_row] = ''.join(chamber_row)

    def push_rock(self, direction):
        "Move falling rock sideways (returns True if you can)"

        # 1. Get the top and bottom rows
        bottom = self.falling.loc[1]
        top = bottom + self.falling.height - 1

        # 2. Check if we can move it
        if direction == RIGHT:
            if not self.can_move_right(bottom, top):
                return False
        else:
            if not self.can_move_left(bottom, top):
                return False

        # 3. We can move it, so we shall
        self.move_rock_sideways(direction, bottom, top)

        # 4. Adjust the location
        self.falling.loc = (self.falling.loc[0] + SIDEWAYS[direction],
                            self.falling.loc[1])

        # 5. We were successful
        return True

    def move_rock_sideways(self, direction, bottom, top):
        "Shift the rock sideways"

        # 1. Get column offset (1 or -1)
        offset = SIDEWAYS[direction]

        # 2. Loop for all rows of the rock
        for rnum in range(bottom, top + 1):

            # 3. Break up the current row
            nxt = list(self.rows[rnum])

            # 4. Loop for the columns of the current row
            for cnum, col in enumerate(self.rows[rnum]):

                # 5. If this is part of the moving rock, remove it
                if col == MOVING:
                    nxt[cnum] = SPACE

            # 6. Loop for the columns of the current row
            for cnum, col in enumerate(self.rows[rnum]):

                # 7. If this is part of the moving rock, add it
                if col == MOVING:
                    nxt[cnum + offset] = MOVING

            # 8. Save the updated row
            self.rows[rnum] = ''.join(nxt)

    def can_move_right(self, bottom, top):
        "Check that the rock can move to the right"

        # 1. Loop for all rows of the rock
        for rnum in range(bottom, top + 1):

            # 2. Find the rightmost part of the rock
            right = self.rows[rnum].rindex(MOVING)

            # 3. Is space to the right a space? In not, can't move
            if self.rows[rnum][right + 1] != SPACE:
                return False

        # 4. Looks good
        return True

    def can_move_left(self, bottom, top):
        "Check that the rock can move to the left"

        # 1. Loop for all rows of the rock
        for rnum in range(bottom, top + 1):

            # 2. Find the leftmost part of the rock
            left = self.rows[rnum].index(MOVING)

            # 3. Is space to the left a space? In not, can't move
            if self.rows[rnum][left - 1] != SPACE:
                return False

        # 4. Looks good
        return True

    def get_highest(self, delta=0):
        "Return the highest rock (or bottom if there is no rock"

        # 1. Loop for all the rows, starting at the top
        for rnum in range(len(self.rows) - 1, 0, -1):

            # 2. If this row is not empty, return the number
            if self.rows[rnum] != self.empty:
                return rnum + delta

        # 3. We have no rocks so we must be at the bottom
        return 0

    def relative_heights(self):
        "Return a tuple of the hights of the columms relative to the lowest"

        # 1. Start with nothing
        heights = [0 for _ in range(self.width)]
        found = [False for _ in range(self.width)]
        lowest = 0

        # 2. Loop for all the rows, starting at the top
        for rnum in range(len(self.rows) - 1, 0, -1):

            # 3. If this row is not empty, check heights
            if self.rows[rnum] != self.empty:

                # 4. Loop for each column
                for indx, col in enumerate(self.rows[rnum][1:-1]):

                    # 5. If there is a rock, save height
                    if col == ROCK and rnum > heights[indx]:
                        heights[indx] = rnum
                        found[indx] = True
                        lowest = rnum

                # 6. If we found all the height, return relative
                if all(found):
                    heights = [h - lowest for h in heights]
                    return tuple(heights)

        # 7. Reached bottom
        return tuple(heights)

    def can_move_down(self, bottom, top):
        "Return True if the rock move downward"

        # 1. Loop for all of the rows that contain the rock
        for rnum in range(bottom, top + 1):

            # 2. For each piece of the rock, check that below is clear
            for cnum, col in enumerate(self.rows[rnum]):
                if col != MOVING:
                    continue

                # 3. If not space or part of the rock, we can't move
                if self.rows[rnum - 1][cnum] not in CLEAR_BELOW:
                    return False

        # 4. All clear
        return True

    def move_down(self):
        "Let the rock fall down one"

        # 1. Get the top and bottom rows
        bottom = self.falling.loc[1]
        top = bottom + self.falling.height - 1

        # 2. Check if we can move it
        if not self.can_move_down(bottom, top):

            # 3. We can't so here it stays
            self.draw_rock(ROCK)
            self.falling = None
            self.rocks += 1
            return False

        # 4. Erase the rock
        self.draw_rock(char=SPACE)

        # 5. Adjust the rock's location
        self.falling.loc = (self.falling.loc[0], bottom - 1)

        # 6. Draw the rock in its new location
        self.draw_rock()

        # 7. Return success
        return True

    def __str__(self):
        "Return a display the chamber"

        # 1. Start with nothing
        result = []

        # 2. Add all the rows to the result
        for row in self.rows:
            result.append(row)

        # 3. Reverse the result (so bottom is at the bottom)
        result.reverse()

        # 4. Return the result as one long string
        return '\n'.join(result)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                       c h a m b e r . p y                      end
# ======================================================================
