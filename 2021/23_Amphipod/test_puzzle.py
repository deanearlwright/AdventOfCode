# ======================================================================
# Amphipod
#   Advent of Code 2021 Day 23 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ p u z z l e . p y
# ======================================================================
"Test solver for Advent of Code 2021 day 23, Amphipod"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_23
import puzzle

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########
"""
EXAMPLE_NO_MOVES = """
#############
#...........#
###A#B#C#D###
  #A#B#C#D#
  #########
"""
EXAMPLE_ONE_MOVE = """
#############
#.........A.#
###.#B#C#D###
  #A#B#C#D#
  #########
"""
EXAMPLE_THREE_MOVES = """
#############
#.....D.D.A.#
###.#B#C#.###
  #A#B#C#.#
  #########
"""
EXAMPLE_SEVEN_MOVES = """
#############
#AA.......AD#
###.#B#C#.###
  #D#B#C#.#
  #D#B#C#.#
  #A#B#C#D#
  #########
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 12521
PART_TWO_RESULT = 44169

# ======================================================================
#                                                             TestPuzzle
# ======================================================================


class TestPuzzle(unittest.TestCase):  # pylint: disable=R0904
    "Test Puzzle object"

    def test_empty_init(self):
        "Test the default Puzzle creation"

        # 1. Create default Puzzle object
        myobj = puzzle.Puzzle()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)

    def test_text_init(self):
        "Test the Puzzle object creation from text"

        # 1. Create Puzzle object from text
        myobj = puzzle.Puzzle(text=aoc_23.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 5)

        # 3. Check methods
        self.assertEqual(myobj.burrow.positions(), "...........BACDBCDA")
        self.assertEqual(myobj.organize(), 12521)

    def test_no_moves(self):
        "Test the Puzzle object creation from text that is complete"

        # 1. Create Puzzle object from text
        myobj = puzzle.Puzzle(text=aoc_23.from_text(EXAMPLE_NO_MOVES))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 5)

        # 3. Check methods
        self.assertEqual(myobj.burrow.positions(), "...........AABBCCDD")
        self.assertEqual(myobj.organize(), 0)

    def test_one_move(self):
        "Test the Puzzle object creation from text that needs only one move"

        # 1. Create Puzzle object from text
        myobj = puzzle.Puzzle(text=aoc_23.from_text(EXAMPLE_ONE_MOVE))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 5)

        # 3. Check methods
        self.assertEqual(myobj.burrow.positions(), ".........A..ABBCCDD")
        self.assertEqual(myobj.organize(), 8)

    def test_three_moves(self):
        "Test the Puzzle object creation from text that needs three moves"

        # 1. Create Puzzle object from text
        myobj = puzzle.Puzzle(text=aoc_23.from_text(EXAMPLE_THREE_MOVES))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 5)

        # 3. Check methods
        self.assertEqual(myobj.burrow.positions(), ".....D.D.A..ABBCC..")
        self.assertEqual(myobj.organize(), 7008)

    def test_seven_moves(self):
        "Test the Puzzle object creation from text that needs three moves"

        # 1. Create Puzzle object from text
        myobj = puzzle.Puzzle(text=aoc_23.from_text(EXAMPLE_SEVEN_MOVES))
        myobj.part2 = True

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, True)
        self.assertEqual(len(myobj.text), 7)

        # 3. Check methods
        self.assertEqual(myobj.burrow.positions(), "AA.......AD.DDABBBBCCCC...D")
        self.assertEqual(myobj.organize(), 25016)

    def test_part_one(self):
        "Test part one example of Puzzle object"

        # 1. Create Puzzle object from text
        myobj = puzzle.Puzzle(part2=False, text=aoc_23.from_text(PART_ONE_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Puzzle object"

        # 1. Create Puzzle object from text
        myobj = puzzle.Puzzle(part2=True, text=aoc_23.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=True), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ p u z z l e . p y                  end
# ======================================================================
