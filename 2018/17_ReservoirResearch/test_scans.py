# ======================================================================
# Reservoir Research
#   Advent of Code 2018 Day 17 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ s c a n s . p y
# ======================================================================
"Test solver for Advent of Code 2018 day 17, Reservoir Research"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_17
import scans

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
x=495, y=2..7
y=7, x=495..501
x=501, y=3..7
x=498, y=2..4
x=506, y=1..2
x=498, y=10..13
x=504, y=10..13
y=13, x=498..504
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

EXAMPLE_TEXT_STR = """......+.......
............#.
.#..#.......#.
.#..#..#......
.#..#..#......
.#.....#......
.#.....#......
.#######......
..............
..............
....#.....#...
....#.....#...
....#.....#...
....#######..."""

EXAMPLE_TEXT_WATER = """......+.......
......|.....#.
.#..#||||...#.
.#..#~~#|.....
.#..#~~#|.....
.#~~~~~#|.....
.#~~~~~#|.....
.#######|.....
........|.....
...|||||||||..
...|#~~~~~#|..
...|#~~~~~#|..
...|#~~~~~#|..
...|#######|.."""

PART_ONE_RESULT = 57
PART_TWO_RESULT = 29

# ======================================================================
#                                                              TestScans
# ======================================================================


class TestScans(unittest.TestCase):  # pylint: disable=R0904
    "Test Scans object"

    def test_empty_init(self):
        "Test the default Scans creation"

        # 1. Create default Scans object
        myobj = scans.Scans()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.clay, None)
        self.assertEqual(myobj.water, None)
        self.assertEqual(str(myobj), '')

    def test_text_init(self):
        "Test the Scans object creation from text"

        # 1. Create Scans object from text
        myobj = scans.Scans(text=aoc_17.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 8)
        self.assertEqual(len(myobj.clay), 34)
        self.assertEqual(1506 in myobj.clay, True)
        self.assertEqual(1507 in myobj.clay, False)
        self.assertEqual(4499 in myobj.clay, False)
        self.assertEqual(4500 in myobj.clay, False)
        self.assertEqual(7497 in myobj.clay, True)
        self.assertEqual(7501 in myobj.clay, True)
        self.assertEqual(7502 in myobj.clay, False)
        self.assertEqual(len(myobj.water), 1)
        self.assertEqual(500 in myobj.water, True)
        self.assertEqual(len(myobj.filled), 0)
        dimensions = myobj.clay_range()
        self.assertEqual(dimensions, [495, 506, 1, 13])
        self.assertEqual(str(myobj), EXAMPLE_TEXT_STR)

        # 3. Drip, drip, drip, little April shower
        myobj.drip(14000)
        self.assertEqual(len(myobj.water), 7)
        self.assertEqual(len(myobj.filled), 0)
        myobj.drip(14000)
        self.assertEqual(len(myobj.water), 6)
        self.assertEqual(len(myobj.filled), 5)
        myobj.drip(14000)
        self.assertEqual(len(myobj.water), 5)
        self.assertEqual(len(myobj.filled), 10)
        myobj.drip(14000)
        self.assertEqual(len(myobj.water), 4)
        self.assertEqual(len(myobj.filled), 12)
        myobj.drip(14000)
        self.assertEqual(len(myobj.water), 3)
        self.assertEqual(len(myobj.filled), 14)
        myobj.drip(14000)
        self.assertEqual(len(myobj.water), 6)
        self.assertEqual(len(myobj.filled), 14)
        myobj.drip(14000)
        self.assertEqual(len(myobj.water), 16)
        self.assertEqual(len(myobj.filled), 14)
        myobj.drip(14000)
        self.assertEqual(len(myobj.water), 15)
        self.assertEqual(len(myobj.filled), 19)
        myobj.drip(14000)
        self.assertEqual(len(myobj.water), 14)
        self.assertEqual(len(myobj.filled), 24)
        myobj.drip(14000)
        self.assertEqual(len(myobj.water), 13)
        self.assertEqual(len(myobj.filled), 29)
        myobj.drip(14000)
        self.assertEqual(len(myobj.water), 21)
        self.assertEqual(len(myobj.filled), 29)
        myobj.drip(14000)
        self.assertEqual(len(myobj.water), 29)
        self.assertEqual(len(myobj.filled), 29)
        myobj.drip(14000)
        self.assertEqual(len(myobj.water), 29)
        self.assertEqual(len(myobj.filled), 29)
        self.assertEqual(str(myobj), EXAMPLE_TEXT_WATER)

    def test_part_one(self):
        "Test part one example of Scans object"

        # 1. Create Scans object from text
        myobj = scans.Scans(text=aoc_17.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False, limit=99), PART_ONE_RESULT)
        self.assertEqual(str(myobj), EXAMPLE_TEXT_WATER)

    def test_part_two(self):
        "Test part two example of Scans object"

        # 1. Create Scans object from text
        myobj = scans.Scans(part2=True, text=aoc_17.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)
        self.assertEqual(str(myobj), EXAMPLE_TEXT_WATER)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                     t e s t _ s c a n s . p y                  end
# ======================================================================
