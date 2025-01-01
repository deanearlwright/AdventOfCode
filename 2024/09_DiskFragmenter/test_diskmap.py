
# ======================================================================
# Disk Fragmenter
#   Advent of Code 2024 Day 09 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ d i s k m a p . p y
# ======================================================================
"Test solver for Advent of Code 2024 day 09, Disk Fragmenter"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_09
import diskmap

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
2333133121414131402
"""

PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 1928
PART_TWO_RESULT = 2858

# ======================================================================
#                                                            TestDiskmap
# ======================================================================


class TestDiskmap(unittest.TestCase):  # pylint: disable=R0904
    "Test Diskmap object"

    def test_empty_init(self):
        "Test the default Diskmap creation"

        # 1. Create default Diskmap object
        myobj = diskmap.Diskmap()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.free), 0)
        self.assertEqual(len(myobj.files), 0)

    def test_text_init(self):
        "Test the Diskmap object creation from text"

        # 1. Create Diskmap object from text
        myobj = diskmap.Diskmap(text=aoc_09.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 1)
        self.assertEqual(len(myobj.free), 8)
        self.assertEqual(len(myobj.files), 10)

        self.assertEqual(myobj.free[0], diskmap.File(-1, 2, 3))
        self.assertEqual(myobj.free[1], diskmap.File(-1, 8, 3))
        self.assertEqual(myobj.free[-1], diskmap.File(-1, 35, 1))

        self.assertEqual(myobj.files[0], diskmap.File(0, 0, 2))
        self.assertEqual(myobj.files[1], diskmap.File(1, 5, 3))
        self.assertEqual(myobj.files[-1], diskmap.File(9, 40, 2))

        # 3. Check methods
        myobj.compact()
        self.assertEqual(len(myobj.files), 14)
        self.assertEqual(myobj.checksum(), 1928)

    def test_text_two(self):
        "Test the Diskmap object creation from text"

        # 1. Create Diskmap object from text
        myobj = diskmap.Diskmap(text=aoc_09.from_text(EXAMPLE_TEXT), part2=True)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, True)
        self.assertEqual(len(myobj.text), 1)
        self.assertEqual(len(myobj.free), 8)
        self.assertEqual(len(myobj.files), 10)

        self.assertEqual(myobj.free[0], diskmap.File(-1, 2, 3))
        self.assertEqual(myobj.free[1], diskmap.File(-1, 8, 3))
        self.assertEqual(myobj.free[-1], diskmap.File(-1, 35, 1))

        self.assertEqual(myobj.files[0], diskmap.File(0, 0, 2))
        self.assertEqual(myobj.files[1], diskmap.File(1, 5, 3))
        self.assertEqual(myobj.files[-1], diskmap.File(9, 40, 2))

        # 3. Check methods
        myobj.compact_two()
        self.assertEqual(len(myobj.files), 10)
        self.assertEqual(myobj.checksum(), 2858)

    def test_part_one(self):
        "Test part one example of Diskmap object"

        # 1. Create Diskmap object from text
        text = aoc_09.from_text(PART_ONE_TEXT)
        myobj = diskmap.Diskmap(text=text)

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Diskmap object"

        # 1. Create Diskmap object from text
        text = aoc_09.from_text(PART_TWO_TEXT)
        myobj = diskmap.Diskmap(part2=True, text=text)

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ d i s k m a p . p y                end
# ======================================================================
