# ======================================================================
# Crab Cups
#   Advent of Code 2020 Day 23 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ g a m e . p y
# ======================================================================
"Test solver for Advent of Code 2020 day 23, Crab Cups"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_23
import game

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
389125467
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = '67384529'
PART_TWO_RESULT = 149245887792

# ======================================================================
#                                                              TestGame
# ======================================================================


class TestGame(unittest.TestCase):  # pylint: disable=R0904
    "Test Game object"

    def test_empty_init(self):
        "Test the default Game creation"

        # 1. Create default Game object
        myobj = game.Game()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.current, None)
        self.assertEqual(myobj.maximum, None)
        self.assertEqual(myobj.cups, {})

    def test_text_init(self):
        "Test the Game object creation from text"

        # 1. Create Game object from text
        myobj = game.Game(text=aoc_23.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 1)
        self.assertEqual(myobj.current, 3)
        self.assertEqual(myobj.maximum, 9)
        self.assertEqual(len(myobj.cups), 9)
        self.assertEqual(myobj.cups[3], 8)
        self.assertEqual(myobj.cups[8], 9)
        self.assertEqual(myobj.cups[9], 1)
        self.assertEqual(myobj.cups[6], 7)
        self.assertEqual(myobj.cups[7], 3)

        # 3. Test methods
        myobj.one_turn()  # move 1
        self.assertEqual(myobj.current, 2)
        myobj.one_turn()  # move 2
        self.assertEqual(myobj.current, 5)
        myobj.one_turn()  # move 3
        self.assertEqual(myobj.current, 8)
        myobj.one_turn()  # move 4
        self.assertEqual(myobj.current, 4)
        myobj.one_turn()  # move 5
        self.assertEqual(myobj.current, 1)
        myobj.one_turn()  # move 6
        self.assertEqual(myobj.current, 9)
        myobj.one_turn()  # move 7
        self.assertEqual(myobj.current, 2)
        myobj.one_turn()  # move 8
        self.assertEqual(myobj.current, 6)
        myobj.one_turn()  # move 9
        self.assertEqual(myobj.current, 5)
        myobj.one_turn()  # move 10
        self.assertEqual(myobj.current, 8)
        self.assertEqual(myobj.labeled(), '92658374')

    def test_part_one(self):
        "Test part one example of Game object"

        # 1. Create Game object from text
        myobj = game.Game(text=aoc_23.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Game object"

        # 1. Create Game object from text
        myobj = game.Game(part2=True, text=aoc_23.from_text(PART_TWO_TEXT))
        self.assertEqual(myobj.current, 3)
        self.assertEqual(myobj.maximum, 1000000)
        self.assertEqual(len(myobj.cups), 1000000)
        self.assertEqual(myobj.cups[3], 8)
        self.assertEqual(myobj.cups[8], 9)
        self.assertEqual(myobj.cups[9], 1)
        self.assertEqual(myobj.cups[6], 7)
        self.assertEqual(myobj.cups[7], 10)
        self.assertEqual(myobj.cups[10], 11)
        self.assertEqual(myobj.cups[1000000], 3)

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ g a m e . p y                end
# ======================================================================
