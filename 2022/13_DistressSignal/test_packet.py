
# ======================================================================
# Distress Signal
#   Advent of Code 2022 Day 13 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ p a c k e t . p y
# ======================================================================
"Test Packet for Advent of Code 2022 day 13, Distress Signal"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import packet

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = ["[1,1,3,1,1]", "[1,1,5,1,1]"]

# ======================================================================
#                                                             TestPacket
# ======================================================================


class TestPacket(unittest.TestCase):  # pylint: disable=R0904
    "Test Packet object"

    def test_empty_init(self):
        "Test the default Packet creation"

        # 1. Create default Packet object
        myobj = packet.Packet()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.left), 0)
        self.assertEqual(len(myobj.right), 0)

    def test_text_init(self):
        "Test the Packet object creation from text"

        # 1. Create Packet object from text
        myobj = packet.Packet(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 2)
        self.assertEqual(len(myobj.left), 5)
        self.assertEqual(len(myobj.right), 5)

        # 3. Check methods
        self.assertEqual(myobj.is_ordered(), True)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ p a c k e t . p y                  end
# ======================================================================
