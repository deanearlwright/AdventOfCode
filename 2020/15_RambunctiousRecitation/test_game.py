# ======================================================================
# Rambunctious Recitation
#   Advent of Code 2020 Day 15 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ g a m e . p y
# ======================================================================
"Test solver for Advent of Code 2020 day 15, Rambunctious Recitation"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_15
import game

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
0,3,6
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 436
PART_TWO_RESULT = 175594

EXAMPLES = [
    {'text': '1,3,2', 'spoken': 1},
    {'text': '2,1,3', 'spoken': 10},
    {'text': '1,2,3', 'spoken': 27},
    {'text': '2,3,1', 'spoken': 78},
    {'text': '3,2,1', 'spoken': 438},
    {'text': '3,1,2', 'spoken': 1836},
]

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

    def test_text_init(self):
        "Test the Game object creation from text"

        # 1. Create Game object from text
        myobj = game.Game(text=aoc_15.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 1)

        self.assertEqual(myobj.number_spoken(turn=9), 4)

    def test_examples_one(self):
        "Test the part one examples"

        # 1. Loop for all the examples
        for example in EXAMPLES:

            # 2. Create the game object
            myobj = game.Game(text=[example['text']])

            # 3. Verify the 2020th spoken
            self.assertEqual(myobj.part_one(verbose=False), example['spoken'])

    def test_part_one(self):
        "Test part one example of Game object"

        # 1. Create Game object from text
        myobj = game.Game(text=aoc_15.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Game object"

        # 1. Create Game object from text
        myobj = game.Game(part2=True, text=aoc_15.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      t e s t _ g a m e . p y                   end
# ======================================================================
