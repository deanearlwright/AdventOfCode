
# ======================================================================
# Monkey Map
#   Advent of Code 2022 Day 22 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         y o u . p y
# ======================================================================
"You for the Advent of Code 2022 Day 22 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import board
import path

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
DELTA = {
    '>': (1, 0),
    '<': (-1, 0),
    'v': (0, 1),
    '^': (0, -1),
}

TURNS = {
    '>': {'L': '^', 'R': 'v'},
    '<': {'L': 'v', 'R': '^'},
    'v': {'L': '>', 'R': '<'},
    '^': {'L': '<', 'R': '>'},
}
LEFT_RIGHT = frozenset(["L", "R"])

FACE_TO_NUMBER = {
    '>': 0,
    'v': 1,
    '<': 2,
    '^': 3,
}

# ======================================================================
#                                                                    You
# ======================================================================


class You(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Monkey Map"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.board = None
        self.path = None
        self.loc = None
        self.facing = '>'

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text, part2)

    def _process_text(self, text, part2):
        "Assign values from text"

        # 1. Create a board with all lines except the last
        self.board = board.Board(text=text[:-1], part2=part2)

        # 2. Create the path with the last line
        self.path = path.Path(text=text[-1], part2=part2)

        # 3. Set the starting location
        self.loc = self.board.find_start()

    def one_step(self, inst):
        "Follow a single instruction"
        # print(self.loc, inst)

        # 1. Turns are done in place
        if inst in LEFT_RIGHT:
            self.facing = TURNS[self.facing][inst]
            return

        # 2. Else move forward as indicated
        for _ in range(int(inst)):

            # 3. Determine the next location
            next_loc = (self.loc[0] + DELTA[self.facing][0],
                        self.loc[1] + DELTA[self.facing][1])

            # 4. What is at that location
            there = self.board.at_loc(next_loc)

            # 5. If it is a tile, move there
            if there == board.TILE:
                self.loc = next_loc
                continue

            # 6. If it is a wall, stop
            if there == board.WALL:
                break

            # 7. We have wandered into space, find the next tile or wall
            next_loc, next_facing = self.board.warp(self.loc, self.facing)
            there = self.board.at_loc(next_loc)

            # 8. If it is a tile, move there
            if there == board.TILE:
                self.loc = next_loc
                self.facing = next_facing
                continue

            # 9. If it is a wall, stop
            if there == board.WALL:
                break

    def all_steps(self):
        "complete the steps of the path"

        # 1. Loop for all the steps
        for inst in self.path.instructions:

            # 2. Execute a single step
            # print(inst)
            self.one_step(inst)
            # print(self.loc, self.facing)

        # 3. Return the final password
        return self.final_password()

    def final_password(self):
        "Compute the final password"

        return 1000 * (self.loc[1]) + \
            4 * (self.loc[0]) + FACE_TO_NUMBER[self.facing]

    def reset(self):
        "Back to the start"
        self.facing = ">"
        self.loc = self.board.find_start()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                           y o u . p y                          end
# ======================================================================
