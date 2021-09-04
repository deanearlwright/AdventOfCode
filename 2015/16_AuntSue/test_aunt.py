# ======================================================================
# Aunt Sue
#   Advent of Code 2015 Day 16 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ a u n t . p y
# ======================================================================
"Test Aunt for Advent of Code 2015 day 16, Aunt Sue"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

import unittest

import aunt

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = "Sue 13: akitas: 10, pomeranians: 0, vizslas: 2"

# ======================================================================
#                                                               TestAunt
# ======================================================================


class TestAunt(unittest.TestCase):  # pylint: disable=R0904
    "Test Aunt object"

    def test_empty_init(self):
        "Test the default Aunt creation"

        # 1. Create default Aunt object
        myobj = aunt.Aunt()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.number, 0)
        self.assertEqual(myobj.attributes, {})

    def test_text_init(self):
        "Test the Aunt object creation from text"

        # 1. Create Aunt object from text
        myobj = aunt.Aunt(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 46)
        self.assertEqual(myobj.number, 13)
        self.assertEqual(len(myobj.attributes), 3)
        self.assertEqual(myobj.attributes["akitas"], 10)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                     t e s t _ a u n t . p y                    end
# ======================================================================
