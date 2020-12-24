# ======================================================================
# Seating System
#   Advent of Code 2020 Day 11 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ c o n w a y . p y
# ======================================================================
"Test solver for Advent of Code 2020 day 11, Seating System"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_11
import conway

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
"""

ROUND_ONE = """
#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##
""".strip()

ROUND_TWO = """
#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##
""".strip()

ROUND_THREE = """
#.##.L#.##
#L###LL.L#
L.#.#..#..
#L##.##.L#
#.##.LL.LL
#.###L#.##
..#.#.....
#L######L#
#.LL###L.L
#.#L###.##
""".strip()

ROUND_FOUR = """
#.#L.L#.##
#LLL#LL.L#
L.L.L..#..
#LLL.##.L#
#.LL.LL.LL
#.LL#L#.##
..L.L.....
#L#LLLL#L#
#.LLLLLL.L
#.#L#L#.##
""".strip()

ROUND_FIVE = """
#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##
""".strip()

PART2_TWO = """
#.LL.LL.L#
#LLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLLL.L
#.LLLLL.L#
""".strip()

PART2_THREE = """
#.L#.##.L#
#L#####.LL
L.#.#..#..
##L#.##.##
#.##.#L.##
#.#####.#L
..#.#.....
LLL####LL#
#.L#####.L
#.L####.L#
""".strip()


PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 37
PART_TWO_RESULT = 26

# ======================================================================
#                                                             TestConway
# ======================================================================


class TestConway(unittest.TestCase):  # pylint: disable=R0904
    "Test Conway object"

    def test_empty_init(self):
        "Test the default Conway creation"

        # 1. Create default Conway object
        myobj = conway.Conway()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.rows, 0)
        self.assertEqual(myobj.cols, 0)
        self.assertEqual(myobj.rnds, 0)
        self.assertEqual(myobj.limit, 4)
        self.assertEqual(len(myobj.seats), 0)
        self.assertEqual(len(myobj.current), 0)
        self.assertEqual(myobj.previous, None)

    def test_text_init(self):
        "Test the Conway object creation from text"

        # 1. Create Conway object from text
        myobj = conway.Conway(text=aoc_11.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 10)
        self.assertEqual(myobj.rows, 10)
        self.assertEqual(myobj.cols, 10)
        self.assertEqual(myobj.rnds, 0)
        self.assertEqual(myobj.limit, 4)
        self.assertEqual(len(myobj.seats), 71)
        self.assertEqual(len(myobj.current), 0)
        self.assertEqual(myobj.previous, None)

        # 3. Test methods
        self.assertEqual(str(myobj), EXAMPLE_TEXT.strip())
        myobj.fill_all_seats()
        self.assertEqual(myobj.rnds, 1)
        self.assertEqual(len(myobj.seats), 71)
        self.assertEqual(len(myobj.current), 71)
        self.assertEqual(myobj.count_occupied(), 71)
        self.assertEqual(myobj.unchanged(), False)
        self.assertEqual(str(myobj), ROUND_ONE)

        myobj.next_round()
        self.assertEqual(myobj.rnds, 2)
        self.assertEqual(len(myobj.seats), 71)
        self.assertEqual(len(myobj.current), 20)
        self.assertEqual(myobj.count_occupied(), 20)
        self.assertEqual(myobj.unchanged(), False)
        self.assertEqual(str(myobj), ROUND_TWO)

        myobj.next_round()
        self.assertEqual(myobj.rnds, 3)
        self.assertEqual(myobj.unchanged(), False)
        self.assertEqual(str(myobj), ROUND_THREE)

        myobj.next_round()
        self.assertEqual(myobj.rnds, 4)
        self.assertEqual(myobj.unchanged(), False)
        self.assertEqual(str(myobj), ROUND_FOUR)

        myobj.next_round()
        self.assertEqual(myobj.rnds, 5)
        self.assertEqual(myobj.unchanged(), False)
        self.assertEqual(str(myobj), ROUND_FIVE)
        self.assertEqual(myobj.count_occupied(), 37)

        myobj.next_round()
        self.assertEqual(myobj.rnds, 6)
        self.assertEqual(myobj.unchanged(), True)
        self.assertEqual(str(myobj), ROUND_FIVE)
        self.assertEqual(myobj.count_occupied(), 37)

    def test_text_init_part2(self):
        "Test the Conway object creation from text for part2"

        # 1. Create Conway object from text
        myobj = conway.Conway(text=aoc_11.from_text(EXAMPLE_TEXT), part2=True)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, True)
        self.assertEqual(len(myobj.text), 10)
        self.assertEqual(myobj.rows, 10)
        self.assertEqual(myobj.cols, 10)
        self.assertEqual(myobj.rnds, 0)
        self.assertEqual(myobj.limit, 5)
        self.assertEqual(len(myobj.seats), 71)
        self.assertEqual(len(myobj.current), 0)
        self.assertEqual(myobj.previous, None)

        # 3. Test methods
        self.assertEqual(str(myobj), EXAMPLE_TEXT.strip())
        myobj.fill_all_seats()
        self.assertEqual(myobj.rnds, 1)
        self.assertEqual(len(myobj.seats), 71)
        self.assertEqual(len(myobj.current), 71)
        self.assertEqual(myobj.count_occupied(), 71)
        self.assertEqual(myobj.unchanged(), False)
        self.assertEqual(str(myobj), ROUND_ONE)

        myobj.next_round()
        self.assertEqual(myobj.rnds, 2)
        self.assertEqual(len(myobj.seats), 71)
        self.assertEqual(len(myobj.current), 7)
        self.assertEqual(myobj.count_occupied(), 7)
        self.assertEqual(myobj.unchanged(), False)
        self.assertEqual(str(myobj), PART2_TWO)

        myobj.next_round()
        self.assertEqual(myobj.rnds, 3)
        self.assertEqual(myobj.unchanged(), False)
        self.assertEqual(str(myobj), PART2_THREE)

    def test_part_one(self):
        "Test part one example of Conway object"

        # 1. Create Conway object from text
        myobj = conway.Conway(text=aoc_11.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Conway object"

        # 1. Create Conway object from text
        myobj = conway.Conway(part2=True, text=aoc_11.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ c o n w a y . p y                  end
# ======================================================================
