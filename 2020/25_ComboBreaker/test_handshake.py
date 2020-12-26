# ======================================================================
# Combo Breaker
#   Advent of Code 2020 Day 25 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ h a n d s h a k e . p y
# ======================================================================
"Test solver for Advent of Code 2020 day 25, Combo Breaker"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_25
import handshake

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
5764801
17807724
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = ""

PART_ONE_RESULT = 14897079
PART_TWO_RESULT = None

# ======================================================================
#                                                          TestHandshake
# ======================================================================


class TestHandshake(unittest.TestCase):  # pylint: disable=R0904
    "Test Handshake object"

    def test_empty_init(self):
        "Test the default Handshake creation"

        # 1. Create default Handshake object
        myobj = handshake.Handshake()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.card_public, None)
        self.assertEqual(myobj.door_public, None)
        self.assertEqual(myobj.card_private, None)
        self.assertEqual(myobj.door_private, None)

    def test_text_init(self):
        "Test the Handshake object creation from text"

        # 1. Create Handshake object from text
        myobj = handshake.Handshake(text=aoc_25.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 2)
        self.assertEqual(myobj.card_public, 5764801)
        self.assertEqual(myobj.door_public, 17807724)
        self.assertEqual(myobj.card_private, None)
        self.assertEqual(myobj.door_private, None)

        # 3. Check methods
        self.assertEqual(myobj.transform_number(17807724, 8), 14897079)
        self.assertEqual(myobj.transform_number(5764801, 11), 14897079)

        self.assertEqual(myobj.guess_private(5764801, limit=20), 8)
        self.assertEqual(myobj.guess_private(17807724, limit=20), 11)

        self.assertEqual(myobj.guess_encryption_key(verbose=False, limit=20), 14897079)

    def test_part_one(self):
        "Test part one example of Handshake object"

        # 1. Create Handshake object from text
        myobj = handshake.Handshake(text=aoc_25.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False, limit=99), PART_ONE_RESULT)

    def not_test_part_two(self):
        "Test part two example of Handshake object"

        # 1. Create Handshake object from text
        myobj = handshake.Handshake(part2=False, text=aoc_25.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=True, limit=99), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ h a n d s h a k e . p y              end
# ======================================================================
