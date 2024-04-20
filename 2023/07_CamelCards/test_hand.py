
# ======================================================================
# Camel Cards
#   Advent of Code 2023 Day 07 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ h a n d . p y
# ======================================================================
"Test Hand for Advent of Code 2023 day 07, Camel Cards"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import hand

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = "32T3K 765"

# ======================================================================
#                                                               TestHand
# ======================================================================


class TestHand(unittest.TestCase):  # pylint: disable=R0904
    "Test Hand object"

    def test_empty_init(self):
        "Test the default Hand creation"

        # 1. Create default Hand object
        myobj = hand.Hand()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.cards, "")
        self.assertEqual(myobj.bid, 0)
        self.assertEqual(myobj.type, 0)
        self.assertEqual(myobj.key, 0)

    def test_text_init(self):
        "Test the Hand object creation from text"

        # 1. Create Hand object from text
        myobj = hand.Hand(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 9)
        self.assertEqual(myobj.cards, "32T3K")
        self.assertEqual(myobj.bid, 765)
        self.assertEqual(myobj.type, hand.ONE_PAIR)
        self.assertEqual(myobj.key, 20302100313)

        # 3. Check method
        self.assertEqual(myobj.winnings(1), 765)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                     t e s t _ h a n d . p y                    end
# ======================================================================
