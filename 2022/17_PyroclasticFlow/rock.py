
# ======================================================================
# Pyroclastic Flow
#   Advent of Code 2022 Day 17 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         r o c k . p y
# ======================================================================
"Rock for the Advent of Code 2022 Day 17 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                   Rock
# ======================================================================


class Rock(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Pyroclastic Flow"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.type = 0
        self.width = 0
        self.height = 0
        self.shape = []
        self.loc = (0, 0)

        # 2. Process text (if any)
        if text is not None and len(text) > 0:

            # 3. Split text into tokens
            tokens = text.split(",")

            # 4. Make the assignments
            self.type = int(tokens[0])
            self.width = int(tokens[1])
            self.height = int(tokens[2])
            shape = tokens[3]

            # 5. Save the shape
            for row in range(self.height):
                self.shape.append(shape[self.width * row:self.width * (row + 1)])

    def set_loc(self, loc):
        "Set the rock at a given location (left, bottom)"
        self.loc = loc

    def go_right(self):
        "Shift the rock to the right"

        # 1. Adjust location
        self.loc = (self.loc[0] + 1, self.loc[1])

        # 2. Return the right column
        return self.loc[0] + self.width - 1

    def go_left(self):
        "Shift the rock to the right"

        # 1. Adjust location
        self.loc = (self.loc[0] - 1, self.loc[1])

        # 2. Return the left column
        return self.loc[0]

    def go_down(self):
        "Shift the rock to the bottom"

        # 1. Adjust location
        self.loc = (self.loc[0], self.loc[1] - 1)

        # 2. Return the bottom row
        return self.loc[1]

    def box(self):
        "Returns the (left, bottom) and (right, top)"

        return self.loc, (self.loc[0] + self.width - 1,
                          self.loc[1] + self.height - 1)

    def copy(self):
        "Return a clean copy of myself"

        return Rock(text=self.text, part2=self.part2)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                          r o c k . p y                         end
# ======================================================================
