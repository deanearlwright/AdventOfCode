# ======================================================================
# Monitoring Station
#   Advent of Code 2019 Day 10 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                           l a s e r . p y
# ======================================================================
"Laser for Monitoring Station problem for Advent of Code 2019 Day 10"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import quadrant

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                  Laser
# ======================================================================


class Laser():   # pylint: disable=R0903
    """Object representing an asteroid shooting laser"""

    def __init__(self, center=None, text=None):

        # 1. Set the initial values
        print("laser init, center=%s" % (str(center)))
        self.quads = quadrant.Quads(center=center, text=text)

    def shoot_until(self, number=200, verbose=False):
        "Shoot a bunch of asteroids"

        # 1. Loop until we shoot the selected one
        print("shoot_until, number = %d" % (number))
        total = 0
        loc = None
        while True:

            # 2. Loop for all the quads, shooting in each
            for quad in self.quads.quads:

                # 3. Get a bead on the astorids in this quad
                for angle in quad:

                    # 4. Shoot one
                    loc = quad.shoot(angle)
                    total += 1

                    # 5. Document it (if requested)
                    if verbose:
                        print("Shot number %d took out asteroid %s" % (total, loc))

                    # 6. Did we get the one we wanted?
                    if total >= number:
                        return loc

        # 6. Return the location of the last asteroid we shot
        return loc

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                        l a s e r . p y                         end
# ======================================================================
