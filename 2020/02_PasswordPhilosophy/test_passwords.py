# ======================================================================
# Password Philosophy
#   Advent of Code 2020 Day 02 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ p a s s w o r d s . p y
# ======================================================================
"Test solver for Advent of Code 2020 day 02, Password Philosophy"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_02
import passwords

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 2
PART_TWO_RESULT = 1

# ======================================================================
#                                                          TestPasswords
# ======================================================================


class TestPasswords(unittest.TestCase):  # pylint: disable=R0904
    "Test Passwords object"

    def test_empty_init(self):
        "Test the default Passwords creation"

        # 1. Create default Passwords object
        myobj = passwords.Passwords()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)

    def test_text_init(self):
        "Test the Passwords object creation from text"

        # 1. Create Passwords object from text
        myobj = passwords.Passwords(text=aoc_02.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 3)

    def test_part_one(self):
        "Test part one example of Passwords object"

        # 1. Create Passwords object from text
        myobj = passwords.Passwords(text=aoc_02.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Passwords object"

        # 1. Create Passwords object from text
        myobj = passwords.Passwords(part2=True,
                                    text=aoc_02.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                t e s t _ p a s s w o r d s . p y               end
# ======================================================================
