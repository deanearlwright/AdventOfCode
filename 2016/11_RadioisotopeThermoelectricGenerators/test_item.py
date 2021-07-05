# ======================================================================
# Radioisotope Thermoelectric Generators
#   Advent of Code 2016 Day 11 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ i t e m . p y
# ======================================================================
"Test Item for Advent of Code 2016 day 11, Radioisotope Thermoelectric Generators"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import item

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = "hydrogen generator"

# ======================================================================
#                                                               TestItem
# ======================================================================


class TestItem(unittest.TestCase):  # pylint: disable=R0904
    "Test Item object"

    def test_empty_init(self):
        "Test the default Item creation"

        # 1. Create default Item object
        myobj = item.Item()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.itype, "?")
        self.assertEqual(myobj.ielement, "??")

        # 3. Check methods
        self.assertEqual(str(myobj), "?? ?")
        self.assertEqual(myobj.initials(), "???")
        self.assertEqual(myobj.is_generator(), False)
        self.assertEqual(myobj.is_microchip(), False)
        self.assertEqual(myobj.is_element("hydrogen"), False)
        hyg = item.Item(text=EXAMPLE_TEXT)
        self.assertTrue(myobj != hyg)

    def test_text_init(self):
        "Test the Item object creation from text"

        # 1. Create Solver object from text
        myobj = item.Item(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 18)
        self.assertEqual(myobj.itype, "generator")
        self.assertEqual(myobj.ielement, "hydrogen")

        # 3. Check methods
        self.assertEqual(str(myobj), "a hydrogen generator")
        self.assertEqual(myobj.initials(), "HyG")
        self.assertEqual(myobj.is_generator(), True)
        self.assertEqual(myobj.is_microchip(), False)
        self.assertEqual(myobj.is_element("hydrogen"), True)
        self.assertEqual(myobj.is_element("lithium"), False)
        hyg = item.Item(text=EXAMPLE_TEXT)
        self.assertTrue(myobj == hyg)
        hym = item.Item(text="hydrogen-compatible microchip")
        self.assertTrue(myobj != hym)
        clone = hyg.clone()
        self.assertTrue(hyg == clone)
        self.assertTrue(hym != clone)
        clone.itype = "microchip"
        self.assertTrue(hym == clone)
        self.assertTrue(hyg != clone)
        other = hyg.other()
        self.assertTrue(hym == other)
        self.assertTrue(hyg != other)
        self.assertTrue(hyg.are_safe(other))
        lim = item.Item(text="lithium-compatible microchip")
        self.assertFalse(hyg.are_safe(lim))
        self.assertTrue(hym.are_safe(lim))


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                     t e s t _ i t e m . p y                    end
# ======================================================================
