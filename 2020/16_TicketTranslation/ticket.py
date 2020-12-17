# ======================================================================
# Ticket Translation
#   Advent of Code 2020 Day 16 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         t i c k e t . p y
# ======================================================================
"A class for the Advent of Code 2020 Day 16 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                 Ticket
# ======================================================================


class Ticket(object):   # pylint: disable=R0902, R0205
    "Object for Ticket Translation"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.numbers = []
        self.valid = True

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.numbers = [int(_) for _ in text.split(',')]

    def __len__(self):
        return len(self.numbers)

    def __iter__(self):
        return iter(self.numbers)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         t i c k e t . p y                      end
# ======================================================================
