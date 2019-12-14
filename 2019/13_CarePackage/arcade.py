# ======================================================================
# Care Package
#   Advent of Code 2019 Day 13 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                           a r c a d e . p y
# ======================================================================
"Arcade game for Care Package problem for Advent of Code 2019 Day 13"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import intcode


# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
TILEID_EMPTY = 0
TILEID_WALL = 1
TILEID_BLOCK = 2
TILEID_PADDLE = 3
TILEID_BALL = 4

TILEIDS = set([TILEID_EMPTY, TILEID_WALL, TILEID_BLOCK,
               TILEID_PADDLE, TILEID_BALL])

# ======================================================================
#                                                                 Arcade
# ======================================================================


class Arcade():
    """Object representing an arcade game"""

    def __init__(self, text=None):

        # 1. Set the initial values
        self.computer = intcode.IntCode(text=text)

    def run_free(self, watch=False):
        "Run the game until it stops, collecting and destroying blocks"

        # 3. Run the computer until it stops
        return self.computer.run(watch=watch)

    def block_tiles_on_the_screen(self):
        "Process the game output to determine the number of blocks left"

        # 1. Start with no blocks
        blocks = set()

        # 2. Get the game output
        output = self.computer.outputs()
        print(output)

        # 3. Loop for each triplet of output
        for indx in range(0, len(output), 3):
            tile_x = output[indx]
            tile_y = output[indx+1]
            tile_id = output[indx+2]
            assert tile_id in TILEIDS

            # 4. Remember blocks and forget empty spaces
            if tile_id == TILEID_BLOCK:
                print("Adding block at (%d,%d)" % (tile_x, tile_y))
                blocks.add((tile_x, tile_y))
            elif tile_id == TILEID_EMPTY:
                print("Discarding block at (%d,%d)" % (tile_x, tile_y))
                blocks.discard((tile_x, tile_y))

        # 5. Return the number of block left
        return len(blocks)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                       a r c a d e . p y                        end
# ======================================================================
