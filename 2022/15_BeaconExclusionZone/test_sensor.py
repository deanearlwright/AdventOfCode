
# ======================================================================
# Beacon Exclusion Zone
#   Advent of Code 2022 Day 15 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ s e n s o r . p y
# ======================================================================
"Test Sensor for Advent of Code 2022 day 15, Beacon Exclusion Zone"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import sensor

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = "Sensor at x=8, y=7: closest beacon is at x=2, y=10"

# ======================================================================
#                                                             TestSensor
# ======================================================================


class TestSensor(unittest.TestCase):  # pylint: disable=R0904
    "Test Sensor object"

    def test_empty_init(self):
        "Test the default Sensor creation"

        # 1. Create default Sensor object
        myobj = sensor.Sensor()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.loc, None)
        self.assertEqual(myobj.beacon, None)
        self.assertEqual(myobj.dist, None)

    def test_text_init(self):
        "Test the Sensor object creation from text"

        # 1. Create Sensor object from text
        myobj = sensor.Sensor(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 50)
        self.assertEqual(myobj.loc, (8, 7))
        self.assertEqual(myobj.beacon, (2, 10))
        self.assertEqual(myobj.dist, 9)

        # 3. Check methods
        self.assertEqual(myobj.is_beacon((5, 5)), False)
        self.assertEqual(myobj.is_beacon((8, -2)), False)
        self.assertEqual(myobj.is_beacon((9, -2)), None)
        self.assertEqual(myobj.is_beacon((0, 0)), None)
        self.assertEqual(myobj.is_beacon((2, 10)), True)
        self.assertEqual(myobj.is_beacon((17, 7)), False)
        self.assertEqual(myobj.is_beacon((18, 7)), None)

        self.assertEqual(myobj.edge(0), ((-2, 7), (18, 7), (-2, 7), (18, 7)))
        self.assertEqual(myobj.edge(1), ((-1, 6), (17, 6), (-1, 8), (17, 8)))
        self.assertEqual(myobj.edge(2), ((0, 5), (16, 5), (0, 9), (16, 9)))
        self.assertEqual(myobj.edge(3), ((1, 4), (15, 4), (1, 10), (15, 10)))
        self.assertEqual(myobj.edge(4), ((2, 3), (14, 3), (2, 11), (14, 11)))


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ s e n s o r . p y                  end
# ======================================================================
