# ======================================================================
# Reindeer Olympics
#   Advent of Code 2015 Day 14 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ r e i n d e e r . p y
# ======================================================================
"Test Reindeer for Advent of Code 2015 day 14, Reindeer Olympics"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import reindeer

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = "Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds."

# ======================================================================
#                                                           TestReindeer
# ======================================================================


class TestReindeer(unittest.TestCase):  # pylint: disable=R0904
    "Test Reindeer object"

    def test_empty_init(self):
        "Test the default Reindeer creation"

        # 1. Create default Reindeer object
        myobj = reindeer.Reindeer()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.name, "")
        self.assertEqual(myobj.speed, 0)
        self.assertEqual(myobj.active, 0)
        self.assertEqual(myobj.passive, 0)
        self.assertEqual(myobj.flying, False)
        self.assertEqual(myobj.until, 0)
        self.assertEqual(myobj.distance, 0)
        self.assertEqual(myobj.points, 0)
        self.assertEqual(myobj.time, 0)

    def test_text_init(self):
        "Test the Reindeer object creation from text"

        # 1. Create Reindeer object from text
        myobj = reindeer.Reindeer(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 73)
        self.assertEqual(myobj.name, "Comet")
        self.assertEqual(myobj.speed, 14)
        self.assertEqual(myobj.active, 10)
        self.assertEqual(myobj.passive, 127)
        self.assertEqual(myobj.flying, False)
        self.assertEqual(myobj.until, 0)
        self.assertEqual(myobj.points, 0)
        self.assertEqual(myobj.time, 0)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ r e i n d e e r . p y                end
# ======================================================================
