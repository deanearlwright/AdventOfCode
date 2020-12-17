# ======================================================================
# Ticket Translation
#   Advent of Code 2020 Day 16 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                            r u l e . p y
# ======================================================================
"A class for the Advent of Code 2020 Day 16 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import re

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
SAMPLE = "row: 6-11 or 33-44"
RE_RULE = re.compile('([a-z ]+): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)')

# ======================================================================
#                                                                   Rule
# ======================================================================


class Rule(object):   # pylint: disable=R0902, R0205
    "Object for Rule Translation"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.name = None
        self.ranges = []
        self.position = set()

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            parts = RE_RULE.match(text)
            if parts is None:
                print('Unable to parse rule: %s' % text)
            else:
                self.name = parts[1]
                self.ranges.append((int(parts[2]), int(parts[3])))
                self.ranges.append((int(parts[4]), int(parts[5])))

    def is_valid(self, number):
        "Returns True if the number is valid for this rule"

        # 1. Loop for all of the range pairs
        for pair in self.ranges:

            # 2. If the number is in the range, return True
            if number >= pair[0] and number <= pair[1]:
                return True

        # 3. If the number matches no range, return False
        return False

    def all_valid(self, numbers):
        "Return True if all of the numbers are valid for this rule"

        # 1. Loop for all the numbers
        for number in numbers:

            # 2. If not valaid, return False
            if not self.is_valid(number):
                return False

        # 3. Return true if it made it through the gauntlet
        return True


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                            r u l e . p y                       end
# ======================================================================
