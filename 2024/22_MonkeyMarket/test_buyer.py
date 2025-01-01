
# ======================================================================
# Monkey Market
#   Advent of Code 2024 Day 22 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ b u y e r . p y
# ======================================================================
"Test Buyer for Advent of Code 2024 day 22, Monkey Market"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import buyer

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = ""

# ======================================================================
#                                                              TestBuyer
# ======================================================================


class TestBuyer(unittest.TestCase):  # pylint: disable=R0904
    "Test Buyer object"

    def test_empty_init(self):
        "Test the default Buyer creation"

        # 1. Create default Buyer object
        myobj = buyer.Buyer()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.initial, 0)
        self.assertEqual(myobj.secret, 0)

    def test_text_init(self):
        "Test the Buyer object creation from text"

        # 1. Create Buyer object from text
        myobj = buyer.Buyer(initial=123)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.initial, 123)
        self.assertEqual(myobj.secret, 123)

        # 3. Check methods
        self.assertEqual(myobj.mix(42, 15), 37)
        self.assertEqual(myobj.prune(100000000), 16113920)

        self.assertEqual(myobj.price(), 3)
        self.assertEqual(myobj.evolve(), 15887950)
        self.assertEqual(myobj.price(), 0)
        self.assertEqual(myobj.evolve(), 16495136)
        self.assertEqual(myobj.price(), 6)
        self.assertEqual(myobj.evolve(), 527345)
        self.assertEqual(myobj.price(), 5)
        self.assertEqual(myobj.evolve(), 704524)
        self.assertEqual(myobj.price(), 4)
        self.assertEqual(myobj.evolve(), 1553684)
        self.assertEqual(myobj.price(), 4)
        self.assertEqual(myobj.evolve(), 12683156)
        self.assertEqual(myobj.price(), 6)
        self.assertEqual(myobj.evolve(), 11100544)
        self.assertEqual(myobj.price(), 4)
        self.assertEqual(myobj.evolve(), 12249484)
        self.assertEqual(myobj.price(), 4)
        self.assertEqual(myobj.evolve(), 7753432)
        self.assertEqual(myobj.price(), 2)
        self.assertEqual(myobj.evolve(), 5908254)

        self.assertEqual(myobj.price_n(0), 3)
        self.assertEqual(myobj.price_n(1), 0)
        self.assertEqual(myobj.price_n(2), 6)
        self.assertEqual(myobj.price_n(3), 5)
        self.assertEqual(myobj.price_n(4), 4)
        self.assertEqual(myobj.price_n(5), 4)
        self.assertEqual(myobj.price_n(6), 6)
        self.assertEqual(myobj.price_n(7), 4)
        self.assertEqual(myobj.price_n(8), 4)

        self.assertEqual(myobj.delta_n(0), -3)
        self.assertEqual(myobj.delta_n(1), 6)
        self.assertEqual(myobj.delta_n(2), -1)
        self.assertEqual(myobj.delta_n(3), -1)
        self.assertEqual(myobj.delta_n(4), 0)
        self.assertEqual(myobj.delta_n(5), 2)
        self.assertEqual(myobj.delta_n(6), -2)
        self.assertEqual(myobj.delta_n(7), 0)
        self.assertEqual(myobj.delta_n(8), -2)

        self.assertEqual(myobj.deltas_n(0), (-3, 6, -1, -1))
        self.assertEqual(myobj.deltas_n(1), (6, -1, -1, 0))
        self.assertEqual(myobj.deltas_n(2), (-1, -1, 0, 2))
        self.assertEqual(myobj.deltas_n(3), (-1, 0, 2, -2))

        self.assertEqual(len(myobj.memo), 0)
        self.assertEqual(len(myobj.deltas_to_bananas()), 7)
        self.assertEqual(len(myobj.memo), 7)

        self.assertEqual(myobj.buy_at((-3, 6, -1, -1)), 4)
        self.assertEqual(myobj.buy_at((6, -1, -1, 0)), 4)
        self.assertEqual(myobj.buy_at((-1, -1, 0, 2)), 6)
        self.assertEqual(myobj.buy_at((-1, 0, 2, -2)), 4)
        self.assertEqual(myobj.buy_at((-1, -1, 0, 7)), 0)
        self.assertEqual(myobj.buy_at((7, -1, 0, 2)), 0)
        self.assertEqual(myobj.buy_at((2, -2, 0, -2)), 2)
        self.assertEqual(myobj.buy_at((0, 2, -2, 0)), 4)

        myobj.reset()
        self.assertEqual(myobj.darwin(10), 5908254)

        myobj.reset(1)
        self.assertEqual(myobj.darwin(2000), 8685429)
        myobj.reset(10)
        self.assertEqual(myobj.darwin(2000), 4700978)
        myobj.reset(100)
        self.assertEqual(myobj.darwin(2000), 15273692)
        myobj.reset(2024)
        self.assertEqual(myobj.darwin(2000), 8667524)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ b u y e r . p y                   end
# ======================================================================
