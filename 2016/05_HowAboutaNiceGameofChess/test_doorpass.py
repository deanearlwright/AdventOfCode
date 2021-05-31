# ======================================================================
# How About a Nice Game of Chess
#   Advent of Code 2016 Day 05 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ d o o r p a s s . p y
# ======================================================================
"Test solver for Advent of Code 2016 day 05, How About a Nice Game of Chess"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_05
import doorpass

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
abc
"""

PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = "18f47a30"
PART_TWO_RESULT = "05ace8e3"

# ======================================================================
#                                                           TestDoorpass
# ======================================================================


class TestDoorpass(unittest.TestCase):  # pylint: disable=R0904
    "Test Doorpass object"

    def test_empty_init(self):
        "Test the default Doorpass creation"

        # 1. Create default Doorpass object
        myobj = doorpass.Doorpass()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.doorID, '')

    def test_text_init(self):
        "Test the Doorpass object creation from text"

        # 1. Create Doorpass object from text
        myobj = doorpass.Doorpass(text=aoc_05.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 1)
        self.assertEqual(myobj.doorID, "abc")

        # Check methods
        self.assertEqual(myobj.password_one(), "18f47a30")
        self.assertEqual(myobj.password_two(), "05ace8e3")

    def test_part_one(self):
        "Test part one example of Doorpass object"

        # 1. Create Doorpass object from text
        myobj = doorpass.Doorpass(text=aoc_05.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Doorpass object"

        # 1. Create Doorpass object from text
        myobj = doorpass.Doorpass(part2=True, text=aoc_05.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ d o o r p a s s . p y                end
# ======================================================================
