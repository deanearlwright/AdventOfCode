
# ======================================================================
# Monkey Map
#   Advent of Code 2022 Day 22 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ p a t h . p y
# ======================================================================
"Test Path for Advent of Code 2022 day 22, Monkey Map"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import path

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = "10R5L5R10L4R5L5"

# ======================================================================
#                                                               TestPath
# ======================================================================


class TestPath(unittest.TestCase):  # pylint: disable=R0904
    "Test Path object"

    def test_empty_init(self):
        "Test the default Path creation"

        # 1. Create default Path object
        myobj = path.Path()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.instructions), 0)

    def test_text_init(self):
        "Test the Path object creation from text"

        # 1. Create Path object from text
        myobj = path.Path(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 15)
        self.assertEqual(len(myobj.instructions), 13)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                     t e s t _ p a t h . p y                    end
# ======================================================================
