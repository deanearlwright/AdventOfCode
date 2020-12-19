# ======================================================================
# Monster Messages
#   Advent of Code 2020 Day 19 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ r u l e s . p y
# ======================================================================
"Test single rule for Advent of Code 2020 day 19, Monster Messages"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import rule

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_ZERO = '0: 4 1 5'
EXAMPLE_ONE = '1: 2 3 | 3 2'
EXAMPLE_FOUR = '4: "a"'

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
        self.assertEqual(myobj.number, None)
        self.assertEqual(myobj.definition, None)

    def test_text_zero(self):
        "Test the Rule object creation from text with one alternate"

        # 1. Create Rule object from text
        myobj = rule.Rule(EXAMPLE_ZERO)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 8)
        self.assertEqual(myobj.number, 0)
        self.assertEqual(myobj.definition, '4 1 5')

        # 3. Check methods
        self.assertEqual(myobj.is_constant(), False)
        self.assertEqual(myobj.alternatives(), ['4 1 5'])

    def test_text_one(self):
        "Test the Rule object creation from text with two alternates"

        # 1. Create Rule object from text
        myobj = rule.Rule(EXAMPLE_ONE)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 12)
        self.assertEqual(myobj.number, 1)
        self.assertEqual(myobj.definition, '2 3 | 3 2')

        # 3. Check methods
        self.assertEqual(myobj.is_constant(), False)
        self.assertEqual(myobj.alternatives(), ['2 3 ', ' 3 2'])

    def test_text_four(self):
        "Test the Rule object creation from text with constant rule"

        # 1. Create Rule object from text
        myobj = rule.Rule(EXAMPLE_FOUR)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 6)
        self.assertEqual(myobj.number, 4)
        self.assertEqual(myobj.definition, '"a"')

        # 3. Check methods
        self.assertEqual(myobj.is_constant(), True)
        self.assertEqual(myobj.letter(), 'a')


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      t e s t _ r u l e . p y                   end
# ======================================================================
