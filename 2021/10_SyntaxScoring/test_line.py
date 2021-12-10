# ======================================================================
# Syntax Scoring
#   Advent of Code 2021 Day 10 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ l i n e . p y
# ======================================================================
"Test Line for Advent of Code 2021 day 10, Syntax Scoring"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import line

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLES = [
    {'text': "[]", 'corrupted': False, 'incomplete': False, 'score': 0},
    {'text': "{()()()}", 'corrupted': False, 'incomplete': False, 'score': 0},
    {'text': "[<>({}){}[([])<>]]", 'corrupted': False, 'incomplete': False, 'score': 0},
    {'text': "(]", 'corrupted': True, 'incomplete': False, 'score': 57},
    {'text': "{()()()>", 'corrupted': True, 'incomplete': False, 'score': 25137},
    {'text': "[({(<(())[]>[[{[]{<()<>>", 'corrupted': False, 'incomplete': True, 'score': 288957},
    {'text': "[(()[<>])]({[<{<<[]>>(", 'corrupted': False, 'incomplete': True, 'score': 5566},
    {'text': "(((({<>}<{<{<>}{[]{[]{}", 'corrupted': False, 'incomplete': True, 'score': 1480781},
    {'text': "{<[[]]>}<{[{[{[]{()[[[]", 'corrupted': False, 'incomplete': True, 'score': 995444},
    {'text': "<{([{{}}[<[[[<>{}]]]>[]]", 'corrupted': False, 'incomplete': True, 'score': 294},
]

# ======================================================================
#                                                               TestLine
# ======================================================================


class TestLine(unittest.TestCase):  # pylint: disable=R0904
    "Test Line object"

    def test_empty_init(self):
        "Test the default Line creation"

        # 1. Create default Line object
        myobj = line.Line()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.corrupted, False)
        self.assertEqual(myobj.incomplete, False)
        self.assertEqual(myobj.illegal, None)
        self.assertEqual(myobj.score, 0)

    def test_text_init(self):
        "Test the Line object creation from text"

        # 1. Loop for all of the examples
        for example in EXAMPLES:

            # 2. Create the line
            myobj = line.Line(text=example['text'])

            # 2. Make sure it has the expected values
            self.assertEqual(myobj.part2, False)
            self.assertEqual(myobj.text, example['text'])
            self.assertEqual(myobj.corrupted, example['corrupted'])
            self.assertEqual(myobj.incomplete, example['incomplete'])
            self.assertEqual(myobj.score, example['score'])
            if example['corrupted']:
                self.assertTrue(myobj.illegal in line.ENDERS)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                     t e s t _ l i n e . p y                    end
# ======================================================================
