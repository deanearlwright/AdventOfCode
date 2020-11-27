# ======================================================================
# Not Quite Lisp
#   Advent of Code 2015 Day 01 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                           l i s p . p y
# ======================================================================
"A solver for the Advent of Code 2015 Day 01 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import collections

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                   Lisp
# ======================================================================


class Lisp(object):   # pylint: disable=R0902, R0205
    "Object for Not Quite Lisp"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.text = text[0]

    def paren_counts(self):
        "Returns count of left and right parens"

        # 1. Start with nothing
        counts = collections.Counter()

        # 2. Count the characters
        counts.update(list(self.text))

        # 3. Return the left and right counts
        return counts['('], counts[')']

    def basement(self):
        "Return the position of the character that causes Santa to enter the basement"

        # 1. Start at the ground floor
        floor = 0

        # 2. Loop for all of the actions
        for number, action in enumerate(self.text):

            # 3. Go up and down
            if action == '(':
                floor += 1
            elif action == ')':
                floor -= 1
            else:
                print("Unexpected character [%c] at position %d" % (action, number))

            # 4. Are we there yet?
            if floor == -1:
                return number + 1

        # 6. That's off
        return -1

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 1. Get the counts
        parens = self.paren_counts()

        # 1. Return the solution for part one
        return parens[0] - parens[1]

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 1. Return the solution for part two
        return self.basement()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      l i s p . p y                     end
# ======================================================================
