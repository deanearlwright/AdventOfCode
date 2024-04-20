
# ======================================================================
# Cosmic Expansion
#   Advent of Code 2023 Day 11 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ i m a g e . p y
# ======================================================================
"Test Image for Advent of Code 2023 day 11, Cosmic Expansion"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import image

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = [
    "...#......",
    ".......#..",
    "#.........",
    "..........",
    "......#...",
    ".#........",
    ".........#",
    "..........",
    ".......#..",
    "#...#.....",
]

# ======================================================================
#                                                              TestImage
# ======================================================================


class TestImage(unittest.TestCase):  # pylint: disable=R0904
    "Test Image object"

    def test_empty_init(self):
        "Test the default Image creation"

        # 1. Create default Image object
        myobj = image.Image()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.expand_col), 0)
        self.assertEqual(len(myobj.expand_row), 0)
        self.assertEqual(len(myobj.galaxies), 0)

    def test_text_init(self):
        "Test the Image object creation from text"

        # 1. Create Image object from text
        myobj = image.Image(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 10)
        self.assertEqual(len(myobj.expand_col), 10 + 1)
        self.assertEqual(len(myobj.expand_row), 10 + 1)
        self.assertEqual(myobj.expand_col, [0, 1, 2, 4, 5, 6, 8, 9, 10, 12, 13])
        self.assertEqual(myobj.expand_row, [0, 1, 2, 3, 5, 6, 7, 8, 10, 11, 12])
        self.assertEqual(len(myobj.galaxies), 9)
        self.assertEqual(myobj.galaxies[0], (0, 4))
        self.assertEqual(myobj.galaxies[8], (11, 5))

        # 3. Check methods
        self.assertEqual(image.Image.manhattan_distance(myobj.galaxies[4], myobj.galaxies[8]), 9)
        self.assertEqual(image.Image.manhattan_distance(myobj.galaxies[0], myobj.galaxies[6]), 15)
        self.assertEqual(image.Image.manhattan_distance(myobj.galaxies[2], myobj.galaxies[5]), 17)
        self.assertEqual(image.Image.manhattan_distance(myobj.galaxies[7], myobj.galaxies[8]), 5)

        self.assertEqual(myobj.all_distances(), 374)

    def test_expansion(self):
        "Test the Image object creation from text"

        # 1. Create Image with expansion factor of 10
        myobj = image.Image(text=EXAMPLE_TEXT, expansion=10)
        self.assertEqual(myobj.all_distances(), 1030)

        # 2. Create Image with expansion factor of 100
        myobj = image.Image(text=EXAMPLE_TEXT, expansion=100)
        self.assertEqual(myobj.all_distances(), 8410)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ i m a g e . p y                   end
# ======================================================================
