
# ======================================================================
# Scratchcards
#   Advent of Code 2023 Day 04 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ c a r d . p y
# ======================================================================
"Test Card for Advent of Code 2023 day 04, Scratchcards"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import card

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"

# ======================================================================
#                                                             TestCard
# ======================================================================


class TestCard(unittest.TestCase):  # pylint: disable=R0904
    "Test Card object"

    def test_empty_init(self):
        "Test the default Card creation"

        # 1. Create default Card object
        myobj = card.Card()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.id, 0)
        self.assertEqual(len(myobj.winning), 0)
        self.assertEqual(len(myobj.having), 0)

    def test_text_init(self):
        "Test the Card object creation from text"

        # 1. Create Card object from text
        myobj = card.Card(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 48)
        self.assertEqual(myobj.id, 1)
        self.assertEqual(len(myobj.winning), 5)
        self.assertEqual(len(myobj.having), 8)
        self.assertTrue(41 in myobj.winning)
        self.assertTrue(83 in myobj.having)

        # 3. Check methods
        self.assertEqual(len(myobj.matches()), 4)
        self.assertEqual(myobj.score(), 8)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ c a r d . p y                end
# ======================================================================
