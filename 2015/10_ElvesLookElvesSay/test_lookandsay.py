# ======================================================================
# Elves Look Elves Say
#   Advent of Code 2015 Day 10 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ l o o k a n d s a y . p y
# ======================================================================
"Test solver for Advent of Code 2015 day 10, Elves Look Elves Say"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_10
import lookandsay

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = ""
PART_ONE_TEXT = ""
PART_TWO_TEXT = ""

PART_ONE_RESULT = 6
PART_TWO_RESULT = 4

# ======================================================================
#                                                         TestLookandsay
# ======================================================================


class TestLookandsay(unittest.TestCase):  # pylint: disable=R0904
    "Test Lookandsay object"

    def test_empty_init(self):
        "Test the default Lookandsay creation"

        # 1. Create default Lookandsay object
        myobj = lookandsay.Lookandsay()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)

    def test_text_init(self):
        "Test the Lookandsay object creation from text"

        # 1. Create Lookandsay object from text
        myobj = lookandsay.Lookandsay(text=aoc_10.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 0)

        # 3. Check methods
        self.assertEqual(myobj.next_sequence('1'), '11')
        self.assertEqual(myobj.next_sequence('11'), '21')
        self.assertEqual(myobj.next_sequence('21'), '1211')
        self.assertEqual(myobj.next_sequence('1211'), '111221')
        self.assertEqual(myobj.next_sequence('111221'), '312211')

    def test_part_one(self):
        "Test part one example of Lookandsay object"

        # 1. Create Lookandsay object from text
        myobj = lookandsay.Lookandsay(text=aoc_10.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(times=5, verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Lookandsay object"

        # 1. Create Lookandsay object from text
        myobj = lookandsay.Lookandsay(part2=True, text=aoc_10.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(times=3, verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end               t e s t _ l o o k a n d s a y . p y              end
# ======================================================================
