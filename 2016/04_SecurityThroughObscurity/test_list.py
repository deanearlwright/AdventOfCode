# ======================================================================
# Security Through Obscurity
#   Advent of Code 2016 Day 04 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                        t e s t _ l i s t . p y
# ======================================================================
"Test solver for Advent of Code 2016 day 04, Security Through Obscurity"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_04
import list

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
aaaaa-bbb-z-y-x-123[abxyz]
a-b-c-d-e-f-g-h-987[abcde]
not-a-real-room-404[oarel]
totally-real-room-200[decoy]
"""

PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = ""

PART_ONE_RESULT = 1514
PART_TWO_RESULT = None

# ======================================================================
#                                                               TestList
# ======================================================================


class TestList(unittest.TestCase):  # pylint: disable=R0904
    "Test List object"

    def test_empty_init(self):
        "Test the default List creation"

        # 1. Create default List object
        myobj = list.List()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)

        # 3. Test methods
        self.assertEqual(myobj.total_valid(), 0)

    def test_text_init(self):
        "Test the List object creation from text"

        # 1. Create List object from text
        myobj = list.List(text=aoc_04.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 4)

        # 3. Test methods
        self.assertEqual(myobj.total_valid(), 1514)

    def test_part_one(self):
        "Test part one example of List object"

        # 1. Create List object from text
        myobj = list.List(text=aoc_04.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of List object"

        # 1. Create List object from text
        myobj = list.List(part2=True, text=aoc_04.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      t e s t _ l i s t . p y                   end
# ======================================================================
