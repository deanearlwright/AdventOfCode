
# ======================================================================
# Plutonian Pebbles
#   Advent of Code 2024 Day 11 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         s t o n e s . p y
# ======================================================================
"A solver for the Advent of Code 2024 Day 11 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from collections import defaultdict
# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                 Stones
# ======================================================================


class Stones(object):   # pylint: disable=R0902, R0205
    "Object for Plutonian Pebbles"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.stones = []
        self.counts = defaultdict(int)

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text()

    def _process_text(self):
        "Assign values from text"

        assert self.text is not None and len(self.text) == 1

        # 1. Convert the text into stones
        self.stones = [int(x) for x in self.text[0].split()]

        # 3. Initialize the counts
        for stone in self.stones:
            self.counts[stone] += 1

    def blink(self):
        "Sets the new stones after a blink"

        # 1. Start with nothing
        result = []

        # 2. Loop for all of the existing stones
        for stone in self.stones:

            # 3. If the stone has a 0, it becomes a one
            if stone == 0:
                result.append(1)
                continue

            # 4. If the stone has a even number of digits, it is split
            digits = str(stone)
            len_digits = len(digits)
            if len_digits % 2 == 0:
                len_two = len_digits // 2
                result.append(int(digits[:len_two]))
                result.append(int(digits[len_two:]))
                continue

            # 5. Else multiple it by 2024
            result.append(stone * 2024)

        # 9. Update the stones
        self.stones = result

    def count_blink(self):
        "Return the new stones after a blink"

        # 1. Start with nothing
        result = defaultdict(int)

        # 2. Loop for all of the existing counts
        for stone, count in self.counts.items():

            # 3. If the stone has is 0, it becomes a one
            if stone == 0:
                result[1] += count
                continue

            # 4. If the stone has a even number of digits, it is split
            digits = str(stone)
            len_digits = len(digits)
            if len_digits % 2 == 0:
                len_two = len_digits // 2
                result[int(digits[:len_two])] += count
                result[int(digits[len_two:])] += count
                continue

            # 5. Else multiple it by 2024
            result[stone * 2024] += count

        # 9. Update the stones
        self.counts = result

    def blinks(self, number=25):
        "Blink multiple times"

        # 1. Loop for the given number
        for indx in range(number):
            # print(indx, len(self.stones))

            # 2. Blink once
            self.blink()

    def count_blinks(self, number=75):
        "Blink multiple times"

        # 1. Loop for the given number
        for indx in range(number):
            # print(indx, len(self.stones))

            # 2. Blink once
            self.count_blink()

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. No solution if no text
        if self.text is None:
            return None

        # 2. Return the solution for part one
        self.blinks(25)
        return len(self.stones)

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. No solution if no text
        if self.text is None:
            return None

        # 2. Return the solution for part one
        self.count_blinks(75)
        return sum(self.counts.values())

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                        s t o n e s . p y                       end
# ======================================================================
