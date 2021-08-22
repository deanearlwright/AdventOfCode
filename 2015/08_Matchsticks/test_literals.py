# ======================================================================
# Matchsticks
#   Advent of Code 2015 Day 08 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ l i t e r a l s . p y
# ======================================================================
"Test solver for Advent of Code 2015 day 08, Matchsticks"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_08
import literals

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
DESCTIPTION = r"""
"" is 2 characters of code (the two double quotes), but the string contains zero characters.
"abc" is 5 characters of code, but 3 characters in the string data.
"aaa\"aaa" is 10 characters of code, but the string itself contains six "a" characters and a single, escaped quote character, for a total of 7 characters in the string data.
"\x27" is 6 characters of code, but the string itself contains just one - an apostrophe ('), escaped using hexadecimal notation.
"""
EXAMPLE_TEXT = r"""
""
"abc"
"aaa\"aaa"
"\x27"
"""

PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = (2 + 5 + 10 + 6) - (0 + 3 + 7 + 1)
PART_TWO_RESULT = (6 + 9 + 16 + 11) - (2 + 5 + 10 + 6)

EXAMPLE_CODE_SIZE = [2, 5, 10, 6]
EXAMPLE_DECODED_SIZE = [0, 3, 7, 1]
EXAMPLE_ENCODED_SIZE = [6, 9, 16, 11]

# ======================================================================
#                                                           TestLiterals
# ======================================================================


class TestLiterals(unittest.TestCase):  # pylint: disable=R0904
    "Test Literals object"

    def test_empty_init(self):
        "Test the default Literals creation"

        # 1. Create default Literals object
        myobj = literals.Literals()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)

    def test_text_init(self):
        "Test the Literals object creation from text"

        # 1. Create Literals object from text
        myobj = literals.Literals(text=aoc_08.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 4)

        # 3. Check methods
        for indx, text in enumerate(myobj.text):
            print(indx, '<%s>' % text)
            self.assertEqual(myobj.code_size(text), EXAMPLE_CODE_SIZE[indx])
        for indx, text in enumerate(myobj.text):
            print(indx, '<%s>' % text, 'decode <%s>' % eval(text))
            self.assertEqual(myobj.decoded_size(text), EXAMPLE_DECODED_SIZE[indx])
        for indx, text in enumerate(myobj.text):
            print(indx, '<%s>' % text, 'encode <%s>' %
                  text.replace('\\', '\\\\').replace('"', '\\"'))
            self.assertEqual(myobj.encoded_size(text), EXAMPLE_ENCODED_SIZE[indx])

    def test_part_one(self):
        "Test part one example of Literals object"

        # 1. Create Literals object from text
        myobj = literals.Literals(text=aoc_08.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Literals object"

        # 1. Create Literals object from text
        myobj = literals.Literals(part2=True, text=aoc_08.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ l i t e r a l s . p y                end
# ======================================================================
