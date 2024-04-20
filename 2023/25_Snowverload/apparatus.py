
# ======================================================================
# Snowverload
#   Advent of Code 2023 Day 25 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         a p p a r a t u s . p y
# ======================================================================
"Apparatus for the Advent of Code 2023 Day 25 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from components import Components
from connections import Connections

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                              Apparatus
# ======================================================================


class Apparatus(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Snowverload"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.components = None
        self.connections = None

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.components = Components(text=text, part2=part2)
            self.connections = Connections(components=self.components)

    def split(self):
        "Return the sizes of the two groups split from the graph"

        return self.connections.karger(3)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------

if __name__ == '__main__':
    pass

# ======================================================================
# end                     a p p a r a t u s . p y                    end
# ======================================================================
