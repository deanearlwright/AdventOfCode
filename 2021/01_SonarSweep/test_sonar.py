# ======================================================================
# Sonar Sweep
#   Advent of Code 2021 Day 01 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ s o n a r . p y
# ======================================================================
"Test solver for Advent of Code 2021 day 01, Sonar Sweep"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_01
import sonar

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
199
200
208
210
200
207
240
269
260
263"""

PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 7
PART_TWO_RESULT = 5

# ======================================================================
#                                                              TestSonar
# ======================================================================


class TestSonar(unittest.TestCase):  # pylint: disable=R0904
    "Test Sonar object"

    def test_empty_init(self):
        "Test the default Sonar creation"

        # 1. Create default Sonar object
        myobj = sonar.Sonar()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)

    def test_text_init(self):
        "Test the Sonar object creation from text"

        # 1. Create Sonar object from text
        myobj = sonar.Sonar(text=aoc_01.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 10)

        # 3. Check methods
        self.assertEqual(myobj.more_than_previous(), 7)
        self.assertEqual(myobj.do_windows(window=1), 7)
        self.assertEqual(myobj.do_windows(), 5)

    def test_part_one(self):
        "Test part one example of Sonar object"

        # 1. Create Sonar object from text
        myobj = sonar.Sonar(text=aoc_01.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Sonar object"

        # 1. Create Sonar object from text
        myobj = sonar.Sonar(part2=True, text=aoc_01.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ s o n a r . p y                   end
# ======================================================================
