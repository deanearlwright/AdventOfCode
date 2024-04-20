
# ======================================================================
# Aplenty
#   Advent of Code 2023 Day 19 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                        t e s t _ r u l e . p y
# ======================================================================
"Test Rule for Advent of Code 2023 day 19, Aplenty"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import rule
from part import Part

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = "m>2090:A"

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
        self.assertEqual(myobj.category, "")
        self.assertEqual(myobj.test, "")
        self.assertEqual(myobj.value, 0)
        self.assertEqual(myobj.branch, "")

    def test_text_init(self):
        "Test the Rule object creation from text"

        # 1. Create Rule object from text
        myobj = rule.Rule(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 8)
        self.assertEqual(myobj.category, "m")
        self.assertEqual(myobj.test, ">")
        self.assertEqual(myobj.value, 2090)
        self.assertEqual(myobj.branch, "A")

        # 3. Check methods
        self.assertEqual(myobj.evaluate(Part("{x=787,m=2655,a=1222,s=2876}")), "A")
        self.assertEqual(myobj.evaluate(Part("{x=787,m=1655,a=1222,s=2876}")), None)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                     t e s t _ r u l e . p y                    end
# ======================================================================
