# ======================================================================
# Custom Customs
#   Advent of Code 2020 Day 06 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ g r o u p s . p y
# ======================================================================
"Test solver for Advent of Code 2020 day 06, Custom Customs"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_06
import groups

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
abc

a
b
c

ab
ac

a
a
a
a

b
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 11
PART_TWO_RESULT = 6

# ======================================================================
#                                                              TestGroups
# ======================================================================


class TestGroups(unittest.TestCase):  # pylint: disable=R0904
    "Test Groups object"

    def test_empty_init(self):
        "Test the default Groups creation"

        # 1. Create default Groups object
        myobj = groups.Groups()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.groups), 0)

    def test_text_init(self):
        "Test the Groups object creation from text"

        # 1. Create Groups object from text
        myobj = groups.Groups(text=aoc_06.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 5)
        self.assertEqual(len(myobj.groups), 5)

    def test_part_one(self):
        "Test part one example of Groups object"

        # 1. Create Groups object from text
        myobj = groups.Groups(text=aoc_06.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Groups object"

        # 1. Create Groups object from text
        myobj = groups.Groups(part2=True, text=aoc_06.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ g r o u p s . p y                  end
# ======================================================================
