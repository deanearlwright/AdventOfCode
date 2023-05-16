
# ======================================================================
# Monkey Math
#   Advent of Code 2022 Day 21 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ m o n k e y s . p y
# ======================================================================
"Test Monkeys for Advent of Code 2022 day 21, Monkey Math"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import monkeys

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = [
    "root: pppw + sjmn",
    "dbpl: 5",
    "cczh: sllz + lgvd",
    "zczc: 2",
    "ptdq: humn - dvpt",
    "dvpt: 3",
    "lfqf: 4",
    "humn: 5",
    "ljgn: 2",
    "sjmn: drzm * dbpl",
    "sllz: 4",
    "pppw: cczh / lfqf",
    "lgvd: ljgn * ptdq",
    "drzm: hmdt - zczc",
    "hmdt: 32",
]

# ======================================================================
#                                                            TestMonkeys
# ======================================================================


class TestMonkeys(unittest.TestCase):  # pylint: disable=R0904
    "Test Monkeys object"

    def test_empty_init(self):
        "Test the default Monkeys creation"

        # 1. Create default Monkeys object
        myobj = monkeys.Monkeys()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.yellers), 0)
        self.assertEqual(len(myobj.needs), 0)
        self.assertEqual(myobj.root, None)
        self.assertEqual(myobj.you, None)

    def test_text_init(self):
        "Test the Monkeys object creation from text"

        # 1. Create Monkeys object from text
        myobj = monkeys.Monkeys(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 15)
        self.assertEqual(len(myobj.yellers), 8)
        self.assertEqual(len(myobj.needs), 14)
        self.assertNotEqual(myobj.root, None)
        self.assertNotEqual(myobj.you, None)

        # 3. Check methods
        self.assertEqual(myobj.satisfy_all(), 152)

    def test_text_two(self):
        "Test the Monkeys object creation from text"

        # 1. Create Monkeys object from text
        myobj = monkeys.Monkeys(text=EXAMPLE_TEXT, part2=True)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, True)
        self.assertEqual(len(myobj.text), 15)
        self.assertEqual(len(myobj.yellers), 8)
        self.assertEqual(len(myobj.needs), 14)
        self.assertNotEqual(myobj.root, None)
        self.assertNotEqual(myobj.you, None)

        # 3. Check methods
        self.assertEqual(myobj.satisfy_all(),
                         "(((4 + (2 * (X - 3))) / 4) == 150)")

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                  t e s t _ m o n k e y s . p y                 end
# ======================================================================
