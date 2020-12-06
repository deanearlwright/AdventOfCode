# ======================================================================
# Custom Customs
#   Advent of Code 2020 Day 06 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                        t e s t _ g r o u p . p y
# ======================================================================
"Test set of answers for Advent of Code 2020 day 06, Custom Customs"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import group

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = "abcx abcy abcz"
EXAMPLES = [
    {'text': 'abc', 'num': 3, 'num2': 3},
    {'text': 'a b c', 'num': 3, 'num2': 0},
    {'text': 'ab ac', 'num': 3, 'num2': 1},
    {'text': 'a a a a', 'num': 1, 'num2': 1},
    {'text': 'b', 'num': 1, 'num2': 1},
]

# ======================================================================
#                                                              TestGroup
# ======================================================================


class TestGroup(unittest.TestCase):  # pylint: disable=R0904
    "Test Group object"

    def test_empty_init(self):
        "Test the default Group creation"

        # 1. Create default Group object
        myobj = group.Group()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.answers), 0)

    def test_text_init(self):
        "Test the Group object creation from text"

        # 1. Create Group object from text
        myobj = group.Group(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 14)
        self.assertEqual(len(myobj.answers), 6)

    def test_example(self):
        "Test part one example of Group object"

        # 1. Loop for all the examples
        for example in EXAMPLES:

            # 2. Create Group object from text
            myobj = group.Group(text=example['text'])

            # 2. Check the number of yes aanswers
            self.assertEqual(len(myobj.answers), example['num'])

    def test_example2(self):
        "Test part two example of Group object"

        # 1. Loop for all the examples
        for example in EXAMPLES:

            # 2. Create Group object from text
            myobj = group.Group(text=example['text'], part2=True)

            # 2. Check the number of yes aanswers
            self.assertEqual(len(myobj.answers), example['num2'])


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                     t e s t _ g r o u p . p y                  end
# ======================================================================
