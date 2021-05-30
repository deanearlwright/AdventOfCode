# ======================================================================
# No Time for a Taxicab
#   Advent of Code 2016 Day 01 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         t a x i c a b . p y
# ======================================================================
"A solver for the Advent of Code 2016 Day 01 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
DELTA = {
  'N': [0, 1],
  'S': [0, -1],
  'E': [1, 0],
  'W': [-1, 0],
}

TURNS = {
  'N': {'L': 'W', 'R': 'E'},
  'S': {'L': 'E', 'R': 'W'},
  'E': {'L': 'N', 'R': 'S'},
  'W': {'L': 'S', 'R': 'N'},
}

# ======================================================================
#                                                                Taxicab
# ======================================================================


class Taxicab(object):   # pylint: disable=R0902, R0205
    "Object for No Time for a Taxicab"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.instructions = []
        self.location = [0, 0]
        self.facing = 'N'

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        assert text is not None and len(text) > 0

        self.instructions = text[0].split(', ')

    def from_start(self):
        "Returns the taxicab distance from the start"

        # print(self.location)
        return abs(self.location[0]) + abs(self.location[1])

    def follow_instructions(self):
        "Follow the instructions"

        # 1. Loop for all of the instructions
        for inst in self.instructions:

            # 2. Execute a single direction
            self.execute_instruction(inst)

    def decode_instruction(self, inst):
        "Determine the new facing and distance"

        # 1. Break up instruction into turn and distance
        turn = inst[0]
        distance = int(inst[1:])

        # 2. Determine the new facing
        facing = TURNS[self.facing][turn]

        # 3 Return the new facing and distance
        return (facing, distance)

    def execute_instruction(self, inst):
        "Execute a single instruction"

        # 1. Get the new facing and distance
        facing, distance = self.decode_instruction(inst)

        # 2. Set the new facing
        self.facing = facing

        # 3. Move forward
        self.location[0] += distance * DELTA[facing][0]
        self.location[1] += distance * DELTA[facing][1]

    def find_hq(self):
        # Find the Easter Bunny HQ
        # which is actually at the first location you visit twice

        # 1. Haven't been anywhere yet
        visited = set()

        # 2. Loop for all of the instructions
        for inst in self.instructions:

            # 3. Get the new facing and distance
            facing, distance = self.decode_instruction(inst)

            # 4. Set the new facing
            self.facing = facing

            # 5. Got the distance blaock by block
            for _ in range(distance):

                # 6. Advance to the next street corner
                self.location[0] += DELTA[facing][0]
                self.location[1] += DELTA[facing][1]

                # 7. Have we been here before?
                loc = self.location[1] * 10000 + self.location[0]
                if loc in visited:

                    # 8. yes --> Found the HQ
                    return

                # 9. no --> remember that we were here and move on
                visited.add(loc)

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        self.follow_instructions()
        return self.from_start()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        self.find_hq()
        return self.from_start()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                       t a x i c a b . p y                      end
# ======================================================================
