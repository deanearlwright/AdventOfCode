# ======================================================================
# The Sum of Its Parts
#   Advent of Code 2018 Day 07 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                      t e s t _ s t e p . p y
# ======================================================================
"Test step for Advent of Code 2018 day 07, The Sum of Its Parts"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import step

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                               TestStep
# ======================================================================


class TestStep(unittest.TestCase):  # pylint: disable=R0904
    "Test Step object"

    def test_empty_init(self):
        "Test the default Step creation"

        # 1. Create default Step object
        myobj = step.Step()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.letter, None)
        self.assertEqual(len(myobj.before), 0)

    def test_init_with_letter(self):
        "Test the Step creation with an argument"

        # 1. Create default Step object
        myobj = step.Step(letter='A')

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.letter, 'A')
        self.assertEqual(len(myobj.before), 0)

        # 3. Add a prereq
        myobj.add_before('C')
        self.assertEqual(myobj.letter, 'A')
        self.assertEqual(len(myobj.before), 1)
        self.assertEqual(myobj.before, set('C'))


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                     t e s t _ s t e p . p y                    end
# ======================================================================
