# ======================================================================
# Camp Cleanup
#   Advent of Code 2022 Day 04 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ e l f . p y
# ======================================================================
"Test Elf for Advent of Code 2022 day 04, Camp Cleanup"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import elf

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = "2-8"

# ======================================================================
#                                                             TestElf
# ======================================================================


class TestElf(unittest.TestCase):  # pylint: disable=R0904
    "Test Elf object"

    def test_empty_init(self):
        "Test the default Elf creation"

        # 1. Create default Elf object
        myobj = elf.Elf()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.low, 0)
        self.assertEqual(myobj.high, 0)

    def test_text_init(self):
        "Test the Elf object creation from text"

        # 1. Create Elf object from text
        myobj = elf.Elf(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 3)
        self.assertEqual(myobj.low, 2)
        self.assertEqual(myobj.high, 8)

        # 3. Check methods
        self.assertEqual(myobj.contains(myobj), True)
        self.assertEqual(myobj.contains(elf.Elf(text="3-12")), False)
        self.assertEqual(myobj.contains(elf.Elf(text="3-6")), True)
        self.assertEqual(myobj.overlaps(elf.Elf(text="3-7")), True)
        self.assertEqual(myobj.overlaps(elf.Elf(text="10-12")), False)
        self.assertEqual(myobj.overlaps(elf.Elf(text="1-6")), True)
        self.assertEqual(myobj.overlaps(elf.Elf(text="1-1")), False)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ e l f . p y                end
# ======================================================================
