# ======================================================================
# Beverage Bandits
#   Advent of Code 2018 Day 15 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                       t e s t _ c a v e . p y
# ======================================================================
"Test container for Advent of Code 2018 day 15, Beverage Bandits"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_15
import cave

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
#######
#.G...#
#...EG#
#.#.#G#
#..G#E#
#.....#
#######
"""
# ======================================================================
#                                                               TestCave
# ======================================================================


class TestCave(unittest.TestCase):  # pylint: disable=R0904
    "Test Cave object"

    def test_empty_init(self):
        "Test the default Cave creation"

        # 1. Create default Cave object
        myobj = cave.Cave()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.items), 0)

    def test_text_init(self):
        "Test the Cave object creation from text"

        # 1. Create Cave object from text
        myobj = cave.Cave(text=aoc_15.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(len(myobj.text), 7)
        self.assertEqual(len(myobj.items), 3)
        self.assertEqual(len(myobj.items['#']), 27)
        self.assertEqual(len(myobj.items['E']), 2)
        self.assertEqual(len(myobj.items['G']), 4)
        self.assertEqual(myobj.max_loc(), 606)
        self.assertEqual(str(myobj), EXAMPLE_TEXT.strip())

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                       t e s t _ c a v e . p y                  end
# ======================================================================
