
# ======================================================================
# Grove Positioning System
#   Advent of Code 2022 Day 20 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ d e v i c e . p y
# ======================================================================
"Test Device for Advent of Code 2022 day 20, Grove Positioning System"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import device

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = [
    "1",
    "2",
    "-3",
    "3",
    "-2",
    "0",
    "4"
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
        self.assertEqual(len(myobj.numbers), 0)
        self.assertEqual(myobj.key, 1)

    def test_text_init(self):
        "Test the Device object creation from text"

        # 1. Create Device object from text
        myobj = device.Device(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 7)
        self.assertEqual(len(myobj.numbers), 7)
        self.assertEqual(myobj.key, 1)

        # 3. Check methods
        myobj.mixer()
        self.assertEqual(myobj.coordinates(), (4, -3, 2))

    def test_text_two(self):
        "Test the Device object creation from text"

        # 1. Create Device object from text
        myobj = device.Device(text=EXAMPLE_TEXT, part2=True)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, True)
        self.assertEqual(len(myobj.text), 7)
        self.assertEqual(len(myobj.numbers), 7)
        self.assertEqual(myobj.key, device.KEY)

        # 3. Check methods
        myobj.mixer_ten()
        self.assertEqual(myobj.coordinates(),
                         (811589153, 2434767459, -1623178306))

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ d e v i c e . p y                  end
# ======================================================================
