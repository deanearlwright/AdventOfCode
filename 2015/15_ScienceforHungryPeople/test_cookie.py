# ======================================================================
# Science for Hungry People
#   Advent of Code 2015 Day 15 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ c o o k i e . p y
# ======================================================================
"Test solver for Advent of Code 2015 day 15, Science for Hungry People"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_15
import cookie

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 62842880
PART_TWO_RESULT = 57600000

# ======================================================================
#                                                             TestCookie
# ======================================================================


class TestCookie(unittest.TestCase):  # pylint: disable=R0904
    "Test Cookie object"

    def test_empty_init(self):
        "Test the default Cookie creation"

        # 1. Create default Cookie object
        myobj = cookie.Cookie()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.ingredients, [])

    def test_text_init(self):
        "Test the Cookie object creation from text"

        # 1. Create Cookie object from text
        myobj = cookie.Cookie(text=aoc_15.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 2)
        self.assertEqual(len(myobj.ingredients), 2)

        # 3. Check methods
        self.assertEqual(myobj.score([44, 56]), 62842880)

    def test_part_one(self):
        "Test part one example of Cookie object"

        # 1. Create Cookie object from text
        myobj = cookie.Cookie(text=aoc_15.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Cookie object"

        # 1. Create Cookie object from text
        myobj = cookie.Cookie(part2=True, text=aoc_15.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ c o o k i e . p y                  end
# ======================================================================
