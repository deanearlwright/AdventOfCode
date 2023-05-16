
# ======================================================================
# Pyroclastic Flow
#   Advent of Code 2022 Day 17 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ r o c k s . p y
# ======================================================================
"Test Rocks for Advent of Code 2022 day 17, Pyroclastic Flow"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import rocks

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                              TestRocks
# ======================================================================


class TestRocks(unittest.TestCase):  # pylint: disable=R0904
    "Test Rocks object"

    def test_empty_init(self):
        "Test the default Rocks creation"

        # 1. Create default Rocks object
        myobj = rocks.Rocks()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.next, 0)
        self.assertEqual(len(myobj.rocks), 0)

    def test_text_init(self):
        "Test the Rocks object creation from text"

        # 1. Create Rocks object from text
        myobj = rocks.Rocks(text=rocks.ROCKS)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 5)
        self.assertEqual(myobj.next, 0)
        self.assertEqual(len(myobj.rocks), 5)

        # 3. Check methods
        self.assertEqual(myobj.next_rock().type, 1)
        self.assertEqual(myobj.next_rock().type, 2)
        self.assertEqual(myobj.next_rock().type, 3)
        self.assertEqual(myobj.next_rock().type, 4)
        self.assertEqual(myobj.next_rock().type, 5)
        self.assertEqual(myobj.next_rock().type, 1)
        self.assertEqual(myobj.next_rock().type, 2)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ r o c k s . p y                   end
# ======================================================================
