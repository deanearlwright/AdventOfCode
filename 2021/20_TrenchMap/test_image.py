# ======================================================================
# Trench Map
#   Advent of Code 2021 Day 20 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ i m a g e . p y
# ======================================================================
"Test solver for Advent of Code 2021 day 20, Trench Map"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_20
import image

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

...............
...............
...............
...............
...............
.....#..#......
.....#.........
.....##..#.....
.......#.......
.......###.....
...............
...............
...............
...............
...............
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 35
PART_TWO_RESULT = 3351

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
        self.assertEqual(myobj.algorithm, None)
        self.assertEqual(myobj.pixels, {})

    def test_text_init(self):
        "Test the Image object creation from text"

        # 1. Create Image object from text
        myobj = image.Image(text=aoc_20.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 16)
        self.assertEqual(len(myobj.algorithm), 512)
        self.assertEqual(len(myobj.pixels), 225)

        # 3. Check methods
        self.assertEqual(myobj.count_light(), 10)

        self.assertEqual(myobj.neighbor((7, 7)), 34)
        self.assertEqual(myobj.next_pixel((7, 7)), '#')

        self.assertEqual(myobj.next_image(1), 24)
        self.assertEqual(myobj.next_image(2), 35)

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
