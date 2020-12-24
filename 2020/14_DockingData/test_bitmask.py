# ======================================================================
# Docking Data
#   Advent of Code 2020 Day 14 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ b i t m a s k . p y
# ======================================================================
"Test solver for Advent of Code 2020 day 14, Docking Data"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_14
import bitmask

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
"""
EXAMPLE_TWO = """
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TWO

PART_ONE_RESULT = 165
PART_TWO_RESULT = 208

# ======================================================================
#                                                            TestBitmask
# ======================================================================


class TestBitmask(unittest.TestCase):  # pylint: disable=R0904
    "Test Bitmask object"

    def test_empty_init(self):
        "Test the default Bitmask creation"

        # 1. Create default Bitmask object
        myobj = bitmask.Bitmask()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.mask), 36)
        self.assertEqual(len(myobj.memory), 0)

    def test_text_init(self):
        "Test the Bitmask object creation from text"

        # 1. Create Bitmask object from text
        myobj = bitmask.Bitmask(text=aoc_14.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 4)
        self.assertEqual(len(myobj.mask), 36)
        self.assertEqual(len(myobj.memory), 0)

    def test_part_one(self):
        "Test part one example of Bitmask object"

        # 1. Create Bitmask object from text
        myobj = bitmask.Bitmask(text=aoc_14.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Bitmask object"

        # 1. Create Bitmask object from text
        myobj = bitmask.Bitmask(part2=True, text=aoc_14.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                  t e s t _ b i t m a s k . p y                 end
# ======================================================================
