# ======================================================================
# The Ideal Stocking Stuffer
#   Advent of Code 2015 Day 04 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ m i n e r . p y
# ======================================================================
"Test solver for Advent of Code 2015 day 04, The Ideal Stocking Stuffer"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_04
import miner

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
abcdef
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 609043
PART_TWO_RESULT = 6742839

# ======================================================================
#                                                              TestMiner
# ======================================================================


class TestMiner(unittest.TestCase):  # pylint: disable=R0904
    "Test Miner object"

    def test_empty_init(self):
        "Test the default Miner creation"

        # 1. Create default Miner object
        myobj = miner.Miner()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)

    def test_text_init(self):
        "Test the Miner object creation from text"

        # 1. Create Miner object from text
        myobj = miner.Miner(text=aoc_04.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 1)

        # 3. Check methods
        self.assertTrue(myobj.md5_number(609043).startswith('000001dbbfa'))

    def test_part_one(self):
        "Test part one example of Miner object"

        # 1. Create Miner object from text
        myobj = miner.Miner(text=aoc_04.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Miner object"

        # 1. Create Miner object from text
        myobj = miner.Miner(part2=True, text=aoc_04.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ m i n e r . p y                   end
# ======================================================================
