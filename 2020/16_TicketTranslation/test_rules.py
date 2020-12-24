# ======================================================================
# Ticket Translation
#   Advent of Code 2020 Day 16 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                        t e s t _ r u l e s . p y
# ======================================================================
"Test Rules class for Advent of Code 2020 day 16, Ticket Translation"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import rules

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = [
    "class: 1-3 or 5-7",
    "row: 6-11 or 33-44",
    "seat: 13-40 or 45-50",
    "your ticket:",
    "7,1,14"
]

# ======================================================================
#                                                              TestRules
# ======================================================================


class TestRules(unittest.TestCase):  # pylint: disable=R0904
    "Test Rules object"

    def test_empty_init(self):
        "Test the default Rules creation"

        # 1. Create default Rules object
        myobj = rules.Rules()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.rules, [])
        self.assertEqual(len(myobj), 0)

    def test_text_init(self):
        "Test the Rules object creation from text"

        # 1. Create Rules object from text
        myobj = rules.Rules(EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, EXAMPLE_TEXT)
        self.assertEqual(len(myobj.rules), 3)
        self.assertEqual(len(myobj), 3)

        # 3. Test methods
        self.assertEqual(myobj.is_valid(1), True)
        self.assertEqual(myobj.is_valid(4), False)
        self.assertEqual(myobj.is_valid(6), True)
        self.assertEqual(myobj.is_valid(11), True)
        self.assertEqual(myobj.is_valid(12), False)
        self.assertEqual(myobj.is_valid(45), True)
        self.assertEqual(myobj.is_valid(99), False)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                     t e s t _ r u l e s . p y                  end
# ======================================================================
