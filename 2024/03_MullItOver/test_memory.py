
# ======================================================================
# Mull It Over
#   Advent of Code 2024 Day 03 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ m e m o r y . p y
# ======================================================================
"Test solver for Advent of Code 2024 day 03, Mull It Over"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_03
import memory

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = """
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""

PART_ONE_RESULT = 161
PART_TWO_RESULT = 48

# ======================================================================
#                                                             TestMemory
# ======================================================================


class TestMemory(unittest.TestCase):  # pylint: disable=R0904
    "Test Memory object"

    def test_empty_init(self):
        "Test the default Memory creation"

        # 1. Create default Memory object
        myobj = memory.Memory()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.muls), 0)

    def test_text_init(self):
        "Test the Memory object creation from text"

        # 1. Create Memory object from text
        myobj = memory.Memory(text=aoc_03.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 1)
        self.assertEqual(len(myobj.muls), 4)

    def test_part_one(self):
        "Test part one example of Memory object"

        # 1. Create Memory object from text
        text = aoc_03.from_text(PART_ONE_TEXT)
        myobj = memory.Memory(text=text)
        self.assertEqual(len(myobj.text), 1)
        self.assertEqual(len(myobj.muls), 4)

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Memory object"

        # 1. Create Memory object from text
        text = aoc_03.from_text(PART_TWO_TEXT)
        myobj = memory.Memory(part2=True, text=text)
        self.assertEqual(len(myobj.text), 1)
        self.assertEqual(len(myobj.muls), 6)

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ m e m o r y . p y                end
# ======================================================================
