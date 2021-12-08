# ======================================================================
# The Treachery of Whales
#   Advent of Code 2021 Day 07 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ c r a b s . p y
# ======================================================================
"Test solver for Advent of Code 2021 day 07, The Treachery of Whales"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_07
import crabs

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
16,1,2,0,4,2,7,1,2,14
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 37
PART_TWO_RESULT = 168

# ======================================================================
#                                                              TestCrabs
# ======================================================================


class TestCrabs(unittest.TestCase):  # pylint: disable=R0904
    "Test Crabs object"

    def test_empty_init(self):
        "Test the default Crabs creation"

        # 1. Create default Crabs object
        myobj = crabs.Crabs()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.crabs), 0)

    def test_text_init(self):
        "Test the Crabs object creation from text"

        # 1. Create Crabs object from text
        myobj = crabs.Crabs(text=aoc_07.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 1)
        self.assertEqual(len(myobj.crabs), 10)

        # 3. Check methods
        self.assertEqual(myobj.cost(16, 2), 14)

        self.assertEqual(myobj.need(2), 37)
        self.assertEqual(myobj.need(1), 41)
        self.assertEqual(myobj.need(10), 71)

        self.assertEqual(myobj.align_median(), 37)
        self.assertEqual(myobj.align_search(), 37)

    def test_text_init_two(self):
        "Test the Crabs object creation from text for part2"

        # 1. Create Crabs object from text
        myobj = crabs.Crabs(text=aoc_07.from_text(EXAMPLE_TEXT), part2=True)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, True)
        self.assertEqual(len(myobj.text), 1)
        self.assertEqual(len(myobj.crabs), 10)

        # 3. Check methods
        self.assertEqual(myobj.cost(16, 5), 66)

        self.assertEqual(myobj.need(2), 206)
        self.assertEqual(myobj.need(5), 168)

        self.assertEqual(myobj.align_median(), 206)
        self.assertEqual(myobj.align_search(), 168)

    def test_part_one(self):
        "Test part one example of Crabs object"

        # 1. Create Crabs object from text
        myobj = crabs.Crabs(text=aoc_07.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Crabs object"

        # 1. Create Crabs object from text
        myobj = crabs.Crabs(part2=True, text=aoc_07.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ c r a b s . p y                   end
# ======================================================================
