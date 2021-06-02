# ======================================================================
# Internet Protocol Version 7
#   Advent of Code 2016 Day 07 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ i p 7 a d d r . p y
# ======================================================================
"Test Ip7addr for Advent of Code 2016 day 07, Internet Protocol Version 7"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import ip7addr

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = "abba[mnop]qrst"
EXAMPLE_MULTIPLE = "abba[mnop]qrst[xyyx]aaquuqzzzz"
EXAMPLE_TWO = "aba[bab]xyxz"

# ======================================================================
#                                                            TestIp7addr
# ======================================================================


class TestIp7addr(unittest.TestCase):  # pylint: disable=R0904
    "Test Ip7addr object"

    def test_empty_init(self):
        "Test the default Ip7addr creation"

        # 1. Create default Ip7addr object
        myobj = ip7addr.Ip7addr()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.nob_abba), 0)
        self.assertEqual(len(myobj.inb_abba), 0)
        self.assertEqual(len(myobj.nob_aba), 0)
        self.assertEqual(len(myobj.inb_aba), 0)

    def test_text_init(self):
        "Test the Ip7addr object creation from text"

        # 1. Create Ip7list object from text
        myobj = ip7addr.Ip7addr(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 14)
        self.assertEqual(len(myobj.nob_abba), 1)
        self.assertEqual(len(myobj.inb_abba), 0)
        self.assertEqual(len(myobj.nob_aba), 0)
        self.assertEqual(len(myobj.inb_aba), 0)

        # 3. Check methods
        self.assertEqual(myobj.is_tls(), True)

    def test_text_multiple(self):
        "Test the Ip7addr object creation from text that has multiple brackets"

        # 1. Create Ip7list object from text
        myobj = ip7addr.Ip7addr(text=EXAMPLE_MULTIPLE)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 30)
        self.assertEqual(len(myobj.nob_abba), 2)
        self.assertEqual(len(myobj.inb_abba), 1)
        self.assertEqual(len(myobj.nob_aba), 0)
        self.assertEqual(len(myobj.inb_aba), 0)

        # 3. Check methods
        self.assertEqual(myobj.is_tls(), False)
        self.assertEqual(myobj.is_ssl(), False)

    def test_text_two(self):
        "Test the Ip7addr object creation from text for part2"

        # 1. Create Ip7list object from text
        myobj = ip7addr.Ip7addr(text=EXAMPLE_TWO)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 12)
        self.assertEqual(len(myobj.nob_abba), 0)
        self.assertEqual(len(myobj.inb_abba), 0)
        self.assertEqual(len(myobj.nob_aba), 2)
        self.assertEqual(len(myobj.inb_aba), 1)

        # 3. Check methods
        self.assertEqual(myobj.is_ssl(), True)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                  t e s t _ i p 7 a d d r . p y                 end
# ======================================================================
