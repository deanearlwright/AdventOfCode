# ======================================================================
# Smoke Basin
#   Advent of Code 2021 Day 09 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ c a v e s . p y
# ======================================================================
"Test solver for Advent of Code 2021 day 09, Smoke Basin"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_09
import caves

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
2199943210
3987894921
9856789892
8767896789
9899965678
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 15
PART_TWO_RESULT = 1134

# ======================================================================
#                                                              TestCaves
# ======================================================================


class TestCaves(unittest.TestCase):  # pylint: disable=R0904
    "Test Caves object"

    def test_empty_init(self):
        "Test the default Caves creation"

        # 1. Create default Caves object
        myobj = caves.Caves()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.heights), 0)
        self.assertEqual(len(myobj.basins), 0)

    def test_text_init(self):
        "Test the Caves object creation from text"

        # 1. Create Caves object from text
        myobj = caves.Caves(text=aoc_09.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 5)
        self.assertEqual(len(myobj.heights), 50)
        self.assertEqual(len(myobj.basins), 0)

        # 3. Check methods
        self.assertEqual(sum(myobj.adjacent_heights((0, 0))), 4)
        self.assertEqual(sum(myobj.adjacent_heights((3, 1))), 31)
        self.assertEqual(sum(myobj.adjacent_heights((9, 0))), 2)
        self.assertEqual(sum(myobj.adjacent_heights((6, 4))), 18)

        self.assertEqual(myobj.is_lowest((0, 0)), False)
        self.assertEqual(myobj.is_lowest((1, 0)), True)
        self.assertEqual(myobj.is_lowest((9, 0)), True)
        self.assertEqual(myobj.is_lowest((2, 2)), True)
        self.assertEqual(myobj.is_lowest((6, 4)), True)
        self.assertEqual(myobj.is_lowest((3, 3)), False)

        lowest = myobj.lowest_points()
        self.assertEqual(len(lowest), 4)
        self.assertEqual(sum([myobj.heights[l] for l in lowest]), 11)

        self.assertEqual(myobj.risk((0, 0)), 3)
        self.assertEqual(myobj.risk((1, 0)), 2)
        self.assertEqual(myobj.total_risk([(0, 0), (1, 0)]), 5)
        self.assertEqual(myobj.total_risk(lowest), 15)
        self.assertEqual(myobj.total_risk(), 15)

    def test_text_init_two(self):
        "Test the Caves object creation from text for part 2"

        # 1. Create Caves object from text
        myobj = caves.Caves(text=aoc_09.from_text(EXAMPLE_TEXT), part2=True)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, True)
        self.assertEqual(len(myobj.text), 5)
        self.assertEqual(len(myobj.heights), 50)
        self.assertEqual(len(myobj.basins), 0)

        # 3. Check methods
        self.assertEqual(len(myobj.not_nines((0, 0))), 2)
        self.assertEqual(len(myobj.not_nines((1, 0))), 1)
        self.assertEqual(len(myobj.not_nines((9, 0))), 2)
        self.assertEqual(len(myobj.not_nines((6, 0))), 3)
        self.assertEqual(len(myobj.not_nines((6, 1))), 1)

        self.assertEqual(len(myobj.grow_basin((0, 0))), 3)
        self.assertEqual(len(myobj.grow_basin((9, 0))), 9)
        self.assertEqual(len(myobj.grow_basin((3, 2))), 14)
        self.assertEqual(len(myobj.grow_basin((6, 4))), 9)

        self.assertEqual(myobj.get_basins(), 1134)

    def test_part_one(self):
        "Test part one example of Caves object"

        # 1. Create Caves object from text
        myobj = caves.Caves(text=aoc_09.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Caves object"

        # 1. Create Caves object from text
        myobj = caves.Caves(part2=True, text=aoc_09.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ c a v e s . p y                   end
# ======================================================================
