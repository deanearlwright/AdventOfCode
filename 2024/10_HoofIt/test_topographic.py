
# ======================================================================
# Hoof It
#   Advent of Code 2024 Day 10 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ t o p o g r a p h i c . p y
# ======================================================================
"Test solver for Advent of Code 2024 day 10, Hoof It"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_10
import topographic

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 36
PART_TWO_RESULT = 81

# ======================================================================
#                                                        TestTopographic
# ======================================================================


class TestTopographic(unittest.TestCase):  # pylint: disable=R0904
    "Test Topographic object"

    def test_empty_init(self):
        "Test the default Topographic creation"

        # 1. Create default Topographic object
        myobj = topographic.Topographic()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.heights), 0)
        self.assertEqual(len(myobj.trailheads), 0)

        # 3. Check methods
        self.assertEqual(myobj.sum_trailhead_scores(), 0)

    def test_text_init(self):
        "Test the Topographic object creation from text"

        # 1. Create Topographic object from text
        myobj = topographic.Topographic(text=aoc_10.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 8)
        self.assertEqual(len(myobj.heights), 64)
        self.assertEqual(len(myobj.trailheads), 9)

        # 3. Check methods
        myobj.determine_trailhead_scores()
        self.assertEqual(myobj.sum_trailhead_scores(), 36)

    def test_part_one(self):
        "Test part one example of Topographic object"

        # 1. Create Topographic object from text
        text = aoc_10.from_text(PART_ONE_TEXT)
        myobj = topographic.Topographic(text=text)

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Topographic object"

        # 1. Create Topographic object from text
        text = aoc_10.from_text(PART_TWO_TEXT)
        myobj = topographic.Topographic(part2=True, text=text)

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end              t e s t _ t o p o g r a p h i c . p y             end
# ======================================================================
