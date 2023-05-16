
# ======================================================================
# Full of Hot Air
#   Advent of Code 2022 Day 25 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ s n a f u . p y
# ======================================================================
"Test Snafu for Advent of Code 2022 day 25, Full of Hot Air"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest
from collections import namedtuple

import snafu

# ----------------------------------------------------------------------
#                                                                  types
# ----------------------------------------------------------------------
Example = namedtuple('Example', 'decimal, snafu')

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = [
    "1=-0-2",
    "12111",
    "2=0=",
    "21",
    "2=01",
    "111",
    "20012",
    "112",
    "1=-1=",
    "1-12",
    "12",
    "1=",
    "122",
]
EXAMPLES = [
    Example(decimal="10", snafu="20"),
    Example(snafu="2=-01", decimal="976"),
    Example(decimal="1", snafu="1"),
    Example(decimal="2", snafu="2"),
    Example(decimal="3", snafu="1="),
    Example(decimal="4", snafu="1-"),
    Example(decimal="5", snafu="10"),
    Example(decimal="6", snafu="11"),
    Example(decimal="7", snafu="12"),
    Example(decimal="8", snafu="2="),
    Example(decimal="9", snafu="2-"),
    Example(decimal="10", snafu="20"),
    Example(decimal="15", snafu="1=0"),
    Example(decimal="20", snafu="1-0"),
    Example(decimal="2022", snafu="1=11-2"),
    Example(decimal="12345", snafu="1-0---0"),
    Example(decimal="314159265", snafu="1121-1110-1=0"),
    Example(snafu="1=-0-2", decimal="1747"),
    Example(snafu="12111", decimal="906"),
    Example(snafu="2=0=", decimal="198"),
    Example(snafu="21", decimal="11"),
    Example(snafu="2=01", decimal="201"),
    Example(snafu="111", decimal="31"),
    Example(snafu="20012", decimal="1257"),
    Example(snafu="112", decimal="32"),
    Example(snafu="1=-1=", decimal="353"),
    Example(snafu="1-12", decimal="107"),
    Example(snafu="12", decimal="7"),
    Example(snafu="1=", decimal="3"),
    Example(snafu="122", decimal="37"),
]


# ======================================================================
#                                                              TestSnafu
# ======================================================================


class TestSnafu(unittest.TestCase):  # pylint: disable=R0904
    "Test Snafu object"

    def test_empty_init(self):
        "Test the default Snafu creation"

        # 1. Create default Snafu object
        myobj = snafu.Snafu()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)

    def test_text_init(self):
        "Test the Snafu object creation from text"

        # 1. Create Snafu object from text
        myobj = snafu.Snafu(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 13)

        # 3. Check methods
        self.assertEqual(myobj.sum_decimal(), "4890")
        self.assertEqual(myobj.sum_snafu(), "2=-1=0")

    def test_examples_to_decimal(self):
        "Test the comversion from snafu to decimal"

        # 1. Loop for all the examples
        for example in EXAMPLES:

            # 2. Convert and test
            decimal_text = example.decimal
            snafu_text = example.snafu
            converted = snafu.Snafu.snafu_to_decimal(snafu_text)
            self.assertEqual(decimal_text, converted)

    def test_examples_to_snafu(self):
        "Test the comversion from decimal to snafu"

        # 1. Loop for all the examples
        for example in EXAMPLES:

            # 2. Convert and test
            decimal_text = example.decimal
            snafu_text = example.snafu
            converted = snafu.Snafu.decimal_to_snafu(decimal_text)
            self.assertEqual(snafu_text, converted)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ s n a f u . p y                   end
# ======================================================================
