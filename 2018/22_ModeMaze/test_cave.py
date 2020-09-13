# ======================================================================
# Mode Maze
#   Advent of Code 2018 Day 22 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ c a v e . p y
# ======================================================================
"Test solver for Advent of Code 2018 day 22, Mode Maze"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_22
import cave

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
depth: 510
target: 10,10
"""
INPUT_TEXT = """
depth: 4002
target: 5,746
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 114
PART_TWO_RESULT = 45

INPUT_ONE_RESULT = 4479
INPUT_TWO_RESULT = None

# ======================================================================
#                                                               TestCave
# ======================================================================


class TestCave(unittest.TestCase):  # pylint: disable=R0904
    "Test Cave object"

    def test_empty_init(self):
        "Test the default Cave creation"

        # 1. Create default Cave object
        myobj = cave.Cave()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.depth, None)
        self.assertEqual(myobj.target, None)
        self.assertEqual(myobj.mouth, None)
        self.assertEqual(myobj.regions, None)
        self.assertEqual(myobj.start, None)
        self.assertEqual(myobj.finish, None)
        self.assertEqual(myobj.maxrow, None)
        self.assertEqual(myobj.maxcol, None)


    def test_text_init(self):
        "Test the Cave object creation from text"

        # 1. Create Cave object from text
        myobj = cave.Cave(text=aoc_22.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 2)
        self.assertEqual(myobj.depth, 510)
        self.assertEqual(myobj.target, 100010)
        self.assertEqual(myobj.mouth, 0)
        self.assertEqual(len(myobj.regions), 0)
        self.assertEqual(myobj.start, None)
        self.assertEqual(myobj.finish, None)
        self.assertEqual(myobj.maxrow, None)
        self.assertEqual(myobj.maxcol, None)

        # 3. Check a couple of regions
        self.assertEqual(myobj.determine_geologic_index(0), 0)
        self.assertEqual(myobj.determine_erosion_level(0), 510)
        self.assertEqual(myobj.determine_region_type(0), cave.ROCKY_TYPE)
        self.assertEqual(myobj.determine_geologic_index(1), 16807)
        self.assertEqual(myobj.determine_erosion_level(1), 17317)
        self.assertEqual(myobj.determine_region_type(1), cave.WET_TYPE)
        self.assertEqual(myobj.determine_geologic_index(cave.ROW_MULT), 48271)
        self.assertEqual(myobj.determine_erosion_level(cave.ROW_MULT), 8415)
        self.assertEqual(myobj.determine_region_type(cave.ROW_MULT), cave.ROCKY_TYPE)
        self.assertEqual(myobj.determine_geologic_index(cave.ROW_MULT+1), 145722555)
        self.assertEqual(myobj.determine_erosion_level(cave.ROW_MULT+1), 1805)
        self.assertEqual(myobj.determine_region_type(cave.ROW_MULT+1), cave.NARROW_TYPE)
        self.assertEqual(myobj.determine_geologic_index(myobj.target), 0)
        self.assertEqual(myobj.determine_erosion_level(myobj.target), 510)
        self.assertEqual(myobj.determine_region_type(myobj.target), cave.ROCKY_TYPE)

    def test_input_init(self):
        "Test the Cave object creation from text"

        # 1. Create Cave object from text
        myobj = cave.Cave(text=aoc_22.from_text(INPUT_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 2)
        self.assertEqual(myobj.depth, 4002)
        self.assertEqual(myobj.target, 7460005)
        self.assertEqual(myobj.mouth, 0)
        self.assertEqual(len(myobj.regions), 0)

        # 3. Try part one
        self.assertEqual(myobj.part_one(verbose=False), INPUT_ONE_RESULT)

    def test_part_one(self):
        "Test part one example of Cave object"

        # 1. Create Cave object from text
        myobj = cave.Cave(text=aoc_22.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)


    def test_part2_init(self):
        "Test the Cave object creation from text for part2"

        # 1. Create Cave object from text
        myobj = cave.Cave(text=aoc_22.from_text(EXAMPLE_TEXT), part2=True)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, True)
        self.assertEqual(len(myobj.text), 2)
        self.assertEqual(myobj.depth, 510)
        self.assertEqual(myobj.target, 100010)
        self.assertEqual(myobj.mouth, 0)
        self.assertEqual(len(myobj.regions), 0)
        self.assertEqual(myobj.start, 100000000)
        self.assertEqual(myobj.finish, 100100010)
        self.assertEqual(myobj.maxrow, 60)
        self.assertEqual(myobj.maxrow, 60)

        # 3. Try part one - to build the regions
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

        # 4. What are all the moves from the start
        self.assertEqual(myobj.valid_tool(myobj.start), True)
        moves = myobj.determine_moves(myobj.start)
        self.assertEqual(len(moves), 2)
        self.assertEqual(moves[0], cave.row_col_tool_to_loc(1, 0, cave.TORCH))
        self.assertEqual(moves[1], cave.row_col_tool_to_loc(0, 0, cave.GEAR))


    def test_part_two(self):
        "Test part two example of Cave object"

        # 1. Create Cave object from text
        myobj = cave.Cave(part2=True, text=aoc_22.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                       t e s t _ c a v e . p y                  end
# ======================================================================
