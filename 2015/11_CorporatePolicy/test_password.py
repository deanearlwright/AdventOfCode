# ======================================================================
# Corporate Policy
#   Advent of Code 2015 Day 11 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ p a s s w o r d . p y
# ======================================================================
"Test solver for Advent of Code 2015 day 11, Corporate Policy"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_11
import password

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
abcdefgh
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = "abcdffaa"
PART_TWO_RESULT = "abcdffbb"

# ======================================================================
#                                                           TestPassword
# ======================================================================


class TestPassword(unittest.TestCase):  # pylint: disable=R0904
    "Test Password object"

    def test_empty_init(self):
        "Test the default Password creation"

        # 1. Create default Password object
        myobj = password.Password()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)

    def test_text_init(self):
        "Test the Password object creation from text"

        # 1. Create Password object from text
        myobj = password.Password(text=aoc_11.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 1)

        # 3. Check methods
        self.assertEqual(myobj.valid_password("hijklmmn"), False)
        self.assertEqual(myobj.valid_password("abbceffg"), False)
        self.assertEqual(myobj.valid_password("abbcegjk"), False)
        self.assertEqual(myobj.valid_password("abcdffaa"), True)
        self.assertEqual(myobj.valid_password("ghjaabcc"), True)

        self.assertEqual(myobj.next_password(), "abcdffaa")
        myobj.current = "ghijklmn"
        self.assertEqual(myobj.next_password(), "ghjaabcc")

    def test_part_one(self):
        "Test part one example of Password object"

        # 1. Create Password object from text
        myobj = password.Password(text=aoc_11.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Password object"

        # 1. Create Password object from text
        myobj = password.Password(part2=True, text=aoc_11.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ p a s s w o r d . p y                end
# ======================================================================
