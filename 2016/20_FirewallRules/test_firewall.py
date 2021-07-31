# ======================================================================
# Firewall Rules
#   Advent of Code 2016 Day 20 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ f i r e w a l l . p y
# ======================================================================
"Test solver for Advent of Code 2016 day 20, Firewall Rules"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_20
import firewall

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
5-8
0-2
4-7
"""

PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 3
PART_TWO_RESULT = 4294967288

# ======================================================================
#                                                           TestFirewall
# ======================================================================


class TestFirewall(unittest.TestCase):  # pylint: disable=R0904
    "Test Firewall object"

    def test_empty_init(self):
        "Test the default Firewall creation"

        # 1. Create default Firewall object
        myobj = firewall.Firewall()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.ranges), 0)

    def test_text_init(self):
        "Test the Firewall object creation from text"

        # 1. Create Firewall object from text
        myobj = firewall.Firewall(text=aoc_20.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 3)
        self.assertEqual(len(myobj.ranges), 3)
        self.assertEqual(myobj.ranges[0][0], 0)
        self.assertEqual(myobj.ranges[0][1], 2)
        self.assertEqual(myobj.ranges[1][0], 4)
        self.assertEqual(myobj.ranges[1][1], 7)

        # 3. Check methods
        self.assertEqual(myobj.lowest(), 3)
        self.assertEqual(myobj.count(9), 2)

    def test_part_one(self):
        "Test part one example of Firewall object"

        # 1. Create Firewall object from text
        myobj = firewall.Firewall(text=aoc_20.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Firewall object"

        # 1. Create Firewall object from text
        myobj = firewall.Firewall(part2=True, text=aoc_20.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ f i r e w a l l . p y                end
# ======================================================================
