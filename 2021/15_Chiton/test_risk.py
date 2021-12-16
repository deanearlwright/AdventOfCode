# ======================================================================
# Chiton
#   Advent of Code 2021 Day 15 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ r i s k . p y
# ======================================================================
"Test solver for Advent of Code 2021 day 15, Chiton"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_15
import risk

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 40
PART_TWO_RESULT = 315

# ======================================================================
#                                                               TestRisk
# ======================================================================


class TestRisk(unittest.TestCase):  # pylint: disable=R0904
    "Test Risk object"

    def test_empty_init(self):
        "Test the default Risk creation"

        # 1. Create default Risk object
        myobj = risk.Risk()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.risks, {})
        self.assertEqual(myobj.goal, risk.START)

    def test_text_init(self):
        "Test the Risk object creation from text"

        # 1. Create Risk object from text
        myobj = risk.Risk(text=aoc_15.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 10)
        self.assertEqual(len(myobj.risks), 100)
        self.assertEqual(myobj.goal, (9, 9))
        self.assertEqual(myobj.risks[(0, 0)], 1)
        self.assertEqual(myobj.risks[(9, 0)], 2)
        self.assertEqual(myobj.risks[(0, 9)], 2)
        self.assertEqual(myobj.risks[(9, 9)], 1)

        # 3. Check mothods
        #self.assertEqual(myobj.find_brute_force_risk(), 40)
        self.assertEqual(myobj.find_network_risk(), 40)

    def test_text_init_two(self):
        "Test the Risk object creation from text"

        # 1. Create Risk object from text
        myobj = risk.Risk(text=aoc_15.from_text(EXAMPLE_TEXT), part2=True)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, True)
        self.assertEqual(len(myobj.text), 10)
        self.assertEqual(len(myobj.risks), 50 * 50)
        self.assertEqual(myobj.goal, (49, 49))
        self.assertEqual(myobj.risks[(0, 0)], 1)
        self.assertEqual(myobj.risks[(9, 0)], 2)
        self.assertEqual(myobj.risks[(0, 9)], 2)
        self.assertEqual(myobj.risks[(9, 9)], 1)
        self.assertEqual(myobj.risks[(10, 0)], 2)
        self.assertEqual(myobj.risks[(49, 0)], 6)
        self.assertEqual(myobj.risks[(0, 10)], 2)
        self.assertEqual(myobj.risks[(0, 49)], 6)
        self.assertEqual(myobj.risks[(49, 49)], 9)

        # 3. Check mothods
        self.assertEqual(myobj.find_network_risk(), 315)

    def test_part_one(self):
        "Test part one example of Risk object"

        # 1. Create Risk object from text
        myobj = risk.Risk(text=aoc_15.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Risk object"

        # 1. Create Risk object from text
        myobj = risk.Risk(part2=True, text=aoc_15.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                     t e s t _ r i s k . p y                    end
# ======================================================================
