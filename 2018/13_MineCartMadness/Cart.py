# ======================================================================
# Mine Cart Madness
#   Advent of Code 2018 Day 13 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                             c a r t . p y
# ======================================================================
"Cart for Mine Card Madness problem of day 13 of Advent of Code 2018"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

CROSSINGS = ('<', '+', '>')

# ======================================================================
#                                                                   Cart
# ======================================================================


class Cart(object):                      # pylint: disable=E0012,R0205
    """Object representing a single cart of Mine Card Madness"""

    def __init__(self, location=None, direction='^',
                        crossings=0, crashed=False,
                        space=' '):

        # 1. Set the initial state
        if not location:
            self.location = (0,0)
        else:
            self.location = location
        self.direction = direction
        self.crossings = crossings
        self.crashed = crashed
        self.space = space

    def step(self, track=None):
        "Go another step along the track"

        # 1. If we have no track, we crash
        if not track:
            self.crashed = True
            return

        # 2. If we are not on the track, we crash
        if track.location(self.location) != self.direction:
            self.crashed = True
            return

        # 3. Replace the piece of track we are on
        track.set_location(self.location, self.space)

        # 4. Determine our new location moving one step

        # 5. Get the piece of track at that location
        self.space = track.location(self.location)

        # 6. Dermine out new direction

        # 7. Put our direction on the track
        track.set_location(self.location, self.direction)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         c a r t . p y                          end
# ======================================================================
