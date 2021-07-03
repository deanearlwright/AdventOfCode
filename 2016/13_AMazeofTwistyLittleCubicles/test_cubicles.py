# ======================================================================
# A Maze of Twisty Little Cubicles
#   Advent of Code 2016 Day 13 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ c u b i c l e s . p y
# ======================================================================
"Test solver for Advent of Code 2016 day 13, A Maze of Twisty Little Cubicles"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_13
import cubicles

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
10
"""
PART_ONE_TEXT = """
1350
"""
PART_TWO_TEXT = """
1350
"""

PART_ONE_RESULT = 92
PART_TWO_RESULT = 124

# ======================================================================
#                                                           TestCubicles
# ======================================================================


class TestCubicles(unittest.TestCase):  # pylint: disable=R0904
    "Test Cubicles object"

    def test_empty_init(self):
        "Test the default Cubicles creation"

        # 1. Create default Cubicles object
        myobj = cubicles.Cubicles()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.maze), 1)
        self.assertEqual(myobj.number, 0)

    def test_text_init(self):
        "Test the Cubicles object creation from text"

        # 1. Create Cubicles object from text
        myobj = cubicles.Cubicles(text=aoc_13.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 1)
        self.assertEqual(len(myobj.maze), 1)
        self.assertEqual(myobj.number, 10)

        # 3. Check methods
        self.assertEqual(myobj.which(0, 0), cubicles.OPEN)
        self.assertEqual(myobj.which(1, 1), cubicles.OPEN)
        self.assertEqual(len(myobj.maze), 2)
        self.assertEqual(myobj.which(-1, 0), cubicles.WALL)
        self.assertEqual(myobj.which(12, -34), cubicles.WALL)
        self.assertEqual(len(myobj.maze), 2)
        self.assertEqual(myobj.which(2, 0), cubicles.OPEN)
        self.assertEqual(myobj.which(6, 1), cubicles.OPEN)
        self.assertEqual(myobj.which(5, 3), cubicles.OPEN)
        self.assertEqual(myobj.which(1, 6), cubicles.OPEN)
        self.assertEqual(len(myobj.maze), 6)
        self.assertEqual(myobj.which(1, 6), cubicles.OPEN)
        self.assertEqual(len(myobj.maze), 6)
        self.assertEqual(myobj.which(9, 0), cubicles.WALL)
        self.assertEqual(myobj.which(5, 1), cubicles.WALL)
        self.assertEqual(myobj.which(4, 3), cubicles.WALL)
        self.assertEqual(myobj.which(0, 6), cubicles.WALL)
        self.assertEqual(len(myobj.maze), 10)

        self.assertEqual(myobj.directions(1, 1), [(1, 2), (0, 1)])
        self.assertEqual(myobj.directions(5, 3), [])
        self.assertEqual(myobj.directions(3, 2), [(4, 2), (3, 3), (2, 2), (3, 1)])

        self.assertEqual(myobj.shortest(0, 0), 2)
        self.assertEqual(myobj.shortest(7, 4), 11)

    def test_part_one(self):
        "Test part one example of Cubicles object"

        # 1. Create Cubicles object from text
        myobj = cubicles.Cubicles(text=aoc_13.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Cubicles object"

        # 1. Create Cubicles object from text
        myobj = cubicles.Cubicles(part2=True, text=aoc_13.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ c u b i c l e s . p y                end
# ======================================================================
