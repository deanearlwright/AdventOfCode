# ======================================================================
# Radioisotope Thermoelectric Generators
#   Advent of Code 2016 Day 11 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ f l o o r . p y
# ======================================================================
"Test Floor for Advent of Code 2016 day 11, Radioisotope Thermoelectric Generators"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import floor
import item
import elevator

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = "The first floor contains a hydrogen-compatible microchip" \
    " and a lithium-compatible microchip."

EMPTY_TEXT = "The fourth floor contains nothing relevant."

MANY_TEXT = "The second floor contains a thulium generator," \
    " a thulium-compatible microchip, a plutonium generator," \
    " and a strontium generator."

HYG = item.Item(text="hydrogen generator")
HYM = item.Item(text="hydrogen-compatible microchip")
LIG = item.Item(text="lithium generator")
LIM = item.Item(text="lithium-compatible microchip")
TRACE = [HYG, HYM, LIG, LIM]
THM = item.Item(text="thulium-compatible microchip")


# ======================================================================
#                                                              TestFloor
# ======================================================================


class TestFloor(unittest.TestCase):  # pylint: disable=R0904
    "Test Floor object"

    def test_empty_init(self):
        "Test the default Floor creation"

        # 1. Create default Floor object
        myobj = floor.Floor()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.number, 0)
        self.assertEqual(myobj.ordinal, "UNKNOWN")
        self.assertEqual(len(myobj.items), 0)

        # 3. Check Methods
        self.assertEqual(str(myobj), "The UNKNOWN floor contains nothing relevant.")
        self.assertEqual(myobj.has(HYG), False)
        self.assertEqual(myobj.has(HYM), False)
        self.assertEqual(myobj.elements(), set())
        self.assertEqual(len(myobj.generators()), 0)
        self.assertEqual(len(myobj.microchips()), 0)
        self.assertEqual(myobj.trace(None, TRACE), "F0 . ... ... ... ...")
        self.assertEqual(myobj.is_safe(), True)
        self.assertEqual(myobj.is_empty(), True)

    def test_text_init(self):
        "Test the Floor object creation from text"

        # 1. Create Solver object from text
        myobj = floor.Floor(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 92)
        self.assertEqual(myobj.number, 1)
        self.assertEqual(myobj.ordinal, "first")
        self.assertEqual(len(myobj.items), 2)

        # 3. Check Methods
        self.assertEqual(str(myobj), EXAMPLE_TEXT)
        self.assertEqual(myobj.has(HYG), False)
        self.assertEqual(myobj.has(HYM), True)
        self.assertEqual(myobj.elements(), set(["hydrogen", "lithium"]))
        self.assertEqual(len(myobj.generators()), 0)
        self.assertEqual(len(myobj.microchips()), 2)
        self.assertEqual(myobj.trace(None, TRACE), "F1 . ... HyM ... LiM")
        self.assertEqual(myobj.is_safe(), True)
        self.assertEqual(myobj.is_empty(), False)
        self.assertEqual(myobj.has_pair(HYG), True)
        other = myobj.clone()
        self.assertEqual(myobj, other)
        myobj.remove(HYM)
        self.assertEqual(myobj.has_pair(HYG), False)
        self.assertEqual(myobj.trace(None, TRACE), "F1 . ... ... ... LiM")
        self.assertEqual(myobj.is_safe(), True)
        self.assertEqual(myobj.is_empty(), False)
        self.assertNotEqual(myobj, other)
        myobj.add(LIG)
        self.assertEqual(myobj.trace(None, TRACE), "F1 . ... ... LiG LiM")
        self.assertEqual(myobj.is_safe(), True)
        self.assertEqual(myobj.is_empty(), False)
        self.assertTrue(myobj.is_safe_with([HYG]))
        self.assertFalse(myobj.is_safe_with([HYM]))
        self.assertTrue(myobj.is_safe_with([HYM, HYG]))
        self.assertTrue(myobj.is_safe_without([LIG]))
        self.assertTrue(myobj.is_safe_without([LIM]))
        self.assertTrue(myobj.is_safe_without([LIG, LIM]))

    def test_empty_floor(self):
        "Test the Floor object creation from text with no items"

        # 1. Create Solver object from text
        myobj = floor.Floor(text=EMPTY_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 43)
        self.assertEqual(myobj.number, 4)
        self.assertEqual(myobj.ordinal, "fourth")
        self.assertEqual(len(myobj.items), 0)

        # 3. Check Methods
        self.assertEqual(str(myobj), EMPTY_TEXT)
        self.assertEqual(myobj.has(HYG), False)
        self.assertEqual(myobj.has(HYM), False)
        self.assertEqual(myobj.elements(), set())
        self.assertEqual(len(myobj.generators()), 0)
        self.assertEqual(len(myobj.microchips()), 0)
        self.assertEqual(myobj.safely_removable(), [])
        lift = elevator.Elevator()
        lift.floor = 4
        self.assertEqual(myobj.trace(lift, TRACE), "F4 E ... ... ... ...")
        self.assertEqual(myobj.is_safe(), True)
        self.assertEqual(myobj.is_empty(), True)
        myobj.add(HYG)
        self.assertEqual(myobj.trace(lift, TRACE), "F4 E HyG ... ... ...")
        self.assertEqual(myobj.is_safe(), True)
        self.assertEqual(myobj.is_empty(), False)
        items = myobj.safely_removable()
        self.assertEqual(len(items), 1)
        self.assertEqual(len(items[0]), 1)
        self.assertEqual(items[0][0], HYG)
        myobj.add(LIM)
        self.assertEqual(myobj.is_safe(), False)
        self.assertEqual(myobj.is_empty(), False)
        lift.load([LIG])
        lift.move_down()
        self.assertEqual(myobj.trace(lift, TRACE), "F4 v HyG ... ... LiM")
        self.assertEqual(myobj.is_safe(), False)
        self.assertEqual(len(myobj.safely_removable()), 2)

    def test_many_floor(self):
        "Test the Floor object creation from text with many items"

        # 1. Create Solver object from text
        myobj = floor.Floor(text=MANY_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 128)
        self.assertEqual(myobj.number, 2)
        self.assertEqual(myobj.ordinal, "second")
        self.assertEqual(len(myobj.items), 4)

        # 3. Check Methods
        self.assertEqual(str(myobj), "The second floor contains a plutonium generator,"
                         " a strontium generator, a thulium generator,"
                         " and a thulium-compatible microchip.")
        self.assertEqual(myobj.has(HYG), False)
        self.assertEqual(myobj.has(HYM), False)
        self.assertEqual(myobj.elements(), set(["plutonium", "strontium", "thulium"]))
        self.assertEqual(len(myobj.generators()), 3)
        self.assertEqual(len(myobj.microchips()), 1)
        self.assertEqual(myobj.has_pair(THM), True)
        self.assertEqual(myobj.has_pair(HYG), False)
        self.assertEqual(myobj.is_safe(), True)
        self.assertEqual(len(myobj.element_items("plutonium")), 1)
        self.assertEqual(len(myobj.element_items("thulium")), 2)
        self.assertEqual(len(myobj.element_items("kryptonium")), 0)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ f l o o r . p y                   end
# ======================================================================
