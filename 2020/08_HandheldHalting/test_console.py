# ======================================================================
# Handheld Halting
#   Advent of Code 2020 Day 08 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ c o n s o l e . p y
# ======================================================================
"Test solver for Advent of Code 2020 day 08, Handheld Halting"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_08
import console

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = ""
PART_ONE_TEXT = ""
PART_TWO_TEXT = ""

PART_ONE_RESULT = None
PART_TWO_RESULT = None

# ======================================================================
#                                                            TestConsole
# ======================================================================


class TestConsole(unittest.TestCase):  # pylint: disable=R0904
    "Test Console object"

    def test_empty_init(self):
        "Test the default Console creation"

        # 1. Create default Console object
        myobj = console.Console()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)

    def test_text_init(self):
        "Test the Console object creation from text"

        # 1. Create Console object from text
        myobj = console.Console(text=aoc_08.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 0)

    def test_part_one(self):
        "Test part one example of Console object"

        # 1. Create Console object from text
        myobj = console.Console(text=aoc_08.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Console object"

        # 1. Create Console object from text
        myobj = console.Console(part2=True, text=aoc_08.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                  t e s t _ c o n s o l e . p y                 end
# ======================================================================
