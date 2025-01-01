
# ======================================================================
# Bridge Repair
#   Advent of Code 2024 Day 07 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         e q u a t i o n s . p y
# ======================================================================
"A solver for the Advent of Code 2024 Day 07 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import equation

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                              Equations
# ======================================================================


class Equations(object):   # pylint: disable=R0902, R0205
    "Object for Bridge Repair"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.equations = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        assert text is not None and len(text) > 0

        # 1. Loop for each line of text
        for line in text:

            # 2. Create an equation from the line
            an_equation = equation.Equation(text=line, part2=self.part2)

            # 3. And add it to the list
            self.equations.append(an_equation)

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. No solution if no text
        if not self.text:
            return None

        # 2. Start with nothing
        result = 0

        # 3. Loop for each equations
        for an_equation in self.equations:

            # 4. If it can be true, accumulate the test value
            if an_equation.can_be_true():
                result += an_equation.left

        # 5. Return the result of part one
        return result

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. No solution if no text
        if not self.text:
            return None

        # 2. Start with nothing
        result = 0

        # 3. Loop for each equations
        for an_equation in self.equations:

            # 4. If it can be true, accumulate the test value
            if an_equation.can_be_true_two():
                result += an_equation.left

        # 5. Return the result of part one
        return result

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                     e q u a t i o n s . p y                    end
# ======================================================================
