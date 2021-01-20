# ======================================================================
# Rambunctious Recitation
#   Advent of Code 2020 Day 15 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         g a m e . p y
# ======================================================================
"A solver for the Advent of Code 2020 Day 15 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import memory

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                   Game
# ======================================================================


class Game(object):   # pylint: disable=R0902, R0205
    "Object for Rambunctious Recitation"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.memory = memory.Memory(part2=part2)

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.memory = memory.Memory(text=text[0], part2=part2)

    def number_spoken(self, turn=2020):
        "Return the nth number spoken"
        assert turn > self.memory.turn

        # 1. Loop until we get to the specified turn
        while self.memory.turn < turn - 1:
            self.memory.add_last_spoken()

        # 2. Return the number spoken on that turn
        return self.memory.age

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 1. Return the solution for part one
        return self.number_spoken(2020)

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 1. Return the solution for part two (just like part one)
        return self.number_spoken(30000000)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                          g a m e . p y                         end
# ======================================================================
