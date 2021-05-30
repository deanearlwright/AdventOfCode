# ======================================================================
# Bathroom Security
#   Advent of Code 2016 Day 02 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ k e y p a d . p y
# ======================================================================
"Test solver for Advent of Code 2016 day 02, Bathroom Security"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_02
import keypad

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
ULL
RRDDD
LURDL
UUUUD
"""

PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = "1985"
PART_TWO_RESULT = "5DB3"

# ======================================================================
#                                                             TestKeypad
# ======================================================================


class TestKeypad(unittest.TestCase):  # pylint: disable=R0904
    "Test Keypad object"

    def test_empty_init(self):
        "Test the default Keypad creation"

        # 1. Create default Keypad object
        myobj = keypad.Keypad()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.keypad[myobj.location], '5')

        # 3. Check methods
        self.assertEqual(myobj.at(), '5')
        self.assertEqual(myobj.can_go('U'), True)
        self.assertEqual(myobj.can_go('D'), True)
        self.assertEqual(myobj.can_go('L'), True)
        self.assertEqual(myobj.can_go('R'), True)
        self.assertEqual(myobj.move('U'), True)
        self.assertEqual(myobj.at(), '2')
        self.assertEqual(myobj.move('U'), False)
        self.assertEqual(myobj.at(), '2')
        self.assertEqual(myobj.move('L'), True)
        self.assertEqual(myobj.at(), '1')
        self.assertEqual(myobj.move('L'), False)
        self.assertEqual(myobj.at(), '1')
        self.assertEqual(myobj.one_line("RRDDD"), '9')

    def test_text_init(self):
        "Test the Keypad object creation from text"

        # 1. Create Keypad object from text
        myobj = keypad.Keypad(text=aoc_02.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 4)
        self.assertEqual(keypad.KEYPAD_ONE[myobj.location], '5')

        # 3. Check methods
        self.assertEqual(myobj.get_code(), "1985")

    def test_part_one(self):
        "Test part one example of Keypad object"

        # 1. Create Keypad object from text
        myobj = keypad.Keypad(text=aoc_02.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Keypad object"

        # 1. Create Keypad object from text
        myobj = keypad.Keypad(part2=True, text=aoc_02.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ k e y p a d . p y                  end
# ======================================================================
