
# ======================================================================
# Guard Gallivant
#   Advent of Code 2024 Day 06 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ g u a r d . p y
# ======================================================================
"Test Guard for Advent of Code 2024 day 06, Guard Gallivant"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import guard

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
OBS = frozenset({(0, 4), (6, 1), (1, 9), (9, 6), (8, 0), (3, 2), (4, 7), (7, 8)})
OBS1 = frozenset({(0, 4), (6, 1), (1, 9), (9, 6), (8, 0), (3, 2), (4, 7), (7, 8), (6, 3)})
OBS2 = frozenset({(0, 4), (6, 1), (1, 9), (9, 6), (8, 0), (3, 2), (4, 7), (7, 8), (7, 6)}) # Problem


# ======================================================================
#                                                              TestGuard
# ======================================================================


class TestGuard(unittest.TestCase):  # pylint: disable=R0904
    "Test Guard object"

    def test_empty_init(self):
        "Test the default Guard creation"

        # 1. Create default Guard object
        myobj = guard.Guard()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.dir, "^")
        self.assertEqual(myobj.loc, (0, 0))
        self.assertEqual(myobj.max_loc, (0, 0))

    def test_text_init(self):
        "Test the Guard object creation from text"

        # 1. Create Guard object from text
        myobj = guard.Guard(direction="^", loc=(6, 4), max_loc=(10, 10))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.dir, "^")
        self.assertEqual(myobj.loc, (6, 4))
        self.assertEqual(myobj.max_loc, (10, 10))

        # 3. Check methods
        self.assertEqual(len(myobj.multiple_steps(OBS)), 41)
        myobj.reset()
        self.assertEqual(len(myobj.multiple_steps(OBS)), 41)
        myobj.reset()
        self.assertEqual(myobj.loop_steps(OBS), False)
        myobj.reset()
        self.assertEqual(myobj.loop_steps(OBS1), True)
        myobj.reset()
        self.assertEqual(myobj.loop_steps(OBS2), True)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ g u a r d . p y                   end
# ======================================================================
