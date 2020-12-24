# ======================================================================
# Rambunctious Recitation
#   Advent of Code 2020 Day 15 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ m e m o r y . p y
# ======================================================================
"Test class for Advent of Code 2020 day 15, Rambunctious Recitation"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import memory

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = "0,3,6"
EXAMPLE_AGES = "0,3,3,1,0,4,0"

# ======================================================================
#                                                             TestMemory
# ======================================================================


class TestMemory(unittest.TestCase):  # pylint: disable=R0904
    "Test Memory object"

    def test_empty_init(self):
        "Test the default Memory creation"

        # 1. Create default Memory object
        myobj = memory.Memory()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.age, None)
        self.assertEqual(myobj.turn, 0)
        self.assertEqual(myobj.numbers, {})

    def test_text_init(self):
        "Test the Memory object creation from text"

        # 1. Create Memory object from text
        myobj = memory.Memory(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 5)
        self.assertEqual(myobj.turn, 3)
        self.assertEqual(len(myobj.numbers), 3)
        self.assertEqual(myobj.age, 0)

        # 3. Speak more numbers
        for age in [int(_) for _ in EXAMPLE_AGES.split(',')]:
            self.assertEqual(myobj.age, age)
            myobj.add(age)

        # 4. Final check
        self.assertEqual(myobj.turn, 10)
        self.assertEqual(len(myobj.numbers), 5)
        self.assertEqual(myobj.age, 2)

    def test_add_last(self):
        "Test the Memory object creation from text"

        # 1. Create Memory object from text
        myobj = memory.Memory(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 5)
        self.assertEqual(myobj.turn, 3)
        self.assertEqual(len(myobj.numbers), 3)
        self.assertEqual(myobj.age, 0)

        # 3. Speak more numbers
        for age in [int(_) for _ in EXAMPLE_AGES.split(',')]:
            self.assertEqual(myobj.age, age)
            myobj.add_last_spoken()

        # 4. Final check
        self.assertEqual(myobj.turn, 10)
        self.assertEqual(len(myobj.numbers), 5)
        self.assertEqual(myobj.age, 2)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ m e m o r y . p y                 end
# ======================================================================
