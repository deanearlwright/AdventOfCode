
# ======================================================================
# Reindeer Maze
#   Advent of Code 2024 Day 16 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                      t e s t _ m a z e . p y
# ======================================================================
"Test solver for Advent of Code 2024 day 16, Reindeer Maze"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_16
import maze

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
"""
EXAMPLE_TWO = """
#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 7036
PART_TWO_RESULT = 45

# ======================================================================
#                                                               TestMaze
# ======================================================================


class TestMaze(unittest.TestCase):  # pylint: disable=R0904
    "Test Maze object"

    def test_empty_init(self):
        "Test the default Maze creation"

        # 1. Create default Maze object
        myobj = maze.Maze()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.walls), 0)
        self.assertEqual(myobj.start, (0, 0))
        self.assertEqual(myobj.end, (0, 0))

    def test_text_init(self):
        "Test the Maze object creation from text"

        # 1. Create Maze object from text
        myobj = maze.Maze(text=aoc_16.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 15)
        self.assertEqual(len(myobj.walls), 121)
        self.assertEqual(myobj.start, (13, 1))
        self.assertEqual(myobj.end, (1, 13))

        # 3. Check methods
        self.assertEqual(myobj.best_maze(), 7036)
        self.assertEqual(myobj.find_tiles(score=7036), 45)

    def test_text_two(self):
        "Test the Maze object creation from second example"

        # 1. Create Maze object from text
        myobj = maze.Maze(text=aoc_16.from_text(EXAMPLE_TWO))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 17)
        self.assertEqual(len(myobj.walls), 157)
        self.assertEqual(myobj.start, (15, 1))
        self.assertEqual(myobj.end, (1, 15))

        # 3. Check methods
        self.assertEqual(myobj.best_maze(), 11048)
        self.assertEqual(myobj.find_tiles(score=11048), 64)

    def test_part_one(self):
        "Test part one example of Maze object"

        # 1. Create Maze object from text
        text = aoc_16.from_text(PART_ONE_TEXT)
        myobj = maze.Maze(text=text)

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Maze object"

        # 1. Create Maze object from text
        text = aoc_16.from_text(PART_TWO_TEXT)
        myobj = maze.Maze(part2=True, text=text)

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False, score=PART_ONE_RESULT), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                     t e s t _ m a z e . p y                    end
# ======================================================================
