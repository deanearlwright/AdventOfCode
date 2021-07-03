# ======================================================================
# Timing is Everything
#   Advent of Code 2016 Day 15 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
#  Tests from
#   https://rosettacode.org/wiki/Chinese_remainder_theorem#Functional
#   https://www.reddit.com/r/adventofcode/comments/5ifn4v/2016_day_15_solutions/
# ======================================================================

# ======================================================================
#                       t e s t _ c r t . p y
# ======================================================================
"Test Cmt for Advent of Code 2016 day 15, Timing is Everything"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import crt

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                TestCRT
# ======================================================================


class TestCRT(unittest.TestCase):  # pylint: disable=R0904
    "Test CRT object"

    def test_rosetta_code_examples(self):
        "Test examples from rosettacode"

        self.assertEqual(crt.chinese_remainder([3, 5, 7], [2, 3, 2]), 23)
        self.assertEqual(crt.chinese_remainder([5, 13], [2, 3]), 42)
        self.assertEqual(crt.chinese_remainder([100, 23], [19, 0]), 1219)
        self.assertEqual(crt.chinese_remainder([11, 12, 13], [10, 4, 12]), 1000)
        self.assertEqual(crt.chinese_remainder([5, 7, 9, 11], [1, 2, 3, 4]), 1731)
        self.assertEqual(crt.chinese_remainder(
            [17353461355013928499, 3882485124428619605195281, 13563122655762143587],
            [7631415079307304117, 1248561880341424820456626, 2756437267211517231]),
            937307771161836294247413550632295202816)

    def test_part_one_example(self):
        "Test example from part one description [disc sizes], [initial values]"

        self.assertEqual(crt.chinese_remainder([5, 2], [-4, -1 - 1]), 5 + 1)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                       t e s t _ c r t . p y                    end
# ======================================================================
