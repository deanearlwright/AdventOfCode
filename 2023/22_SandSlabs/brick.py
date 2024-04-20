
# ======================================================================
# Sand Slabs
#   Advent of Code 2023 Day 22 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         b r i c k . p y
# ======================================================================
"Brick for the Advent of Code 2023 Day 22 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from collections import namedtuple
# ----------------------------------------------------------------------
#                                                                  types
# ----------------------------------------------------------------------
Position = namedtuple("Positions", "x, y, z")
Corners = namedtuple("Corners", "end0, end1")

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                  Brick
# ======================================================================


class Brick(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Sand Slabs"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.corners = None

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            ends = self.text.split('~')
            assert len(ends) == 2
            end0 = Position(*[int(i) for i in ends[0].split(",")])
            end1 = Position(*[int(i) for i in ends[1].split(",")])
            self.corners = Corners(end0, end1)

    def grid(self):
        "Return the xy grid that this brick spans"
        return [(x, y)
                for x in range(self.corners.end0.x, self.corners.end1.x + 1)
                for y in range(self.corners.end0.y, self.corners.end1.y + 1)]

    def drop(self, amount):
        "Lower the brick by the indicated amount"
        self.corners = Corners(Position(self.corners.end0.x,
                                        self.corners.end0.y,
                                        self.corners.end0.z - amount),
                               Position(self.corners.end1.x,
                                        self.corners.end1.y,
                                        self.corners.end1.z - amount))

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                      b r i c k . p y                     end
# ======================================================================
