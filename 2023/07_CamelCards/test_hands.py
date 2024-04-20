
# ======================================================================
# Camel Cards
#   Advent of Code 2023 Day 07 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ h a n d s . p y
# ======================================================================
"Test Hands for Advent of Code 2023 day 07, Camel Cards"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import hands
import hand

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = [
    "32T3K 765",
    "T55J5 684",
    "KK677 28",
    "KTJJT 220",
    "QQQJA 483",
]

# ======================================================================
#                                                              TestHands
# ======================================================================


class TestHands(unittest.TestCase):  # pylint: disable=R0904
    "Test Hands object"

    def test_empty_init(self):
        "Test the default Hands creation"

        # 1. Create default Hands object
        myobj = hands.Hands()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.hands), 0)

    def test_text_init(self):
        "Test the Hands object creation from text"

        # 1. Create Hands object from text
        myobj = hands.Hands(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 5)
        self.assertEqual(len(myobj.hands), 5)
        self.assertEqual(myobj.hands[0].type, hand.ONE_PAIR)
        self.assertEqual(myobj.hands[1].type, hand.THREE_OF_A_KIND)
        self.assertEqual(myobj.hands[2].type, hand.TWO_PAIR)
        self.assertEqual(myobj.hands[3].type, hand.TWO_PAIR)
        self.assertEqual(myobj.hands[4].type, hand.THREE_OF_A_KIND)
        self.assertEqual(myobj.hands[0].key, 20302100313)
        self.assertEqual(myobj.hands[1].key, 41005051105)
        self.assertEqual(myobj.hands[2].key, 31313060707)
        self.assertEqual(myobj.hands[3].key, 31310111110)
        self.assertEqual(myobj.hands[4].key, 41212121114)

        # 3. Check methods
        self.assertEqual(myobj.winnings(), 6440)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ h a n d s . p y                   end
# ======================================================================
