# ======================================================================
# Like a Rogue
#   Advent of Code 2016 Day 18 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                             r o w . p y
# ======================================================================
"Row for the Advent of Code 2016 Day 18 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from collections import Counter

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
TILE_TRAP = '^'
TILE_SAFE = '.'
TILE_WALL = ':'


NEXT_TRAP = frozenset(['^^.', '.^^', '^..', '..^'])

# ======================================================================
#                                                                    Row
# ======================================================================


class Row(object):   # pylint: disable=R0902, R0205
    "Object for Like a Rogue"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.tiles = ''

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.tiles = TILE_WALL + text + TILE_WALL

    def count_safe(self):
        "Return the number of safe tiles in the row"
        return Counter(list(self.tiles))[TILE_SAFE]

    def next_tiles(self):
        "Return the tiles in the next row"

        # 1. Start with nothing
        result = []

        # 2. Loop for all of the current tiles
        for indx, tile in enumerate(self.tiles):

            # 3. Just add walls
            if tile == TILE_WALL:
                result.append(tile)
                continue

            # 4. Determine the left, center, and right tiles
            previous = self.tiles[indx - 1: indx + 2].replace(':', '.')

            # 5. Determine if the tile in the next row is a trap or not
            if previous in NEXT_TRAP:
                next_tile = TILE_TRAP
            else:
                next_tile = TILE_SAFE

            # 6. Add the tile to the result
            result.append(next_tile)

        # 7. Return the tiles in the next row
        return ''.join(result)

    def __str__(self):
        return self.tiles

    def __hash__(self):
        return hash(self.tiles)

    def __eq__(self, other):
        return other and self.tiles == other.tiles


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                           r o w . p y                          end
# ======================================================================
