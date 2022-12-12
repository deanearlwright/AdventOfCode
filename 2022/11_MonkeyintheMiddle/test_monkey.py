# ======================================================================
# Monkey in the Middle
#   Advent of Code 2022 Day 11 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ m o n k e y . p y
# ======================================================================
"Test Monkey for Advent of Code 2022 day 11, Monkey in the Middle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import monkey

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = ["Monkey 1:",
                "  Starting items: 54, 65, 75, 74",
                "  Operation: new = old + 6",
                "  Test: divisible by 19",
                "    If true: throw to monkey 2",
                "    If false: throw to monkey 0"]

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
        self.assertEqual(myobj.number, 0)
        self.assertEqual(myobj.items, [])
        self.assertEqual(myobj.operation, [])
        self.assertEqual(myobj.test, 0)
        self.assertEqual(myobj.true, 0)
        self.assertEqual(myobj.false, 0)
        self.assertEqual(myobj.inspections, 0)
        self.assertEqual(myobj.modulo, 3)

    def test_text_init(self):
        "Test the Monkey object creation from text"

        # 1. Create Monkey object from text
        myobj = monkey.Monkey(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 6)
        self.assertEqual(myobj.number, 1)
        self.assertEqual(myobj.items, [54, 65, 75, 74])
        self.assertEqual(myobj.operation, ["+", "6"])
        self.assertEqual(myobj.test, 19)
        self.assertEqual(myobj.true, 2)
        self.assertEqual(myobj.false, 0)
        self.assertEqual(myobj.inspections, 0)
        self.assertEqual(myobj.modulo, 3)

        # 3. Check methods
        self.assertEqual(myobj.new_worry(54), 20)
        self.assertEqual(myobj.new_worry(65), 23)
        self.assertEqual(myobj.new_worry(75), 27)
        self.assertEqual(myobj.new_worry(74), 26)

        self.assertEqual(myobj.round(), [(20, 0), (23, 0), (27, 0), (26, 0)])
        self.assertEqual(myobj.items, [])
        self.assertEqual(myobj.inspections, 4)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ m o n k e y . p y                end
# ======================================================================
