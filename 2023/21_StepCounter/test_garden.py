
# ======================================================================
# Step Counter
#   Advent of Code 2023 Day 21 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                      t e s t _ g a r d e n . p y
# ======================================================================
"Test Garden for Advent of Code 2023 day 21, Step Counter"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import garden # pylint: disable=W0622

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = [
    "...........",
    ".....###.#.",
    ".###.##..#.",
    "..#.#...#..",
    "....#.#....",
    ".##..S####.",
    ".##..#...#.",
    ".......##..",
    ".##.#.####.",
    ".##..##.##.",
    "...........",
]

# ======================================================================
#                                                             TestGarden
# ======================================================================


class TestGarden(unittest.TestCase):  # pylint: disable=R0904
    "Test Garden object"

    def test_empty_init(self):
        "Test the default Garden creation"

        # 1. Create default Garden object
        myobj = garden.Garden()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.rows, 0)
        self.assertEqual(myobj.cols, 0)
        self.assertEqual(myobj.start, None)

    def test_text_init(self):
        "Test the Garden object creation from text"

        # 1. Create Garden object from text
        myobj = garden.Garden(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 11)
        self.assertEqual(myobj.rows, 11)
        self.assertEqual(myobj.cols, 11)
        self.assertEqual(myobj.start, (5, 5))

        # 3. Check Methods
        self.assertEqual(myobj.plots(max_steps=0), 1)
        self.assertEqual(myobj.plots(max_steps=1), 2)
        self.assertEqual(myobj.plots(max_steps=2), 4)
        self.assertEqual(myobj.plots(max_steps=6), 16)

        self.assertEqual(myobj.infinite(max_steps=0), 1)
        self.assertEqual(myobj.infinite(max_steps=1), 2)
        self.assertEqual(myobj.infinite(max_steps=2), 4)
        self.assertEqual(myobj.infinite(max_steps=6), 16)
        self.assertEqual(myobj.infinite(max_steps=10), 50)
        self.assertEqual(myobj.infinite(max_steps=50), 1594)
        # self.assertEqual(myobj.infinite(max_steps=100), 6536)
        # self.assertEqual(myobj.infinite(max_steps=500), 167004)
        # self.assertEqual(myobj.infinite(max_steps=1000), 668697)
        # self.assertEqual(myobj.infinite(max_steps=5000), 16733044)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ g a r d e n . p y                  end
# ======================================================================
