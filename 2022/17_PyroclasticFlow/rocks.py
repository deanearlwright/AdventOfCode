
# ======================================================================
# Pyroclastic Flow
#   Advent of Code 2022 Day 17 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         r o c k s . p y
# ======================================================================
"Rocks for the Advent of Code 2022 Day 17 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import rock

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
ROCKS = [
    "1,4,1,####",
    "2,3,3,.#.###.#.",
    "3,3,3,..#..####",
    "4,1,4,####",
    "5,2,2,####"
]

# ======================================================================
#                                                                  Rocks
# ======================================================================


class Rocks(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Pyroclastic Flow"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.next = 0
        self.rocks = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        # 1. Loop for the lines of text
        for line in text:

            # 2. Create a rock
            a_rock = rock.Rock(text=line, part2=self.part2)

            # 3. Add the rock
            self.rocks.append(a_rock)

    def next_rock(self):
        "Return the next rock to fall"

        # 1. Make a copy of the rock
        a_rock = self.rocks[self.next].copy()

        # 2. Increment the next counter
        self.next = (self.next + 1) % len(self.rocks)

        # 3. Return the falling rock
        return a_rock


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         r o c k s . p y                        end
# ======================================================================
