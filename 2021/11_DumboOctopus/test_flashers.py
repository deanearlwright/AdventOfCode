# ======================================================================
# Dumbo Octopus
#   Advent of Code 2021 Day 11 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ f l a s h e r s . p y
# ======================================================================
"Test solver for Advent of Code 2021 day 11, Dumbo Octopus"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_11
import flashers

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
"""
STEP_ONE = """
6594254334
3856965822
6375667284
7252447257
7468496589
5278635756
3287952832
7993992245
5957959665
6394862637
"""
STEP_TWO = """
8807476555
5089087054
8597889608
8485769600
8700908800
6600088989
6800005943
0000007456
9000000876
8700006848
"""
STEP_TEN = """
0481112976
0031112009
0041112504
0081111406
0099111306
0093511233
0442361130
5532252350
0532250600
0032240000
"""
STEP_100 = """
0397666866
0749766918
0053976933
0004297822
0004229892
0053222877
0532222966
9322228966
7922286866
6789998766
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 1656
PART_TWO_RESULT = 195

# ======================================================================
#                                                           TestFlashers
# ======================================================================


class TestFlashers(unittest.TestCase):  # pylint: disable=R0904
    "Test Flashers object"

    def test_empty_init(self):
        "Test the default Flashers creation"

        # 1. Create default Flashers object
        myobj = flashers.Flashers()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.octos, {})
        self.assertEqual(myobj.flashes, 0)
        self.assertEqual(myobj.step, 0)

    def test_text_init(self):
        "Test the Flashers object creation from text"

        # 1. Create Flashers object from text
        myobj = flashers.Flashers(text=aoc_11.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 10)
        self.assertEqual(len(myobj.octos), 100)
        self.assertEqual(myobj.flashes, 0)
        self.assertEqual(myobj.step, 0)
        self.assertEqual(str(myobj).strip(), EXAMPLE_TEXT.strip())

        # 3. Check methods
        self.assertEqual(len(myobj.neighbors((0, 0))), 3)
        self.assertEqual(len(myobj.neighbors((1, 0))), 5)
        self.assertEqual(len(myobj.neighbors((1, 1))), 8)

        self.assertEqual(myobj.single_step(), 0)
        self.assertEqual(len(myobj.octos), 100)
        self.assertEqual(myobj.flashes, 0)
        self.assertEqual(myobj.step, 1)
        self.assertEqual(str(myobj).strip(), STEP_ONE.strip())

        self.assertEqual(myobj.single_step(), 35)
        self.assertEqual(len(myobj.octos), 100)
        self.assertEqual(myobj.flashes, 35)
        self.assertEqual(myobj.step, 2)
        self.assertEqual(str(myobj).strip(), STEP_TWO.strip())

        self.assertEqual(myobj.run_until(10), 204)
        self.assertEqual(len(myobj.octos), 100)
        self.assertEqual(myobj.flashes, 204)
        self.assertEqual(myobj.step, 10)
        self.assertEqual(str(myobj).strip(), STEP_TEN.strip())

        self.assertEqual(myobj.run_until(100), 1656)
        self.assertEqual(len(myobj.octos), 100)
        self.assertEqual(myobj.flashes, 1656)
        self.assertEqual(myobj.step, 100)
        self.assertEqual(str(myobj).strip(), STEP_100.strip())

        self.assertEqual(myobj.all_flash(), 195)

    def test_part_one(self):
        "Test part one example of Flashers object"

        # 1. Create Flashers object from text
        myobj = flashers.Flashers(text=aoc_11.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Flashers object"

        # 1. Create Flashers object from text
        myobj = flashers.Flashers(part2=True, text=aoc_11.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ f l a s h e r s . p y                end
# ======================================================================
