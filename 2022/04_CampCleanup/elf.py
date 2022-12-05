# ======================================================================
# Camp Cleanup
#   Advent of Code 2022 Day 04 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         e l f . p y
# ======================================================================
"Elf for the Advent of Code 2022 Day 04 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                    Elf
# ======================================================================


class Elf(object):   # pylint: disable=R0902, R0205
    "Object for Camp Cleanup"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.low = 0
        self.high = 0

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        # 1. Split the text into two parts
        parts = text.split("-")

        # 2. Save the parts
        self.low = int(parts[0])
        self.high = int(parts[1])

    def contains(self, other):
        "Does this elf's assignment contain the other's?"

        # 1. Return false if not contained
        if self.low > other.low:
            return False
        if self.high < other.high:
            return False

        # 2. It is contained
        return True

    def overlaps(self, other):
        "Does this elf's assignment overlap the other's?"

        # 1. Return false if not overlapped
        if self.high < other.low:
            return False
        if self.low > other.high:
            return False

        # 2. It is overlapped
        return True


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                           e l f . p y                          end
# ======================================================================
