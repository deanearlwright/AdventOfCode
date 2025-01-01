
# ======================================================================
# Bridge Repair
#   Advent of Code 2024 Day 07 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ e q u a t i o n . p y
# ======================================================================
"Test Equation for Advent of Code 2024 day 07, Bridge Repair"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import equation

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = "190: 10 19"

# ======================================================================
#                                                           TestEquation
# ======================================================================


class TestEquation(unittest.TestCase):  # pylint: disable=R0904
    "Test Equation object"

    def test_empty_init(self):
        "Test the default Equation creation"

        # 1. Create default Equation object
        myobj = equation.Equation()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.left, 0)
        self.assertEqual(len(myobj.right), 0)

    def test_text_init(self):
        "Test the Equation object creation from text"

        # 1. Create Equation object from text
        myobj = equation.Equation(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 10)
        self.assertEqual(myobj.left, 190)
        self.assertEqual(len(myobj.right), 2)
        self.assertEqual(myobj.right, [10, 19])

        # 3. Check methods
        self.assertTrue(myobj.recursive_can_be_true(10, [10]))
        self.assertTrue(myobj.recursive_can_be_true(190, [10, 19]))
        self.assertTrue(myobj.can_be_true())
        self.assertFalse(myobj.recursive_can_be_true(3268, [81, 40, 27]))
        self.assertTrue(myobj.recursive_can_be_true(3267, [81, 40, 27]))
        self.assertFalse(myobj.recursive_can_be_true(83, [7, 5]))

        self.assertTrue(myobj.recursive_can_be_true_two(10, [10]))
        self.assertTrue(myobj.recursive_can_be_true_two(190, [10, 19]))
        self.assertTrue(myobj.recursive_can_be_true_two(156, [15, 6]))
        self.assertTrue(myobj.recursive_can_be_true_two(7290, [6, 8, 6, 15]))
        self.assertTrue(myobj.recursive_can_be_true_two(192, [17, 8, 14]))
        self.assertFalse(myobj.recursive_can_be_true_two(3268, [81, 40, 27]))


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ e q u a t i o n . p y                end
# ======================================================================
