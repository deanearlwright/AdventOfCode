# ======================================================================
# RPG Simulator 20XX
#   Advent of Code 2015 Day 21 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ s h o p . p y
# ======================================================================
"Test Shop for Advent of Code 2015 day 21, RPG Simulator 20XX"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import shop

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = ""

# ======================================================================
#                                                               TestShop
# ======================================================================


class TestShop(unittest.TestCase):  # pylint: disable=R0904
    "Test Shop object"

    def test_empty_init(self):
        "Test the default Shop creation"

        # 1. Create default Shop object
        myobj = shop.Shop()

        # 2. Make sure it has the default values
        self.assertEqual(len(myobj.items), 19)

        # 3. Check methods
        self.assertEqual(len(list(myobj.combinations())), 1680)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                     t e s t _ s h o p . p y                    end
# ======================================================================
