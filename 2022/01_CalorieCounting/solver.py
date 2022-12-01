# ======================================================================
# Calorie Counting
#   Advent of Code 2022 Day 01 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         s o l v e r . p y
# ======================================================================
"A solver for the Advent of Code 2022 Day 01 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                  Solver
# ======================================================================


class Solver(object):   # pylint: disable=R0902, R0205
    "Object for Calorie Counting"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.most = 0
        self.each = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        # 1. Start with nothing
        cal = 0

        # 2. Loop for all the lines of code
        for line in text:

            # 3. If blank line, start at new elf
            if len(line) == 0:
                if cal > self.most:
                    self.most = cal
                if cal > 0:
                    self.each.append(cal)
                cal = 0
                continue

            # 4. Else add it to the total
            cal = cal + int(line)

        # 5.
        if cal > self.most:
            self.most = cal
        if cal > 0:
            self.each.append(cal)

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.most

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        sss = sorted(self.each)

        return sss[-1] + sss[-2] + sss[-3]


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      s o l v e r . p y                     end
# ======================================================================
