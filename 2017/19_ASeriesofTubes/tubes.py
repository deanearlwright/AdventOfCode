# ======================================================================
# A Series of Tubes
#   Advent of Code 2017 Day 19 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         t u b e s . p y
# ======================================================================
"A solver for tubes for Advent of Code 2017 Day 19"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
DIRECTIONS = frozenset(['<', '>', 'v', '^'])
DELTA = {
    '<': (-1, 0),
    '>': (1, 0),
    'v': (0, 1),
    '^': (0, -1)
}

LETTERS = frozenset(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
TUBES = frozenset(['|', '-'])
CORNER = frozenset(['+'])

ON_PATH = LETTERS | TUBES | CORNER

NEW_DIR = {
    '<': '^v',
    '>': '^v',
    'v': '<>',
    '^': '<>'
}

# ======================================================================
#                                                                  Tubes
# ======================================================================


class Tubes(object):   # pylint: disable=R0902, R0205
    "Object for A Series of Tubes"

    def __init__(self, steps=None, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.start = None
        self.position = None
        self.direction = None
        self.letters = []
        self.steps = 0

        # 2. Process text (if any)
        if text is not None:
            self.find_start()

    def find_start(self):
        "Find the start of the routing diagram"

        # 1. Look for a vertical line in the first row
        self.start = self.text[0].index('|')

        # 2. We start at that point on the first row, heading down
        self.position = (self.start, 0)
        self.direction = 'v'

    def next_pos(self, position, direction):
        "Get a nearby location and value, None if illegal"

        # 1. Advance to next location
        new_pos = (position[0] + DELTA[direction][0],
                   position[1] + DELTA[direction][1])

        # 2. Check if off the grid
        if new_pos[0] < 0 or new_pos[1] < 0:
            return None, None
        if new_pos[1] >= len(self.text) or new_pos[0] >= len(self.text[new_pos[1]]):
            return None, None

        # 3. Get the value at the new grid position
        here = self.text[new_pos[1]][new_pos[0]]

        # 4. Check is still on the path
        if here not in ON_PATH:
            return new_pos, None

        # 5. Return new position and what is there
        return new_pos, here

    def step(self, verbose=False):
        "Move a single step"

        # 1. Advance to next location
        new_pos, at_pos = self.next_pos(self.position, self.direction)

        # 2. Check if off the grid
        if not new_pos or not at_pos:
            return False

        # 3. If this is a letter, add it to the collection
        if at_pos in LETTERS:
            self.letters.append(at_pos)
            if verbose:
                print("Added %s at (%d,%d)" %
                      (at_pos, new_pos[0], new_pos[1]))

        # 4. If this is a corner, determine new direction
        if at_pos in CORNER:
            for new_dir in NEW_DIR[self.direction]:
                next_pos, next_pos = self.next_pos(new_pos, new_dir)
                if next_pos and next_pos:
                    break
            if verbose:
                print("Change direction from %s to %s at (%d,%d)" %
                      (self.direction, new_dir, new_pos[0], new_pos[1]))

        else:
            new_dir = self.direction

        # 5. Set the new position (and maybe a new direction)
        self.position = new_pos
        self.direction = new_dir

        # 6. Accumulate number of steps
        self.steps += 1

        # 7. Return success
        return True

    def run(self, verbose=False, limit=0):
        "Step until we can't set no more"

        # 1. Set the initial step count
        self.steps = 1

        # 2. Loop (mostly) for ever
        while True:

            # 3. Take a step, exit if we fall down
            if not self.step(verbose=verbose):
                break

            # 4. Have we gone too far?
            if self.steps > limit > 0:
                break


    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 1. Follow the path
        self.run(verbose=verbose, limit=limit)

        # 1. Return the solution for part one
        return ''.join(self.letters)


    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 1. Follow the path
        self.run(verbose=verbose, limit=limit)

        # 1. Return the solution for part two
        return self.steps

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      t u b e s . p y                     end
# ======================================================================
