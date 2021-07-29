# ======================================================================
# Like a Rogue
#   Advent of Code 2016 Day 18 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                      t e s t _ r o o m . p y
# ======================================================================
"Test solver for Advent of Code 2016 day 18, Like a Rogue"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_18
import room

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
.^^.^.^^^^
"""
PART_ONE_TEXT = ""
PART_TWO_TEXT = ""

PART_ONE_RESULT = None
PART_TWO_RESULT = None

# ======================================================================
#                                                               TestRoom
# ======================================================================


class TestRoom(unittest.TestCase):  # pylint: disable=R0904
    "Test Room object"

    def test_empty_init(self):
        "Test the default Room creation"

        # 1. Create default Room object
        myobj = room.Room()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.row, None)

        # 3. Check methods
        self.assertEqual(myobj.safe(10), None)

    def test_text_init(self):
        "Test the Room object creation from text"

        # 1. Create Room object from text
        myobj = room.Room(text=aoc_18.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 1)
        self.assertNotEqual(myobj.row, None)

        # 3. Check methods
        self.assertEqual(myobj.safe(10), 38)

    def test_part_one(self):
        "Test part one example of Room object"

        # 1. Create Room object from text
        myobj = room.Room(text=aoc_18.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Room object"

        # 1. Create Room object from text
        myobj = room.Room(part2=True, text=aoc_18.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                     t e s t _ r o o m . p y                    end
# ======================================================================
