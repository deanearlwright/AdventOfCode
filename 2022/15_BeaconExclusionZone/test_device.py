
# ======================================================================
# Beacon Exclusion Zone
#   Advent of Code 2022 Day 15 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ d e v i c e . p y
# ======================================================================
"Test Device for Advent of Code 2022 day 15, Beacon Exclusion Zone"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_15
import device

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
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
        self.assertEqual(len(myobj.sensors), 0)
        self.assertEqual(myobj.top, None)
        self.assertEqual(myobj.bottom, None)
        self.assertEqual(myobj.left, None)
        self.assertEqual(myobj.right, None)
        self.assertEqual(myobj.middle, (0, 0))

    def test_text_init(self):
        "Test the Device object creation from text"

        # 1. Create Device object from text
        myobj = device.Device(text=aoc_15.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 14)
        self.assertEqual(len(myobj.sensors), 14)
        self.assertEqual(myobj.top.loc[1], 0)
        self.assertEqual(myobj.bottom.loc[1], 20)
        self.assertEqual(myobj.left.loc[0], 0)
        self.assertEqual(myobj.right.loc[0], 20)
        self.assertEqual(myobj.middle, (10, 10))

        # 3. Check methods
        self.assertEqual(myobj.count_not_beacons_row(row=10), 26)
        self.assertEqual(myobj.find_unknown_beacon(limit=20), (14, 11))
        self.assertEqual(myobj.tuning_frequency(row=20), 56000011)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ d e v i c e . p y                  end
# ======================================================================
