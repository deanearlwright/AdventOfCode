
# ======================================================================
# Hot Springs
#   Advent of Code 2023 Day 12 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         s p r i n g s . p y
# ======================================================================
"Springs for the Advent of Code 2023 Day 12 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from springrow import Springrow

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                Springs
# ======================================================================


class Springs(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Hot Springs"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.rows = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            for line in text:
                self.rows.append(Springrow(text=line, part2=part2))

    def total_arrangements(self):
        "Return the total number of possible arrangements"

        return sum(row.arrangements() for row in self.rows)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                       s p r i n g s . p y                      end
# ======================================================================
