
# ======================================================================
# Point of Incidence
#   Advent of Code 2023 Day 13 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ v a l l e y . p y
# ======================================================================
"Test Valley for Advent of Code 2023 day 13, Point of Incidence"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import valley

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_ONE_TEXT = [
    "#.##..##.",
    "..#.##.#.",
    "##......#",
    "##......#",
    "..#.##.#.",
    "..##..##.",
    "#.#.##.#.",
]
EXAMPLE_TWO_TEXT = [
    "#...##..#",
    "#....#..#",
    "..##..###",
    "#####.##.",
    "#####.##.",
    "..##..###",
    "#....#..#",
]
CORRECTED_ONE_TEXT = [
    "..##..##.",
    "..#.##.#.",
    "##......#",
    "##......#",
    "..#.##.#.",
    "..##..##.",
    "#.#.##.#.",
]
CORRECTED_TWO_TEXT = [
    "#...##..#",
    "#...##..#",
    "..##..###",
    "#####.##.",
    "#####.##.",
    "..##..###",
    "#....#..#",
]
REFLECTIONS = [
    (EXAMPLE_ONE_TEXT, 5, 300),
    (EXAMPLE_TWO_TEXT, 400, 100),
    (CORRECTED_ONE_TEXT, 305, None),
    (CORRECTED_TWO_TEXT, 100, None)
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
        self.assertEqual(myobj.rows, 0)
        self.assertEqual(myobj.cols, 0)

    def test_text_init(self):
        "Test the Valley object creation from text"

        # 1. Create Valley object from text
        myobj = valley.Valley(text=EXAMPLE_ONE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 7)
        self.assertEqual(myobj.rows, 7)
        self.assertEqual(myobj.cols, 9)

        # 3. Check methods
        self.assertEqual(myobj.are_vertical_twins(-1, 0), True)
        self.assertEqual(myobj.are_vertical_twins(0, 1), False)
        self.assertEqual(myobj.are_vertical_twins(1, 2), False)
        self.assertEqual(myobj.are_vertical_twins(4, 5), True)
        self.assertEqual(myobj.are_vertical_twins(1, 100), True)

        self.assertEqual(myobj.are_horizontal_twins(-1, 0), True)
        self.assertEqual(myobj.are_horizontal_twins(0, 1), False)
        self.assertEqual(myobj.are_horizontal_twins(1, 2), False)
        self.assertEqual(myobj.are_horizontal_twins(2, 3), True)
        self.assertEqual(myobj.are_horizontal_twins(1, 100), True)

        self.assertEqual(myobj.vertical(), 5)
        self.assertEqual(myobj.horizontal(), 0)
        self.assertEqual(myobj.reflections(), 5)

    def test_reflections(self):
        "Test the Valley object creation from text"

        # 1. Loop for the reflection tests:
        for test in REFLECTIONS:

            # 2. Create Valley object from text
            myobj = valley.Valley(text=test[0])

            # 3. Verifty the reflections for part 1
            self.assertEqual(myobj.reflections(), test[1])

            # 3. And verifty the reflections for part 2
            if test[2] is not None:
                self.assertEqual(myobj.corrected_reflections(), test[2])

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ v a l l e y . p y                  end
# ======================================================================
