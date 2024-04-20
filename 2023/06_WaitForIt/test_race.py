
# ======================================================================
# Wait For It
#   Advent of Code 2023 Day 06 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ r a c e . p y
# ======================================================================
"Test Race for Advent of Code 2023 day 06, Wait For It"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import race

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = ""

# ======================================================================
#                                                             TestRace
# ======================================================================


class TestRace(unittest.TestCase):  # pylint: disable=R0904
    "Test Race object"

    def test_empty_init(self):
        "Test the default Race creation"

        # 1. Create default Race object
        myobj = race.Race()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.num, 0)
        self.assertEqual(myobj.time, 0)
        self.assertEqual(myobj.distance, 0)

    def test_text_init(self):
        "Test the Race object creation from text"

        # 1. Create Race object from text
        myobj = race.Race(num=1, time=7, distance=9)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.num, 1)
        self.assertEqual(myobj.time, 7)
        self.assertEqual(myobj.distance, 9)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ r a c e . p y                end
# ======================================================================
