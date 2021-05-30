# ======================================================================
# Bathroom Security
#   Advent of Code 2016 Day 02 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         k e y p a d . p y
# ======================================================================
"A solver for the Advent of Code 2016 Day 02 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
KEYPAD_ONE = "######123##456##789######"
DELTA_ONE = {
  'U': -5,
  'D': 5,
  'L': -1,
  'R': 1,
}

KEYPAD_TWO = "##########1#####234###56789###ABC#####D##########"

DELTA_TWO = {
  'U': -7,
  'D': 7,
  'L': -1,
  'R': 1,
}

# ======================================================================
#                                                                 Keypad
# ======================================================================


class Keypad(object):   # pylint: disable=R0902, R0205
    "Object for Bathroom Security"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        if part2:
            self.keypad = KEYPAD_TWO
            self.delta = DELTA_TWO
        else:
            self.keypad = KEYPAD_ONE
            self.delta = DELTA_ONE
        self.location = self.keypad.find('5')

    def at(self):
        "Return the label on the current key"
        return self.keypad[self.location]

    def can_go(self, way):
        "Returns true if you can go in that direction from here"
        return '#' != self.keypad[self.location + self.delta[way]]

    def move(self, way):
        "Change the location to after moving (if possible)"
        if self.can_go(way):
            self.location += self.delta[way]
            return True
        return False

    def one_line(self, line):
        "Execute on line of instructions and return key"

        # 1. Loop for each of the instructions
        for inst in line:

            # 2. Make the move (if we can)
            self.move(inst)

        # 3. Return the current key
        return self.at()

    def get_code(self):
        "Follow the bathroom instructions and return the code"

        # 1. Start with nothing
        result = []

        # 2. Loop for each line of the instructions
        for line in self.text:

            # 3. Add the keypad code for that line
            result.append(self.one_line(line))

        # Return the entire code
        return ''.join(result)

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.get_code()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.get_code()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                        k e y p a d . p y                       end
# ======================================================================
