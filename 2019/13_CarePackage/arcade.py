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

JOYSTICK_NEUTRAL = 0
JOYSTICK_LEFT = -1
JOYSTICK_RIGHT = 1

# ======================================================================
#                                                                 Arcade
# ======================================================================


class Arcade():
    """Object representing an arcade game"""

    def __init__(self, text=None, free=False):

        # 1. Set the initial values
        self.computer = intcode.IntCode(text=text)
        self.score = None
        self.ball_x = None
        self.paddle_x = None
        self.joystick = None
        self.blocks = set()

        # 2. Do you want to play for free
        if free:
            self.computer.alter(0, 2)

    def run_demo(self, watch=False):
        "Run the game until it stops, collecting and destroying blocks"

        # 1. Run the computer until it stops
        return self.computer.run(watch=watch)

    def run_game(self, watch=False):
        "Run the game moving the joystick"

        # 1. Assume the computer wants input
        result = intcode.STOP_INP

        # 2. Run while the computer wants input
        while result == intcode.STOP_INP:

            # 3. Run the computer until it stops
            result = self.computer.run(inp=[self.joystick_input()])

            # 4. Go through the output
            num_blocks = self.block_tiles_on_the_screen()
            if watch:
                print("Number of blocks = %d, score is %d" % (num_blocks, self.score))

        # 5. Return the reason for the machine stopping
        return result

    def joystick_input(self):
        "Compute the joystik input for the arcade game"

        # 1. Assume we like thing just the way they are
        result = JOYSTICK_NEUTRAL

        # 2. Only change things if we have all the information
        if self.ball_x is not None and self.paddle_x is not None:

            # 3. Move the paddle in the direction of the ball
            if self.paddle_x < self.ball_x:
                # |   P  B   |,   P < B --> move paddle to the right
                result = JOYSTICK_RIGHT
            elif self.paddle_x > self.ball_x:
                # | B    P   |,   P > B <-- move paddle to the left
                result = JOYSTICK_LEFT

        # 4. Return joystick instruction
        #print("Joystick = %d" % (result))
        return result

    def block_tiles_on_the_screen(self):
        "Process the game output to determine the number of blocks left (and other stuff)"

        # 2. Get the game output
        output = self.computer.outputs()
        # print(output)

        # 3. Loop for each triplet of output
        for indx in range(0, len(output), 3):
            tile_x = output[indx]
            tile_y = output[indx + 1]
            tile_id = output[indx + 2]
            assert (tile_id in TILEIDS) or (tile_x == -1 and tile_y == 0)

            # 4. Remember blocks and forget empty spaces (also score, ball and paddle)
            if tile_x == -1 and tile_y == 0:
                #print("Setting score to %d" % (tile_id))
                self.score = tile_id
            elif tile_id == TILEID_BLOCK:
                #print("Adding block at (%d,%d)" % (tile_x, tile_y))
                self.blocks.add((tile_x, tile_y))
            elif tile_id == TILEID_EMPTY:
                if (tile_x, tile_y) in self.blocks:
                    #print("Discarding block at (%d,%d)" % (tile_x, tile_y))
                    self.blocks.discard((tile_x, tile_y))
            elif tile_id == TILEID_BALL:
                #print("Ball at (%d,%d)" % (tile_x, tile_y))
                self.ball_x = tile_x
            elif tile_id == TILEID_PADDLE:
                #print("Paddle at (%d,%d)" % (tile_x, tile_y))
                self.paddle_x = tile_x

        # 5. Return the number of block left
        return len(self.blocks)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                       a r c a d e . p y                        end
# ======================================================================
