
# ======================================================================
# Haunted Wasteland
#   Advent of Code 2023 Day 08 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ n e t w o r k . p y
# ======================================================================
"Test Network for Advent of Code 2023 day 08, Haunted Wasteland"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import network

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = [
    "LLR",

    "AAA = (BBB, BBB)",
    "BBB = (AAA, ZZZ)",
    "ZZZ = (ZZZ, ZZZ)",

]

# ======================================================================
#                                                            TestNetwork
# ======================================================================


class TestNetwork(unittest.TestCase):  # pylint: disable=R0904
    "Test Network object"

    def test_empty_init(self):
        "Test the default Network creation"

        # 1. Create default Network object
        myobj = network.Network()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.directions, "")
        self.assertEqual(len(myobj.nodes), 0)
        self.assertEqual(len(myobj.starts), 0)
        self.assertEqual(len(myobj.stops), 0)

    def test_text_init(self):
        "Test the Network object creation from text"

        # 1. Create Network object from text
        myobj = network.Network(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 4)
        self.assertEqual(myobj.directions, "LLR")
        self.assertEqual(len(myobj.nodes), 3)
        self.assertEqual(len(myobj.starts), 1)
        self.assertEqual(len(myobj.stops), 1)

        # 3. Check methods
        self.assertEqual(network.lcm(54, 24), 216)
        self.assertEqual(myobj.navigate_one("AAA", "ZZZ"), 6)
        self.assertEqual(myobj.brute_navigate(), 6)
        self.assertEqual(myobj.navigate(), 6)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                  t e s t _ n e t w o r k . p y                 end
# ======================================================================
