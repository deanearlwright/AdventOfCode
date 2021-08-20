# ======================================================================
# Probably a Fire Hazard
#   Advent of Code 2015 Day 06 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ l i g h t s . p y
# ======================================================================
"Test solver for Advent of Code 2015 day 06, Probably a Fire Hazard"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_06
import lights

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
turn on 0,0 through 999,999
toggle 0,0 through 999,0
turn off 499,499 through 500,500
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = ""

PART_ONE_RESULT = 998996
PART_TWO_RESULT = None

# ======================================================================
#                                                             TestLights
# ======================================================================


class TestLights(unittest.TestCase):  # pylint: disable=R0904
    "Test Lights object"

    def test_empty_init(self):
        "Test the default Lights creation"

        # 1. Create default Lights object
        myobj = lights.Lights()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.lights), 0)

    def test_text_init(self):
        "Test the Lights object creation from text"

        # 1. Create Lights object from text
        myobj = lights.Lights(text=aoc_06.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 3)
        self.assertEqual(len(myobj.lights), 0)

        # 3. Check methods
        myobj.turn_on(0, 0, 999, 999)
        self.assertEqual(len(myobj.lights), 1000000)
        myobj.toggle(0, 0, 999, 0)
        self.assertEqual(len(myobj.lights), 1000000 - 1000)
        myobj.turn_off(499, 499, 500, 500)
        self.assertEqual(len(myobj.lights), 1000000 - (1000 + 4))
        self.assertEqual(myobj.count_lights(), 998996)

    def test_part_one(self):
        "Test part one example of Lights object"

        # 1. Create Lights object from text
        myobj = lights.Lights(text=aoc_06.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Lights object"

        # 1. Create Lights object from text
        myobj = lights.Lights(part2=True, text=aoc_06.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ l i g h t s . p y                  end
# ======================================================================
