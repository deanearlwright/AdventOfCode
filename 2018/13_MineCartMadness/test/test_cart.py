# ======================================================================
# Mine Cart Madness
#   Advent of Code 2018 Day 13 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                        t e s t _ c a r t . p y
# ======================================================================
"Test Carts for day 13 of Advent of Code 2018, Mine Cart Madness"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import cart

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------


# ======================================================================
#                                                               TestCart
# ======================================================================


class TestCart(unittest.TestCase):  # pylint: disable=R0904
    """Test Cart object"""

    def test_empty_init(self):
        """Test default Cart object creation"""

        # 1. Create default Cart object
        mycart = cart.Cart()

        # 2. Make sure it has the default values
        self.assertEqual(mycart.location, (0, 0))
        self.assertEqual(mycart.direction, '^')
        self.assertEqual(mycart.crossings, 0)
        self.assertEqual(mycart.crashed, None)
        self.assertEqual(mycart.space, '|')

        # 3. Check methods
        self.assertEqual(str(mycart), 'cart: l=(0, 0) d=^ x=0 c=None s=|')


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ c a r t . p y                     end
# ======================================================================
