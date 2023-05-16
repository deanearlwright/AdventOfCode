
# ======================================================================
# Monkey Board
#   Advent of Code 2022 Day 22 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ b o a r d . p y
# ======================================================================
"Test Board for Advent of Code 2022 day 22, Monkey Board"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_22
import board

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
"""

# ======================================================================
#                                                              TestBoard
# ======================================================================


class TestBoard(unittest.TestCase):  # pylint: disable=R0904
    "Test Board object"

    def test_empty_init(self):
        "Test the default Board creation"

        # 1. Create default Board object
        myobj = board.Board()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.rows), 0)

    def test_text_init(self):
        "Test the Board object creation from text"

        # 1. Create Board object from text
        myobj = board.Board(text=aoc_22.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 12)
        self.assertEqual(len(myobj.rows), 14)

        # 3. Check methods
        self.assertEqual(myobj.find_start(), (9, 1))
        self.assertEqual(myobj.at_loc((1, 1)), board.WARP)
        self.assertEqual(myobj.at_loc((9, 1)), board.TILE)
        self.assertEqual(myobj.at_loc((12, 1)), board.WALL)
        self.assertEqual(myobj.at_loc((12, 0)), board.WARP)
        self.assertEqual(myobj.at_loc((16, 1)), board.WARP)
        self.assertEqual(myobj.at_loc((17, 1)), board.WARP)
        self.assertEqual(myobj.at_loc((1, 13)), board.WARP)
        self.assertEqual(myobj.at_loc((15, 12)), board.WALL)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ b o a r d . p y                   end
# ======================================================================
