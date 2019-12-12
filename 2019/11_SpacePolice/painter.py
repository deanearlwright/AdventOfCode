# ======================================================================
# Space Police
#   Advent of Code 2019 Day 10 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                           p a i n t e r . p y
# ======================================================================
"Hull painter for Space Police problem for Advent of Code 2019 Day 11"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import intcode

import hull

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
FACE_UP = '^'
FACE_LEFT = '<'
FACE_RIGHT = '>'
FACE_DOWN = 'v'

TURN_LEFT = 0
TURN_RIGHT = 1

FACE_TURN = {(FACE_UP, TURN_LEFT): FACE_LEFT,
             (FACE_UP, TURN_RIGHT): FACE_RIGHT,
             (FACE_LEFT, TURN_LEFT): FACE_DOWN,
             (FACE_LEFT, TURN_RIGHT): FACE_UP,
             (FACE_RIGHT, TURN_LEFT): FACE_UP,
             (FACE_RIGHT, TURN_RIGHT): FACE_DOWN,
             (FACE_DOWN, TURN_LEFT): FACE_RIGHT,
             (FACE_DOWN, TURN_RIGHT): FACE_LEFT}

FACE_MOVE = {FACE_UP: (1, 0),
             FACE_DOWN: (-1, 0),
             FACE_LEFT: (0, -1),
             FACE_RIGHT: (0, 1)}

# ======================================================================
#                                                                Painter
# ======================================================================


class Painter():
    """Object representing an ship's hull painter"""

    def __init__(self, text=None, white=False):

        # 1. Set the initial values
        self.loc = (0, 0)
        self.facing = FACE_UP
        self.computer = intcode.IntCode(text=text)

        # 2. If we want to start on a white panel, paint it white
        if white:
            self.hull = hull.Hull(white=self.loc)
        else:
            self.hull = hull.Hull()


    def __str__(self):
        return str(self.hull)

    def run(self, watch=False):
        "Run the painter until it stops, use panel colors for input"

        # 1. Assume the computer wants input
        result = intcode.STOP_INP

        # 2. Run while the computer wants input
        while result == intcode.STOP_INP:

            # 3. Run the computer until it stops
            result = self.computer.run(watch=watch, inp=[self.hull.color(self.loc)])

            # 4. If still looking for input, get and execute the output
            if result == intcode.STOP_INP:

                # 5. Ouput is color to paint and which way to turn
                color, turn = self.computer.outputs()

                # 6. Paint the panel at this location
                self.hull.paint(self.loc, color)

                # 7. Turn the painter
                self.facing = FACE_TURN[(self.facing, turn)]

                # 8. Move forward one space
                self.loc = (self.loc[0] + FACE_MOVE[self.facing][0],
                            self.loc[1] + FACE_MOVE[self.facing][1])

        # 9. Return the reason for the machine stopping
        return result

    def at_least_once(self):
        "Return the number of panels painted at least once"

        return self.hull.at_least_once()

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      p a i n t e r . p y                       end
# ======================================================================
