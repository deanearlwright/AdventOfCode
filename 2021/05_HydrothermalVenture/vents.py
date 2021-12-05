# ======================================================================
# Hydrothermal Venture
#   Advent of Code 2021 Day 05 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         v e n t s . p y
# ======================================================================
"A solver for the Advent of Code 2021 Day 05 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import vent

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                  Vents
# ======================================================================


class Vents(object):   # pylint: disable=R0902, R0205
    "Object for Hydrothermal Venture"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.vents = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            for line in text:
                self.vents.append(vent.Vent(text=line, part2=part2))

    def overlaps(self):
        "Return the count of overlapping lines"

        # 1. Start with nothing
        intersections = set()

        # 2. Loop for all of the vents
        for v1_index, vent_one in enumerate(self.vents):

            # 3. Loop for the remaining vents
            for v2_index in range(v1_index + 1, len(self.vents)):

                # 4. Determine their intersection
                both = vent_one.locs & self.vents[v2_index].locs
                # print(v1_index, v2_index, both)

                # 5. Accumulate the common points
                intersections |= both

        # 6. Retirn the common points
        # print(intersections)
        return intersections

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return len(self.overlaps())

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return len(self.overlaps())


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         v e n t s . p y                        end
# ======================================================================
