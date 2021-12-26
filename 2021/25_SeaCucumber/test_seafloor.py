# ======================================================================
# Sea Cucumber
#   Advent of Code 2021 Day 25 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ s e a f l o o r . p y
# ======================================================================
"Test solver for Advent of Code 2021 day 25, Sea Cucumber"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_25
import seafloor

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>
"""
STEP_ONE = """
....>.>v.>
v.v>.>v.v.
>v>>..>v..
>>v>v>.>.v
.>v.v...v.
v>>.>vvv..
..v...>>..
vv...>>vv.
>.v.v..v.v
"""
STEP_TWO = """
>.v.v>>..v
v.v.>>vv..
>v>.>.>.v.
>>v>v.>v>.
.>..v....v
.>v>>.v.v.
v....v>v>.
.vv..>>v..
v>.....vv.
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 58
PART_TWO_RESULT = 58

# ======================================================================
#                                                           TestSeafloor
# ======================================================================


class TestSeafloor(unittest.TestCase):  # pylint: disable=R0904
    "Test Seafloor object"

    def test_empty_init(self):
        "Test the default Seafloor creation"

        # 1. Create default Seafloor object
        myobj = seafloor.Seafloor()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.eastern, set())
        self.assertEqual(myobj.southern, set())
        self.assertEqual(myobj.rows, 0)
        self.assertEqual(myobj.cols, 0)
        self.assertEqual(myobj.steps, 0)
        self.assertEqual(myobj.moved, True)

    def test_text_init(self):
        "Test the Seafloor object creation from text"

        # 1. Create Seafloor object from text
        myobj = seafloor.Seafloor(text=aoc_25.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 9)
        self.assertEqual(len(myobj.eastern), 23)
        self.assertEqual(len(myobj.southern), 26)
        self.assertEqual(myobj.rows, 9)
        self.assertEqual(myobj.cols, 10)
        self.assertEqual(myobj.steps, 0)
        self.assertEqual(myobj.moved, True)

        self.assertFalse((0, 0) in myobj.eastern)
        self.assertTrue((0, 0) in myobj.southern)
        self.assertFalse((1, 0) in myobj.eastern)
        self.assertFalse((1, 0) in myobj.southern)
        self.assertFalse((2, 1) in myobj.eastern)
        self.assertTrue((2, 1) in myobj.southern)
        self.assertTrue((3, 1) in myobj.eastern)
        self.assertFalse((3, 1) in myobj.southern)
        self.assertTrue((9, 0) in myobj.eastern)
        self.assertFalse((9, 0) in myobj.southern)
        self.assertTrue((9, 8) in myobj.eastern)
        self.assertFalse((9, 8) in myobj.southern)

        # 3. Check methods
        self.assertEqual(myobj.in_front_of((0, 0), seafloor.SOUTH), (0, 1))
        self.assertEqual(myobj.in_front_of((4, 0), seafloor.EAST), (5, 0))
        self.assertEqual(myobj.in_front_of((9, 0), seafloor.EAST), (0, 0))
        self.assertEqual(myobj.in_front_of((9, 8), seafloor.EAST), (0, 8))
        self.assertEqual(myobj.in_front_of((4, 8), seafloor.SOUTH), (4, 0))

        self.assertEqual(myobj.run(), 58)

    def test_part_one(self):
        "Test part one example of Seafloor object"

        # 1. Create Seafloor object from text
        myobj = seafloor.Seafloor(text=aoc_25.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Seafloor object"

        # 1. Create Seafloor object from text
        myobj = seafloor.Seafloor(part2=True, text=aoc_25.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ s e a f l o o r . p y                end
# ======================================================================
