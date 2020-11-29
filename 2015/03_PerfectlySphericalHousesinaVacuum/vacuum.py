# ======================================================================
# Perfectly Spherical Houses in a Vacuum
#   Advent of Code 2015 Day 03 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         v a c u u m . p y
# ======================================================================
"A solver for the Advent of Code 2015 Day 03 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
DELTA = {
    '^': (0, 1),
    'v': (0, -1),
    '>': (1, 0),
    '<': (-1, 0),
}

# ======================================================================
#                                                                 Vacuum
# ======================================================================


class Vacuum(object):   # pylint: disable=R0902, R0205
    "Object for Perfectly Spherical Houses in a Vacuum"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.houses = {}
        self.location = (0, 0)

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.text = text[0]

    def do_deliveries(self):
        "Deliver the presents"

        # 1. Deliver a present at the origin
        self.houses[self.location] = 1

        # 2. Loop for all the instructions
        for move in self.text:

            # 3. Adjust the location
            self.new_loc(move)

            # 4. Deliver a present here
            self.houses[self.location] = 1 + self.houses.get(self.location, 0)

    def new_loc(self, move):
        "Move according to the elf's directions"

        # 1. Get the change in location
        delta = DELTA[move]

        # 2. Update the location
        self.location = (self.location[0] + delta[0], self.location[1] + delta[1])

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 1. Follow the elf's direction and deliver presents
        self.do_deliveries()

        # 1. Return the solution for part one
        return len(self.houses)

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 1. Return the solution for part two
        return None


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      v a c u u m . p y                     end
# ======================================================================
