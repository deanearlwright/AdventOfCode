# ======================================================================
# Toboggan Trajectory
#   Advent of Code 2020 Day 03 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ t o b o g g a n . p y
# ======================================================================
"Test solver for Advent of Code 2020 day 03, Toboggan Trajectory"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_03
import toboggan

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
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 7
PART_TWO_RESULT = 336

# ======================================================================
#                                                           TestToboggan
# ======================================================================


class TestToboggan(unittest.TestCase):  # pylint: disable=R0904
    "Test Toboggan object"

    def test_empty_init(self):
        "Test the default Toboggan creation"

        # 1. Create default Toboggan object
        myobj = toboggan.Toboggan()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.loc, (0, 0))
        self.assertEqual(myobj.delta, (3, 1))
        self.assertEqual(myobj.trees, None)

    def test_text_init(self):
        "Test the Toboggan object creation from text"

        # 1. Create Toboggan object from text
        myobj = toboggan.Toboggan(text=aoc_03.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 11)
        self.assertEqual(myobj.loc, (0, 0))
        self.assertEqual(myobj.delta, (3, 1))
        self.assertNotEqual(myobj.trees, None)

    def test_part_one(self):
        "Test part one example of Toboggan object"

        # 1. Create Toboggan object from text
        myobj = toboggan.Toboggan(text=aoc_03.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Toboggan object"

        # 1. Create Toboggan object from text
        myobj = toboggan.Toboggan(part2=True, text=aoc_03.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ t o b o g g a n . p y                end
# ======================================================================
