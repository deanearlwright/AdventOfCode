
# ======================================================================
# If You Give A Seed A Fertilizer
#   Advent of Code 2023 Day 05 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         r a n g e m a p . p y
# ======================================================================
"Rangemap for the Advent of Code 2023 Day 05 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                               Rangemap
# ======================================================================


class Rangemap(object):   # pylint: disable=R0902, R0903, R0205
    "Object for If You Give A Seed A Fertilizer"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.dest_start = 0
        self.source_start = 0
        self.range_length = 0

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        assert text is not None and len(text) > 0

        # 1. Break into three integers
        ints = [int(x) for x in text.split()]
        assert len(ints) == 3

        # 2. Make the assignments
        self.dest_start, self.source_start, self.range_length = ints
        self.dest_end = self.dest_start + self.range_length
        self.start_end = self.source_start + self.range_length

    def in_source(self, number):
        "Returns true if number is in the source range"

        return self.source_start <= number < self.start_end

    def in_dest(self, number):
        "Returns true if number is in the destination range"

        return self.dest_start <= number < self.dest_end

    def mapped(self, number):
        "Returns the source number mapped to the destination"

        # 1. If number is in source range, map it to the destination
        if self.in_source(number):
            return number + self.dest_start - self.source_start

        # 2. Else the mapped number is the source number
        return number

    def unmapped(self, number):
        "Returns the destination number mapped to the source"

        # 1. If number is in destination range, map it to the source
        if self.in_dest(number):
            return number + self.source_start - self.dest_start

        # 2. Else the mapped number is the source number
        return number

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                      r a n g e m a p . p y                     end
# ======================================================================
