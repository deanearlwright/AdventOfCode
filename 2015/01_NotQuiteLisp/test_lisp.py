# ======================================================================
# Not Quite Lisp
#   Advent of Code 2015 Day 01 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ l i s p . p y
# ======================================================================
"Test solver for Advent of Code 2015 day 01, Not Quite Lisp"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_01
import lisp

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
(()(()(
"""
EXAMPLES = {
    '(())': 0,
    '()()': 0,
    '(((': 3,
    '(()(()(': 3,
    '))(((((': 3,
    '())': -1,
    '))(': -1,
    ')))': -3,
    ')())())': -3,
}

EXAMPLES2 = {
    ')': 1,
    '()())': 5,
}

PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 3
PART_TWO_RESULT = -1

# ======================================================================
#                                                              TestLisp
# ======================================================================


class TestLisp(unittest.TestCase):  # pylint: disable=R0904
    "Test Lisp object"

    def test_empty_init(self):
        "Test the default Lisp creation"

        # 1. Create default Lisp object
        myobj = lisp.Lisp()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)

    def test_text_init(self):
        "Test the Lisp object creation from text"

        # 1. Create Lisp object from text
        myobj = lisp.Lisp(text=aoc_01.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 7)

    def test_part_one(self):
        "Test part one example of Lisp object"

        # 1. Create Lisp object from text
        myobj = lisp.Lisp(text=aoc_01.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Lisp object"

        # 1. Create Lisp object from text
        myobj = lisp.Lisp(part2=True, text=aoc_01.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)

    def test_part_one_examples(self):
        "Test the part one examples"

        # 1. Loop for all the examples
        for example, result in EXAMPLES.items():

            # 2. Create Lisp object from text
            myobj = lisp.Lisp(text=[example])

            # 2. Check the part one result
            self.assertEqual(myobj.part_one(verbose=False), result)

    def test_part_two_examples(self):
        "Test the part two examples"

        # 1. Loop for all the examples
        for example, result in EXAMPLES2.items():

            # 2. Create Lisp object from text
            myobj = lisp.Lisp(part2=True, text=[example])

            # 2. Check the part two result
            self.assertEqual(myobj.part_two(verbose=False), result)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ l i s p . p y                end
# ======================================================================
