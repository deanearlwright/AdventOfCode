# ======================================================================
# Radioisotope Thermoelectric Generators
#   Advent of Code 2016 Day 11 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ s t a t e . p y
# ======================================================================
"Test State for Advent of Code 2016 day 11, Radioisotope Thermoelectric Generators"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import state
import item
import aoc_11

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
The second floor contains a hydrogen generator.
The third floor contains a lithium generator.
The fourth floor contains nothing relevant.
The elevator is on floor 1 of 4.
"""

EXAMPLE_TRACE = """
F4 . ... ... ... ...
F3 . ... ... LiG ...
F2 . HyG ... ... ...
F1 E ... HyM ... LiM
"""

TEXT_AFTER_ONE_MOVE = """
The first floor contains a lithium-compatible microchip.
The second floor contains a hydrogen generator and a hydrogen-compatible microchip.
The third floor contains a lithium generator.
The fourth floor contains nothing relevant.
The elevator is on floor 2 of 4.
"""

TRACE_AFTER_ONE_MOVE = """
F4 . ... ... ... ...
F3 . ... ... LiG ...
F2 E HyG HyM ... ...
F1 . ... ... ... LiM
"""
TRACE_AFTER_TWO_MOVES = """
F4 . ... ... ... ...
F3 E HyG HyM LiG ...
F2 . ... ... ... ...
F1 . ... ... ... LiM
"""

GOAL_TEXT = """
The first floor contains nothing relevant.
The second floor contains nothing relevant.
The third floor contains nothing relevant.
The fourth floor contains a hydrogen-compatible microchip, a hydrogen generator, a lithium generator, and a lithium-compatible microchip.
The elevator is on floor 4 of 4.
"""

# ======================================================================
#                                                              TestState
# ======================================================================


class TestState(unittest.TestCase):  # pylint: disable=R0904
    "Test State object"

    def test_empty_init(self):
        "Test the default State creation"

        # 1. Create default State object
        myobj = state.State()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(str(myobj.lift), "The elevator is on floor 1 of 4.")
        self.assertEqual(myobj.floors, [])
        self.assertEqual(myobj.items, [])

        # 3. Check methods
        self.assertEqual(str(myobj), "The elevator is on floor 1 of 4.")
        self.assertEqual(myobj.directions(), ['U'])
        self.assertEqual(myobj.is_goal(), False)
        self.assertEqual(myobj.is_safe(), True)

    def test_text_init(self):
        "Test the State object creation from text"

        # 1. Create Generators object from text
        myobj = state.State(text=aoc_11.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 5)
        self.assertEqual(str(myobj.lift), "The elevator is on floor 1 of 4.")
        self.assertEqual(len(myobj.floors), 4)
        self.assertEqual(len(myobj.items), 4)

        # 3. Check methods
        self.assertEqual(myobj.is_safe(), True)
        self.assertEqual(str(myobj), EXAMPLE_TEXT.strip())
        self.assertEqual(myobj.trace(), EXAMPLE_TRACE.strip())
        self.assertEqual(myobj.directions(), ['U'])
        self.assertEqual(myobj.is_goal(), False)
        myclone = myobj.clone()
        self.assertEqual(myobj, myclone)
        self.assertEqual(hash(myobj), hash(myclone))
        moves = myobj.legal_moves()
        self.assertEqual(len(moves), 1)
        self.assertEqual(moves[0][0], 'U')
        self.assertEqual(len(moves[0][1]), 1)
        # print(moves[0][1][0])
        self.assertEqual(moves[0][1][0], item.Item(text='hydrogen-compatible microchip'))
        myobj2 = myobj.execute_move(moves[0])
        self.assertEqual(str(myobj2.lift), "The elevator is on floor 2 of 4.")
        self.assertEqual(str(myobj2), TEXT_AFTER_ONE_MOVE.strip())
        self.assertEqual(myobj2.trace(), TRACE_AFTER_ONE_MOVE.strip())
        self.assertEqual(myobj2.is_goal(), False)
        self.assertEqual(myobj2.is_safe(), True)
        move2 = ('U', myobj2.floors[1].element_items("hydrogen"))
        self.assertEqual(move2[0], 'U')
        self.assertEqual(len(move2[1]), 2)
        myobj3 = myobj2.execute_move(move2)
        self.assertEqual(str(myobj3.lift), "The elevator is on floor 3 of 4.")
        self.assertEqual(myobj3.trace(), TRACE_AFTER_TWO_MOVES.strip())
        self.assertEqual(myobj3.is_goal(), False)
        self.assertEqual(myobj3.is_safe(), True)

    def test_goal_init(self):
        "Test the State object creation from goal text"

        # 1. Create Generators object from text
        myobj = state.State(text=aoc_11.from_text(GOAL_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 5)
        self.assertEqual(str(myobj.lift), "The elevator is on floor 4 of 4.")
        self.assertEqual(len(myobj.floors), 4)
        self.assertEqual(len(myobj.items), 4)

        # 3. Check methods
        self.assertEqual(myobj.is_goal(), True)
        self.assertEqual(myobj.is_safe(), True)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ s t a t e . p y                   end
# ======================================================================
