
# ======================================================================
# Monkey Math
#   Advent of Code 2022 Day 21 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         m o n k e y . p y
# ======================================================================
"Monkey for the Advent of Code 2022 Day 21 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
VARIABLE = "X"

# ======================================================================
#                                                                 Monkey
# ======================================================================


class Monkey(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Monkey Math"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.name = None
        self.yells = None
        self.op1 = None
        self.operation = None
        self.op2 = None
        self.needs = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        # 1. Split the line of test into tokens
        tokens = text.split()

        # 2. Save the name (first token minus the colon)
        self.name = tokens[0][:-1]

        # 3. If only two tokens, monkey yells a specific number
        if len(tokens) == 2:
            self.yells = int(tokens[1])

        # 4. Else the monkey performs some math operation
        else:
            self.op1 = tokens[1]
            self.operation = tokens[2]
            self.op2 = tokens[3]
            self.needs = [self.op1, self.op2]

    def do_the_math(self, value1, value2):
        "Do the indicated math"

        # 1a. Are we doing something with variables
        if isinstance(value1, str) or isinstance(value2, str):
            result = f"({value1} {self.operation} {value2})"  # infix

        # 1b. Determine the result
        elif self.operation == "+":
            result = value1 + value2
        elif self.operation == "-":
            result = value1 - value2
        elif self.operation == "*":
            result = value1 * value2
        elif self.operation == "/":
            result = value1 // value2
        else:
            print(f"Unknown operation {self.operation} for {self.name}")
            return -999999

        # 2. Save the result
        self.yells = result

        # 3. And return it
        return result

    def hears(self, what):
        "The monkey hears a value it is waiting for"

        assert what in self.needs
        # 1. No longer waiting on that monkey
        self.needs.remove(what)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                      m o n k e y . p y                     end
# ======================================================================
