# ======================================================================
# Like a GIF For Your Yard
#   Advent of Code 2015 Day 18 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ c o n w a y . p y
# ======================================================================
"Test solver for Advent of Code 2015 day 18, Like a GIF For Your Yard"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_18
import conway

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
.#.#.#
...##.
#....#
..#...
#.#..#
####..
"""
STEP_ONE = """
..##..
..##.#
...##.
......
#.....
#.##..
"""
STEP_TWO = """
..###.
......
..###.
......
.#....
.#....
"""
EXAMPLE_TWO = """
##.#.#
...##.
#....#
..#...
#.#..#
####.#
"""
TWO_STEP_ONE = """
#.##.#
####.#
...##.
......
#...#.
#.####
"""
TWO_STEP_TWO = """
#..#.#
#....#
.#.##.
...##.
.#..##
##.###
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 4
PART_TWO_RESULT = 7

# ======================================================================
#                                                             TestConway
# ======================================================================


class TestConway(unittest.TestCase):  # pylint: disable=R0904
    "Test Conway object"

    def test_empty_init(self):
        "Test the default Conway creation"

        # 1. Create default Conway object
        myobj = conway.Conway()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.grid), 0)
        self.assertEqual(myobj.size, 0)

    def test_text_init(self):
        "Test the Conway object creation from text"

        # 1. Create Conway object from text
        myobj = conway.Conway(text=aoc_18.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 6)
        self.assertEqual(len(myobj.grid), 15)
        self.assertEqual(myobj.size, 6)

        # 3. Check methods
        self.assertEqual(myobj.number_on(), 15)
        self.assertEqual(str(myobj), EXAMPLE_TEXT.strip())
        self.assertEqual(myobj.neighbors((0, 0)), 1)
        self.assertEqual(myobj.neighbors((1, 1)), 2)
        self.assertEqual(myobj.neighbors((1, 4)), 6)
        myobj.grid = myobj.next_gen()
        self.assertEqual(str(myobj), STEP_ONE.strip())
        myobj.grid = myobj.next_gen()
        self.assertEqual(str(myobj), STEP_TWO.strip())
        myobj.grid = myobj.next_gen()
        myobj.grid = myobj.next_gen()
        self.assertEqual(myobj.number_on(), 4)

    def test_text_init_two(self):
        "Test the Conway object creation from text"

        # 1. Create Conway object from text
        myobj = conway.Conway(text=aoc_18.from_text(EXAMPLE_TEXT), part2 = True)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, True)
        self.assertEqual(len(myobj.text), 6)
        self.assertEqual(len(myobj.grid), 17)
        self.assertEqual(myobj.size, 6)

        # 3. Check methods
        self.assertEqual(myobj.number_on(), 17)
        self.assertEqual(str(myobj), EXAMPLE_TWO.strip())
        self.assertEqual(myobj.neighbors((0, 0)), 1)
        self.assertEqual(myobj.neighbors((1, 1)), 3)
        self.assertEqual(myobj.neighbors((1, 4)), 6)
        myobj.grid = myobj.next_gen()
        self.assertEqual(str(myobj), TWO_STEP_ONE.strip())
        myobj.grid = myobj.next_gen()
        self.assertEqual(str(myobj), TWO_STEP_TWO.strip())
        myobj.grid = myobj.next_gen()
        myobj.grid = myobj.next_gen()
        myobj.grid = myobj.next_gen()
        self.assertEqual(myobj.number_on(), 17)

    def test_part_one(self):
        "Test part one example of Conway object"

        # 1. Create Conway object from text
        myobj = conway.Conway(text=aoc_18.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Conway object"

        # 1. Create Conway object from text
        myobj = conway.Conway(part2=True, text=aoc_18.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ c o n w a y . p y                  end
# ======================================================================
