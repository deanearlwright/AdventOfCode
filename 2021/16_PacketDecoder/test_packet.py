# ======================================================================
# Packet Decoder
#   Advent of Code 2021 Day 16 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ p a c k e t . p y
# ======================================================================
"Test Packet for Advent of Code 2021 day 16, Packet Decoder"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import packet

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_LITERAL = "D2FE28"
EXAMPLE_LITERAL_A = "D14"
EXAMPLE_LITERAL_B = "5224"
EXAMPLE_OP_BITS = "38006F45291200"
EXAMPLE_OP_PKTS = "EE00D40C823060"

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
        self.assertEqual(myobj.bits, "")
        self.assertEqual(myobj.version, 0)
        self.assertEqual(myobj.ptype, 0)
        self.assertEqual(myobj.ltype, 0)
        self.assertEqual(myobj.length, 0)
        self.assertEqual(myobj.size, 0)
        self.assertEqual(myobj.literal, 0)
        self.assertEqual(len(myobj.packets), 0)

        # 3. Check methods
        self.assertEqual(myobj.is_literal(), False)
        self.assertEqual(myobj.is_operator(), True)
        self.assertEqual(sum(myobj.versions()), 0)

    def test_text_literal(self):
        "Test the literal Packet object creation from text"

        # 1. Create Packet object from text
        myobj = packet.Packet(text=EXAMPLE_LITERAL)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 6)
        self.assertEqual(myobj.text, "D2FE28")
        self.assertEqual(len(myobj.bits), 6 * 4)
        self.assertEqual(myobj.bits, "110100101111111000101000")
        self.assertEqual(myobj.version, 6)
        self.assertEqual(myobj.ptype, 4)
        self.assertEqual(myobj.ltype, 0)
        self.assertEqual(myobj.length, 0)
        self.assertEqual(myobj.size, 21)
        self.assertEqual(myobj.literal, 2021)
        self.assertEqual(len(myobj.packets), 0)

        # 3. Check methods
        self.assertEqual(myobj.is_literal(), True)
        self.assertEqual(myobj.is_operator(), False)
        self.assertEqual(sum(myobj.versions()), 6)

    def test_text_literal_a(self):
        "Test the literal Packet object creation from text"

        # 1. Create Packet object from text
        myobj = packet.Packet(text=EXAMPLE_LITERAL_A)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 3)
        self.assertEqual(len(myobj.bits), 3 * 4)
        self.assertEqual(myobj.version, 6)
        self.assertEqual(myobj.ptype, 4)
        self.assertEqual(myobj.ltype, 0)
        self.assertEqual(myobj.length, 0)
        self.assertEqual(myobj.size, 11)
        self.assertEqual(myobj.literal, 10)
        self.assertEqual(len(myobj.packets), 0)

        # 3. Check methods
        self.assertEqual(myobj.is_literal(), True)
        self.assertEqual(myobj.is_operator(), False)
        self.assertEqual(sum(myobj.versions()), 6)

    def test_text_literal_b(self):
        "Test the literal Packet object creation from text"

        # 1. Create Packet object from text
        myobj = packet.Packet(text=EXAMPLE_LITERAL_B)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 4)
        self.assertEqual(len(myobj.bits), 4 * 4)
        self.assertEqual(myobj.version, 2)
        self.assertEqual(myobj.ptype, 4)
        self.assertEqual(myobj.ltype, 0)
        self.assertEqual(myobj.length, 0)
        self.assertEqual(myobj.size, 16)
        self.assertEqual(myobj.literal, 20)
        self.assertEqual(len(myobj.packets), 0)

        # 3. Check methods
        self.assertEqual(myobj.is_literal(), True)
        self.assertEqual(myobj.is_operator(), False)
        self.assertEqual(sum(myobj.versions()), 2)

    def test_text_operator_bits(self):
        "Test the bit operator Packet object creation from text"

        # 1. Create Packet object from text
        myobj = packet.Packet(text=EXAMPLE_OP_BITS)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 14)
        self.assertEqual(myobj.text, EXAMPLE_OP_BITS)
        self.assertEqual(len(myobj.bits), 14 * 4)
        self.assertEqual(myobj.version, 1)
        self.assertEqual(myobj.ptype, 6)
        self.assertEqual(myobj.ltype, 0)
        self.assertEqual(myobj.length, 27)
        self.assertEqual(myobj.size, 49)
        self.assertEqual(myobj.literal, 0)
        self.assertEqual(len(myobj.packets), 2)

        # 3. Check methods
        self.assertEqual(myobj.is_literal(), False)
        self.assertEqual(myobj.is_operator(), True)
        self.assertEqual(sum(myobj.versions()), 1 + 6 + 2)

    def test_text_operator_pkts(self):
        "Test the packet operator Packet object creation from text"

        # 1. Create Packet object from text
        myobj = packet.Packet(text=EXAMPLE_OP_PKTS)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 14)
        self.assertEqual(myobj.text, EXAMPLE_OP_PKTS)
        self.assertEqual(len(myobj.bits), 14 * 4)
        self.assertEqual(myobj.version, 7)
        self.assertEqual(myobj.ptype, 3)
        self.assertEqual(myobj.ltype, 1)
        self.assertEqual(myobj.length, 3)
        self.assertEqual(myobj.size, 51)
        self.assertEqual(myobj.literal, 0)
        self.assertEqual(len(myobj.packets), 3)

        # 3. Check methods
        self.assertEqual(myobj.is_literal(), False)
        self.assertEqual(myobj.is_operator(), True)
        self.assertEqual(sum(myobj.versions()), 7 + 2 + 4 + 1)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ p a c k e t . p y                  end
# ======================================================================
