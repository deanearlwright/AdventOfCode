
# ======================================================================
# Gear Ratios
#   Advent of Code 2023 Day 03 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ s c h e m a t i c . p y
# ======================================================================
"Test Schematic for Advent of Code 2023 day 03, Gear Ratios"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import schematic

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598.."
]

# ======================================================================
#                                                          TestSchematic
# ======================================================================


class TestSchematic(unittest.TestCase):  # pylint: disable=R0904
    "Test Schematic object"

    def test_empty_init(self):
        "Test the default Schematic creation"

        # 1. Create default Schematic object
        myobj = schematic.Schematic()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.symbols), 0)
        self.assertEqual(len(myobj.parts), 0)

    def test_text_init(self):
        "Test the Schematic object creation from text"

        # 1. Create Schematic object from text
        myobj = schematic.Schematic(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 10)
        self.assertEqual(len(myobj.symbols), 6)
        self.assertEqual(len(myobj.parts), 10)

        # 3. Check methods
        self.assertEqual(myobj.total_parts(), 4361)
        self.assertEqual(myobj.total_gears(), 467835)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                t e s t _ s c h e m a t i c . p y               end
# ======================================================================
