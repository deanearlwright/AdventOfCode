# ======================================================================
# Matchsticks
#   Advent of Code 2015 Day 08 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         l i t e r a l s . p y
# ======================================================================
"A solver for the Advent of Code 2015 Day 08 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                               Literals
# ======================================================================


class Literals(object):   # pylint: disable=R0902, R0205
    "Object for Matchsticks"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text

    @staticmethod
    def code_size(text):
        "Return the code size"
        return len(text)

    @staticmethod
    def decoded_size(text):
        "Return the decoded size"
        return len(eval(text))

    @staticmethod
    def encoded_size(text):
        "Return the decoded size"
        return 2 + len(text.replace('\\', '\\\\').replace('"', '\\"'))

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return (sum([Literals.code_size(_) for _ in self.text])
                - sum([Literals.decoded_size(_) for _ in self.text]))

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return (sum([Literals.encoded_size(_) for _ in self.text])
                - sum([Literals.code_size(_) for _ in self.text]))


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      l i t e r a l s . p y                     end
# ======================================================================
