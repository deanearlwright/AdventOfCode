# ======================================================================
# Rain Risk
#   Advent of Code 2020 Day 12 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ n a v i g a t i o n . p y
# ======================================================================
"Test solver for Advent of Code 2020 day 12, Rain Risk"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_12
import navigation

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
F10
N3
F7
R90
F11
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 25
PART_TWO_RESULT = 286

# ======================================================================
#                                                         TestNavigation
# ======================================================================


class TestNavigation(unittest.TestCase):  # pylint: disable=R0904
    "Test Navigation object"

    def test_empty_init(self):
        "Test the default Navigation creation"

        # 1. Create default Navigation object
        myobj = navigation.Navigation()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)

    def test_text_init(self):
        "Test the Navigation object creation from text"

        # 1. Create Navigation object from text
        myobj = navigation.Navigation(text=aoc_12.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 5)

    def test_part_one(self):
        "Test part one example of Navigation object"

        # 1. Create Navigation object from text
        myobj = navigation.Navigation(text=aoc_12.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Navigation object"

        # 1. Create Navigation object from text
        myobj = navigation.Navigation(part2=True, text=aoc_12.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end               t e s t _ n a v i g a t i o n . p y              end
# ======================================================================
