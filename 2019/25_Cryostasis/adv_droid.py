# ======================================================================
# Cryostasis
#   Advent of Code 2019 Day 25 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                           a d v _ d r o i d . p y
# ======================================================================
"Adventure droid for the Cryostasis problem for AoC 2019 Day 25"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

from textwrap import wrap

import intcode

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
NL = 10

TRANSLATE = {
    'n': 'north',
    's': 'south',
    'e': 'east',
    'w': 'west',
    'i': 'inv',
    't': 'take',
    'd': 'drop',
    'q': 'quit'}

TEXT_WIDTH = 50

# ======================================================================
#                                                                  Droid
# ======================================================================


class Droid():
    """Object representing an adventure droid"""

    def __init__(self, text=None):

        # 1. Set the initial values
        self.computer = intcode.IntCode(text=text)
        self.out = None
        self.inp = None

    def interactive(self, watch=False):
        "Run the droid interactively"

        # 1. Assume that the droid will want more input
        halted = intcode.STOP_INP

        # 2. Loop while obtaining input
        while halted == intcode.STOP_INP:

            # 3. Run the droid
            halted = self.computer.run(watch=watch)

            # 4. Output anything from the droid
            self.out = self.computer.outputs()
            output = ''.join([chr(_) for _ in self.out])
            for text in output.split(chr(NL)):
                for line in wrap(text, width=TEXT_WIDTH):
                    print(line)

            # 5. Get human input
            self.inp = Droid.get_input()
            if self.inp == 'quit':
                break

            # 6. Send the input to the computer
            for inp in self.inp:
                self.computer.add_inp([ord(inp)])
            self.computer.add_inp([NL])

        # 7. Return computer status
        return halted

    @staticmethod
    def get_input():
        "Get an massage human input"

        # 1. Assume human has nothing to say
        human = ''

        # 2. Loop until we get some input
        while not human:

            # 3. Attemp to obtain some input
            human = input('--> ').strip().lower()

            # 4. Break it into words
            words = human.split()

            # 5. Expand single letter commands
            for index, word in enumerate(words):
                if word in TRANSLATE:
                    words[index] = TRANSLATE[word]

            # 6. Put the words back together
            human = ' '.join(words)

        # 7. Return the input
        return human


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                     a d v _ d r o i d . p y                    end
# ======================================================================
