
# ======================================================================
# Historian Hysteria
#   Advent of Code 2024 Day 01 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ l o c a t i o n s . p y
# ======================================================================
"Test solver for Advent of Code 2024 day 01, Historian Hysteria"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_01
import locations

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
3   4
4   3
2   5
1   3
3   9
3   3"""

PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 11
PART_TWO_RESULT = 31

# ======================================================================
#                                                          TestLocations
# ======================================================================


class TestLocations(unittest.TestCase):  # pylint: disable=R0904
    "Test Locations object"

    def test_empty_init(self):
        "Test the default Locations creation"

        # 1. Create default Locations object
        myobj = locations.Locations()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.left), 0)
        self.assertEqual(len(myobj.right), 0)

    def test_text_init(self):
        "Test the Locations object creation from text"

        # 1. Create Locations object from text
        myobj = locations.Locations(text=aoc_01.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 6)
        self.assertEqual(len(myobj.left), 6)
        self.assertEqual(len(myobj.right), 6)
        self.assertEqual(myobj.left[0], 3)
        self.assertEqual(myobj.right[0], 4)

    def test_part_one(self):
        "Test part one example of Locations object"

        # 1. Create Locations object from text
        text = aoc_01.from_text(PART_ONE_TEXT)
        myobj = locations.Locations(text=text)

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Locations object"

        # 1. Create Locations object from text
        text = aoc_01.from_text(PART_TWO_TEXT)
        myobj = locations.Locations(part2=True, text=text)

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                t e s t _ l o c a t i o n s . p y               end
# ======================================================================
