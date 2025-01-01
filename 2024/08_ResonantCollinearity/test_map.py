
# ======================================================================
# Resonant Collinearity
#   Advent of Code 2024 Day 08 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         t e s t _ m a p . p y
# ======================================================================
"Test solver for Advent of Code 2024 day 08, Resonant Collinearity"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_08
import map

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""
EXAMPLE_TWO = """
T....#....
...T......
.T....#...
.........#
..#.......
..........
...#......
..........
....#.....
..........
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 14
PART_TWO_RESULT = 34

# ======================================================================
#                                                                TestMap
# ======================================================================


class TestMap(unittest.TestCase):  # pylint: disable=R0904
    "Test Map object"

    def test_empty_init(self):
        "Test the default Map creation"

        # 1. Create default Map object
        myobj = map.Map()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.rows, 0)
        self.assertEqual(myobj.cols, 0)
        self.assertEqual(len(myobj.antennas), 0)
        self.assertEqual(len(myobj.frequencies), 0)
        self.assertEqual(len(myobj.antinodes), 0)

    def test_text_init(self):
        "Test the Map object creation from text"

        # 1. Create Map object from text
        myobj = map.Map(text=aoc_08.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 12)
        self.assertEqual(myobj.rows, 12)
        self.assertEqual(myobj.cols, 12)
        self.assertEqual(len(myobj.antennas), 7)
        self.assertEqual(len(myobj.frequencies), 2)
        self.assertEqual(len(myobj.antinodes), 2)
        self.assertEqual(len(myobj.antinodes["0"]), 10)
        self.assertEqual(len(myobj.antinodes["A"]), 5)

    def test_text_two(self):
        "Test the Map object creation from text for part two"

        # 1. Create Map object from text
        myobj = map.Map(text=aoc_08.from_text(EXAMPLE_TWO), part2=True)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, True)
        self.assertEqual(len(myobj.text), 10)
        self.assertEqual(myobj.rows, 10)
        self.assertEqual(myobj.cols, 10)
        self.assertEqual(len(myobj.antennas), 3)
        self.assertEqual(len(myobj.frequencies), 1)
        self.assertEqual(len(myobj.antinodes), 1)
        self.assertEqual(len(myobj.antinodes["T"]), 9)

    def test_part_one(self):
        "Test part one example of Map object"

        # 1. Create Map object from text
        text = aoc_08.from_text(PART_ONE_TEXT)
        myobj = map.Map(text=text)

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Map object"

        # 1. Create Map object from text
        text = aoc_08.from_text(PART_TWO_TEXT)
        myobj = map.Map(part2=True, text=text)

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                      t e s t _ m a p . p y                     end
# ======================================================================
