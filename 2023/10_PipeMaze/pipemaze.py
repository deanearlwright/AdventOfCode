
# ======================================================================
# Pipe Maze
#   Advent of Code 2023 Day 10 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         p i p e m a z e . p y
# ======================================================================
"Pipemaze for the Advent of Code 2023 Day 10 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import re

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
NORTH = (-1, 0)
SOUTH = (1, 0)
EAST = (0, 1)
WEST = (0, -1)
NONE = (0, 0)
START = 'S'
GROUND = '.'
PIPE = '|'

TURNS = {
    NORTH: {
        '|': NORTH,
        '-': NONE,
        'L': NONE,
        'J': NONE,
        '7': WEST,
        'F': EAST,
        '.': NONE,
        'S': NONE,
    },
    SOUTH: {
        '|': SOUTH,
        '-': NONE,
        'L': EAST,
        'J': WEST,
        '7': NONE,
        'F': NONE,
        '.': NONE,
        'S': NONE,
    },
    EAST: {
        '|': NONE,
        '-': EAST,
        'L': NONE,
        'J': NORTH,
        '7': SOUTH,
        'F': NONE,
        '.': NONE,
        'S': NONE,
    },
    WEST: {
        '|': NONE,
        '-': WEST,
        'L': NORTH,
        'J': NONE,
        '7': NONE,
        'F': SOUTH,
        '.': NONE,
        'S': NONE,
    },
}

RE_TO_BLANK = re.compile(r"F-*7|L-*J") # U bends
RE_TO_PIPE = re.compile(r"F-*J|L-*7")  # Kind of pipe -- just shifty

# ======================================================================
#                                                               Pipemaze
# ======================================================================


class Pipemaze(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Pipe Maze"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.start = None

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        # 0. Precondition axioms
        assert text is not None and len(text) > 0

        # 1. Find the start
        for rindx, row in enumerate(text):
            sindx = row.find(START)
            if sindx != -1:
                self.start = (rindx, sindx)
                break

    def step(self, location, direction):
        "Return the new location and the new direction"

        # 1. Determine the new location
        new_loc = (location[0] + direction[0], location[1] + direction[1])

        # 2. Determine the pipe at that location
        new_pipe = self.text[new_loc[0]][new_loc[1]]

        # 3. Determine the new direction
        new_direction = TURNS[direction][new_pipe]

        # 4. Return the new direction and location
        return new_loc, new_direction

    def furthest(self):
        "Return the furthest distance from the starting position"

        # 1. Start at the start going in different directions
        animals = [(self.start, SOUTH), (self.start, EAST)]

        # 2. Advance both one step
        animals = [self.step(*animals[0]), self.step(*animals[1])]
        steps = 1

        # 3. Loop until they reach the same location
        while animals[0][0] != animals[1][0]:

            # 4. Advance them both
            animals = [self.step(*animals[0]), self.step(*animals[1])]

            # 5. And increment the step count
            steps += 1

        # 6. Return the furthest distance
        return steps

    def loop_locations(self):
        "Return the locations that are part of the loop"

        # 1. Start at the start and record the location
        animal = (self.start, SOUTH)
        result = set([animal[0]])

        # 2. Advance both one step and record the location
        animal = self.step(*animal)
        result.add(animal[0])

        # 3. Loop until it gets back to the start
        while animal[0] != self.start:

            # 4. Advance one step
            animal = self.step(*animal)

            # 5. And record the pipe segment location
            result.add(animal[0])

        # 6. Return the locations of the pipes in the loop
        return result

    def set_to_ground(self, loop_locs):
        "Turn the now loop squares to ground"

        # 1. Loop for the rows
        for rindx, row in enumerate(self.text):
            row = list(row)

            # 2. Loop for all the columns
            for cindx, _ in enumerate(row):

                # 3. If this square isn't in the loop change it to ground(.)
                if (rindx, cindx) not in loop_locs:
                    row[cindx] = GROUND

            # 4. Update the row
            self.text[rindx] = "".join(row)

    def find_inside(self):
        "Return the count of the inside squares - thanks to ProfONeil's perl regex"

        # 1. Find the squares of the loop pipe
        keep = self.loop_locations()

        # 2. Set the other squares to ground
        self.set_to_ground(keep)

        # 3. Start with nothing
        result = 0

        # 4. Loop for all the rows
        for row in self.text:

            # 5. Get count of the inside squares in this row
            knt = Pipemaze.find_inside_row(row)

            # 6. Update the total count
            result += knt

        # 7. Return the count of inside squares
        return result

    @staticmethod
    def find_inside_row(row):
        "Return the number of inside squares for this row"

        # 1. Use regexs to simplify the row (U bends and offset pipes)
        row = RE_TO_BLANK.sub("", row)
        row = RE_TO_PIPE.sub(PIPE, row)

        # 2. Start with none
        result = 0
        parity = 0

        # 3. Loop for all the remaining squares in the row
        for square in row:

            # 4. If it is a pipe, increment parity
            if square == PIPE:
                parity += 1

            # 5. Else if it is ground, inside if odd parity
            elif square == GROUND:
                if parity % 2 == 1:
                    result += 1

        # 6. Return result
        return result

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                      p i p e m a z e . p y                     end
# ======================================================================
