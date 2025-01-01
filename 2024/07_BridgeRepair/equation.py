
# ======================================================================
# Bridge Repair
#   Advent of Code 2024 Day 07 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         e q u a t i o n . p y
# ======================================================================
"Equation for the Advent of Code 2024 Day 07 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                               Equation
# ======================================================================


class Equation(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Bridge Repair"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.left = 0
        self.right = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        assert text is not None and len(text) > 0

        # 1. Split left from right
        parts = text.split(":")
        assert len(parts) == 2

        # 2. Save the left side of the equation
        self.left = int(parts[0])

        # 3. Save the right side of the equation
        self.right = [int(x) for x in parts[1].split()]

    def can_be_true(self):
        "Return True if the equation can be true with + and *"

        return Equation.recursive_can_be_true(self.left, self.right)

    @staticmethod
    def recursive_can_be_true(left, right):
        "Return True if the equation can be true with + and *"

        # 1. Base cases
        if len(right) == 0:
            return False
        if len(right) == 1:
            return left == right[0]
        if left < right[0]:
            return False

        # 2. Try multiplication
        if 0 == left % right[-1]:
            if Equation.recursive_can_be_true(left // right[-1], right[:-1]):
                return True

        # 3. Try addition
        if left > right[-1]:
            if Equation.recursive_can_be_true(left - right[-1], right[:-1]):
                return True

        # 4. Well you can't say we didn't try
        return False

    def can_be_true_two(self):
        "Return True if the equation can be true with +, *, and ||"

        return Equation.recursive_can_be_true_two(self.left, self.right)

    @staticmethod
    def recursive_can_be_true_two(left, right):
        "Return True if the equation can be true with + and *"

        # 1. Base cases
        if len(right) == 0:
            return False
        if len(right) == 1:
            return left == right[0]
        if left < right[0]:
            return False

        # 2. Try multiplication
        new_right = [right[0] * right[1]]
        if new_right[0] <= left:
            if len(right) > 2:
                new_right.extend(right[2:])
            if Equation.recursive_can_be_true_two(left, new_right):
                return True

        # 3. Try addition
        new_right = [right[0] + right[1]]
        if new_right[0] <= left:
            if len(right) > 2:
                new_right.extend(right[2:])
            if Equation.recursive_can_be_true_two(left, new_right):
                return True

        # 4. Give that funky new operator a try
        new_right = [int(str(right[0]) + str(right[1]))]
        if new_right[0] <= left:
            if len(right) > 2:
                new_right.extend(right[2:])
            return Equation.recursive_can_be_true_two(left, new_right)

        # 5. Well we really tried this time
        return False

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                      e q u a t i o n . p y                     end
# ======================================================================
