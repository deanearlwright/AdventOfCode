# ======================================================================
# Treetop Tree House
#   Advent of Code 2022 Day 08 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ t r e e s . p y
# ======================================================================
"Test Trees for Advent of Code 2022 day 08, Treetop Tree House"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import trees

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = [
    "30373",
    "25512",
    "65332",
    "33549",
    "35390"]

# ======================================================================
#                                                              TestTrees
# ======================================================================


class TestTrees(unittest.TestCase):  # pylint: disable=R0904
    "Test Trees object"

    def test_empty_init(self):
        "Test the default Trees creation"

        # 1. Create default Trees object
        myobj = trees.Trees()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.grid), 0)

    def test_text_init(self):
        "Test the Trees object creation from text"

        # 1. Create Trees object from text
        myobj = trees.Trees(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 5)
        self.assertEqual(len(myobj.grid), 25)
        self.assertEqual(myobj.grid[(2, 2)], 3)
        self.assertEqual(myobj.grid[(1, 3)], 3)
        self.assertEqual(myobj.grid[(2, 1)], 5)
        self.assertEqual(myobj.grid[(2, 3)], 5)

        # 3. Check methods
        self.assertEqual(myobj.is_visible(0, 0), True) # edge
        self.assertEqual(myobj.is_visible(0, 1), True) # edge
        self.assertEqual(myobj.is_visible(0, 4), True) # edge
        self.assertEqual(myobj.is_visible(1, 1), True) # The top-left 5 is visible
        self.assertEqual(myobj.is_visible(2, 1), True) # The top-middle 5 is visible
        self.assertEqual(myobj.is_visible(3, 1), False) # The top-right 1 is not visible
        self.assertEqual(myobj.is_visible(1, 2), True) # The left-middle 5 is visible
        self.assertEqual(myobj.is_visible(2, 2), False) # The The center 3 is not visible
        self.assertEqual(myobj.is_visible(3, 2), True) # The right-middle 3 is visible
        self.assertEqual(myobj.is_visible(1, 3), False) # The bottom-left 3 is not visible
        self.assertEqual(myobj.is_visible(2, 3), True) # The bottom-center 5 is visible
        self.assertEqual(myobj.is_visible(3, 3), False) # The bottom-right 4 is not visible

        self.assertEqual(myobj.count_visible(), 21)

        self.assertEqual(myobj.scenic_score(0, 0), 0) # edge
        self.assertEqual(myobj.scenic_score(0, 1), 0) # edge
        self.assertEqual(myobj.scenic_score(1, 4), 0) # edge
        self.assertEqual(myobj.scenic_score(2, 1), 4) # middle 5 in second row
        self.assertEqual(myobj.scenic_score(2, 3), 8) # middle 5 in fourth row

        self.assertEqual(myobj.highest_scenic_score(), 8)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ t r e e s . p y                   end
# ======================================================================
