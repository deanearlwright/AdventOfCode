# ======================================================================
# Shuttle Search
#   Advent of Code 2020 Day 13 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                           b u s . p y
# ======================================================================
"A people mover for the Advent of Code 2020 Day 13 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                    Bus
# ======================================================================


class Bus(object):   # pylint: disable=R0902, R0205
    "Object for Shuttle Search"

    def __init__(self, bid=None, offset=0):

        # 1. Set the initial values
        self.bid = 0
        self.offset = offset

        # 2. Set bid if one is given
        if bid is not None:
            self.bid = int(bid)

    def next_depart_after(self, time):
        "Return when the next time the bus departs after specified time"
        delta = time % self.bid
        if delta == 0:
            return time
        return time + self.bid - delta


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                            b u s . p y                         end
# ======================================================================
