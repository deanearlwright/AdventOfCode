
# ======================================================================
# Point of Incidence
#   Advent of Code 2023 Day 13 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ v a l l e y s . p y
# ======================================================================
"Test Valleys for Advent of Code 2023 day 13, Point of Incidence"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import valleys

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = [
    "#.##..##.",
    "..#.##.#.",
    "##......#",
    "##......#",
    "..#.##.#.",
    "..##..##.",
    "#.#.##.#.",
    "",
    "#...##..#",
    "#....#..#",
    "..##..###",
    "#####.##.",
    "#####.##.",
    "..##..###",
    "#....#..#",
]

# ======================================================================
#                                                            TestValleys
# ======================================================================


class TestValleys(unittest.TestCase):  # pylint: disable=R0904
    "Test Valleys object"

    def test_empty_init(self):
        "Test the default Valleys creation"

        # 1. Create default Valleys object
        myobj = valleys.Valleys()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.valleys), 0)

    def test_text_init(self):
        "Test the Valleys object creation from text"

        # 1. Create Valleys object from text
        myobj = valleys.Valleys(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 15)
        self.assertEqual(len(myobj.valleys), 2)

        # 3. Check methods
        self.assertEqual(myobj.valleys[0].vertical(), 5)
        self.assertEqual(myobj.valleys[1].cols, 9)
        self.assertEqual(myobj.valleys[1].are_vertical_twins(6, 7), True)
        self.assertEqual(myobj.valleys[1].are_vertical_twins(5, 8), False)
        self.assertEqual(myobj.valleys[1].vertical(), 0)
        self.assertEqual(myobj.valleys[0].horizontal(), 0)
        self.assertEqual(myobj.valleys[1].horizontal(), 4)
        self.assertEqual(myobj.valleys[0].reflections(), 5)
        self.assertEqual(myobj.valleys[1].reflections(), 400)
        self.assertEqual(myobj.reflections(), 405)
        self.assertEqual(myobj.corrected_reflections(), 400)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                  t e s t _ v a l l e y s . p y                 end
# ======================================================================
