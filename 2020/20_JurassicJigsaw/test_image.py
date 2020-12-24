# ======================================================================
# Jurassic Jigsaw
#   Advent of Code 2020 Day 20 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ i m a g e . p y
# ======================================================================
"Test solver for Advent of Code 2020 day 20, Jurassic Jigsaw"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest
import re  # just for testing

import aoc_20
import image

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
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 20899048083289
PART_TWO_RESULT = 273

MONSTER_IMAGE = """
.####...#####..#...###..
# ..#..#.#.####..#.#.
.#.#...#.###...#.##.##..
#.#.##.###.#.##.##.#####
..##.###.####..#.####.##
...#.#..##.##...#..#..##
# .##.#..#.#..#..##.#.#..
.###.##.....#...###.#...
# .####.#.#....##.#..#.#.
##...#..#....#..#...####
..#.##...###..#.#####..#
....#.##.#.#####....#...
..##.##.###.....#.##..#.
# ...#...###..####....##.
.#.##...#.##.#.#.###...#
# .###.#..####...##..#...
# .###...#.##...#.######.
.###.###.#######..#####.
..##.#..#..#.#######.###
# .#..##.########..#..##.
# .#####..#.#...##..#....
#....##..#.#########..##
#...#.....#..##...###.##
#..###....##.#...##.##.#
""".strip()

MONSTER = """                  #
#    ##    ##    ###
 #  #  #  #  #  #   """

MONSTER_RE1 = re.compile('..................#.')
MONSTER_RE2 = re.compile('#....##....##....###')
MONSTER_RE3 = re.compile('.#..#..#..#..#..#...')

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
        self.assertEqual(myobj.tiles, None)

    def test_text_init(self):
        "Test the Image object creation from text"

        # 1. Create Image object from text
        myobj = image.Image(text=aoc_20.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 99)
        self.assertEqual(myobj.tiles.size, 3)

    def test_part_one(self):
        "Test part one example of Image object"

        # 1. Create Image object from text
        myobj = image.Image(text=aoc_20.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Image object"

        # 1. Create Image object from text
        myobj = image.Image(part2=True, text=aoc_20.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ i m a g e . p y                   end
# ======================================================================
