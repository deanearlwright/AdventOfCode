# ======================================================================
# Seven Segment Search
#   Advent of Code 2021 Day 08 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ p a t t e r n . p y
# ======================================================================
"Test Pattern for Advent of Code 2021 day 08, Seven Segment Search"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import pattern

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_ONE = "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe"
EXAMPLE_TWO = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"

# ======================================================================
#                                                            TestPattern
# ======================================================================


class TestPattern(unittest.TestCase):  # pylint: disable=R0904
    "Test Pattern object"

    def test_empty_init(self):
        "Test the default Pattern creation"

        # 1. Create default Pattern object
        myobj = pattern.Pattern()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.signals), 0)
        self.assertEqual(len(myobj.output), 0)

    def test_text_init(self):
        "Test the Pattern object creation from text"

        # 1. Create Pattern object from text
        myobj = pattern.Pattern(text=EXAMPLE_ONE)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 86)
        self.assertEqual(len(myobj.signals), 10)
        self.assertEqual(len(myobj.output), 4)

        # 3. Test methods
        self.assertEqual(myobj.one_four_seven_eight(), 2)

    def test_text_init_two(self):
        "Test the Pattern object creation from text for part two"

        # 1. Create Pattern object from text
        myobj = pattern.Pattern(text=EXAMPLE_TWO)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 84)
        self.assertEqual(len(myobj.signals), 10)
        self.assertEqual(len(myobj.output), 4)

        # 3. Test methods
        self.assertEqual(myobj.value(), 5353)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                  t e s t _ p a t t e r n . p y                 end
# ======================================================================
