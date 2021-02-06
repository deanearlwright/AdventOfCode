# ======================================================================
# Allergen Assessment
#   Advent of Code 2020 Day 21 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                       t e s t _ l a b e l . p y
# ======================================================================
"Test Label for Advent of Code 2020 day 21, Allergen Assessment"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import label

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = "mxmxvkd kfcds sqjhc nhms (contains dairy, fish)"

# ======================================================================
#                                                              TestLabel
# ======================================================================


class TestLabel(unittest.TestCase):  # pylint: disable=R0904
    "Test Label object"

    def test_empty_init(self):
        "Test the default Label creation"

        # 1. Create default Label object
        myobj = label.Label()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.ingredients), 0)
        self.assertEqual(len(myobj.allergens), 0)

    def test_text_init(self):
        "Test the Label object creation from text"

        # 1. Create Label object from text
        myobj = label.Label(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 47)
        self.assertEqual(len(myobj.ingredients), 4)
        self.assertEqual(len(myobj.allergens), 2)

        # 3. Check methods
        self.assertEqual(myobj.has_ingredient('mxmxvkd'), True)
        self.assertEqual(myobj.has_ingredient('kfcds'), True)
        self.assertEqual(myobj.has_ingredient('dairy'), False)
        self.assertEqual(myobj.has_allergen('dairy'), True)
        self.assertEqual(myobj.has_allergen('fish'), True)
        self.assertEqual(myobj.has_allergen('soy'), False)
        self.assertEqual(myobj.has_allergen('kfcds'), False)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                     t e s t _ l a b e l . p y                  end
# ======================================================================
