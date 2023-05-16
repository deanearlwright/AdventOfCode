
# ======================================================================
# Proboscidea Volcanium
#   Advent of Code 2022 Day 16 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ v a l v e . p y
# ======================================================================
"Test Valve for Advent of Code 2022 day 16, Proboscidea Volcanium"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import valve

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = "Valve BB has flow rate=13; tunnels lead to valves CC, AA"

# ======================================================================
#                                                              TestValve
# ======================================================================


class TestValve(unittest.TestCase):  # pylint: disable=R0904
    "Test Valve object"

    def test_empty_init(self):
        "Test the default Valve creation"

        # 1. Create default Valve object
        myobj = valve.Valve()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.name, None)
        self.assertEqual(myobj.number, 0)
        self.assertEqual(myobj.rate, 0)
        self.assertEqual(len(myobj.tunnels), 0)

    def test_text_init(self):
        "Test the Valve object creation from text"

        # 1. Create Valve object from text
        myobj = valve.Valve(text=EXAMPLE_TEXT, number=2)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 56)
        self.assertEqual(myobj.name, "BB")
        self.assertEqual(myobj.number, 2)
        self.assertEqual(myobj.rate, 13)
        self.assertEqual(len(myobj.tunnels), 2)
        self.assertEqual(myobj.tunnels[0], "CC")
        self.assertEqual(myobj.tunnels[1], "AA")

        # 3. Check methods
        self.assertEqual(myobj.info(), (2, 13, ["CC", "AA"]))


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ v a l v e . p y                   end
# ======================================================================
