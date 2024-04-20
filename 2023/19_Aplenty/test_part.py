
# ======================================================================
# Aplenty
#   Advent of Code 2023 Day 19 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                        t e s t _ p a r t . p y
# ======================================================================
"Test Rule for Advent of Code 2023 day 19, Aplenty"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import part

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = "{x=787,m=2655,a=1222,s=2876}"

# ======================================================================
#                                                               TestPart
# ======================================================================


class TestPart(unittest.TestCase):  # pylint: disable=R0904
    "Test Part object"

    def test_empty_init(self):
        "Test the default Rule creation"

        # 1. Create default Rule object
        myobj = part.Part()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.categories, {})

    def test_text_init(self):
        "Test the Part object creation from text"

        # 1. Create Rule object from text
        myobj = part.Part(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 28)
        self.assertEqual(len(myobj.categories), 4)
        self.assertEqual(myobj.categories["x"], 787)
        self.assertEqual(myobj.categories["m"], 2655)
        self.assertEqual(myobj.categories["a"], 1222)
        self.assertEqual(myobj.categories["s"], 2876)

        # 3. Check methods
        self.assertEqual(myobj.value("x"), 787)
        self.assertEqual(myobj.value("m"), 2655)
        self.assertEqual(myobj.value("a"), 1222)
        self.assertEqual(myobj.value("s"), 2876)

        self.assertEqual(myobj.total(), 7540)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                     t e s t _ p a r t . p y                    end
# ======================================================================
