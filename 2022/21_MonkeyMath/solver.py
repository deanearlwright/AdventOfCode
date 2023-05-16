
# ======================================================================
# Monkey Math
#   Advent of Code 2022 Day 21 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         s o l v e r . p y
# ======================================================================
"A solver for the Advent of Code 2022 Day 21 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import re
import monkeys

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
# (((4 + (2 * (X - 3))) / 4) == 150)
RE_EQUALITY = re.compile(r"^\((.*) (==) ([0-9]+)\)$")
RE_NUM_RIGHT = re.compile(r"^\((.*) ([+*/-]) ([0-9]+)\)$")
RE_NUM_LEFT = re.compile(r"^\(([0-9]+) ([+*/-]) (.*)\)$")

# ======================================================================
#                                                                 Solver
# ======================================================================


class Solver(object):   # pylint: disable=R0902, R0205
    "Object for Monkey Math"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.monkeys = None

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.monkeys = monkeys.Monkeys(text=text, part2=part2)

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        if self.monkeys:
            return self.monkeys.satisfy_all()
        return None

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        if self.monkeys:
            equation = self.monkeys.satisfy_all()
            return Solver.solve_for_x(equation)
        return None

    @staticmethod
    def solve_for_x(equation):
        "Solve a monkey equation ala (((4 + (2 * (X - 3))) / 4) == 150)"

        # 1. Split out the equality
        equation, operator, right = Solver.split_equation(equation)
        if operator != "==":
            print("Equation not equality")
            return None
        if not right.isdigit():
            print("Right side of equality not numberic")
        result = int(right)

        # 2. Loop until we are just left with X the unknown
        while equation != "X":

            # 3. Divide the equation into left operator right
            left, operator, right = Solver.split_equation(equation)

            # 4. Execute the operation
            if left.isdigit():
                result = Solver.execute(result, operator, left, True)
                equation = right
            else:
                result = Solver.execute(result, operator, right, False)
                equation = left

        # 5, Return the result
        return result

    @staticmethod
    def split_equation(equation):
        "Split the equation into left operator right"

        # 1. Try equality
        match = RE_EQUALITY.match(equation)
        if match:
            return match.group(1, 2, 3)

        # 2. Try number on right
        match = RE_NUM_RIGHT.match(equation)
        if match:
            return match.group(1, 2, 3)

        # 3. Try number on left
        match = RE_NUM_LEFT.match(equation)
        if match:
            return match.group(1, 2, 3)

        # 4. What??
        print(f"Unable to match equation '{equation}'")
        return "X", "?", "X"

    @staticmethod
    def execute(result, operation, svalue, x_on_right):
        "Reverse the operaton on the result"

        # 1. Check the operation
        if operation == "?":
            print("Unknown operation")
            return result

        # 2. Check the value
        if not svalue.isdigit():
            print(f"value ({svalue}) is not numeric")
            return result
        value = int(svalue)

        # 3. Reverse the operation
        if operation == "-":
            if x_on_right:
                result = value - result
            else:
                result += value
        elif operation == "+":
            result -= value
        elif operation == "/":
            if x_on_right:
                result = value / result
            else:
                result *= value
        elif operation == "*":
            result /= value
        else:
            print(f"Unexpected operation ({operation})")

        # 4. Check for integer
        if int(result) != result:
            print(f"Non-integer result after {operation} {value}")

        # 5. Return the updated result
        return int(result)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                      s o l v e r . p y                     end
# ======================================================================
