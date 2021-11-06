# ======================================================================
# Wizard Simulator 20XX
#   Advent of Code 2015 Day 22 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ s t a t e . p y
# ======================================================================
"Test State for Advent of Code 2015 day 22, Wizard Simulator 20XX"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import state

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = ""

# ======================================================================
#                                                              TestState
# ======================================================================


class TestState(unittest.TestCase):  # pylint: disable=R0904
    "Test State object"

    def test_empty_init(self):
        "Test the default State creation"

        # 1. Create default Shop object
        myobj = state.State()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.turn, 0)
        self.assertEqual(myobj.wizard, None)
        self.assertEqual(myobj.boss, None)
        self.assertEqual(len(myobj.active), 0)
        self.assertEqual(len(myobj.tried), 0)

        # 3. Check methods


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ s t a t e . p y                   end
# ======================================================================
