# ======================================================================
# Ticket Translation
#   Advent of Code 2020 Day 16 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         t e s t _ r u l e . p y
# ======================================================================
"Test Rule class for Advent of Code 2020 day 16, Ticket Translation"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import rule

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = "row: 6-11 or 33-44"

# ======================================================================
#                                                               TestRule
# ======================================================================


class TestRule(unittest.TestCase):  # pylint: disable=R0904
    "Test Rule object"

    def test_empty_init(self):
        "Test the default Rule creation"

        # 1. Create default Rule object
        myobj = rule.Rule()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.name, None)
        self.assertEqual(myobj.ranges, [])

    def test_text_init(self):
        "Test the Rule object creation from text"

        # 1. Create Rule object from text
        myobj = rule.Rule(EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, EXAMPLE_TEXT)
        self.assertEqual(myobj.name, 'row')
        self.assertEqual(len(myobj.ranges), 2)
        self.assertEqual(myobj.ranges[0][0], 6)
        self.assertEqual(myobj.ranges[0][1], 11)
        self.assertEqual(myobj.ranges[1][0], 33)
        self.assertEqual(myobj.ranges[1][1], 44)

        # 3. Test methods
        self.assertEqual(myobj.is_valid(1), False)
        self.assertEqual(myobj.is_valid(6), True)
        self.assertEqual(myobj.is_valid(7), True)
        self.assertEqual(myobj.is_valid(11), True)
        self.assertEqual(myobj.is_valid(12), False)
        self.assertEqual(myobj.is_valid(40), True)
        self.assertEqual(myobj.is_valid(45), False)
        self.assertEqual(myobj.is_valid(50), False)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      t e s t _ r u l e . p y                   end
# ======================================================================
