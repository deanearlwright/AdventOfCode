
# ======================================================================
# Proboscidea Volcanium
#   Advent of Code 2022 Day 16 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         v a l v e . p y
# ======================================================================
"Valve for the Advent of Code 2022 Day 16 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                  Valve
# ======================================================================


class Valve(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Proboscidea Volcanium"

    def __init__(self, text=None, part2=False, number=0):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.name = None
        self.number = number
        self.rate = 0
        self.tunnels = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        # 1. Break text into tokens
        tokens = text.split()

        # 2. Set Name and flow rate
        self.name = tokens[1]
        self.rate = int(tokens[4][5:-1])

        # 3. Set the tunnels
        for tunnel in tokens[9:]:
            self.tunnels.append(tunnel.replace(",", ""))

    def info(self):
        "Return number, rate, and tunnels"
        return self.number, self.rate, self.tunnels


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         v a l v e . p y                        end
# ======================================================================
