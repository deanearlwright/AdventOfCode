# ======================================================================
# Amphipod
#   Advent of Code 2021 Day 23 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         r o o m . p y
# ======================================================================
"Room for the Advent of Code 2021 Day 23 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                   Room
# ======================================================================


class Room(object):   # pylint: disable=R0902, R0205
    "Object for Amphipod"

    def __init__(self, doorway=None, homeroom=None, contents=None):

        # 1. Set the initial values
        self.doorway = 0
        self.homeroom = homeroom
        self.contents = []

        # 2. Update the values
        if doorway:
            self.doorway = doorway
        if contents:
            self.contents = contents.copy()

    def is_homey(self):
        "Is the room full of the correct amphipods?"
        return all([self.homeroom == c for c in self.contents])

    def is_my_room(self, amphipod):
        "Is this my room?"
        return self.homeroom == amphipod

    def __str__(self):
        return ''.join(self.contents)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         r o o m . p y                          end
# ======================================================================
