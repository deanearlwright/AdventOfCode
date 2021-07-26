# ======================================================================
# Radioisotope Thermoelectric Generators
#   Advent of Code 2016 Day 11 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ e l e v a t o r . p y
# ======================================================================
"Test Elevator for Advent of Code 2016 day 11, Radioisotope Thermoelectric Generators"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import elevator
import item

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = "The elevator is on floor 2 of 6."
HYG = item.Item(text="hydrogen generator")
HYM = item.Item(text="hydrogen-compatible microchip")
LIG = item.Item(text="lithium generator")
LIM = item.Item(text="lithium-compatible microchip")

# ======================================================================
#                                                           TestElevator
# ======================================================================


class TestElevator(unittest.TestCase):  # pylint: disable=R0904
    "Test Elevator object"

    def test_empty_init(self):
        "Test the default Elevator creation"

        # 1. Create default Elevator object
        myobj = elevator.Elevator()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.floor, 1)
        self.assertEqual(myobj.floors, 4)
        self.assertEqual(len(myobj.items), 0)
        self.assertEqual(myobj.last, 0)
        self.assertEqual(myobj.direction, ' ')

        # 3. Check methods
        self.assertEqual(str(myobj), "The elevator is on floor 1 of 4.")
        self.assertEqual(myobj.directions(), ['U'])

    def test_text_init(self):
        "Test the Elevator object creation from text"

        # 1. Create Solver object from text
        myobj = elevator.Elevator(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 32)
        self.assertEqual(myobj.floor, 2)
        self.assertEqual(myobj.floors, 6)
        self.assertEqual(len(myobj.items), 0)
        self.assertEqual(myobj.last, 0)
        self.assertEqual(myobj.direction, ' ')

        # 3. Check Methods
        self.assertEqual(str(myobj), "The elevator is on floor 2 of 6.")
        self.assertEqual(myobj.directions(), ['U', 'D'])
        self.assertEqual(myobj.next_floor('U'), 3)
        self.assertEqual(myobj.next_floor('D'), 1)
        self.assertFalse(myobj.can_move())
        self.assertFalse(myobj.can_move_up())
        self.assertFalse(myobj.can_move_down())
        self.assertTrue(myobj.is_safe())
        myobj.load([HYG])
        self.assertTrue(myobj.is_safe())
        self.assertEqual(len(myobj.items), 1)
        self.assertTrue(myobj.can_move())
        self.assertTrue(myobj.can_move_up())
        self.assertTrue(myobj.can_move_down())
        myobj.move_down()
        self.assertEqual(myobj.floor, 1)
        self.assertEqual(myobj.floors, 6)
        self.assertEqual(myobj.last, 2)
        self.assertEqual(myobj.direction, 'v')
        self.assertEqual(str(myobj), "The elevator is on floor 1 of 6.")
        self.assertEqual(myobj.directions(), ['U'])
        self.assertTrue(myobj.can_move())
        self.assertTrue(myobj.can_move_up())
        self.assertFalse(myobj.can_move_down())
        myobj.load([LIM])
        self.assertEqual(len(myobj.items), 2)
        self.assertFalse(myobj.is_safe())
        stuff = myobj.unload()
        self.assertEqual(len(myobj.items), 0)
        self.assertEqual(len(stuff), 2)
        self.assertTrue(myobj.is_safe())
        self.assertFalse(myobj.can_move())
        myobj.load([LIM])
        self.assertTrue(myobj.can_move_up())
        myobj.move_up()
        self.assertEqual(myobj.last, 1)
        self.assertEqual(myobj.direction, '^')
        self.assertEqual(str(myobj), EXAMPLE_TEXT)
        myobj.floor = myobj.floors
        self.assertFalse(myobj.can_move_up())
        self.assertTrue(myobj.can_move_down())


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ e l e v a t o r . p y                end
# ======================================================================
