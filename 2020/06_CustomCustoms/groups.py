# ======================================================================
# Custom Customs
#   Advent of Code 2020 Day 06 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         g r o u p s . p y
# ======================================================================
"A solver for the Advent of Code 2020 Day 06 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import group

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                 Groups
# ======================================================================


class Groups(object):   # pylint: disable=R0902, R0205
    "Object for Custom Customs"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.groups = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            for line in text:
                self.groups.append(group.Group(text=line, part2=part2))

    def sum_yes_answers(self):
        "Sum the number of yes answers in each group"
        return sum([len(_.answers) for _ in self.groups])

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 1. Return the solution for part one
        return self.sum_yes_answers()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 1. Return the solution for part two
        return self.sum_yes_answers()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         g r o u p s . p y                      end
# ======================================================================
