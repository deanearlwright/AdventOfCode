# ======================================================================
# Reindeer Olympics
#   Advent of Code 2015 Day 14 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ o l y m p i c s . p y
# ======================================================================
"Test solver for Advent of Code 2015 day 14, Reindeer Olympics"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_14
import olympics

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 1120
PART_TWO_RESULT = 689

EXAMPLE_RACE_TIME = 1000
# ======================================================================
#                                                           TestOlympics
# ======================================================================


class TestOlympics(unittest.TestCase):  # pylint: disable=R0904
    "Test Olympics object"

    def test_empty_init(self):
        "Test the default Olympics creation"

        # 1. Create default Olympics object
        myobj = olympics.Olympics()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.reindeer), 0)

    def test_text_init(self):
        "Test the Olympics object creation from text"

        # 1. Create Olympics object from text
        myobj = olympics.Olympics(text=aoc_14.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 2)
        self.assertEqual(len(myobj.reindeer), 2)

    def test_part_one(self):
        "Test part one example of Olympics object"

        # 1. Create Olympics object from text
        myobj = olympics.Olympics(text=aoc_14.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False, race_time=EXAMPLE_RACE_TIME),
                         PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Olympics object"

        # 1. Create Olympics object from text
        myobj = olympics.Olympics(part2=True, text=aoc_14.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False, race_time=EXAMPLE_RACE_TIME),
                         PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ o l y m p i c s . p y                end
# ======================================================================
