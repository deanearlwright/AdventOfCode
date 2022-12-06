# ======================================================================
# Supply Stacks
#   Advent of Code 2022 Day 05 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ s t a c k . p y
# ======================================================================
"Test Stack for Advent of Code 2022 day 05, Supply Stacks"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import stack

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = ["    [D]    ", "[N] [C]    ", "[Z] [M] [P]"]

# ======================================================================
#                                                              TestStack
# ======================================================================


class TestStack(unittest.TestCase):  # pylint: disable=R0904
    "Test Stack object"

    def test_empty_init(self):
        "Test the default Stack creation"

        # 1. Create default Stack object
        myobj = stack.Stack()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.crates), 0)

    def test_text_init(self):
        "Test the Stack object creation from text"

        # 1. Create Stack object from text
        myobj = stack.Stack(text=EXAMPLE_TEXT, number=1)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 3)
        self.assertEqual(len(myobj.crates), 2)
        self.assertEqual(myobj.crates[0], "Z")
        self.assertEqual(myobj.crates[1], "N")

        # 3. Check methods
        self.assertEqual(myobj.labels(), "ZN")
        self.assertEqual(myobj.top(), "N")
        self.assertEqual(myobj.remove(), ["N"])
        self.assertEqual(len(myobj.crates), 1)
        self.assertEqual(myobj.top(), "Z")
        myobj.add("a")
        myobj.add("b")
        myobj.add("c")
        self.assertEqual(len(myobj.crates), 4)
        self.assertEqual(myobj.remove(2), ["c", "b"])
        self.assertEqual(len(myobj.crates), 2)
        self.assertEqual(myobj.top(), "a")
        self.assertEqual(myobj.labels(), "Za")
        self.assertEqual(myobj.remove(2), ["a", "Z"])
        self.assertEqual(myobj.top(), " ")
        self.assertEqual(myobj.labels(), "")


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ s t a c k . p y                   end
# ======================================================================
