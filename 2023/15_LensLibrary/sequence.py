
# ======================================================================
# Lens Library
#   Advent of Code 2023 Day 15 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         s e q u e n c e . p y
# ======================================================================
"Sequence for the Advent of Code 2023 Day 15 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from box import Box

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
REMOVE = "-=0123456789"
# ======================================================================
#                                                               Sequence
# ======================================================================


class Sequence(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Lens Library"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.steps = []
        self.boxes = [Box(number=num) for num in range(256)]

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.steps = self.text.split(",")

    @staticmethod
    def appendex1a(chars):
        "Return the hash of the characters"

        # 1. Start with nothing
        result = 0

        # 2. For each character of chars
        for char in chars:

            # 3. Determine the ASCII code for the character
            num = ord(char)

            # 4. Increase the current value by the ASCII code
            result += num

            # 5. Multiple the current value by 17
            result *= 17

            # 6. Take the remainder when divided by 256
            result = result % 256

        # 7. Return the hash of the characters
        return result

    def steps_hash(self):
        "Return the hashed initialization sequence using the HASH algorithm"

        # 1. Start with nothing
        result = 0

        # 2. Loop for all the steps in the sequence
        for step in self.steps:

            # 3. Hash the individual step
            step_hash = Sequence.appendex1a(step)

            # 4. Accumulate the result
            result += step_hash

        # 5. Return initialization sequence verification number
        return result

    def execute(self):
        "Execute the instruction steps and return the focusing power"

        # 1. Loop for all the steps
        for step in self.steps:

            # 2. Determine to which box the instruction step applies
            label = step
            for char in REMOVE:
                label = label.replace(char, '')
            bindx = Sequence.appendex1a(label)

            # 3. Execute the instruction
            self.boxes[bindx].operation(step)

        # Return the focusing power of the boxes
        return sum(abox.power() for abox in self.boxes)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                      s e q u e n c e . p y                     end
# ======================================================================
