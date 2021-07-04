# ======================================================================
# Dragon Checksum
#   Advent of Code 2016 Day 16 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ d r a g o n . p y
# ======================================================================
"Test solver for Advent of Code 2016 day 16, Dragon Checksum"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_16
import dragon

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
10000
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = ""

PART_ONE_RESULT = None
PART_TWO_RESULT = None

# ======================================================================
#                                                             TestDragon
# ======================================================================


class TestDragon(unittest.TestCase):  # pylint: disable=R0904
    "Test Dragon object"

    def test_dragon_fill(self):
        "Test the dragon_fill utility function"

        self.assertTrue(dragon.dragon_fill("1", 3), "100")
        self.assertTrue(dragon.dragon_fill("0", 3), "001")
        self.assertTrue(dragon.dragon_fill("11111", 11), "11111000000")
        self.assertTrue(dragon.dragon_fill("111100001010", 25), "1111000010100101011110000")
        self.assertTrue(dragon.dragon_fill("10000", 20), "10000011110010000111")

    def test_checksum(self):
        "Test the checksum utility function"

        self.assertTrue(dragon.checksum("110010110100"), "100")
        self.assertTrue(dragon.checksum("10000011110010000111"), "01100")

    def test_empty_init(self):
        "Test the default Dragon creation"

        # 1. Create default Dragon object
        myobj = dragon.Dragon()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.seed, "")

    def test_text_init(self):
        "Test the Dragon object creation from text"

        # 1. Create Dragon object from text
        myobj = dragon.Dragon(text=aoc_16.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 1)
        self.assertEqual(myobj.seed, "10000")

        # 3. Check methods
        self.assertEqual(myobj.fill_and_check(20), "01100")

    def test_part_one(self):
        "Test part one example of Dragon object"

        # 1. Create Dragon object from text
        myobj = dragon.Dragon(text=aoc_16.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Dragon object"

        # 1. Create Dragon object from text
        myobj = dragon.Dragon(part2=True, text=aoc_16.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ d r a g o n . p y                  end
# ======================================================================
