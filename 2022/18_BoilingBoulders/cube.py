
# ======================================================================
# Boiling Boulders
#   Advent of Code 2022 Day 18 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         c u b e . p y
# ======================================================================
"Cube for the Advent of Code 2022 Day 18 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                   Cube
# ======================================================================


class Cube(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Boiling Boulders"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.loc = None
        self.others = set()

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            tokens = [int(x) for x in text.split(",")]
            self.loc = (tokens[0], tokens[1], tokens[2])

    @staticmethod
    def bool_to_int(a_bool):
        "Convert False to 0, True to 1"
        if a_bool:
            return 1
        return 0

    def is_connected(self, other):
        "Return true if connected to the other cube"

        # 1. Have we make the connection previously?
        if other in self.others:
            return True
        if self in other.others:
            self.others.add(other)
            return True

        # 2. Need to have two dims in common and differ only by one
        diff = sum([abs(dim_self - dim_other)
                    for dim_self, dim_other in zip(self.loc, other.loc)])
        if 1 != diff:
            return False

        # 3. Remember who your neighbors are
        self.others.add(other)
        other.others.add(self)

        # 4. We have a connection
        return True

    def unconnected_sides(self):
        "Return the number of unconnected sides"

        return 6 - len(self.others)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                          c u b e . p y                         end
# ======================================================================
