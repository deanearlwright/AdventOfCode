
# ======================================================================
# Mull It Over
#   Advent of Code 2024 Day 03 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         m e m o r y . p y
# ======================================================================
"A solver for the Advent of Code 2024 Day 03 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import re

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
RE_MUL = re.compile(r"mul\(\d{1,3},\d{1,3}\)")
RE_MUL2 = re.compile(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)")

# ======================================================================
#                                                                 Memory
# ======================================================================


class Memory(object):   # pylint: disable=R0902, R0205
    "Object for Mull It Over"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.muls = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        assert text is not None and len(text) > 0

        # 1. Loop for each line of the input
        for line in text:

            # 2. Get the multiplies from the line
            if self.part2:
                muls = RE_MUL2.findall(line)
            else:
                muls = RE_MUL.findall(line)

            # 3. Add them to what we already have
            self.muls.extend(muls)

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Start with nothing
        result = 0

        # 2. Loop for all of the multiply instructions
        for mul in self.muls:

            # 3. Get the two numbers
            nums = mul.strip("mul()").split(",")

            # 4. Multiple the numbers and add to the result
            result += int(nums[0]) * int(nums[1])

        # 5. Return the solution for part one
        return result

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Start with nothing
        result = 0
        enabled = True

        # 2. Loop for every line of text
        for mul in self.muls:

            # 3. If do(). enable multiplication
            if mul.startswith("do()"):
                enabled = True
                continue

            # 4. If don't, disable multiplication
            if mul.startswith("don't()"):
                enabled = False
                continue

            # 5. If disabled, ignore line
            if not enabled:
                continue

            # 6. if mul, do it
            if mul.startswith("mul("):
                mul = RE_MUL.findall(mul)
                if len(mul) != 1:
                    continue
                nums = mul[0].strip("mul()").split(",")
                result += int(nums[0]) * int(nums[1])

        # 7. Return the solution for part two
        return result

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                        m e m o r y . p y                       end
# ======================================================================
