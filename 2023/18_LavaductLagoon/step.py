
# ======================================================================
# Lavaduct Lagoon
#   Advent of Code 2023 Day 18 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         s t e p . p y
# ======================================================================
"Step for the Advent of Code 2023 Day 18 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
ACTIONS = ['R', 'D', 'L', 'U']

# ======================================================================
#                                                                 Step
# ======================================================================


class Step(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Lavaduct Lagoon"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.action = ""
        self.meters = 0
        self.hex_color = ""

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        # 1. Precondition axioms
        assert text is not None and len(text) > 0

        # 2. Break into parts
        parts = text.split()
        assert len(parts) == 3

        # 3. Save the parts
        self.action = parts[0]
        self.meters = int(parts[1])
        self.hex_color = parts[2].replace('(', '').replace(')', '').replace('#', '')

        # 4. Post condition axioms
        assert self.action in ACTIONS
        assert 0 < self.meters < 100
        assert len(self.hex_color) == 6

    def specs(self):
        "Get the specifics for this step"

        # 1. Pretty easy for part 1
        if not self.part2:
            return self.action, self.meters, self.hex_color

        # 2. Get the distance and direction from the hex color
        action = ACTIONS[int(self.hex_color[5])]
        meters = int(self.hex_color[:5], 16)

        # 3. Return the decoded action
        return action, meters, self.hex_color

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                      s t e p . p y                     end
# ======================================================================
