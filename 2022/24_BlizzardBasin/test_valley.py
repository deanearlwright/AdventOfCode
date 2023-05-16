
# ======================================================================
# Blizzard Basin
#   Advent of Code 2022 Day 24 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ v a l l e y . p y
# ======================================================================
"Test Valley for Advent of Code 2022 day 24, Blizzard Basin"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import valley

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = [
    "#.######",  # Entrance is (1,0)
    "#>>.<^<#",
    "#.<..<<#",
    "#>v.><>#",
    "#<^v^^>#",
    "######.#",  # Exit is (6,5)
]
SNOW_TEXT = [
    "#.#####",
    "#.....#",
    "#>....#",
    "#.....#",
    "#...v.#",
    "#.....#",
    "#####.#",
]
SNOW_TEXT2 = [
    "#.#####",
    "#.....#",
    "#<....#",
    "#.....#",
    "#...^.#",
    "#.....#",
    "#####.#",
]

# ======================================================================
#                                                             TestValley
# ======================================================================


class TestValley(unittest.TestCase):  # pylint: disable=R0904
    "Test Valley object"

    def test_empty_init(self):
        "Test the default Valley creation"

        # 1. Create default Valley object
        myobj = valley.Valley()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.height, 0)
        self.assertEqual(myobj.width, 0)
        self.assertEqual(myobj.snow, None)
        self.assertEqual(myobj.start, None)
        self.assertEqual(myobj.goal, None)

    def test_text_init(self):
        "Test the Valley object creation from text"

        # 1. Create Valley object from text
        myobj = valley.Valley(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 6)
        self.assertEqual(myobj.height, 5)
        self.assertEqual(myobj.width, 7)
        self.assertEqual(len(myobj.snow), 19)
        self.assertIn(valley.Snow(col=1, row=1, facing='>'), myobj.snow)
        self.assertIn(valley.Snow(col=1, row=4, facing='<'), myobj.snow)
        self.assertIn(valley.Snow(col=5, row=1, facing='^'), myobj.snow)
        self.assertIn(valley.Snow(col=3, row=4, facing='v'), myobj.snow)
        self.assertEqual(myobj.start, (1, 0))
        self.assertEqual(myobj.goal, (6, 5))

        # 3. Check methods
        snow = myobj.next_snow(myobj.snow)
        self.assertEqual(len(snow), 19)
        self.assertIn(valley.Snow(col=2, row=1, facing='>'), snow)
        self.assertIn(valley.Snow(col=6, row=4, facing='<'), snow)
        self.assertIn(valley.Snow(col=5, row=4, facing='^'), snow)
        self.assertIn(valley.Snow(col=3, row=1, facing='v'), snow)

        self.assertEqual(myobj.find_path(), 18)

    def test_snow(self):
        "Test the movement of snow in the Valley object"

        # 1. Create Valley object from text
        myobj = valley.Valley(text=SNOW_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 7)
        self.assertEqual(myobj.height, 6)
        self.assertEqual(myobj.width, 6)
        self.assertEqual(len(myobj.snow), 2)
        self.assertIn(valley.Snow(col=1, row=2, facing='>'), myobj.snow)
        self.assertIn(valley.Snow(col=4, row=4, facing='v'), myobj.snow)

        self.assertEqual(myobj.start, (1, 0))
        self.assertEqual(myobj.goal, (5, 6))

        # 3. Check methods
        snow = myobj.next_snow(myobj.snow)
        self.assertEqual(len(snow), 2)
        self.assertIn(valley.Snow(col=2, row=2, facing='>'), snow)
        self.assertIn(valley.Snow(col=4, row=5, facing='v'), snow)
        snow = myobj.next_snow(snow)
        self.assertEqual(len(snow), 2)
        self.assertIn(valley.Snow(col=3, row=2, facing='>'), snow)
        self.assertIn(valley.Snow(col=4, row=1, facing='v'), snow)
        snow = myobj.next_snow(snow)
        self.assertEqual(len(snow), 2)
        self.assertIn(valley.Snow(col=4, row=2, facing='>'), snow)
        self.assertIn(valley.Snow(col=4, row=2, facing='v'), snow)
        snow = myobj.next_snow(snow)
        self.assertEqual(len(snow), 2)
        self.assertIn(valley.Snow(col=5, row=2, facing='>'), snow)
        self.assertIn(valley.Snow(col=4, row=3, facing='v'), snow)
        snow = myobj.next_snow(snow)
        self.assertEqual(len(snow), 2)
        self.assertIn(valley.Snow(col=1, row=2, facing='>'), snow)
        self.assertIn(valley.Snow(col=4, row=4, facing='v'), snow)

    def test_snow2(self):
        "Test the movement of snow in the Valley object"

        # 1. Create Valley object from text
        myobj = valley.Valley(text=SNOW_TEXT2)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 7)
        self.assertEqual(myobj.height, 6)
        self.assertEqual(myobj.width, 6)
        self.assertEqual(len(myobj.snow), 2)
        self.assertIn(valley.Snow(col=1, row=2, facing='<'), myobj.snow)
        self.assertIn(valley.Snow(col=4, row=4, facing='^'), myobj.snow)

        self.assertEqual(myobj.start, (1, 0))
        self.assertEqual(myobj.goal, (5, 6))

        # 3. Check methods
        snow = myobj.next_snow(myobj.snow)
        self.assertEqual(len(snow), 2)
        self.assertIn(valley.Snow(col=5, row=2, facing='<'), snow)
        self.assertIn(valley.Snow(col=4, row=3, facing='^'), snow)
        snow = myobj.next_snow(snow)
        self.assertEqual(len(snow), 2)
        self.assertIn(valley.Snow(col=4, row=2, facing='<'), snow)
        self.assertIn(valley.Snow(col=4, row=2, facing='^'), snow)
        snow = myobj.next_snow(snow)
        self.assertEqual(len(snow), 2)
        self.assertIn(valley.Snow(col=3, row=2, facing='<'), snow)
        self.assertIn(valley.Snow(col=4, row=1, facing='^'), snow)
        snow = myobj.next_snow(snow)
        self.assertEqual(len(snow), 2)
        self.assertIn(valley.Snow(col=2, row=2, facing='<'), snow)
        self.assertIn(valley.Snow(col=4, row=5, facing='^'), snow)
        snow = myobj.next_snow(snow)
        self.assertEqual(len(snow), 2)
        self.assertIn(valley.Snow(col=1, row=2, facing='<'), snow)
        self.assertIn(valley.Snow(col=4, row=4, facing='^'), snow)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ v a l l e y . p y                  end
# ======================================================================
