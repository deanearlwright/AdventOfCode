
# ======================================================================
# If You Give A Seed A Fertilizer
#   Advent of Code 2023 Day 05 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ r a n g e m a p . p y
# ======================================================================
"Test Rangemap for AoC 2023 day 05, If You Give A Seed A Fertilizer"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import rangemap

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = "50 98 2"

# ======================================================================
#                                                           TestRangemap
# ======================================================================


class TestRangemap(unittest.TestCase):  # pylint: disable=R0904
    "Test Rangemap object"

    def test_empty_init(self):
        "Test the default Rangemap creation"

        # 1. Create default Rangemap object
        myobj = rangemap.Rangemap()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.dest_start, 0)
        self.assertEqual(myobj.source_start, 0)
        self.assertEqual(myobj.range_length, 0)

    def test_text_init(self):
        "Test the Rangemap object creation from text"

        # 1. Create Rangemap object from text
        myobj = rangemap.Rangemap(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 7)
        self.assertEqual(myobj.dest_start, 50)
        self.assertEqual(myobj.source_start, 98)
        self.assertEqual(myobj.range_length, 2)

        # 3. Check methods
        self.assertFalse(myobj.in_source(97))
        self.assertTrue(myobj.in_source(98))
        self.assertTrue(myobj.in_source(99))
        self.assertFalse(myobj.in_source(100))

        self.assertFalse(myobj.in_dest(49))
        self.assertTrue(myobj.in_dest(50))
        self.assertTrue(myobj.in_dest(51))
        self.assertFalse(myobj.in_dest(52))

        self.assertEqual(myobj.mapped(97), 97)
        self.assertEqual(myobj.mapped(98), 50)
        self.assertEqual(myobj.mapped(99), 51)
        self.assertEqual(myobj.mapped(100), 100)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ r a n g e m a p . p y                end
# ======================================================================
