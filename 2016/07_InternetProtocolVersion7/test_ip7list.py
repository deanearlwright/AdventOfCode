# ======================================================================
# Internet Protocol Version 7
#   Advent of Code 2016 Day 07 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ i p 7 l i s t . p y
# ======================================================================
"Test solver for Advent of Code 2016 day 07, Internet Protocol Version 7"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_07
import ip7list

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
abba[mnop]qrst
abcd[bddb]xyyx
aaaa[qwer]tyui
ioxxoj[asdfgh]zxcvbn
"""

EXAMPLE_TWO = """
aba[bab]xyz
xyx[xyx]xyx
aaa[kek]eke
zazbz[bzb]cdb
"""

PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TWO

PART_ONE_RESULT = 2
PART_TWO_RESULT = 3

# ======================================================================
#                                                              TestIp7list
# ======================================================================


class TestIp7list(unittest.TestCase):  # pylint: disable=R0904
    "Test Ip7list object"

    def test_empty_init(self):
        "Test the default Ip7list creation"

        # 1. Create default Ip7list object
        myobj = ip7list.Ip7list()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.addrs), 0)

    def test_text_init(self):
        "Test the Ip7list object creation from text"

        # 1. Create Ip7list object from text
        myobj = ip7list.Ip7list(text=aoc_07.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 4)
        self.assertEqual(len(myobj.addrs), 4)

    def test_part_one(self):
        "Test part one example of Ip7list object"

        # 1. Create Ip7list object from text
        myobj = ip7list.Ip7list(text=aoc_07.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Ip7list object"

        # 1. Create Ip7list object from text
        myobj = ip7list.Ip7list(part2=True, text=aoc_07.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ i p 7 l i s t . p y                end
# ======================================================================
