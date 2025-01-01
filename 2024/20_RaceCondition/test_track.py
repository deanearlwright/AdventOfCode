
# ======================================================================
# Race Condition
#   Advent of Code 2024 Day 20 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ t r a c k . p y
# ======================================================================
"Test solver for Advent of Code 2024 day 20, Race Condition"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_20
import track

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 0
PART_TWO_RESULT = 0

# ======================================================================
#                                                              TestTrack
# ======================================================================


class TestTrack(unittest.TestCase):  # pylint: disable=R0904
    "Test Track object"

    def test_empty_init(self):
        "Test the default Track creation"

        # 1. Create default Track object
        myobj = track.Track()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.rows, 0)
        self.assertEqual(myobj.cols, 0)
        self.assertEqual(myobj.start, None)
        self.assertEqual(myobj.end, None)
        self.assertEqual(len(myobj.walls), 0)
        self.assertEqual(len(myobj.spaces), 0)
        self.assertEqual(len(myobj.cheats), 0)

    def test_text_init(self):
        "Test the Track object creation from text"

        # 1. Create Track object from text
        myobj = track.Track(text=aoc_20.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 15)
        self.assertEqual(myobj.rows, 15)
        self.assertEqual(myobj.cols, 15)
        self.assertEqual(myobj.start, (3, 1))
        self.assertEqual(myobj.end, (7, 5))
        self.assertEqual(len(myobj.walls), 140)
        self.assertEqual(len(myobj.spaces), 85)

        self.assertEqual(len(myobj.cheats), 44)
        self.assertEqual(max(myobj.cheats.values()), 64)
        self.assertEqual(min(myobj.cheats.values()), 2)

    def test_text_two(self):
        "Test the Track object creation from text"

        # 1. Create Track object from text
        myobj = track.Track(text=aoc_20.from_text(EXAMPLE_TEXT), part2=True)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, True)
        self.assertEqual(len(myobj.text), 15)
        self.assertEqual(myobj.rows, 15)
        self.assertEqual(myobj.cols, 15)
        self.assertEqual(myobj.start, (3, 1))
        self.assertEqual(myobj.end, (7, 5))
        self.assertEqual(len(myobj.walls), 140)
        self.assertEqual(len(myobj.spaces), 85)

        self.assertEqual(len(myobj.cheats), 44)
        self.assertEqual(max(myobj.cheats.values()), 64)
        self.assertEqual(min(myobj.cheats.values()), 2)

        self.assertEqual(myobj.cheats2[100], 0)
        self.assertEqual(myobj.cheats2[76], 3)
        self.assertEqual(myobj.cheats2[74], 4)
        self.assertEqual(myobj.cheats2[72], 22)
        self.assertEqual(myobj.cheats2[70], 12)
        self.assertEqual(myobj.cheats2[68], 14)
        self.assertEqual(myobj.cheats2[66], 12)
        self.assertEqual(myobj.cheats2[64], 19)
        self.assertEqual(myobj.cheats2[62], 20)
        self.assertEqual(myobj.cheats2[60], 23)
        self.assertEqual(myobj.cheats2[58], 25)
        self.assertEqual(myobj.cheats2[56], 39)
        self.assertEqual(myobj.cheats2[54], 29)
        self.assertEqual(myobj.cheats2[52], 31)
        self.assertEqual(myobj.cheats2[50], 32)

    def test_part_one(self):
        "Test part one example of Track object"

        # 1. Create Track object from text
        text = aoc_20.from_text(PART_ONE_TEXT)
        myobj = track.Track(text=text)

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Track object"

        # 1. Create Track object from text
        text = aoc_20.from_text(PART_TWO_TEXT)
        myobj = track.Track(part2=True, text=text)

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ t r a c k . p y                   end
# ======================================================================
