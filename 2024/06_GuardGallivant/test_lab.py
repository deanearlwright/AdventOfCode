
# ======================================================================
# Guard Gallivant
#   Advent of Code 2024 Day 06 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ l a b . p y
# ======================================================================
"Test solver for Advent of Code 2024 day 06, Guard Gallivant"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_06
import lab

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 41
PART_TWO_RESULT = 6

# ======================================================================
#                                                                TestLab
# ======================================================================


class TestLab(unittest.TestCase):  # pylint: disable=R0904
    "Test Lab object"

    def test_empty_init(self):
        "Test the default Lab creation"

        # 1. Create default Lab object
        myobj = lab.Lab()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.obstructions), 0)
        self.assertEqual(myobj.rows, 0)
        self.assertEqual(myobj.cols, 0)
        self.assertEqual(myobj.guard, None)

    def test_text_init(self):
        "Test the Lab object creation from text"

        # 1. Create Lab object from text
        myobj = lab.Lab(text=aoc_06.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 10)
        self.assertEqual(len(myobj.obstructions), 8)
        self.assertEqual(myobj.rows, 10)
        self.assertEqual(myobj.cols, 10)
        self.assertNotEqual(myobj.guard, None)
        self.assertEqual(myobj.guard.loc, (6, 4))
        self.assertEqual(myobj.guard.max_loc, (10, 10))

        # 3. Check methods
        self.assertEqual(len(myobj.guard_tour()), 41)
        self.assertEqual(myobj.place_obstructions(), 6)

    def test_part_one(self):
        "Test part one example of Lab object"

        # 1. Create Lab object from text
        text = aoc_06.from_text(PART_ONE_TEXT)
        myobj = lab.Lab(text=text)

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Lab object"

        # 1. Create Lab object from text
        text = aoc_06.from_text(PART_TWO_TEXT)
        myobj = lab.Lab(part2=True, text=text)

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                      t e s t _ l a b . p y                     end
# ======================================================================
