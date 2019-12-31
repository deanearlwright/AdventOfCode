# ======================================================================
# Corruption Checksum
#   Advent of Code 2017 Day 02 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                 t e s t _ s p r e a d s h e e t . p y
# ======================================================================
"Test spreadsheet checksum for AoC 2017 day 2, Corruption Checksum"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import spreadsheet
import aoc_02

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

P1_EXAMPLE_TEXT = """
! Example 1 from part 1

5 1 9 5
7 5 3
2 4 6 8

! Solution = 8 + 4 + 6 = 18
"""


# ======================================================================
#                                                        TestSpreadsheet
# ======================================================================


class TestSpreadsheet(unittest.TestCase):  # pylint: disable=R0904
    """Test Spreadsheet object"""

    def test_empty_init(self):
        """Test default Spreadsheet creation"""

        # 1. Create default Captcha object
        myss = spreadsheet.Spreadsheet()

        # 2. Make sure it has the default values
        self.assertEqual(myss.text, None)
        self.assertEqual(myss.part2, False)

        # 3. Check methods
        self.assertEqual(myss.checksum(), None)

    def test_value_init(self):
        "Test Spreadsheet object creation with values"

        # 1. Create Captcha object with values
        myss = spreadsheet.Spreadsheet(text=["5 1 9 6", "7 5 3", "2 4 6 8"])

        # 2. Make sure it has the specified values
        self.assertEqual(len(myss.text), 3)
        self.assertEqual(myss.part2, False)

        # 3. Check methods
        self.assertEqual(myss.checksum(verbose=False), 18)

    def test_text_init(self):
        """Test Spreadsheet object creation from text"""

        # 1. Create Spreadsheet object from text
        myss = spreadsheet.Spreadsheet(text=aoc_02.from_text(P1_EXAMPLE_TEXT))

        # 2. Make sure it has the specified values
        self.assertEqual(len(myss.text), 3)
        self.assertEqual(myss.part2, False)

        # 3. Check methods
        self.assertEqual(myss.checksum(), 18)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end             t e s t _ s p r e a d s h e e t . p y              end
# ======================================================================
