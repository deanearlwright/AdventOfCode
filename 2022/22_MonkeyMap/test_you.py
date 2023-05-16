
# ======================================================================
# Monkey Map
#   Advent of Code 2022 Day 22 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                       t e s t _ y o u . p y
# ======================================================================
"Test You for Advent of Code 2022 day 22, Monkey Map"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_22
import you

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5
"""

# ======================================================================
#                                                                TestYou
# ======================================================================
# pylint: disable=R0904, R0915


class TestYou(unittest.TestCase):
    "Test You object"

    def test_empty_init(self):
        "Test the default You creation"

        # 1. Create default You object
        myobj = you.You()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.board, None)
        self.assertEqual(myobj.path, None)
        self.assertEqual(myobj.loc, None)
        self.assertEqual(myobj.facing, '>')

    def test_text_init(self):
        "Test the You object creation from text"

        # 1. Create You object from text
        myobj = you.You(text=aoc_22.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 13)
        self.assertNotEqual(myobj.board, None)
        self.assertNotEqual(myobj.path, None)
        self.assertEqual(myobj.loc, (9, 1))
        self.assertEqual(myobj.facing, '>')

        myobj.one_step("10")
        self.assertEqual(myobj.loc, (11, 1))
        self.assertEqual(myobj.facing, '>')
        myobj.one_step("R")
        self.assertEqual(myobj.loc, (11, 1))
        self.assertEqual(myobj.facing, 'v')
        myobj.one_step("5")
        self.assertEqual(myobj.loc, (11, 6))
        self.assertEqual(myobj.facing, 'v')
        myobj.one_step("L")
        self.assertEqual(myobj.loc, (11, 6))
        self.assertEqual(myobj.facing, '>')
        myobj.one_step("5")
        self.assertEqual(myobj.loc, (4, 6))
        self.assertEqual(myobj.facing, '>')
        myobj.one_step("R")
        self.assertEqual(myobj.loc, (4, 6))
        self.assertEqual(myobj.facing, 'v')
        myobj.one_step("10")
        self.assertEqual(myobj.loc, (4, 8))
        self.assertEqual(myobj.facing, 'v')
        myobj.one_step("L")
        self.assertEqual(myobj.loc, (4, 8))
        self.assertEqual(myobj.facing, '>')
        myobj.one_step("4")
        self.assertEqual(myobj.loc, (8, 8))
        self.assertEqual(myobj.facing, '>')
        myobj.one_step("R")
        self.assertEqual(myobj.loc, (8, 8))
        self.assertEqual(myobj.facing, 'v')
        myobj.one_step("5")
        self.assertEqual(myobj.loc, (8, 6))
        self.assertEqual(myobj.facing, 'v')
        myobj.one_step("L")
        self.assertEqual(myobj.loc, (8, 6))
        self.assertEqual(myobj.facing, '>')
        myobj.one_step("5")
        self.assertEqual(myobj.loc, (8, 6))
        self.assertEqual(myobj.facing, '>')

        myobj.reset()
        self.assertEqual(myobj.loc, (9, 1))
        self.assertEqual(myobj.facing, '>')
        self.assertEqual(myobj.all_steps(), 6032)

    def test_two_init(self):
        "Test the You object creation from text for part twi"

        # 1. Create You object from text
        myobj = you.You(text=aoc_22.from_text(EXAMPLE_TEXT), part2=True)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, True)
        self.assertEqual(len(myobj.text), 13)
        self.assertNotEqual(myobj.board, None)
        self.assertNotEqual(myobj.path, None)
        self.assertEqual(myobj.loc, (9, 1))
        self.assertEqual(myobj.facing, '>')

        myobj.one_step("10")
        self.assertEqual(myobj.loc, (11, 1))
        self.assertEqual(myobj.facing, '>')
        myobj.one_step("R")
        self.assertEqual(myobj.loc, (11, 1))
        self.assertEqual(myobj.facing, 'v')
        myobj.one_step("5")
        self.assertEqual(myobj.loc, (11, 6))
        self.assertEqual(myobj.facing, 'v')
        myobj.one_step("L")
        self.assertEqual(myobj.loc, (11, 6))
        self.assertEqual(myobj.facing, '>')
        myobj.one_step("5")
        self.assertEqual(myobj.loc, (15, 11))
        self.assertEqual(myobj.facing, 'v')
        myobj.one_step("R")
        self.assertEqual(myobj.loc, (15, 11))
        self.assertEqual(myobj.facing, '<')
        myobj.one_step("10")
        self.assertEqual(myobj.loc, (11, 11))
        self.assertEqual(myobj.facing, '<')
        myobj.one_step("L")
        self.assertEqual(myobj.loc, (11, 11))
        self.assertEqual(myobj.facing, 'v')
        myobj.one_step("4")
        self.assertEqual(myobj.loc, (2, 6))
        self.assertEqual(myobj.facing, '^')
        myobj.one_step("R")
        self.assertEqual(myobj.loc, (2, 6))
        self.assertEqual(myobj.facing, '>')
        myobj.one_step("5")
        self.assertEqual(myobj.loc, (7, 6))
        self.assertEqual(myobj.facing, '>')
        myobj.one_step("L")
        self.assertEqual(myobj.loc, (7, 6))
        self.assertEqual(myobj.facing, '^')
        myobj.one_step("5")
        self.assertEqual(myobj.loc, (7, 5))
        self.assertEqual(myobj.facing, '^')

        myobj.reset()
        self.assertEqual(myobj.loc, (9, 1))
        self.assertEqual(myobj.facing, '>')
        self.assertEqual(myobj.all_steps(), 5031)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                      t e s t _ y o u . p y                     end
# ======================================================================
