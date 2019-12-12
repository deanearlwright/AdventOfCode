# ======================================================================
# Space Police
#   Advent of Code 2019 Day 11 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                           p a n e l . p y
# ======================================================================
"Hull panel for Space Police problem for Advent of Code 2019 Day 11"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
COLOR_BLACK = 0
COLOR_WHITE = 1

COLORS = set([COLOR_BLACK, COLOR_WHITE])

COLOR_LETTERS = {COLOR_BLACK: '.',
                 COLOR_WHITE: '#'}

# ======================================================================
#                                                                  Panel
# ======================================================================


class Panel():
    """Object representing a panel on the space ship hull"""

    def __init__(self, loc=(0, 0), color=COLOR_BLACK):

        # 0. Preconditions
        assert color in COLORS

        # 1. Set the initial values
        self.loc = loc
        self.colored = color
        self.history = [color]

    def __str__(self):
        return COLOR_LETTERS[self.colored]

    def color(self):
        "Return the color of the panel"
        return self.colored

    def paint(self, color):
        "Paint the panel"

        # 0. Preconditions
        assert color in COLORS

        # 1. Set the color (which might be new or it might now)
        self.colored = color

        # 2. And record it in the history
        self.history.append(color)

    def painted(self):
        "Return True if panel has been painted"

        return len(self) > 0

    def __len__(self):
        return len(self.history) - 1

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         p a n e l . p y                        end
# ======================================================================
