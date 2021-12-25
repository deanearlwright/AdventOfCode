# ======================================================================
# Amphipod
#   Advent of Code 2021 Day 23 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         h a l l w a y . p y
# ======================================================================
"Hallway for the Advent of Code 2021 Day 23 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
SPACE = '.'
WALL = '#'

# ======================================================================
#                                                                Hallway
# ======================================================================


class Hallway(object):   # pylint: disable=R0902, R0205
    "Object for Amphipod"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.spaces = []
        self.doorways = []

        # 2. Process text (if any)
        if text is not None and len(text) > 3:
            self.map_hallway()

    def map_hallway(self):
        "Decode the hallway information"

        # 1. Need an list of that length
        self.spaces = list(self.text[1][1:-1])

        # 2. Where are the doors
        for index, what in enumerate(self.text[2][1:-1]):
            if what != WALL:
                self.doorways.append(index)

    def __str__(self):
        "Return a little diagram"
        return ''.join([WALL, ''.join(self.spaces), WALL])


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                       h a l l w a y . p y                      end
# ======================================================================
