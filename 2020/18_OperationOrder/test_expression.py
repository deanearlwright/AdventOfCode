# ======================================================================
# Operation Order
#   Advent of Code 2020 Day 18 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ e x p r e s s i o n . p y
# ======================================================================
"Test Expression object for Advent of Code 2020 day 18, Operation Order"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import expression

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLES = [
   {'text': '1', 'tokens': 1, 'result': 1, 'r2': 1},
   {'text': '1 + 2', 'tokens': 3, 'result': 3, 'r2': 3},
   {'text': '2 * 3', 'tokens': 3, 'result': 6, 'r2': 6},
   {'text': '(2 * 3)', 'tokens': 5, 'result': 6, 'r2': 6},
   {'text': '1 + 2 * 3 + 4 * 5 + 6', 'tokens': 11, 'result': 71, 'r2': 231},
   {'text': '1 + (2 * 3) + (4 * (5 + 6))', 'tokens': 17, 'result': 51, 'r2': 51},
   {'text': '2 * 3 + (4 * 5)', 'tokens': 9, 'result': 26, 'r2': 46},
   {'text': '5 + (8 * 3 + 9 + 3 * 4 * 3)', 'tokens': 15, 'result': 437, 'r2': 1445},
   {'text': '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))', 'tokens': 23, 'result': 12240, 'r2': 669060},
   {'text': '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', 'tokens': 27, 'result': 13632, 'r2': 23340},
]

# ======================================================================
#                                                         TestExpression
# ======================================================================


class TestExpression(unittest.TestCase):  # pylint: disable=R0904
    "Test Expression object"

    def test_empty_init(self):
        "Test the default Expression creation"

        # 1. Create default Expression object
        myobj = expression.Expression()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.tokens), 0)

    def test_text_init(self):
        "Test the Expression object creation from text"

        # 1. Create Expression object from text
        myobj = expression.Expression(text='123')

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 3)
        self.assertEqual(len(myobj.tokens), 1)

        # 3. Check methods
        self.assertEqual(myobj.get_operand(myobj.tokens, '+'), (['123'], []))
        self.assertEqual(myobj.evaluate(), 123)

    def test_part_one(self):
        "Test examples from part one"

        # 1. Loop for all of the examples
        for exp in EXAMPLES:

            # 2. Create the expression object
            myobj = expression.Expression(text=exp['text'])
            self.assertEqual(len(myobj.tokens), exp['tokens'])

            # 3. Check the value
            self.assertEqual(myobj.evaluate(), exp['result'])

    def test_part_two(self):
        "Test examples from part two"

        # 1. Loop for all of the examples
        for exp in EXAMPLES:

            # 2. Create the expression object
            myobj = expression.Expression(text=exp['text'], part2=True)
            self.assertEqual(len(myobj.tokens), exp['tokens'])

            # 3. Check the value
            self.assertEqual(myobj.evaluate(), exp['r2'])
            # print('%d = %s' % (exp['r2'], exp['text']))


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end              t e s t _ e x p r e s s i o n . p y               end
# ======================================================================
