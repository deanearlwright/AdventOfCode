
# ======================================================================
# Code Chronicle
#   Advent of Code 2024 Day 25 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ s c h e m a t i c s . p y
# ======================================================================
"Test solver for Advent of Code 2024 day 25, Code Chronicle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_25
import schematics

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = ""

PART_ONE_RESULT = 3
PART_TWO_RESULT = None

# ======================================================================
#                                                         TestSchematics
# ======================================================================


class TestSchematics(unittest.TestCase):  # pylint: disable=R0904
    "Test Schematics object"

    def test_empty_init(self):
        "Test the default Schematics creation"

        # 1. Create default Schematics object
        myobj = schematics.Schematics()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.keys), 0)
        self.assertEqual(len(myobj.locks), 0)

    def test_text_init(self):
        "Test the Schematics object creation from text"

        # 1. Create Schematics object from text
        myobj = schematics.Schematics(text=aoc_25.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 40)
        self.assertEqual(len(myobj.keys), 3)
        self.assertEqual(len(myobj.locks), 2)
        self.assertEqual(myobj.keys[0], [5, 0, 2, 1, 3])
        self.assertEqual(myobj.locks[0], [0, 5, 3, 4, 3])

        # 3. Check methods
        self.assertTrue(myobj.is_overlap([0, 5, 3, 4, 3], [5, 0, 2, 1, 3]))
        self.assertFalse(myobj.is_overlap([0, 5, 3, 4, 3], [3, 0, 2, 0, 1]))
        self.assertEqual(myobj.combinations(), 3)

    def test_part_one(self):
        "Test part one example of Schematics object"

        # 1. Create Schematics object from text
        text = aoc_25.from_text(PART_ONE_TEXT)
        myobj = schematics.Schematics(text=text)

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Schematics object"

        # 1. Create Schematics object from text
        text = aoc_25.from_text(PART_TWO_TEXT)
        myobj = schematics.Schematics(part2=True, text=text)

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end               t e s t _ s c h e m a t i c s . p y              end
# ======================================================================
