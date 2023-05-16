
# ======================================================================
# Pyroclastic Flow
#   Advent of Code 2022 Day 17 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ c h a m b e r . p y
# ======================================================================
"Test Chamber for Advent of Code 2022 day 17, Pyroclastic Flow"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import chamber
import rock

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = "7"
ROCK_ONE_INIT = "|..@@@@.|\n|.......|\n|.......|\n|.......|\n+-------+"
ROCK_ONE_RGHT = "|...@@@@|\n|.......|\n|.......|\n|.......|\n+-------+"
ROCK_ONE_LEFT = "|.@@@@..|\n|.......|\n|.......|\n|.......|\n+-------+"
ROCK_ONE_DOWN = "|.......|\n|@@@@...|\n|.......|\n|.......|\n+-------+"
ROCK_ONE_REST = "|.......|\n|.......|\n|.......|\n|####...|\n+-------+"

# ======================================================================
#                                                            TestChamber
# ======================================================================


class TestChamber(unittest.TestCase):  # pylint: disable=R0904
    "Test Chamber object"

    def test_empty_init(self):
        "Test the default Chamber creation"

        # 1. Create default Chamber object
        myobj = chamber.Chamber()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.width, 0)
        self.assertEqual(len(myobj.rows), 0)
        self.assertEqual(myobj.falling, None)
        self.assertEqual(myobj.rocks, 0)

    def test_text_init(self):
        "Test the Chamber object creation from text"

        # 1. Create Chamber object from text
        myobj = chamber.Chamber(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 1)
        self.assertEqual(myobj.width, 7)
        self.assertEqual(len(myobj.rows), 1)
        self.assertEqual(myobj.falling, None)
        self.assertEqual(myobj.rocks, 0)

        # 3. Check methods
        self.assertEqual(str(myobj), "+-------+")
        self.assertEqual(myobj.get_highest(), 0)

        rock_one = rock.Rock(text="1,4,1,####")
        myobj.add_rock(rock_one)
        self.assertEqual(rock_one.loc, (3, 4))
        self.assertEqual(str(myobj), ROCK_ONE_INIT)

        self.assertEqual(myobj.push_rock('>'), True)
        self.assertEqual(str(myobj), ROCK_ONE_RGHT)
        self.assertEqual(myobj.push_rock('>'), False)
        self.assertEqual(str(myobj), ROCK_ONE_RGHT)
        self.assertEqual(myobj.push_rock('<'), True)
        self.assertEqual(str(myobj), ROCK_ONE_INIT)
        self.assertEqual(myobj.push_rock('<'), True)
        self.assertEqual(str(myobj), ROCK_ONE_LEFT)
        self.assertEqual(myobj.push_rock('<'), True)
        self.assertEqual(myobj.push_rock('<'), False)
        self.assertEqual(myobj.push_rock('<'), False)
        self.assertEqual(rock_one.loc, (1, 4))
        self.assertEqual(myobj.move_down(), True)
        self.assertEqual(rock_one.loc, (1, 3))
        self.assertEqual(str(myobj), ROCK_ONE_DOWN)
        self.assertEqual(myobj.move_down(), True)
        self.assertEqual(myobj.move_down(), True)
        self.assertEqual(myobj.move_down(), False)
        self.assertEqual(str(myobj), ROCK_ONE_REST)
        self.assertEqual(myobj.falling, None)
        self.assertEqual(myobj.rocks, 1)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                  t e s t _ c h a m b e r . p y                 end
# ======================================================================
