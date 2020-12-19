# ======================================================================
# Operation Order
#   Advent of Code 2020 Day 18 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         h o m e w o r k . p y
# ======================================================================
"A solver for the Advent of Code 2020 Day 18 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import expression

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                               Homework
# ======================================================================


class Homework(object):   # pylint: disable=R0902, R0205
    "Object for Operation Order"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.expressions = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            for line in text:
                self.expressions.append(expression.Expression(text=line, part2=part2))

    def evaluate_all(self):
        "Returns the sum of evaluating all of the expressions"

        # 1. Start with nothing
        result = 0

        # 2. Loop for all of the expressions
        for exp in self.expressions:

            # 3. Evaluate the expression
            value = exp.evaluate()
            # if self.part2:
            #    print('%d = %s' % (value, exp.tokens))

            # 4. Accumulate the value of the expressions
            result += value

        # 5. Return the sum of the expressions
        return result

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 1. Return the solution for part one
        return self.evaluate_all()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 1. Return the solution for part two
        return self.evaluate_all()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      h o m e w o r k . p y                     end
# ======================================================================
