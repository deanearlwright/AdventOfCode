# ======================================================================
# Science for Hungry People
#   Advent of Code 2015 Day 15 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ i n g r e d i e n t . p y
# ======================================================================
"Test Ingredient for Advent of Code 2015 day 15, Science for Hungry People"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import ingredient

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = "Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8"

# ======================================================================
#                                                         TestIngredient
# ======================================================================


class TestIngredient(unittest.TestCase):  # pylint: disable=R0904
    "Test Ingredient object"

    def test_empty_init(self):
        "Test the default Ingredient creation"

        # 1. Create default Ingredient object
        myobj = ingredient.Ingredient()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.name, "")
        self.assertEqual(myobj.qualities, [0, 0, 0, 0])
        self.assertEqual(myobj.cals, 0)

    def test_text_init(self):
        "Test the Ingredient object creation from text"

        # 1. Create Ingredient object from text
        myobj = ingredient.Ingredient(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 73)
        self.assertEqual(myobj.name, "Butterscotch")
        self.assertEqual(myobj.qualities, [-1, -2, 6, 3])
        self.assertEqual(myobj.cals, 8)

        # 3. Test Methods
        self.assertEqual(myobj.properties(3), [-3, -6, 18, 9])
        self.assertEqual(myobj.calories(2), 16)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end               t e s t _ i n g r e d i e n t . p y              end
# ======================================================================
