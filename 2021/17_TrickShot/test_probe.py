# ======================================================================
# Trick Shot
#   Advent of Code 2021 Day 17 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ p r o b e . p y
# ======================================================================
"Test solver for Advent of Code 2021 day 17, Trick Shot"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_17
import probe

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
target area: x=20..30, y=-10..-5
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 45
PART_TWO_RESULT = 112

# ======================================================================
#                                                              TestProbe
# ======================================================================


class TestProbe(unittest.TestCase):  # pylint: disable=R0904
    "Test Probe object"

    def test_empty_init(self):
        "Test the default Probe creation"

        # 1. Create default Probe object
        myobj = probe.Probe()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.start, (0, 0))
        self.assertEqual(myobj.target, None)
        self.assertEqual(myobj.position, (0, 0))
        self.assertEqual(myobj.velocity, None)
        self.assertEqual(myobj.height, 0)

    def test_text_init(self):
        "Test the Probe object creation from text"

        # 1. Create Probe object from text
        myobj = probe.Probe(text=aoc_17.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 1)
        self.assertEqual(myobj.start, (0, 0))
        self.assertEqual(myobj.target, [20, 30, -10, -5])
        self.assertEqual(myobj.position, (0, 0))
        self.assertEqual(myobj.velocity, None)
        self.assertEqual(myobj.height, 0)

        # 3. Check methods
        myobj.reload((7, 2))
        self.assertEqual(myobj.position, (0, 0))
        self.assertEqual(myobj.velocity, (7, 2))
        self.assertEqual(myobj.is_in_target(), False)
        self.assertEqual(myobj.is_possible(), True)
        myobj.step()
        self.assertEqual(myobj.position, (7, 2))
        self.assertEqual(myobj.velocity, (6, 1))
        self.assertEqual(myobj.is_in_target(), False)
        self.assertEqual(myobj.is_possible(), True)
        myobj.step()
        self.assertEqual(myobj.position, (13, 3))
        self.assertEqual(myobj.velocity, (5, 0))
        self.assertEqual(myobj.is_in_target(), False)
        self.assertEqual(myobj.is_possible(), True)
        myobj.step()
        myobj.step()
        myobj.step()
        myobj.step()
        self.assertEqual(myobj.position, (27, -3))
        self.assertEqual(myobj.velocity, (1, -4))
        self.assertEqual(myobj.is_in_target(), False)
        self.assertEqual(myobj.is_possible(), True)
        myobj.step()
        self.assertEqual(myobj.position, (28, -7))
        self.assertEqual(myobj.velocity, (0, -5))
        self.assertEqual(myobj.is_in_target(), True)
        self.assertEqual(myobj.is_possible(), True)
        myobj.step()
        self.assertEqual(myobj.position, (28, -12))
        self.assertEqual(myobj.velocity, (0, -6))
        self.assertEqual(myobj.is_in_target(), False)
        self.assertEqual(myobj.is_possible(), False)
        self.assertEqual(myobj.height, 3)

        self.assertEqual(myobj.fire((7, 2)), 3)
        self.assertEqual(myobj.fire((6, 3)), 6)
        self.assertEqual(myobj.fire((9, 0)), 0)
        self.assertEqual(myobj.fire((17, -4)), -1)
        self.assertEqual(myobj.fire((6, 9)), 45)

        self.assertEqual(myobj.highest(), 45)
        self.assertEqual(myobj.count(), 112)

    def test_part_one(self):
        "Test part one example of Probe object"

        # 1. Create Probe object from text
        myobj = probe.Probe(text=aoc_17.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Probe object"

        # 1. Create Probe object from text
        myobj = probe.Probe(part2=True, text=aoc_17.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ p r o b e . p y                   end
# ======================================================================
