# ======================================================================
# Doesnot He Have InternElves For This
#   Advent of Code 2015 Day 05 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ t h e l i s t . p y
# ======================================================================
"Test solver for Advent of Code 2015 day 05, Doesnot He Have InternElves For This"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_05
import thelist

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
ugknbfddgicrmopn
aaa
jchzalrnumimnmhp
haegwjzuvuyypxyu
dvszwmarrgswjxmb
"""
EXAMPLE_TWO = """
qjhvhtzxzqqjkmpb
xxyxx
uurcxstgmygtbstg
ieodomkazucvgmuy
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TWO

PART_ONE_RESULT = 2
PART_TWO_RESULT = 2

# ======================================================================
#                                                            TestThelist
# ======================================================================


class TestThelist(unittest.TestCase):  # pylint: disable=R0904
    "Test Thelist object"

    def test_empty_init(self):
        "Test the default Thelist creation"

        # 1. Create default Thelist object
        myobj = thelist.Thelist()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)

    def test_text_init(self):
        "Test the Thelist object creation from text"

        # 1. Create Thelist object from text
        myobj = thelist.Thelist(text=aoc_05.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 5)

        # 3. Check methods
        self.assertEqual(myobj.is_nice('ugknbfddgicrmopn'), True)
        self.assertEqual(myobj.is_nice('aaa'), True)
        self.assertEqual(myobj.is_nice('jchzalrnumimnmhp'), False)
        self.assertEqual(myobj.is_nice('haegwjzuvuyypxyu'), False)
        self.assertEqual(myobj.is_nice('dvszwmarrgswjxmb'), False)

    def test_text_two(self):
        "Test the Thelist object creation from text"

        # 1. Create Thelist object from text
        myobj = thelist.Thelist(text=aoc_05.from_text(EXAMPLE_TWO), part2=True)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, True)
        self.assertEqual(len(myobj.text), 4)

        # 3. Check methods
        self.assertEqual(myobj.is_nice('qjhvhtzxzqqjkmpb'), True)
        self.assertEqual(myobj.is_nice('xxyxx'), True)
        self.assertEqual(myobj.is_nice('ieodomkazucvgmuy'), False)
        self.assertEqual(myobj.is_nice('haegwjzuvuyypxyu'), False)

    def test_part_one(self):
        "Test part one example of Thelist object"

        # 1. Create Thelist object from text
        myobj = thelist.Thelist(text=aoc_05.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Thelist object"

        # 1. Create Thelist object from text
        myobj = thelist.Thelist(part2=True, text=aoc_05.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                  t e s t _ t h e l i s t . p y                 end
# ======================================================================
