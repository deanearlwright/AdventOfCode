# ======================================================================
# Binary Boarding
#   Advent of Code 2020 Day 05 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         p h o n e . p y
# ======================================================================
"A solver for the Advent of Code 2020 Day 05 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import bpass
# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                  Phone
# ======================================================================


class Phone(object):   # pylint: disable=R0902, R0205
    "Object for Binary Boarding"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.passes = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            for line in text:
                self.passes.append(bpass.Bpass(text=line, part2=part2))

    def get_highest_seat(self):
        "Get the highest seat ID"

        # 1. Get all of the seat IDs
        seats = [_.seat for _ in self.passes]

        # 2. Return the highest one
        return max(seats)

    def find_missing_seat(self):
        "Find the seat number on the lost boarding pass"

        # 1. Get all of the seat IDs
        seats = [_.seat for _ in self.passes]

        # 2. Sort them low to high
        seats.sort()

        # 3. Assumme the first one is missing
        result = seats[0]

        # 4. Loop until we find the hole
        for seat in seats:

            # 5. Do we have the seat?
            if result != seat:
                return result

            # 6. Well it could be the next one
            result = seat + 1

        # 7. What happened?
        return None

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 1. Return the solution for part one
        return self.get_highest_seat()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 1. Return the solution for part two
        return self.find_missing_seat()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         p h o n e . p y                        end
# ======================================================================
