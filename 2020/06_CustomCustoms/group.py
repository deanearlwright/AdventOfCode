# ======================================================================
# Custom Customs
#   Advent of Code 2020 Day 06 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                          g r o u p . p y
# ======================================================================
"A solver for the Advent of Code 2020 Day 06 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                  Group
# ======================================================================


class Group(object):   # pylint: disable=R0902, R0205
    "Object for Custom Customs"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.answers = set()

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            persons = text.split(' ')
            self.answers = set(persons[0])
            for person in persons[1:]:
                answers = set(person)
                if part2:
                    self.answers &= answers
                else:
                    self.answers |= answers


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                          g r o u p . p y                       end
# ======================================================================
