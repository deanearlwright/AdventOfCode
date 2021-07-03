# ======================================================================
# One-Time Pad
#   Advent of Code 2016 Day 14 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                       t e s t _ p a d . p y
# ======================================================================
"Test solver for Advent of Code 2016 day 14, One-Time Pad"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_14
import pad

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
abc
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 22728
PART_TWO_RESULT = 22551

# ======================================================================
#                                                                TestPad
# ======================================================================


class TestPad(unittest.TestCase):  # pylint: disable=R0904
    "Test Pad object"

    def test_hashes(self):
        "Test the two has methods"
        self.assertEqual(pad.part_one_hash("abc0"), "577571be4de9dcce85a041ba0410f29f")
        self.assertEqual(pad.part_two_hash("abc0"), "a107ff634856bb300138cac6568c0f24")

    def test_empty_init(self):
        "Test the default Pad creation"

        # 1. Create default Pad object
        myobj = pad.Pad()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.salt, "")
        self.assertEqual(myobj.hashes, {})
        self.assertEqual(myobj.keys, [])

    def test_text_init(self):
        "Test the Pad object creation from text"

        # 1. Create Pad object from text
        myobj = pad.Pad(text=aoc_14.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 1)
        self.assertEqual(myobj.salt, "abc")
        self.assertEqual(myobj.hashes, {})
        self.assertEqual(myobj.keys, [])

        # 3. Check methods
        self.assertEqual(myobj.is_key(15), False)
        self.assertEqual(myobj.is_key(16), False)
        self.assertEqual(myobj.is_key(17), False)
        self.assertEqual(myobj.is_key(18), False)
        self.assertEqual(myobj.is_key(38), False)
        self.assertEqual(myobj.is_key(39), True)
        self.assertEqual(myobj.is_key(40), False)
        self.assertEqual(myobj.is_key(92), True)
        self.assertEqual(myobj.is_key(22728), True)

        self.assertEqual(myobj.get_keys(64), 22728)

    def test_part_one(self):
        "Test part one example of Pad object"

        # 1. Create Pad object from text
        myobj = pad.Pad(text=aoc_14.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Pad object"

        # 1. Create Pad object from text
        myobj = pad.Pad(part2=True, text=aoc_14.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                     t e s t _ p a d . p y                      end
# ======================================================================
