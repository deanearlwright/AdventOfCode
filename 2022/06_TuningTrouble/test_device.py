# ======================================================================
# Tuning Trouble
#   Advent of Code 2022 Day 06 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ d e v i c e . p y
# ======================================================================
"Test Device for Advent of Code 2022 day 06, Tuning Trouble"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import device

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLES = [
    ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7, 19),
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5, 23),
    ("nppdvjthqldpwncqszvftbrmjlhg", 6, 23),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10, 29),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11, 26)
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
        self.assertEqual(len(myobj.chars), 0)

    def test_text_init(self):
        "Test the Device object creation from text"

        # 1. Create Device object from text
        myobj = device.Device(text=EXAMPLES[0][0])

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 30)
        self.assertEqual(len(myobj.chars), 0)

        # 3. Check methods
        self.assertEqual(myobj.start_of_packet(), EXAMPLES[0][1])

    def test_all(self):
        "Test all the examples"

        # 1. Loop for all the examples
        for text, result4, result14 in EXAMPLES:

            # 2. Create the device
            dev = device.Device(text=text)

            # 3. Verify the results
            self.assertEqual(dev.start_of_packet(4), result4)
            self.assertEqual(dev.start_of_packet(14), result14)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ d e v i c e . p y                  end
# ======================================================================
