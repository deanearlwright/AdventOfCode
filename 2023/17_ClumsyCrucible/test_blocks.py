
# ======================================================================
# Clumsy Crucible
#   Advent of Code 2023 Day 17 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ b l o c k s . p y
# ======================================================================
"Test Blocks for Advent of Code 2023 day 17, Clumsy Crucible"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import blocks

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = [
    "2413432311323",
    "3215453535623",
    "3255245654254",
    "3446585845452",
    "4546657867536",
    "1438598798454",
    "4457876987766",
    "3637877979653",
    "4654967986887",
    "4564679986453",
    "1224686865563",
    "2546548887735",
    "4322674655533",
]

# ======================================================================
#                                                             TestBlocks
# ======================================================================


class TestBlocks(unittest.TestCase):  # pylint: disable=R0904
    "Test Blocks object"

    def test_empty_init(self):
        "Test the default Blocks creation"

        # 1. Create default Blocks object
        myobj = blocks.Blocks()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.rows, 0)
        self.assertEqual(myobj.cols, 0)

    def test_text_init(self):
        "Test the Blocks object creation from text"

        # 1. Create Blocks object from text
        myobj = blocks.Blocks(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 13)
        self.assertEqual(myobj.rows, 13)
        self.assertEqual(myobj.cols, 13)

        # 3. Check methods
        self.assertEqual(myobj.heat_loss((0, 0)), 2)
        self.assertEqual(myobj.heat_loss((1, 4)), 4)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ b l o c k s . p y                  end
# ======================================================================
