# ======================================================================
# Adapter Array
#   Advent of Code 2020 Day 10 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ j o l t s . p y
# ======================================================================
"Test solver for Advent of Code 2020 day 10, Adapter Array"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_10
import jolts

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_7_5_TEXT = """
16
10
15
5
1
11
7
19
6
12
4
"""
EXAMPLE_22_10_TEXT = """
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
"""
PART_ONE_TEXT = EXAMPLE_22_10_TEXT
PART_TWO_TEXT = EXAMPLE_22_10_TEXT

PART_ONE_RESULT = 22 * 10
PART_TWO_RESULT = 19208

# ======================================================================
#                                                              TestJolts
# ======================================================================


class TestJolts(unittest.TestCase):  # pylint: disable=R0904
    "Test Jolts object"

    def test_empty_init(self):
        "Test the default Jolts creation"

        # 1. Create default Jolts object
        myobj = jolts.Jolts()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.adapters), 0)
        self.assertEqual(len(myobj.ordered), 0)
        self.assertEqual(myobj.start, 0)
        self.assertEqual(myobj.device, None)

    def test_text_init(self):
        "Test the Jolts object creation from text"

        # 1. Create Jolts object from text
        myobj = jolts.Jolts(text=aoc_10.from_text(EXAMPLE_7_5_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 11)
        self.assertEqual(len(myobj.adapters), 11)
        self.assertEqual(len(myobj.ordered), 11)
        self.assertEqual(myobj.start, 0)
        self.assertEqual(myobj.device, 22)

        # 3. Test methods
        self.assertEqual(myobj.get_part_one_differences(), 7 * 5)

        self.assertEqual(myobj.how_many_ways(), 8)

    def test_part_one(self):
        "Test part one example of Jolts object"

        # 1. Create Jolts object from text
        myobj = jolts.Jolts(text=aoc_10.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Jolts object"

        # 1. Create Jolts object from text
        myobj = jolts.Jolts(part2=True, text=aoc_10.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ j o l t s . p y                   end
# ======================================================================
