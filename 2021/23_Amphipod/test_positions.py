# ======================================================================
# Amphipod
#   Advent of Code 2021 Day 23 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ p o s i t i o n s . p y
# ======================================================================
"Test Positions for Advent of Code 2021 day 23, Amphipod"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import positions

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = "...........BACDBCDA"
EXAMPLE_VALUES = ['.' for _ in range(19)]
EXAMPLE_DISPLAY = """
#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########
""".strip()
EXAMPLE_DOORWAYS = [2, 4, 6, 8]
EXAMPLE_HOMEROOMS = {
  'A': [11, 12],
  'B': [13, 14],
  'C': [15, 16],
  'D': [17, 18],
}
ONE_MOVE = ".........A..ABBCCDD"
SOLUTION = "...........AABBCCDD"
A_FROM_D = ".....D.D...BAC.BC.A"

# ======================================================================
#                                                          TestPositions
# ======================================================================


class TestPositions(unittest.TestCase):  # pylint: disable=R0904
    "Test Positions object"

    def test_empty_init(self):
        "Test the default Positions creation"

        # 1. Create default Positions object
        myobj = positions.Positions()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.hall_len, 11)
        self.assertEqual(myobj.room_len, 2)
        self.assertEqual(myobj.room_num, 4)
        self.assertEqual(myobj.spaces, EXAMPLE_VALUES)
        self.assertEqual(myobj.doorways, EXAMPLE_DOORWAYS)
        self.assertEqual(myobj.homerooms, EXAMPLE_HOMEROOMS)

    def test_text_init(self):
        "Test the Positions object creation from text"

        # 1. Create Positions object from text
        myobj = positions.Positions(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 19)
        self.assertEqual(myobj.hall_len, 11)
        self.assertEqual(myobj.room_len, 2)
        self.assertEqual(myobj.room_num, 4)
        self.assertEqual(myobj.spaces, list(EXAMPLE_TEXT))
        self.assertEqual(myobj.doorways, EXAMPLE_DOORWAYS)
        self.assertEqual(myobj.homerooms, EXAMPLE_HOMEROOMS)

        # 3. Check methods
        self.assertEqual(str(myobj), EXAMPLE_TEXT)
        self.assertEqual(myobj.display(), EXAMPLE_DISPLAY)

        self.assertEqual(myobj.are_all_home(), False)
        self.assertEqual(myobj.frozen(), [12, 16])
        self.assertEqual(myobj.doorway_for_who('A'), 2)
        self.assertEqual(myobj.doorway_for_who('C'), 6)
        self.assertEqual(myobj.hall_steps([0, 11], who='A'), 3)
        self.assertEqual(myobj.hall_steps([0, 12], who='A'), 4)
        self.assertEqual(myobj.hall_steps([7, 11], who='A'), 6)
        self.assertEqual(myobj.hall_steps([7, 12], who='A'), 7)
        self.assertEqual(myobj.hall_steps([9, 11], who='A'), 8)
        self.assertEqual(myobj.room_steps([12, 7]), 7)
        self.assertEqual(myobj.room_steps([13, 3]), 2)
        self.assertEqual(myobj.steps([9, 11], who='A'), 8)
        self.assertEqual(myobj.steps([13, 3], who='B'), 2)
        self.assertEqual(myobj.steps([13, 12], who='A'), 5)
        self.assertEqual(myobj.cost([9, 18], who='D'), 3000)

        self.assertEqual(myobj.moves_from_room(11), [0, 1, 3, 5, 7, 9, 10])

        self.assertEqual(myobj.all_moves(who='A'), [])
        self.assertEqual(myobj.all_moves(who='B'),
                         [(11, 0), (11, 1), (11, 3), (11, 5), (11, 7), (11, 9), (11, 10),
                          (15, 0), (15, 1), (15, 3), (15, 5), (15, 7), (15, 9), (15, 10)])
        self.assertEqual(myobj.all_moves(who='C'),
                         [(13, 0), (13, 1), (13, 3), (13, 5), (13, 7), (13, 9), (13, 10)])
        self.assertEqual(myobj.all_moves(who='D'),
                         [(17, 0), (17, 1), (17, 3), (17, 5), (17, 7), (17, 9), (17, 10)])

    def test_one_move(self):
        "Test the Puzzle object creation from text that needs only one move"

        # 1. Create Positions object from text
        myobj = positions.Positions(text=ONE_MOVE)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 19)
        self.assertEqual(myobj.hall_len, 11)
        self.assertEqual(myobj.room_len, 2)
        self.assertEqual(myobj.room_num, 4)
        self.assertEqual(myobj.spaces, list(ONE_MOVE))
        self.assertEqual(myobj.doorways, EXAMPLE_DOORWAYS)
        self.assertEqual(myobj.homerooms, EXAMPLE_HOMEROOMS)

        # 3. Check methods
        self.assertEqual(myobj.can_enter_room('A', 13), False)
        self.assertEqual(myobj.can_enter_room('A', 11), True)
        self.assertEqual(myobj.moves_from_hall(9, who='A'), [11])
        self.assertEqual(myobj.moves_from(9, who='A'), [11])
        self.assertEqual(myobj.all_moves(), [(9, 11)])
        self.assertEqual(myobj.steps((9, 11)), 8)
        self.assertEqual(myobj.cost((9, 11)), 8)
        self.assertEqual(myobj.execute((9, 11)), SOLUTION)

    def test_a_from_d(self):
        "Test the Puzzle object creation from text where we need to move the A from the D room"

        # 1. Create Positions object from text
        myobj = positions.Positions(text=A_FROM_D)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 19)
        self.assertEqual(myobj.hall_len, 11)
        self.assertEqual(myobj.room_len, 2)
        self.assertEqual(myobj.room_num, 4)
        self.assertEqual(myobj.spaces, list(A_FROM_D))
        self.assertEqual(myobj.doorways, EXAMPLE_DOORWAYS)
        self.assertEqual(myobj.homerooms, EXAMPLE_HOMEROOMS)

        # 3. Check methods
        self.assertEqual(myobj.doorway_for_room(18), 8)
        self.assertEqual(myobj.can_leave_room(18), True)
        self.assertEqual(myobj.moves_from_room(18), [9, 10])
        self.assertEqual(myobj.moves_from(18), [9, 10])
        self.assertEqual(myobj.all_moves(who='A'), [(18, 9), (18, 10)])
        self.assertEqual(myobj.steps((18, 9)), 3)
        self.assertEqual(myobj.cost((18, 9)), 3)
        self.assertEqual(myobj.execute((18, 9)), ".....D.D.A.BAC.BC..")


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                t e s t _ p o s i t i o n s . p y               end
# ======================================================================
