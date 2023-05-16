
# ======================================================================
# Monkey Math
#   Advent of Code 2022 Day 21 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ m o n k e y . p y
# ======================================================================
"Test Monkey for Advent of Code 2022 day 21, Monkey Math"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import monkey

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = "ptdq: humn - dvpt"

# ======================================================================
#                                                             TestMonkey
# ======================================================================


class TestMonkey(unittest.TestCase):  # pylint: disable=R0904
    "Test Monkey object"

    def test_empty_init(self):
        "Test the default Monkey creation"

        # 1. Create default Monkey object
        myobj = monkey.Monkey()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.name, None)
        self.assertEqual(myobj.yells, None)
        self.assertEqual(myobj.op1, None)
        self.assertEqual(myobj.operation, None)
        self.assertEqual(myobj.op2, None)
        self.assertEqual(len(myobj.needs), 0)

    def test_text_init(self):
        "Test the Monkey object creation from text"

        # 1. Create Monkey object from text
        myobj = monkey.Monkey(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 17)
        self.assertEqual(myobj.name, "ptdq")
        self.assertEqual(myobj.yells, None)
        self.assertEqual(myobj.op1, "humn")
        self.assertEqual(myobj.operation, "-")
        self.assertEqual(myobj.op2, "dvpt")
        self.assertEqual(len(myobj.needs), 2)

        # 3. Check operations
        self.assertEqual(myobj.do_the_math(31, 2), 29)
        myobj.hears("dvpt")
        self.assertEqual(len(myobj.needs), 1)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ m o n k e y . p y                end
# ======================================================================
