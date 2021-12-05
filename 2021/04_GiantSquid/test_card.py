# ======================================================================
# Giant Squid
#   Advent of Code 2021 Day 04 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                      t e s t _ c a r d . p y
# ======================================================================
"Test Card for Advent of Code 2021 day 04, Giant Squid"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_04
import card

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""

# ======================================================================
#                                                               TestCard
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
        self.assertEqual(myobj.numbers, None)
        self.assertEqual(myobj.called, None)
        self.assertEqual(myobj.last, None)

    def test_text_init(self):
        "Test the Card object creation from text"

        # 1. Create Card object from text
        myobj = card.Card(text=aoc_04.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 5)
        self.assertEqual(len(myobj.numbers), 25)
        self.assertEqual(len(myobj.called), 25)
        self.assertEqual(myobj.last, None)
        self.assertEqual(myobj.has_won, False)

        # 3. Check methods
        self.assertEqual(myobj.covered(), 0)
        self.assertEqual(myobj.call(7), False)
        self.assertEqual(myobj.last, 7)
        self.assertEqual(myobj.covered(), 1)
        self.assertEqual(myobj.call(4), False)
        self.assertEqual(myobj.covered(), 2)
        self.assertEqual(myobj.call(9), False)
        self.assertEqual(myobj.call(5), False)
        self.assertEqual(myobj.call(11), False)
        self.assertEqual(myobj.call(17), False)
        self.assertEqual(myobj.last, 17)
        self.assertEqual(myobj.call(23), False)
        self.assertEqual(myobj.call(2), False)
        self.assertEqual(myobj.call(0), False)
        self.assertEqual(myobj.call(14), False)
        self.assertEqual(myobj.call(21), False)
        self.assertEqual(myobj.has_won, False)
        self.assertEqual(myobj.call(24), True)
        self.assertEqual(myobj.has_won, True)
        self.assertEqual(myobj.covered(), 12)
        self.assertEqual(myobj.score(), 4512)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                     t e s t _ c a r d . p y                    end
# ======================================================================
