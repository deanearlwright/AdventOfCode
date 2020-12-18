# ======================================================================
# Conway Cubes
#   Advent of Code 2020 Day 17 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ p o c k e t . p y
# ======================================================================
"Test solver for Advent of Code 2020 day 17, Conway Cubes"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_17
import pocket

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
.#.
..#
###
"""
EXAMPLE_COUNT = [5, 11, 21, 38, 0, 0, 112]
EXAMPLE_COUNT_TWO = [5, 29, 60, 0, 0, 0, 848]

PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 112
PART_TWO_RESULT = 848

# ======================================================================
#                                                             TestPocket
# ======================================================================


class TestPocket(unittest.TestCase):  # pylint: disable=R0904
    "Test Pocket object"

    def test_empty_init(self):
        "Test the default Pocket creation"

        # 1. Create default Pocket object
        myobj = pocket.Pocket()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.cycle, 0)
        self.assertEqual(myobj.active, set())

        # 3. Check methods
        self.assertEqual(myobj.count(), 0)
        self.assertEqual(len([_ for _ in myobj.nearby((0, 0, 0))]), 26)
        self.assertEqual(myobj.count_nearby((0, 0, 0)), 0)

    def test_text_init(self):
        "Test the Pocket object creation from text"

        # 1. Create Pocket object from text
        myobj = pocket.Pocket(text=aoc_17.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 3)
        self.assertEqual(myobj.cycle, 0)
        self.assertEqual(len(myobj.active), 5)

        # 3. Check methods
        self.assertEqual(myobj.count(), EXAMPLE_COUNT[0])
        self.assertEqual(len([_ for _ in myobj.nearby((0, 0, 0))]), 26)
        self.assertEqual(myobj.count_nearby((0, 0, 0)), 1)
        self.assertEqual(myobj.count_nearby((0, 0, 1)), 1)
        self.assertEqual(myobj.count_nearby((1, 1, 0)), 5)
        self.assertEqual(myobj.count_nearby((1, 1, 1)), 5)

        myobj.one_cycle()
        self.assertEqual(myobj.count(), EXAMPLE_COUNT[1])
        myobj.one_cycle()
        self.assertEqual(myobj.count(), EXAMPLE_COUNT[2])
        myobj.one_cycle()
        self.assertEqual(myobj.count(), EXAMPLE_COUNT[3])

    def test_text_init_two(self):
        "Test the Pocket object creation from text for part two"

        # 1. Create Pocket object from text
        myobj = pocket.Pocket(text=aoc_17.from_text(EXAMPLE_TEXT), part2=True)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, True)
        self.assertEqual(len(myobj.text), 3)
        self.assertEqual(myobj.cycle, 0)
        self.assertEqual(len(myobj.active), 5)

        # 3. Check methods
        self.assertEqual(myobj.count(), EXAMPLE_COUNT[0])
        self.assertEqual(len([_ for _ in myobj.nearby((0, 0, 0, 0))]), 80)
        self.assertEqual(myobj.count_nearby((0, 0, 0, 0)), 1)
        self.assertEqual(myobj.count_nearby((0, 0, 1, 0)), 1)
        self.assertEqual(myobj.count_nearby((1, 1, 0, 0)), 5)
        self.assertEqual(myobj.count_nearby((1, 1, 1, 1)), 5)

        myobj.one_cycle()
        self.assertEqual(myobj.count(), EXAMPLE_COUNT_TWO[1])
        myobj.one_cycle()
        self.assertEqual(myobj.count(), EXAMPLE_COUNT_TWO[2])

    def test_part_one(self):
        "Test part one example of Pocket object"

        # 1. Create Pocket object from text
        myobj = pocket.Pocket(text=aoc_17.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Pocket object"

        # 1. Create Pocket object from text
        myobj = pocket.Pocket(part2=True, text=aoc_17.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ p o c k e t . p y                  end
# ======================================================================
