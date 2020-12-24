# ======================================================================
# Monster Messages
#   Advent of Code 2020 Day 19 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         r u l e . p y
# ======================================================================
"A production rule for the Advent of Code 2020 Day 19 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                   Rule
# ======================================================================


class Rule(object):   # pylint: disable=R0902, R0205
    "Object for Monster Messages"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.number = None
        self.definition = None

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            assert text.find(':') > 0
            number, definition = text.split(':')
            self.number = int(number)
            self.definition = definition.strip()

    def is_constant(self):
        "Returns True if rule is for a constant"

        return self.definition and self.definition[0] == '"'

    def letter(self):
        "Returns the letter for a constant rule"

        # 0. Precondition axiom
        assert self.is_constant()

        # 1. Return the letter
        return self.definition[1]

    def alternatives(self):
        "Returns the sub rule lists of the rule"

        # 0. Precondition axiom
        assert not self.is_constant()

        # 1. Return the sub rules
        return self.definition.split('|')


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                           r u l e . p y                        end
# ======================================================================
