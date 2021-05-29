# ======================================================================
# Squares With Three Sides
#   Advent of Code 2016 Day 03 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ t r i a n g l e s . p y
# ======================================================================
"Test solver for Advent of Code 2016 day 03, Squares With Three Sides"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_03
import triangles

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
  5  10  25
  7   9  13
 15   4   8
"""

EXAMPLE_TWO = """
  810  679   10
  783  255  616
  545  626  626
   84  910  149
  607  425  901
  556  616  883
"""

PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TWO

PART_ONE_RESULT = 1
PART_TWO_RESULT = 5

# ======================================================================
#                                                          TestTriangles
# ======================================================================


class TestTriangles(unittest.TestCase):  # pylint: disable=R0904
    "Test Triangles object"

    def test_empty_init(self):
        "Test the default Triangles creation"

        # 1. Create default Triangles object
        myobj = triangles.Triangles()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, [])

        # 3. Check methods
        self.assertEqual(myobj.check_sides([5, 10, 25]), False)
        self.assertEqual(myobj.check_sides([10, 5, 25]), False)
        self.assertEqual(myobj.check_sides([7, 9, 13]), True)
        self.assertEqual(myobj.check_sides([9, 7, 13]), True)
        self.assertEqual(myobj.check_sides([9, 7, 13, 1]), False)
        self.assertEqual(myobj.check_sides([]), False)
        self.assertEqual(myobj.check_sides([15, 4, 8]), False)

        self.assertEqual(myobj.check_row("  5  10  25"), False)
        self.assertEqual(myobj.check_row("  7   9  13"), True)
        self.assertEqual(myobj.check_row(" 15   4   8"), False)

        self.assertEqual(myobj.check_row("810 783 545"), True)
        self.assertEqual(myobj.check_row(" 84 607 556"), True)
        self.assertEqual(myobj.check_row("679 225 626"), True)
        self.assertEqual(myobj.check_row("910 425 616"), True)
        self.assertEqual(myobj.check_row(" 10 616 626"), False)
        self.assertEqual(myobj.check_row("149 901 883"), True)

    def test_text_init(self):
        "Test the Triangles object creation from text"

        # 1. Create Triangles object from text
        myobj = triangles.Triangles(text=aoc_03.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 3)

        # 3. Check methods
        self.assertEqual(myobj.count_triangles(), 1)

    def test_part_one(self):
        "Test part one example of Triangles object"

        # 1. Create Triangles object from text
        myobj = triangles.Triangles(text=aoc_03.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Triangles object"

        # 1. Create Triangles object from text
        myobj = triangles.Triangles(part2=True, text=aoc_03.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                t e s t _ t r i a n g l e s . p y               end
# ======================================================================
