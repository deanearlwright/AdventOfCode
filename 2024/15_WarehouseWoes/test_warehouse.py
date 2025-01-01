
# ======================================================================
# Warehouse Woes
#   Advent of Code 2024 Day 15 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ w a r e h o u s e . p y
# ======================================================================
"Test solver for Advent of Code 2024 day 15, Warehouse Woes"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_15
import warehouse

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<
"""
EXAMPLE_TWO = """
##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
"""
EXAMPLE_THREE = """
#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TWO

PART_ONE_RESULT = 2028
PART_TWO_RESULT = 9021

# ======================================================================
#                                                          TestWarehouse
# ======================================================================


class TestWarehouse(unittest.TestCase):  # pylint: disable=R0904
    "Test Warehouse object"

    def test_empty_init(self):
        "Test the default Warehouse creation"

        # 1. Create default Warehouse object
        myobj = warehouse.Warehouse()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.robot, None)
        self.assertEqual(len(myobj.boxes), 0)
        self.assertEqual(len(myobj.walls), 0)
        self.assertEqual(myobj.rows, 0)
        self.assertEqual(myobj.cols, 0)

    def test_text_init(self):
        "Test the Warehouse object creation from text"

        # 1. Create Warehouse object from text
        myobj = warehouse.Warehouse(text=aoc_15.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 9)
        self.assertNotEqual(myobj.robot, None)
        self.assertNotEqual(myobj.robot.loc, (3, 3))
        self.assertEqual(len(myobj.boxes), 6)
        self.assertEqual(len(myobj.walls), 30)
        self.assertEqual(myobj.rows, 8)
        self.assertEqual(myobj.cols, 8)

        # 3. Check methods
        self.assertEqual(myobj.move_robot(), True)
        self.assertEqual(myobj.move_robot(), True)
        self.assertEqual(myobj.move_robot(), True)
        self.assertEqual(myobj.move_robot(), True)
        self.assertEqual(myobj.move_robot(), True)
        self.assertEqual(myobj.move_robot(), True)
        self.assertEqual(myobj.move_robot(), True)
        self.assertEqual(myobj.move_robot(), True)
        self.assertEqual(myobj.move_robot(), True)
        self.assertEqual(myobj.move_robot(), True)
        self.assertEqual(myobj.move_robot(), True)
        self.assertEqual(myobj.move_robot(), True)
        self.assertEqual(myobj.move_robot(), True)
        self.assertEqual(myobj.move_robot(), True)
        self.assertEqual(myobj.move_robot(), True)
        self.assertEqual(myobj.move_robot(), False)
        self.assertEqual(myobj.gps(), 2028)

    def test_text_two(self):
        "Test the Warehouse object creation from second example"

        # 1. Create Warehouse object from text
        myobj = warehouse.Warehouse(text=aoc_15.from_text(EXAMPLE_TWO))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 20)
        self.assertNotEqual(myobj.robot, None)
        self.assertNotEqual(myobj.robot.loc, (3, 3))
        self.assertEqual(len(myobj.boxes), 21)
        self.assertEqual(len(myobj.walls), 37)
        self.assertEqual(myobj.rows, 10)
        self.assertEqual(myobj.cols, 10)

        # 3. Check methods
        myobj.move_until_finished()
        self.assertEqual(myobj.gps(), 10092)

    def test_text_three(self):
        "Test the Warehouse object creation from part 2 small example"

        # 1. Create Warehouse object from text
        myobj = warehouse.Warehouse(text=aoc_15.from_text(EXAMPLE_THREE), part2=True)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, True)
        self.assertEqual(len(myobj.text), 8)
        self.assertNotEqual(myobj.robot, None)
        self.assertNotEqual(myobj.robot.loc, (3, 3))
        self.assertEqual(len(myobj.boxes), 3)
        self.assertEqual(len(myobj.walls), 50)
        self.assertEqual(myobj.rows, 7)
        self.assertEqual(myobj.cols, 14)

        # 3. Check methods
        self.assertEqual(myobj.move_robot(), True)
        self.assertEqual(myobj.move_robot(), True)
        self.assertEqual(myobj.move_robot(), True)
        self.assertEqual(myobj.move_robot(), True)
        self.assertEqual(myobj.move_robot(), True)
        self.assertEqual(myobj.move_robot(), True)
        self.assertEqual(myobj.move_robot(), True)
        self.assertEqual(myobj.move_robot(), True)
        self.assertEqual(myobj.move_robot(), True)
        self.assertEqual(myobj.move_robot(), True)
        self.assertEqual(myobj.move_robot(), True)
        self.assertEqual(myobj.move_robot(), False)
        self.assertEqual(myobj.gps(), 618)

    def test_part_one(self):
        "Test part one example of Warehouse object"

        # 1. Create Warehouse object from text
        text = aoc_15.from_text(PART_ONE_TEXT)
        myobj = warehouse.Warehouse(text=text)

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Warehouse object"

        # 1. Create Warehouse object from text
        text = aoc_15.from_text(PART_TWO_TEXT)
        myobj = warehouse.Warehouse(part2=True, text=text)

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                t e s t _ w a r e h o u s e . p y               end
# ======================================================================
