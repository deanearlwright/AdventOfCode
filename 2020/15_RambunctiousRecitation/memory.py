# ======================================================================
# Rambunctious Recitation
#   Advent of Code 2020 Day 15 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         m e m o r y . p y
# ======================================================================
"Saves numbers for the Advent of Code 2020 Day 15 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                 Memory
# ======================================================================


class Memory(object):   # pylint: disable=R0902, R0205
    "Object for Rambunctious Recitation"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.turn = 0
        self.numbers = {}
        self.age = None
        self.text = text

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            for number in text.split(','):
                self.add(int(number))

    def add_last_spoken(self):
        "Add the last number spoken"
        self.add(self.age)

    def add(self, number):
        "Add a number to the memory, Returns previous delta"

        # 1. Increment the turn number
        self.turn += 1

        # 2. If the number is new, the age is 0
        if number not in self.numbers:
            age = 0

        # 3. Else the age is calulated from when last seen
        else:
            age = self.turn - self.numbers[number]

        # 4. Save the turn the number was last used
        self.numbers[number] = self.turn

        # 5. Save last for later
        self.age = age


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                        m e m o r y . p y                       end
# ======================================================================
