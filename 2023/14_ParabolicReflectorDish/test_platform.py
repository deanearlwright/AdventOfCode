
# ======================================================================
# Parabolic Reflector Dish
#   Advent of Code 2023 Day 14 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ p l a t f o r m . p y
# ======================================================================
"Test Platform for Advent of Code 2023 day 14, Parabolic Reflector Dish"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import platform

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = [
    "O....#....",
    "O.OO#....#",
    ".....##...",
    "OO.#O....O",
    ".O.....O#.",
    "O.#..O.#.#",
    "..O..#O..O",
    ".......O..",
    "#....###..",
    "#OO..#....",
]

# ======================================================================
#                                                           TestPlatform
# ======================================================================


class TestPlatform(unittest.TestCase):  # pylint: disable=R0904
    "Test Platform object"

    def test_empty_init(self):
        "Test the default Platform creation"

        # 1. Create default Platform object
        myobj = platform.Platform()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.grid), 0)
        self.assertEqual(myobj.rows, 0)
        self.assertEqual(myobj.cols, 0)

    def test_text_init(self):
        "Test the Platform object creation from text"

        # 1. Create Platform object from text
        myobj = platform.Platform(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 10)
        self.assertEqual(len(myobj.grid), 10)
        self.assertEqual(myobj.rows, 10)
        self.assertEqual(myobj.cols, 10)

        # 3. Check methods
        self.assertEqual(myobj.total_load(), 104)
        myobj.tilt_north()
        self.assertEqual(myobj.total_load(), 136)
        myobj.tilt_west()
        myobj.tilt_south()
        myobj.tilt_east()
        myobj.spin()
        myobj.spin()

    def test_spinning(self):
        "Test the Platform object creation from text"

        # 1. Create Platform object from text
        myobj = platform.Platform(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 10)
        self.assertEqual(len(myobj.grid), 10)
        self.assertEqual(myobj.rows, 10)
        self.assertEqual(myobj.cols, 10)

        # 3. Do the part two spinning
        myobj.you_spin_me_round()
        self.assertEqual(myobj.total_load(), 64)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ p l a t f o r m . p y                end
# ======================================================================
