# ======================================================================
# Jurassic Jigsaw
#   Advent of Code 2020 Day 20 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                       t e s t _ t i l e . p y
# ======================================================================
"Test tile object for Advent of Code 2020 day 20, Jurassic Jigsaw"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_20
import tile

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###
"""
EXAMPLE_FLIPPED = """
Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###
"""

# ======================================================================
#                                                               TestTile
# ======================================================================


class TestTile(unittest.TestCase):  # pylint: disable=R0904
    "Test Tile object"

    def test_empty_init(self):
        "Test the default Tile creation"

        # 1. Create default Tile object
        myobj = tile.Tile()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.number, None)
        self.assertEqual(myobj.lines, [])
        self.assertEqual(myobj.orientations, [])
        self.assertEqual(myobj.borders, [])

    def test_text_init(self):
        "Test the Tile object creation from text"

        # 1. Create Tile object from text
        myobj = tile.Tile(text=aoc_20.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 11)
        self.assertEqual(myobj.number, 2311)
        self.assertEqual(len(myobj.lines), 10)
        self.assertEqual(len(myobj.orientations), 8)
        self.assertEqual(len(myobj.borders), 8)
        self.assertEqual(myobj.borders[0], ['..##.#..#.', '..###..###',
                                            '.#####..#.', '...#.##..#'])


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                     t e s t _ t i l e . p y                    end
# ======================================================================
