# ======================================================================
# Packet Decoder
#   Advent of Code 2021 Day 16 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ p a c k e t s . p y
# ======================================================================
"Test solver for Advent of Code 2021 day 16, Packet Decoder"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_16
import packets

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
D2FE28
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = "9C0141080250320F1802104A08"

PART_ONE_RESULT = 6
PART_TWO_RESULT = 1

EXAMPLES = [
    {'text': "D2FE28", 'length': 0, 'packets': 0, 'versions': 6},
    {'text': "38006F45291200", 'length': 27, 'packets': 2, 'versions': 1 + 6 + 2},
    {'text': "EE00D40C823060", 'length': 3, 'packets': 3, 'versions': 7 + 2 + 4 + 1},
    {'text': "8A004A801A8002F478", 'length': 1, 'packets': 1, 'versions': 16},
    {'text': "620080001611562C8802118E34", 'length': 2, 'packets': 2, 'versions': 12},
    {'text': "C0015000016115A2E0802F182340", 'length': 84, 'packets': 2, 'versions': 23},
    {'text': "A0016C880162017C3686B18A3D4780", 'length': 91, 'packets': 1, 'versions': 31},
]

EXAMPLES_TWO = [
    {'text': "C200B40A82", 'value': 3},
    {'text': "04005AC33890", 'value': 54},
    {'text': "880086C3E88112", 'value': 7},
    {'text': "CE00C43D881120", 'value': 9},
    {'text': "D8005AC2A8F0", 'value': 1},
    {'text': "F600BC2D8F", 'value': 0},
    {'text': "9C005AC2F8F0", 'value': 0},
    {'text': "9C0141080250320F1802104A08", 'value': 1},
]

# ======================================================================
#                                                            TestPackets
# ======================================================================


class TestPackets(unittest.TestCase):  # pylint: disable=R0904
    "Test Packets object"

    def test_empty_init(self):
        "Test the default Packets creation"

        # 1. Create default Packets object
        myobj = packets.Packets()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)

    def test_text_init(self):
        "Test the Packets object creation from text"

        # 1. Create Packets object from text
        myobj = packets.Packets(text=aoc_16.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 1)

        # 3. Check methods
        self.assertEqual(myobj.packet.versions(), [6])

    def test_examples(self):
        "Test the examples"

        # 1. Loop for all of the examples
        for example in EXAMPLES:

            # 2. Decode the packet
            myobj = packets.Packets(text=[example['text']])

            # 3. Check the results
            self.assertEqual(myobj.packet.length, example['length'])
            self.assertEqual(len(myobj.packet.packets), example['packets'])
            self.assertEqual(sum(myobj.packet.versions()), example['versions'])

    def test_examples_two(self):
        "Test the examples for part 2"

        # 1. Loop for all of the examples
        for example in EXAMPLES_TWO:

            # 2. Decode the packet
            myobj = packets.Packets(text=[example['text']], part2=True)

            # 3. Check the results
            self.assertEqual(myobj.packet.execute(), example['value'])

    def test_part_one(self):
        "Test part one example of Packets object"

        # 1. Create Packets object from text
        myobj = packets.Packets(text=aoc_16.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Packets object"

        # 1. Create Packets object from text
        myobj = packets.Packets(part2=True, text=aoc_16.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                  t e s t _ p a c k e t s . p y                 end
# ======================================================================
