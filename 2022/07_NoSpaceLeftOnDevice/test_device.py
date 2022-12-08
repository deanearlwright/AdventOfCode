# ======================================================================
# No Space Left On Device
#   Advent of Code 2022 Day 07 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ d e v i c e . p y
# ======================================================================
"Test Device for Advent of Code 2022 day 07, No Space Left On Device"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import device

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = ["$ cd /", "$ ls", "dir a", "123 b.txt", "444 c.dat"]

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
        self.assertEqual(myobj.root, None)
        self.assertEqual(myobj.current, None)

    def test_text_init(self):
        "Test the Device object creation from text"

        # 1. Create Device object from text
        myobj = device.Device(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 5)
        self.assertNotEqual(myobj.root, None)
        self.assertNotEqual(myobj.current, None)
        self.assertEqual(myobj.current, myobj.root)
        self.assertEqual(myobj.current.name, "/")

        # 3. Check methods
        self.assertEqual(myobj.current.size(), 567)
        self.assertEqual(myobj.current.size_under(100000), 567)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ d e v i c e . p y                  end
# ======================================================================
