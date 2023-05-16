
# ======================================================================
# Unstable Diffusion
#   Advent of Code 2022 Day 23 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ g r o v e . p y
# ======================================================================
"Test Grove for Advent of Code 2022 day 23, Unstable Diffusion"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import grove

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = [
    ".....",
    "..##.",
    "..#..",
    ".....",
    "..##.",
    "....."
]
NORTH = [grove.Loc(col=-1, row=-1),
         grove.Loc(col=0, row=-1),
         grove.Loc(col=1, row=-1)]
# ======================================================================
#                                                              TestGrove
# ======================================================================


class TestGrove(unittest.TestCase):  # pylint: disable=R0904
    "Test Grove object"

    def test_empty_init(self):
        "Test the default Grove creation"

        # 1. Create default Grove object
        myobj = grove.Grove()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.elves), 0)

    def test_text_init(self):
        "Test the Grove object creation from text"

        # 1. Create Grove object from text
        myobj = grove.Grove(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 6)
        self.assertEqual(len(myobj.elves), 5)

        # 3. Check methods
        self.assertEqual(myobj.is_elf_at(grove.Loc(0, 0)), False)
        self.assertEqual(myobj.is_elf_at(grove.Loc(2, 1)), True)
        self.assertEqual(myobj.is_clear(grove.Loc(0, 0), NORTH), True)
        self.assertEqual(myobj.is_clear(grove.Loc(2, 1), NORTH), True)
        self.assertEqual(myobj.is_clear(grove.Loc(3, 2), NORTH), False)
        self.assertEqual(myobj.rectangle(), ((2, 1), (3, 4)))
        self.assertEqual(str(myobj), "##\n#.\n..\n##")


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ g r o v e . p y                   end
# ======================================================================
