# ======================================================================
# Aunt Sue
#   Advent of Code 2015 Day 16 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ m f c s a m . p y
# ======================================================================
"Test Mfcsam for Advent of Code 2015 day 16, Aunt Sue"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_16
import mfcsam

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1
"""

# ======================================================================
#                                                             TestMfcsam
# ======================================================================


class TestMfcsam(unittest.TestCase):  # pylint: disable=R0904
    "Test Mfcsam object"

    def test_empty_init(self):
        "Test the default Mfcsam creation"

        # 1. Create default Mfcsam object
        myobj = mfcsam.Mfcsam()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.compounds, {})

    def test_text_init(self):
        "Test the Mfcsam object creation from text"

        # 1. Create Mfcsam object from text
        myobj = mfcsam.Mfcsam(text=aoc_16.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 10)
        self.assertEqual(len(myobj.compounds), 10)

        # 3. Check methods
        self.assertEqual(myobj.is_match('katz', 7), False)
        self.assertEqual(myobj.is_match('cats', 0), False)
        self.assertEqual(myobj.is_match('cats', 7), True)
        self.assertEqual(myobj.is_match('cats', 8), False)

        self.assertEqual(myobj.is_complete_match({'cats': 8}), False)
        self.assertEqual(myobj.is_complete_match({'cats': 7}), True)
        self.assertEqual(myobj.is_complete_match({'cats': 7, 'trees': 3}), True)
        self.assertEqual(myobj.is_complete_match({'cats': 7, 'trees': 3, 'perfumes': 2}), False)
        self.assertEqual(myobj.is_complete_match({'cats': 7, 'trees': 3, 'perfumes': 1}), True)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ m f c s a m . p y                end
# ======================================================================
