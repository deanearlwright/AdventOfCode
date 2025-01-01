
# ======================================================================
# Restroom Redoubt
#   Advent of Code 2024 Day 14 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ l o b b y . p y
# ======================================================================
"Test solver for Advent of Code 2024 day 14, Restroom Redoubt"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_14
import lobby

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
TEST_SIZE = (11, 7)

EXAMPLE_TEXT = """
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = ""

PART_ONE_RESULT = 12
PART_TWO_RESULT = 0

# ======================================================================
#                                                              TestLobby
# ======================================================================


class TestLobby(unittest.TestCase):  # pylint: disable=R0904
    "Test Lobby object"

    def test_empty_init(self):
        "Test the default Lobby creation"

        # 1. Create default Lobby object
        myobj = lobby.Lobby()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.size, (101, 103))
        self.assertEqual(len(myobj.robots), 0)

    def test_text_init(self):
        "Test the Lobby object creation from text"

        # 1. Create Lobby object from text
        myobj = lobby.Lobby(text=aoc_14.from_text(EXAMPLE_TEXT), size=TEST_SIZE)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 12)
        self.assertEqual(myobj.size, (11, 7))
        self.assertEqual(len(myobj.robots), 12)

        # 3. Check methods()
        print(myobj)
        print("\n")
        self.assertEqual(myobj.quadrants(), [4, 4, 0, 2, 2])
        self.assertEqual(myobj.safety(), 0)
        myobj.move_all_multiple()
        print(myobj)
        print("\n")
        self.assertEqual(myobj.quadrants(), [3, 1, 3, 4, 1])
        self.assertEqual(myobj.safety(), 12)

    def test_part_one(self):
        "Test part one example of Lobby object"

        # 1. Create Lobby object from text
        text = aoc_14.from_text(PART_ONE_TEXT)
        myobj = lobby.Lobby(text=text, size=TEST_SIZE)

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Lobby object"

        # 1. Create Lobby object from text
        text = aoc_14.from_text(PART_TWO_TEXT)
        myobj = lobby.Lobby(part2=True, text=text, size=TEST_SIZE)

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ l o b b y . p y                   end
# ======================================================================
