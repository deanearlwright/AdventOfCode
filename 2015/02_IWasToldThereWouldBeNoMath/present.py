
# ======================================================================
# I Was Told There Would Be No Math
#   Advent of Code 2015 Day 02 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         p r e s e n t . p y
# ======================================================================
"A solver for the Advent of Code 2015 Day 02 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                Present
# ======================================================================


class Present(object):   # pylint: disable=R0902, R0205
    "Present object for I Was Told There Would Be No Math"

    def __init__(self, length=0, width=0, height=0, text=None):

        # 1. Set the initial values
        self.length = length
        self.width = width
        self.height = height
        self.text = text

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            parts = text.split('x')
            assert len(parts) == 3
            self.length = int(parts[0])
            self.width = int(parts[1])
            self.height = int(parts[2])

    def area(self):
        "Returns the surface error"
        return 2 * self.length * self.width + \
            2 * self.width * self.height + \
            2 * self.height * self.length

    def slack(self):
        "Returns the area of the smallest side"
        sides = [self.length, self.width, self.height]
        sides.sort()
        return sides[0] * sides[1]

    def paper(self):
        "Return total paper needed for the present"
        return self.area() + self.slack()

    def wrap(self):
        "Returns the ribbon to wrap the smallest side"
        sides = [self.length, self.width, self.height]
        sides.sort()
        return 2 * sides[0] + 2 * sides[1]

    def bow(self):
        "Return the ribbon for the bow"
        return self.length * self.width * self.height

    def ribbon(self):
        "Return total ribbon needed for the present"
        return self.wrap() + self.bow()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                        p r e s e n t . p y                     end
# ======================================================================
