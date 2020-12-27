# ======================================================================
# Jurassic Jigsaw
#   Advent of Code 2020 Day 20 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                       t e s t _ t i l e s . p y
# ======================================================================
"Test solver for Advent of Code 2020 day 20, Jurassic Jigsaw"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_20
import tiles

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

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...
"""

GRID = [1951, 2311, 3079, 2729, 1427, 2473, 2971, 1489, 1171]

IMAGE = """
.#.#..#.##...#.##..#####
###....#.#....#..#......
##.##.###.#.#..######...
###.#####...#.#####.#..#
##.#....#.##.####...#.##
...########.#....#####.#
....#..#...##..#.#.###..
.####...#..#.....#......
#..#.##..#..###.#.##....
#.####..#.####.#.#.###..
###.#.#...#.######.#..##
#.####....##..########.#
##..##.#...#...#.#.#.#..
...#..#..#.#.##..###.###
.#.#....#.##.#...###.##.
###.#...#..#.##.######..
.#.#.###.##.##.#..#.##..
.####.###.#...###.#..#.#
..#.#..#..#.#.#.####.###
#..####...#.#.#.###.###.
#####..#####...###....##
#.##..#..#...#..####...#
.#.###..##..##..####.##.
...###...##...#...#..###
""".strip()

# ======================================================================
#                                                              TestTiles
# ======================================================================


class TestTiles(unittest.TestCase):  # pylint: disable=R0904
    "Test Tiles object"

    def test_empty_init(self):
        "Test the default Tiles creation"

        # 1. Create default Tiles object
        myobj = tiles.Tiles()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.tiles, [])
        self.assertEqual(myobj.size, 0)
        self.assertEqual(myobj.grid, None)

    def test_text_init(self):
        "Test the Tiles object creation from text"

        # 1. Create Tiles object from text
        myobj = tiles.Tiles(text=aoc_20.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 9 * 11)
        self.assertEqual(len(myobj.tiles), 9)
        self.assertEqual(myobj.size, 3)
        self.assertEqual(myobj.grid, None)

        # 3. Test placing tiles into a grid
        myobj.position_tiles()
        self.assertNotEqual(myobj.grid, None)
        numbers = []
        for row in myobj.grid:
            for col in row:
                numbers.append(col[0].number)
        self.assertEqual(numbers, GRID)

        # 4. Test the image
        self.assertEqual(myobj.get_image(), IMAGE)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ t i l e s . p y                   end
# ======================================================================