
# ======================================================================
# IfYouGiveASeedAFertilizer
#   Advent of Code 2023 Day 05 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         m u l t i r a n g e . p y
# ======================================================================
"Multirange for the Advent of Code 2023 Day 05 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                             Multirange
# ======================================================================


class Multirange(object):   # pylint: disable=R0902, R0903, R0205
    "Object for IfYouGiveASeedAFertilizer"

    def __init__(self, name=None, ranges=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.name = name
        self.ranges = ranges

    def forward_map(self, number):
        "Returns updated number based on the mapping"

        # 1. Loop for all the mappings
        for one_range in self.ranges:

            # 2. If the number is in the range, return the mapped number
            if one_range.in_source(number):
                return one_range.mapped(number)

        # 3. There was no range mapping applicible, just return the number
        return number

    def reverse_map(self, number):
        "Returns updated dest to source number"

        # 1. Loop for all the mappings
        for one_range in self.ranges:

            # 2. If the number is in the range, return the mapped number
            if one_range.in_dest(number):
                return one_range.unmapped(number)

        # 3. There was no range mapping applicible, just return the number
        return number


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    m u l t i r a n g e . p y                   end
# ======================================================================
