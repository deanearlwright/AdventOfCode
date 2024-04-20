
# ======================================================================
# The Floor Will Be Lava
#   Advent of Code 2023 Day 16 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ c o n t r a p t i o n . p y
# ======================================================================
"Test Contraption for Advent of Code 2023 day 16, The Floor Will Be Lava"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import contraption
from tile import SOUTH

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = [
    ".|...\\....",
    "|.-.\\.....",
    ".....|-...",
    "........|.",
    "..........",
    ".........\\",
    "..../.\\\\..",
    ".-.-/..|..",
    ".|....-|.\\",
    "..//.|....",
]

# ======================================================================
#                                                        TestContraption
# ======================================================================


class TestContraption(unittest.TestCase):  # pylint: disable=R0904
    "Test Contraption object"

    def test_empty_init(self):
        "Test the default Contraption creation"

        # 1. Create default Contraption object
        myobj = contraption.Contraption()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.rows, 0)
        self.assertEqual(myobj.cols, 0)
        self.assertEqual(len(myobj.tiles), 0)

    def test_text_init(self):
        "Test the Contraption object creation from text"

        # 1. Create Contraption object from text
        myobj = contraption.Contraption(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 10)
        self.assertEqual(myobj.rows, 10)
        self.assertEqual(myobj.cols, 10)
        self.assertEqual(len(myobj.tiles), 100)

        # 3. Check methods
        self.assertEqual(myobj.bounce(), 46)
        myobj.reset()
        self.assertEqual(myobj.bounce(initial=((0, 3), SOUTH)), 51)

    def test_text_two(self):
        "Test the Contraption object creation from text"

        # 1. Create Contraption object from text
        myobj = contraption.Contraption(text=EXAMPLE_TEXT, part2=True)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, True)
        self.assertEqual(len(myobj.text), 10)
        self.assertEqual(myobj.rows, 10)
        self.assertEqual(myobj.cols, 10)
        self.assertEqual(len(myobj.tiles), 100)

        # 3. Check methods
        self.assertEqual(myobj.bounce(), 46)
        self.assertEqual(myobj.max_bounce(), 51)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end              t e s t _ c o n t r a p t i o n . p y             end
# ======================================================================
