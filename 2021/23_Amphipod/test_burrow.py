# ======================================================================
# Amphipod
#   Advent of Code 2021 Day 23 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ b u r r o w . p y
# ======================================================================
"Test map for Advent of Code 2021 day 23, Amphipod"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_23
import burrow

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

# ======================================================================
#                                                             TestBurrow
# ======================================================================


class TestBurrow(unittest.TestCase):  # pylint: disable=R0904
    "Test Burrow object"

    def test_empty_init(self):
        "Test the default Burrow creation"

        # 1. Create default Burrow object
        myobj = burrow.Burrow()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.hallway, None)
        self.assertEqual(myobj.rooms, {})
        self.assertEqual(myobj.hall_len, 0)
        self.assertEqual(myobj.room_len, 0)
        self.assertEqual(myobj.poss_len, 0)

    def test_text_init(self):
        "Test the Burrow object creation from text"

        # 1. Create Burrow object from text
        myobj = burrow.Burrow(text=aoc_23.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 5)
        self.assertEqual(len(myobj.hallway.doorways), 4)
        self.assertEqual(len(myobj.rooms), 4)
        self.assertEqual(myobj.hall_len, 11)
        self.assertEqual(myobj.room_len, 2)
        self.assertEqual(myobj.poss_len, 11 + 4 * 2)

        # 3. Check methods
        self.assertEqual(str(myobj), EXAMPLE_TEXT.strip())
        self.assertEqual(myobj.position(0), '.')
        self.assertEqual(myobj.position(11), 'B')
        self.assertEqual(myobj.position(14), 'D')
        self.assertEqual(myobj.positions(), "...........BACDBCDA")

        self.assertEqual(myobj.is_in_hall(0), True)
        self.assertEqual(myobj.is_in_hall(10), True)
        self.assertEqual(myobj.is_in_hall(11), False)

    def test_two_init(self):
        "Test the Burrow object creation from text"

        # 1. Create Burrow object from text for part2
        myobj = burrow.Burrow(text=aoc_23.from_text(EXAMPLE_TEXT), part2=True)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, True)
        self.assertEqual(len(myobj.text), 7)
        self.assertEqual(len(myobj.hallway.doorways), 4)
        self.assertEqual(len(myobj.rooms), 4)
        self.assertEqual(myobj.hall_len, 11)
        self.assertEqual(myobj.room_len, 4)
        self.assertEqual(myobj.poss_len, 11 + 4 * 4)

        # 3. Check methods
        self.assertEqual(len(myobj.positions()), myobj.poss_len)
        self.assertEqual(myobj.position(0), '.')
        self.assertEqual(myobj.position(11), 'B')
        self.assertEqual(myobj.position(12), 'D')
        self.assertEqual(myobj.position(13), 'D')
        self.assertEqual(myobj.position(14), 'A')
        self.assertEqual(myobj.positions(), "...........BDDACCBDBBACDACA")

        self.assertEqual(myobj.is_in_hall(0), True)
        self.assertEqual(myobj.is_in_hall(10), True)
        self.assertEqual(myobj.is_in_hall(11), False)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ b u r r o w . p y                  end
# ======================================================================
