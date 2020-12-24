# ======================================================================
# Jurassic Jigsaw
#   Advent of Code 2020 Day 20 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                           t i l e s . p y
# ======================================================================
"Multiple tiles for the Advent of Code 2020 Day 20 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import math

import tile

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
TILE_SIZE = 10

# ----------------------------------------------------------------------
#                                                                utility
# ----------------------------------------------------------------------


# ======================================================================
#                                                                  Tiles
# ======================================================================


class Tiles(object):   # pylint: disable=R0902, R0205
    "Object for Jurassic Jigsaw"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.tiles = []
        self.size = 0
        self.grid = None

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Read and save the tiled image"

        # 1. Start with nothing
        tile_text = []

        # 2. Loop for all lines in the imput
        for line in text:

            # 3. Add this line to the tile_text
            tile_text.append(line)

            # 4. Do we have enough lines for an image?
            if len(tile_text) == TILE_SIZE + 1:

                # 5. Yes, Create a tile and add it to the collection
                self.tiles.append(tile.Tile(text=tile_text, part2=self.part2))
                tile_text = []

        # 6. Determine image size
        self.size = math.isqrt(len(self.tiles))

        # 7. Post condition axioms
        assert len(self.tiles) == self.size ** 2

    def position_tiles(self):
        "Position the oriented tiles in a nice grid"

        # 1. Find a (hopefully) working able solution
        self.grid = self._position_tiles(
            [[None] * self.size for _ in range(self.size)], 0, 0)

    def number_at(self, row, col):
        "Return the tile number at the grid location"
        if self.grid is None:
            return 0
        if row == -1:
            row = self.size - 1
        if col == -1:
            col = self.size - 1
        return self.grid[row][col][0].number

    @staticmethod
    def _already_placed(grid, the_tile):
        "Returns True if the tile is already in the grid"

        # 1. Loop for all the rows and columns
        for row in grid:
            for col in row:

                # 2. If the tile is here, return True
                if col is not None and col[0] == the_tile:
                    return True

        # 3. Not found
        return False

    def _position_tiles(self, grid, row, col):
        "Recursively position the oriented tiles in a nice grid"

        # 1. Have we done enough?
        if row == self.size:
            return grid

        # 3. Loop for all the possible tiles (that aren't already in the grid)
        for the_tile in self.tiles:
            if self._already_placed(grid, the_tile):
                continue

            # 4. Try placing the tile in the row and column of the grid
            rest = self._position_tile(grid, row, col, the_tile)
            if rest is not None:
                return rest

        # 5. Nothing to see here
        return None

    def _position_tile(self, grid, row, col, the_tile):
        "Try to orient the tile at the row and column in the grid"

        # 1. Loop for all of the possible orientations of the tile
        for index, border in enumerate(the_tile.borders):

            # 2. Do the borders match?
            if col > 0:
                other, other_index = grid[row][col - 1]
                if other.borders[other_index][tile.B_RIGHT] != border[tile.B_LEFT]:
                    continue
            if row > 0:
                other, other_index = grid[row - 1][col]
                if other.borders[other_index][tile.B_BOTTOM] != border[tile.B_TOP]:
                    continue

            # 3. The tile looks good in this orientation, save it in the grid
            grid[row][col] = (the_tile, index)

            # 4. Where does the next tile go?
            next_col = col + 1
            next_row = row
            if next_col == self.size:
                next_col = 0
                next_row += 1

            # 5. Now try to fill in the rest
            rest = self._position_tiles(grid, next_row, next_col)
            if rest is not None:
                return rest

        # 6. That could have gone better
        grid[row][col] = None
        return None

    def get_image(self):
        "Get the combined image"

        # 1. If we don't have a grid, get it (if we can)
        if self.grid is None:
            self.position_tiles()
            if self.grid is None:
                return None

        # 2. Start with nothing will become rows
        result = []

        # 3. Loop for all of the rows in the grid
        for row in self.grid:

            # 4. Collect the borderless tiles for this row of the
            row_tiles = []
            for row_tile, index in row:
                row_tiles.append(tile.remove_border(row_tile.orientations[index]))

            # 5. Add each of the rows of the image of this grid row to the result
            for image_row in range(len(row_tiles[0][0])):
                row_of_image = []
                for row_tile in row_tiles:
                    row_of_image.extend(row_tile[image_row])
                result.append(''.join(row_of_image))

        # 6. Return combined image
        return '\n'.join(result)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         t i l e s . p y                        end
# ======================================================================
