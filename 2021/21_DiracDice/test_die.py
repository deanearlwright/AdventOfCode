# ======================================================================
# Dirac Dice
#   Advent of Code 2021 Day 21 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ d i e . p y
# ======================================================================
"Test Die for Advent of Code 2021 day 21, Dirac Dice"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import die

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = "100"

# ======================================================================
#                                                                TestDie
# ======================================================================


class TestDie(unittest.TestCase):  # pylint: disable=R0904
    "Test Die object"

    def test_empty_init(self):
        "Test the default Die creation"

        # 1. Create default Die object
        myobj = die.Die()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.rolled, 0)
        self.assertEqual(myobj.sides, 100)
        self.assertEqual(myobj.last, 0)

    def test_text_init(self):
        "Test the Die object creation from text"

        # 1. Create Die object from text
        myobj = die.Die(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 3)
        self.assertEqual(myobj.rolled, 0)
        self.assertEqual(myobj.sides, 100)
        self.assertEqual(myobj.last, 0)

        # 3. Check methods
        self.assertEqual(myobj.roll(), 1)
        self.assertEqual(myobj.rolled, 1)
        self.assertEqual(myobj.last, 1)
        self.assertEqual(myobj.roll(), 2)
        self.assertEqual(myobj.rolled, 2)
        self.assertEqual(myobj.last, 2)
        myobj.last = 99
        self.assertEqual(myobj.last, 99)
        self.assertEqual(myobj.roll(), 100)
        self.assertEqual(myobj.rolled, 3)
        self.assertEqual(myobj.last, 100)
        self.assertEqual(myobj.roll(), 1)
        self.assertEqual(myobj.rolled, 4)
        self.assertEqual(myobj.last, 1)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ d i e . p y                end
# ======================================================================
