
# ======================================================================
# The Floor Will Be Lava
#   Advent of Code 2023 Day 16 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         c o n t r a p t i o n . p y
# ======================================================================
"Contraption for the Advent of Code 2023 Day 16 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import tile

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
FIRST_LOC = (0, 0)
FIRST_DIR = tile.EAST

# ======================================================================
#                                                            Contraption
# ======================================================================


class Contraption(object):   # pylint: disable=R0902, R0903, R0205
    "Object for The Floor Will Be Lava"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.rows = 0
        self.cols = 0
        self.tiles = {}

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        # 0. Precondition axioms
        assert text is not None and len(text) > 0

        # 1. Determine the number of rows and columns
        self.rows = len(self.text)
        self.cols = len(self.text[0])

        # 2. Loop for all the rows and columns
        for rindx, row in enumerate(self.text):
            assert self.cols == len(row)
            for cindx, char in enumerate(row):

                # 3. Create and save a tile for this location
                self.tiles[(rindx, cindx)] = tile.Tile(row=rindx, col=cindx, char=char)

    def bounce(self, initial=(FIRST_LOC, FIRST_DIR)):
        "Bounce the light around the times, return energized count"

        # 1. Might need to reset the tiles
        if self.part2:
            self.reset()

        # 2. Start with just the initial beam
        beams = [initial]

        # 3. While there are place to enlighten
        while beams:

            # 4. Get the location and direction for one of the beams
            bloc, bdir = beams.pop()

            # 5. Get the cooresponding tile
            btile = self.tiles[bloc]

            # 6. Loop for all of the new directions
            for new_dir in btile.entered(bdir):

                # 7. Get the new location
                new_loc = btile.next(new_dir)

                # 8. Add the new loc and direction (if not off the charts)
                if 0 <= new_loc[0] < self.rows and 0 <= new_loc[1] < self.cols:
                    beams.append((new_loc, new_dir))

        # 9. Return the energized count
        return self.energized()

    def energized(self):
        "Return the energized count"
        return sum(t.energized() for t in self.tiles.values())

    def reset(self):
        "Reset all of the time in the contraction"
        for til in self.tiles.values():
            til.reset()

    def max_bounce(self):
        "Find the maximum number of energized tiles while adjusting the starting beam"

        # 1. Start with nothing
        result = 0

        # 2. Try all of the top row
        for col in range(self.cols):
            result = max(result, self.bounce(initial=((0, col), tile.SOUTH)))

        # 3. Try all of the bottom row
        for col in range(self.cols):
            result = max(result, self.bounce(initial=((self.rows - 1, col), tile.NORTH)))

        # 4. Try all of the left side
        for row in range(self.rows):
            result = max(result, self.bounce(initial=((row, 0), tile.EAST)))

        # 5. Try all of the right side
        for row in range(self.rows):
            result = max(result, self.bounce(initial=((row, self.cols - 1), tile.WEST)))

        # 6. Return the maximum number of energized tiles
        return result


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------

if __name__ == '__main__':
    pass

# ======================================================================
# end                   c o n t r a p t i o n . p y                  end
# ======================================================================
