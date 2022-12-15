
# ======================================================================
# Regolith Reservoir
#   Advent of Code 2022 Day 14 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ d e v i c e . p y
# ======================================================================
"Test Device for Advent of Code 2022 day 14, Regolith Reservoir"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import device

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = [
    "498,4 -> 498,6 -> 496,6",
    "503,4 -> 502,4 -> 502,9 -> 494,9"
]

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
        self.assertEqual(myobj.scan, None)

    def test_text_init(self):
        "Test the Device object creation from text"

        # 1. Create Device object from text
        myobj = device.Device(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 2)
        self.assertNotEqual(myobj.scan, None)

        # 3. Check methods
        self.assertEqual(myobj.count_sand(), 24)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ d e v i c e . p y                  end
# ======================================================================
