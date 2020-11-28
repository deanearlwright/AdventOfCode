
# ======================================================================
# I Was Told There Would Be No Math
#   Advent of Code 2015 Day 02 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ p r e s e n t . p y
# ======================================================================
"Test present for Advent of Code 2015 day 02, I Was Told There Would Be No Math"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import present

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLES = [
    {'text': '2x3x4',
     'area': 52, 'slack': 6, 'paper': 58,
     'wrap': 10, 'bow': 24, 'ribbon': 34},
    {'text': '1x1x10',
     'area': 42, 'slack': 1, 'paper': 43,
     'wrap': 4, 'bow': 10, 'ribbon': 14},
]

# ======================================================================
#                                                            TestPresent
# ======================================================================


class TestPresent(unittest.TestCase):  # pylint: disable=R0904
    "Test Present object"

    def test_empty_init(self):
        "Test the default Present creation"

        # 1. Create default Present object
        myobj = present.Present()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.length, 0)
        self.assertEqual(myobj.width, 0)
        self.assertEqual(myobj.height, 0)
        self.assertEqual(myobj.text, None)

        # 3. Test methods
        self.assertEqual(myobj.area(), 0)
        self.assertEqual(myobj.slack(), 0)
        self.assertEqual(myobj.paper(), 0)

    def test_examples(self):
        "Test the Present object creation from example text"

        # 1. Loop for all of the examples
        for example in EXAMPLES:

            # 2. Create Present object from text
            myobj = present.Present(text=example['text'])

            # 3. Check the methods
            self.assertEqual(myobj.area(), example['area'])
            self.assertEqual(myobj.slack(), example['slack'])
            self.assertEqual(myobj.paper(), example['paper'])

    def test_examples_two(self):
        "Test the Present object creation from example text"

        # 1. Loop for all of the examples
        for example in EXAMPLES:

            # 2. Create Present object from text
            myobj = present.Present(text=example['text'])

            # 3. Check the methods
            self.assertEqual(myobj.wrap(), example['wrap'])
            self.assertEqual(myobj.bow(), example['bow'])
            self.assertEqual(myobj.ribbon(), example['ribbon'])


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                  t e s t _ p r e s e n t . p y                 end
# ======================================================================
