
# ======================================================================
# Distress Signal
#   Advent of Code 2022 Day 13 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ d e v i c e . p y
# ======================================================================
"Test Device for Advent of Code 2022 day 13, Distress Signal"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_13
import device

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
"""


# ======================================================================
#                                                             TestDevice
# ======================================================================


class TestDevice(unittest.TestCase):  # pylint: disable=R0904
    "Test Device object"

    def test_empty_init(self):
        "Test the default Device creation"

        # 1. Create default Device object
        myobj = device.Device()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.packets), 0)

    def test_text_init(self):
        "Test the Device object creation from text"

        # 1. Create Device object from text
        myobj = device.Device(text=aoc_13.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 16)
        self.assertEqual(len(myobj.packets), 8)

        # 3. Check packets
        self.assertEqual(myobj.packets[0].is_ordered(), True)   # Pair 1
        self.assertEqual(myobj.packets[1].is_ordered(), True)   # Pair 2
        self.assertEqual(myobj.packets[2].is_ordered(), False)  # Pair 3
        self.assertEqual(myobj.packets[3].is_ordered(), True)   # Pair 4
        self.assertEqual(myobj.packets[4].is_ordered(), False)  # Pair 5
        self.assertEqual(myobj.packets[5].is_ordered(), True)   # Pair 6
        self.assertEqual(myobj.packets[6].is_ordered(), False)  # Pair 7
        self.assertEqual(myobj.packets[7].is_ordered(), False)  # Pair 8

        # 4. Check methods
        self.assertEqual(myobj.right_order(), 13)

    def test_text_two(self):
        "Test the Device object creation from text"

        # 1. Create Device object from text
        myobj = device.Device(text=aoc_13.from_text(EXAMPLE_TEXT),
                              part2=True)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, True)
        self.assertEqual(len(myobj.text), 16)
        self.assertEqual(len(myobj.packets), 9)

        # 3. Check methods
        self.assertEqual(myobj.decorder_key(), 140)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ d e v i c e . p y                  end
# ======================================================================
