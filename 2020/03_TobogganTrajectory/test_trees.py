# ======================================================================
# Toboggan Trajectory
#   Advent of Code 2020 Day 03 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ t r e e s . p y
# ======================================================================
"Test solver for Advent of Code 2020 day 03, Toboggan Trajectory"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_03
import trees

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
"""

# ======================================================================
#                                                              TestTrees
# ======================================================================


class TestTrees(unittest.TestCase):  # pylint: disable=R0904
    "Test Map object"

    def test_empty_init(self):
        "Test the default Trees creation"

        # 1. Create default Map object
        myobj = trees.Trees()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.trees, None)
        self.assertEqual(myobj.rows, 0)
        self.assertEqual(myobj.cols, 0)

    def test_text_init(self):
        "Test the Trees object creation from text"

        # 1. Create Map object from text
        myobj = trees.Trees(text=aoc_03.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 11)
        self.assertEqual(len(myobj.trees), 11)
        self.assertEqual(myobj.rows, 11)
        self.assertEqual(myobj.cols, 11)

        # 3. Test methods
        self.assertEqual(myobj.is_tree((0, 0)), False)
        self.assertEqual(myobj.is_tree((1, 0)), False)
        self.assertEqual(myobj.is_tree((2, 0)), True)
        self.assertEqual(myobj.is_tree((3, 1)), False)
        self.assertEqual(myobj.is_tree((6, 2)), True)
        self.assertEqual(myobj.is_tree((9, 3)), False)
        self.assertEqual(myobj.is_tree((12, 4)), True)
        self.assertEqual(myobj.is_tree((15, 5)), True)
        self.assertEqual(myobj.is_tree((18, 6)), False)
        self.assertEqual(myobj.is_tree((21, 7)), True)
        self.assertEqual(myobj.is_tree((24, 8)), True)
        self.assertEqual(myobj.is_tree((27, 9)), True)
        self.assertEqual(myobj.is_tree((30, 10)), True)
        self.assertEqual(myobj.is_tree((33, 11)), False)
        self.assertEqual(myobj.is_tree((36, 12)), False)

        self.assertEqual(myobj.is_last((0, 0)), False)
        self.assertEqual(myobj.is_last((9, 3)), False)
        self.assertEqual(myobj.is_last((27, 9)), False)
        self.assertEqual(myobj.is_last((30, 10)), True)
        self.assertEqual(myobj.is_last((33, 11)), True)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ t r e e s . p y                   end
# ======================================================================
