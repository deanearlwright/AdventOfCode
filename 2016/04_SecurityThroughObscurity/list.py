# ======================================================================
# Security Through Obscurity
#   Advent of Code 2016 Day 04 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                             l i s t . p y
# ======================================================================
"A solver for the Advent of Code 2016 Day 04 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import room

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
LOOK4 = "northpole object storage"

# ======================================================================
#                                                                   List
# ======================================================================


class List(object):   # pylint: disable=R0902, R0205
    "Object for Security Through Obscurity"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.rooms = []

        # 2. If we have some text, create some rooms
        if text and len(text) > 0:
            for line in text:
                self.rooms.append(room.Room(text=line, part2=self.part2))

    def total_valid(self):
        "Return the total of the ids of the valid rooms"

        # 1. Start with nothing
        result = 0

        # 2. Loop for all of the rooms
        for here in self.rooms:

            # 3. If this is a valid room, add in the id
            if here.valid:
                result += here.id

        # 4. Return the total of the ids of valid rooms
        return result

    def find_north_pole_objects(self):
        "Return the id of the room with the north pole objects"

        # 1. Loop for all of the valid rooms
        for here in self.rooms:
            if not here.valid:
                continue

            # 2. Get the real name of the room
            real_name = here.decrypt()

            # 3. Are these the droids we are looking for
            if real_name == LOOK4:
                return here.id

        #  4. We didn't find it
        return None

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.total_valid()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.find_north_pole_objects()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                           l i s t . p y                        end
# ======================================================================
