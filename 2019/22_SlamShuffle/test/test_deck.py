# ======================================================================
# Slam Shuffle
#   Advent of Code 2019 Day 11 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                      t e s t _ d e c k . p y
# ======================================================================
"Test space deck for Advent of Code 2019 day 22, Slam Shuffle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import deck

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
INSTRUCTIONS = [
['deal with increment 7',
 'deal into new stack',
 'deal into new stack'],
['cut 6',
 'deal with increment 7',
 'deal into new stack'],
['deal with increment 7',
 'deal with increment 9',
 'cut -2'],
['deal into new stack',
 'cut -2',
 'deal with increment 7',
 'cut 8',
 'cut -4',
 'deal with increment 7',
 'cut 3',
 'deal with increment 9',
 'deal with increment 3',
 'cut -1']
]

INSTRUCTION_RESULTS = [
'0 3 6 9 2 5 8 1 4 7',
'3 0 7 4 1 8 5 2 9 6',
'6 3 0 7 4 1 8 5 2 9',
'9 2 5 8 1 4 7 0 3 6']

# ======================================================================
#                                                               TestDeck
# ======================================================================


class TestDeck(unittest.TestCase):  # pylint: disable=R0904
    """Test Deck object"""

    def test_empty_init(self):
        """Test default Deck object creation"""

        # 1. Create default Deck object
        mydeck = deck.Deck()

        # 2. Make sure it has the default values
        self.assertEqual(mydeck.size, deck.DEFAULT_SIZE)
        self.assertEqual(len(mydeck.cards), deck.DEFAULT_SIZE)

        # 3. Check methods
        self.assertEqual(str(mydeck), '0 1 2 3 4 ... 10002 10003 10004 10005 10006')
        mydeck.deal_into_new_stack()
        self.assertEqual(len(mydeck.cards), deck.DEFAULT_SIZE)
        self.assertEqual(str(mydeck), '10006 10005 10004 10003 10002 ... 4 3 2 1 0')
        mydeck.cut(3)
        self.assertEqual(len(mydeck.cards), deck.DEFAULT_SIZE)
        self.assertEqual(str(mydeck), '10003 10002 10001 10000 9999 ... 1 0 10006 10005 10004')
        mydeck.cut(-3)
        self.assertEqual(len(mydeck.cards), deck.DEFAULT_SIZE)
        self.assertEqual(str(mydeck), '10006 10005 10004 10003 10002 ... 4 3 2 1 0')
        mydeck.deal_with_increment(3)
        self.assertEqual(len(mydeck.cards), deck.DEFAULT_SIZE)
        self.assertEqual(str(mydeck), '10006 6670 3334 10005 6669 ... 6672 3336 0 6671 3335')
        self.assertEqual(mydeck.position(10006), 0)
        self.assertEqual(mydeck.position(6670), 1)
        self.assertEqual(mydeck.position(3334), 2)
        self.assertEqual(mydeck.position(10005), 3)
        self.assertEqual(mydeck.position(6669), 4)
        self.assertEqual(mydeck.position(6672), 10002)
        self.assertEqual(mydeck.position(3336), 10003)
        self.assertEqual(mydeck.position(0), 10004)
        self.assertEqual(mydeck.position(6671), 10005)
        self.assertEqual(mydeck.position(3335), 10006)


    def test_value_10_init(self):
        "Test Deck object creation with 10 cards"

        # 1. Create default Deck object
        mydeck = deck.Deck(size=10)

        # 2. Make sure it has the specified values
        self.assertEqual(mydeck.size, 10)
        self.assertEqual(len(mydeck.cards), 10)

        # 3. Check methods
        self.assertEqual(str(mydeck), '0 1 2 3 4 5 6 7 8 9')
        mydeck.deal_into_new_stack()
        self.assertEqual(len(mydeck.cards), 10)
        self.assertEqual(str(mydeck), '9 8 7 6 5 4 3 2 1 0')
        mydeck.deal_into_new_stack()
        self.assertEqual(len(mydeck.cards), 10)
        self.assertEqual(str(mydeck), '0 1 2 3 4 5 6 7 8 9')
        mydeck.cut(3)
        self.assertEqual(len(mydeck.cards), 10)
        self.assertEqual(str(mydeck), '3 4 5 6 7 8 9 0 1 2')
        mydeck.cut(-3)
        self.assertEqual(len(mydeck.cards), 10)
        self.assertEqual(str(mydeck), '0 1 2 3 4 5 6 7 8 9')
        mydeck.deal_with_increment(3)
        self.assertEqual(len(mydeck.cards), 10)
        self.assertEqual(str(mydeck), '0 7 4 1 8 5 2 9 6 3')
        self.assertEqual(mydeck.position(0), 0)
        self.assertEqual(mydeck.position(7), 1)
        self.assertEqual(mydeck.position(4), 2)
        self.assertEqual(mydeck.position(1), 3)
        self.assertEqual(mydeck.position(8), 4)
        self.assertEqual(mydeck.position(5), 5)
        self.assertEqual(mydeck.position(2), 6)
        self.assertEqual(mydeck.position(9), 7)
        self.assertEqual(mydeck.position(6), 8)
        self.assertEqual(mydeck.position(3), 9)

    def test_value_17_init(self):
        "Test Deck object creation with 17 cards"

        # 1. Create default Deck object
        mydeck = deck.Deck(size=17)

        # 2. Make sure it has the specified values
        self.assertEqual(mydeck.size, 17)
        self.assertEqual(len(mydeck.cards), 17)

        # 3. Check methods
        self.assertEqual(str(mydeck), '0 1 2 3 4 ... 12 13 14 15 16')
        mydeck.deal_into_new_stack()
        self.assertEqual(len(mydeck.cards), 17)
        self.assertEqual(str(mydeck), '16 15 14 13 12 ... 4 3 2 1 0')
        mydeck.deal_into_new_stack()
        self.assertEqual(len(mydeck.cards), 17)
        self.assertEqual(str(mydeck), '0 1 2 3 4 ... 12 13 14 15 16')
        mydeck.cut(3)
        self.assertEqual(len(mydeck.cards), 17)
        self.assertEqual(str(mydeck), '3 4 5 6 7 ... 15 16 0 1 2')
        mydeck.cut(-3)
        self.assertEqual(len(mydeck.cards), 17)
        self.assertEqual(str(mydeck), '0 1 2 3 4 ... 12 13 14 15 16')
        mydeck.deal_with_increment(3)
        self.assertEqual(len(mydeck.cards), 17)
        self.assertEqual(str(mydeck), '0 6 12 1 7 ... 4 10 16 5 11')
        self.assertEqual(mydeck.position(0), 0)
        self.assertEqual(mydeck.position(6), 1)
        self.assertEqual(mydeck.position(12), 2)
        self.assertEqual(mydeck.position(1), 3)
        self.assertEqual(mydeck.position(7), 4)
        self.assertEqual(mydeck.position(4), 12)
        self.assertEqual(mydeck.position(10), 13)
        self.assertEqual(mydeck.position(16), 14)
        self.assertEqual(mydeck.position(5), 15)
        self.assertEqual(mydeck.position(11), 16)

    def test_instructions(self):
        "Test Deck object with multiple instructions"

        # 1. Loop for all of the instructions
        for inum, insts in enumerate(INSTRUCTIONS):

            # 2. Create a deck and execute the instructions
            mydeck = deck.Deck(size=10)
            mydeck.instructions(insts)

            # 3. Check the result
            self.assertEqual(str(mydeck), INSTRUCTION_RESULTS[inum])

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                     t e s t _ d e c k . p y                    end
# ======================================================================
