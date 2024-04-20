
# ======================================================================
# Lavaduct Lagoon
#   Advent of Code 2023 Day 18 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                      t e s t _ l a g o o n . p y
# ======================================================================
"Test Lagoon for Advent of Code 2023 day 18, Lavaduct Lagoon"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import lagoon

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = [
    "R 6 (#70c710)",
    "D 5 (#0dc571)",
    "L 2 (#5713f0)",
    "D 2 (#d2c081)",
    "R 2 (#59c680)",
    "D 2 (#411b91)",
    "L 5 (#8ceee2)",
    "U 2 (#caa173)",
    "L 1 (#1b58a2)",
    "U 2 (#caa171)",
    "R 2 (#7807d2)",
    "U 3 (#a77fa3)",
    "L 2 (#015232)",
    "U 2 (#7a21e3)",
]
TRENCH = """#######
#.....#
###...#
..#...#
..#...#
###.###
#...#..
##..###
.#....#
.######"""

# ======================================================================
#                                                             TestLagoon
# ======================================================================


class TestLagoon(unittest.TestCase):  # pylint: disable=R0904
    "Test Lagoon object"

    def test_empty_init(self):
        "Test the default Lagoon creation"

        # 1. Create default Lagoon object
        myobj = lagoon.Lagoon()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.plan, None)
        self.assertEqual(len(myobj.trench), 0)
        self.assertEqual(len(myobj.corners), 0)

    def test_text_init(self):
        "Test the Lagoon object creation from text"

        # 1. Create Lagoon object from text
        myobj = lagoon.Lagoon(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 14)
        self.assertNotEqual(myobj.plan, None)
        self.assertEqual(len(myobj.trench), 0)
        self.assertEqual(len(myobj.corners), 0)

        # 3. Check methods
        self.assertEqual(myobj.execute_plan(), 38)
        self.assertEqual(myobj.get_dimensions(), (0, 0, 9, 6))
        self.assertEqual(str(myobj), TRENCH)
        self.assertEqual(len(myobj.corners), 15)

        self.assertEqual(myobj.row_interior(0, 0, 6), 0)
        self.assertEqual(myobj.row_interior(1, 0, 6), 5)
        self.assertEqual(myobj.row_interior(2, 0, 6), 3)
        self.assertEqual(myobj.row_interior(3, 0, 6), 3)
        self.assertEqual(myobj.row_interior(4, 0, 6), 3)
        self.assertEqual(myobj.row_interior(5, 0, 6), 1)
        self.assertEqual(myobj.row_interior(6, 0, 6), 3)
        self.assertEqual(myobj.row_interior(7, 0, 6), 2)
        # self.assertEqual(myobj.row_interior(8, 0, 6), 0)

        self.assertEqual(myobj.cubic_meters(), 62)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ l a g o o n . p y                  end
# ======================================================================
