# ======================================================================
# Scrambled Letters and Hash
#   Advent of Code 2016 Day 21 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ p w o r d . p y
# ======================================================================
"Test solver for Advent of Code 2016 day 21, Scrambled Letters and Hash"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_21
import pword

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
swap position 4 with position 0
swap letter d with letter b
reverse positions 0 through 4
rotate left 1 step
move position 1 to position 4
move position 3 to position 0
rotate based on position of letter b
rotate based on position of letter d
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_WORD = "abcde"
PART_TWO_WORD = "decab"

PART_ONE_RESULT = "decab"
PART_TWO_RESULT = "abcde"

# ======================================================================
#                                                              TestPword
# ======================================================================


class TestPword(unittest.TestCase):  # pylint: disable=R0904
    "Test Pword object"

    def test_empty_init(self):
        "Test the default Pword creation"

        # 1. Create default Pword object
        myobj = pword.Pword()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)

    def test_text_init(self):
        "Test the Pword object creation from text"

        # 1. Create Pword object from text
        myobj = pword.Pword(text=aoc_21.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 8)

        # 3. Check methods
        self.assertEqual(myobj.execute('swap position 4 with position 0', 'abcde'), 'ebcda')
        self.assertEqual(myobj.execute('swap letter d with letter b', 'ebcda'), 'edcba')
        self.assertEqual(myobj.execute('reverse positions 0 through 4', 'edcba'), 'abcde')
        self.assertEqual(myobj.execute('rotate left 1 step', 'abcde'), 'bcdea')
        self.assertEqual(myobj.execute('move position 1 to position 4', 'bcdea'), 'bdeac')
        self.assertEqual(myobj.execute('move position 3 to position 0', 'bdeac'), 'abdec')
        self.assertEqual(myobj.execute('rotate based on position of letter b', 'abdec'), 'ecabd')
        self.assertEqual(myobj.execute('rotate based on position of letter d', 'ecabd'), 'decab')

        self.assertEqual(myobj.unexecute('swap position 4 with position 0', 'ebcda'), 'abcde')
        self.assertEqual(myobj.unexecute('swap letter d with letter b', 'edcba'), 'ebcda')
        self.assertEqual(myobj.unexecute('reverse positions 0 through 4', 'abcde'), 'edcba')
        self.assertEqual(myobj.unexecute('rotate left 1 step', 'bcdea'), 'abcde')
        self.assertEqual(myobj.unexecute('move position 1 to position 4', 'bdeac'), 'bcdea')
        self.assertEqual(myobj.unexecute('move position 3 to position 0', 'abdec'), 'bdeac')
        self.assertEqual(myobj.unexecute('rotate based on position of letter b', 'ecabd'), 'abdec')
        self.assertEqual(myobj.unexecute('rotate based on position of letter d', 'decab'), 'ecabd')

    def test_part_one(self):
        "Test part one example of Pword object"

        # 1. Create Pword object from text
        myobj = pword.Pword(text=aoc_21.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False, word=PART_ONE_WORD), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Pword object"

        # 1. Create Pword object from text
        myobj = pword.Pword(part2=True, text=aoc_21.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False, word=PART_TWO_WORD), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ p w o r d . p y                   end
# ======================================================================
