# ======================================================================
# Timing is Everything
#   Advent of Code 2016 Day 15 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         d i s c s . p y
# ======================================================================
"A solver for the Advent of Code 2016 Day 15 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import re
import crt

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
RE_DISC = re.compile("Disc #[0-9]+ has ([0-9]+) positions; at time=0, it is at position ([0-9]+).")

# ======================================================================
#                                                                  Discs
# ======================================================================


class Discs(object):   # pylint: disable=R0902, R0205
    "Object for Timing is Everything"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.sizes = []
        self.positions = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            for line in text:
                match = RE_DISC.match(line)
                if match:
                    self.sizes.append(int(match.group(1)))
                    self.positions.append(int(match.group(2)))
                else:
                    print("Unable to parse %s" % line)

        # 3. For part2, and another disc
        if self.part2:
            self.sizes.append(11)
            self.positions.append(0)

    def useCRT(self):
        "Solve the puzzle using the Chineese Remainder Theorem"

        # 1. Adjust the positions
        adjusted = []
        for offset, position in enumerate(self.positions):
            adjusted.append(-position - offset)

        # 2. Use CRT
        result = crt.chinese_remainder(self.sizes, adjusted)

        # 3. Drop time is one less
        if result == 0:
            return None
        return result - 1

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.useCRT()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.useCRT()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      d i s c s . p y                     end
# ======================================================================
