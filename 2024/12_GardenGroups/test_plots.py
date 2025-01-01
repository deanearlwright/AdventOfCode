
# ======================================================================
# Garden Groups
#   Advent of Code 2024 Day 12 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ p l o t s . p y
# ======================================================================
"Test solver for Advent of Code 2024 day 12, Garden Groups"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_12
import plots

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_ONE = """
AAAA
BBCD
BBCC
EEEC
""" # 140, 80
EXAMPLE_TWO = """
OOOOO
OXOXO
OOOOO
OXOXO
OOOOO
""" # 772, 436
EXAMPLE_THREE = """
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
""" # 1930, 1206
EXAMPLE_FOUR = """
EEEEE
EXXXX
EEEEE
EXXXX
EEEEE
""" # ---, 236
EXAMPLE_FIVE = """
AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA
""" # ---, 368
PART_ONE_TEXT = EXAMPLE_ONE
PART_TWO_TEXT = EXAMPLE_ONE

PART_ONE_RESULT = 140
PART_TWO_RESULT = 80

# ======================================================================
#                                                              TestPlots
# ======================================================================


class TestPlots(unittest.TestCase):  # pylint: disable=R0904
    "Test Plots object"

    def test_empty_init(self):
        "Test the default Plots creation"

        # 1. Create default Plots object
        myobj = plots.Plots()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.rows, 0)
        self.assertEqual(myobj.cols, 0)
        self.assertEqual(len(myobj.regions), 0)
        self.assertEqual(len(myobj.mapped), 0)

    def test_text_init(self):
        "Test the Plots object creation from text"

        # 1. Create Plots object from text
        myobj = plots.Plots(text=aoc_12.from_text(EXAMPLE_ONE))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 4)
        self.assertEqual(myobj.rows, 4)
        self.assertEqual(myobj.cols, 4)
        self.assertEqual(len(myobj.regions), 5)
        self.assertEqual(len(myobj.mapped), 16)

        # 3. Check methods
        self.assertEqual(myobj.part_one(), 140)
        self.assertEqual(myobj.part_two(), 80)

    def test_text_two(self):
        "Test the Plots object creation from text"

        # 1. Create Plots object from text
        myobj = plots.Plots(text=aoc_12.from_text(EXAMPLE_TWO))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 5)
        self.assertEqual(myobj.rows, 5)
        self.assertEqual(myobj.cols, 5)
        self.assertEqual(len(myobj.regions), 5)
        self.assertEqual(len(myobj.mapped), 25)

        # 3. Check methods
        self.assertEqual(myobj.part_one(), 772)
        self.assertEqual(myobj.part_two(), 436)

    def test_text_three(self):
        "Test the Plots object creation from text"

        # 1. Create Plots object from text
        myobj = plots.Plots(text=aoc_12.from_text(EXAMPLE_THREE))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 10)
        self.assertEqual(myobj.rows, 10)
        self.assertEqual(myobj.cols, 10)
        self.assertEqual(len(myobj.regions), 11)
        self.assertEqual(len(myobj.mapped), 100)

        # 3. Check methods
        self.assertEqual(myobj.part_one(), 1930)
        self.assertEqual(myobj.part_two(), 1206)

    def test_text_four(self):
        "Test the Plots object creation from text"

        # 1. Create Plots object from text
        myobj = plots.Plots(text=aoc_12.from_text(EXAMPLE_FOUR), part2=True)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, True)
        self.assertEqual(len(myobj.text), 5)
        self.assertEqual(myobj.rows, 5)
        self.assertEqual(myobj.cols, 5)
        self.assertEqual(len(myobj.regions), 3)
        self.assertEqual(len(myobj.mapped), 25)

        # 3. Check methods
        self.assertEqual(myobj.part_two(), 236)

    def test_text_five(self):
        "Test the Plots object creation from text"

        # 1. Create Plots object from text
        myobj = plots.Plots(text=aoc_12.from_text(EXAMPLE_FIVE), part2=True)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, True)
        self.assertEqual(len(myobj.text), 6)
        self.assertEqual(myobj.rows, 6)
        self.assertEqual(myobj.cols, 6)
        self.assertEqual(len(myobj.regions), 3)
        self.assertEqual(len(myobj.mapped), 36)

        # 3. Check methods
        self.assertEqual(myobj.part_two(), 368)

    def test_part_one(self):
        "Test part one example of Plots object"

        # 1. Create Plots object from text
        text = aoc_12.from_text(PART_ONE_TEXT)
        myobj = plots.Plots(text=text)

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Plots object"

        # 1. Create Plots object from text
        text = aoc_12.from_text(PART_TWO_TEXT)
        myobj = plots.Plots(part2=True, text=text)

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ p l o t s . p y                   end
# ======================================================================
