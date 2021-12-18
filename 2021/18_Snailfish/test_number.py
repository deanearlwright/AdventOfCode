# ======================================================================
# Snailfish
#   Advent of Code 2021 Day 18 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ n u m b e r . p y
# ======================================================================
"Test Number for Advent of Code 2021 day 18, Snailfish"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import number

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = "[[[[4,3],4],4],[7,[[8,4],9]]]"

# ======================================================================
#                                                             TestNumber
# ======================================================================


class TestNumber(unittest.TestCase):  # pylint: disable=R0904
    "Test Number object"

    def test_empty_init(self):
        "Test the default Number creation"

        # 1. Create default Number object
        myobj = number.Number()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.pair, [])

        # 3. Check methods
        self.assertEqual(myobj.find_comma("1,2"), 1)
        self.assertEqual(myobj.find_comma("[1,2],3"), 5)
        self.assertEqual(myobj.find_comma("9,[8,7]"), 1)
        self.assertEqual(myobj.find_comma("[1,9],[8,5]"), 5)

        self.assertEqual(myobj.split_text("[1,2]"), ['1', '2'])
        self.assertEqual(myobj.split_text("[[1,2],3]"), ['[1,2]', '3'])
        self.assertEqual(myobj.split_text("[9,[8,7]]"), ['9', '[8,7]'])
        self.assertEqual(myobj.split_text("[[1,9],[8,5]]"), ['[1,9]', '[8,5]'])

        self.assertEqual(myobj.text_to_num("[1,2]"), [1, 2])
        self.assertEqual(myobj.text_to_num("[[1,2],3]"), [[1, 2], 3])
        self.assertEqual(myobj.text_to_num("[9,[8,7]]"), [9, [8, 7]])
        self.assertEqual(myobj.text_to_num("[[1,9],[8,5]]"), [[1, 9], [8, 5]])

        self.assertEqual(myobj.explode_left("[[[[", "1"), "[[[[")
        self.assertEqual(myobj.explode_left("[7,[6,[5,[4,", "3"), "[7,[6,[5,[7,")

        self.assertEqual(myobj.explode_right("8", ",1],2],3],4]"), ",9],2],3],4]")
        self.assertEqual(myobj.explode_right("2", "]]]]"), "]]]]")

        myobj.pair = [[[[[9, 8], 1], 2], 3], 4]
        self.assertEqual(myobj.explode(), True)
        self.assertEqual(myobj.pair, [[[[0, 9], 2], 3], 4])
        myobj.pair = [7, [6, [5, [4, [3, 2]]]]]
        self.assertEqual(myobj.explode(), True)
        self.assertEqual(myobj.pair, [7, [6, [5, [7, 0]]]])
        myobj.pair = [[6, [5, [4, [3, 2]]]], 1]
        self.assertEqual(myobj.explode(), True)
        self.assertEqual(myobj.pair, [[6, [5, [7, 0]]], 3])
        myobj.pair = [[3, [2, [1, [7, 3]]]], [6, [5, [4, [3, 2]]]]]
        self.assertEqual(myobj.explode(), True)
        self.assertEqual(myobj.pair, [[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]])
        self.assertEqual(myobj.explode(), True)
        self.assertEqual(myobj.pair, [[3, [2, [8, 0]]], [9, [5, [7, 0]]]])

        myobj.pair = [[[[0, 7], 4], [15, [0, 13]]], [1, 1]]
        self.assertEqual(myobj.split(), True)
        self.assertEqual(myobj.pair, [[[[0, 7], 4], [[7, 8], [0, 13]]], [1, 1]])
        self.assertEqual(myobj.split(), True)
        self.assertEqual(myobj.pair, [[[[0, 7], 4], [[7, 8], [0, [6, 7]]]], [1, 1]])

        myobj.pair = [[[[[4, 3], 4], 4], [7, [[8, 4], 9]]], [1, 1]]
        self.assertEqual(myobj.reduce(), [[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]])

        myobj.pair = [[[[4, 3], 4], 4], [7, [[8, 4], 9]]]
        self.assertEqual(myobj.add([1, 1]),
                         [[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]])

        self.assertEqual(myobj.recursive_magnitude([9, 1]), 29)
        self.assertEqual(myobj.recursive_magnitude([1, 9]), 21)
        self.assertEqual(myobj.recursive_magnitude([[9, 1], [1, 9]]), 129)
        self.assertEqual(myobj.recursive_magnitude([[1, 2], [[3, 4], 5]]), 143)
        self.assertEqual(
            myobj.recursive_magnitude([[[[8, 7], [7, 7]], [[8, 6], [7, 7]]],
                                       [[[0, 7], [6, 6]], [8, 7]]]),
            3488)

    def test_text_init(self):
        "Test the Number object creation from text"

        # 1. Create Number object from text
        myobj = number.Number(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 29)
        self.assertEqual(myobj.pair, [[[[4, 3], 4], 4], [7, [[8, 4], 9]]])
        self.assertEqual(str(myobj), EXAMPLE_TEXT)

        # 3. Check methods
        self.assertEqual(myobj.add([1, 1]), [[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]])

    def test_sumation(self):
        "Test the Number object sumatation"

        # 1. Create Number object from text
        myobj = number.Number(text="[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]")

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.pair, [[[0, [4, 5]], [0, 0]], [[[4, 5], [2, 6]], [9, 5]]])

        # 3. Check methods
        self.assertEqual(
            myobj.add([7, [[[3, 7], [4, 3]], [[6, 3], [8, 8]]]]),
            [[[[4, 0], [5, 4]], [[7, 7], [6, 0]]], [[8, [7, 7]], [[7, 9], [5, 0]]]])
        self.assertEqual(
            myobj.add([[2, [[0, 8], [3, 4]]], [[[6, 7], 1], [7, [1, 6]]]]),
            [[[[6, 7], [6, 7]], [[7, 7], [0, 7]]], [[[8, 7], [7, 7]], [[8, 8], [8, 0]]]])
        self.assertEqual(
            myobj.add([[[[2, 4], 7], [6, [0, 5]]], [[[6, 8], [2, 8]], [[2, 1], [4, 5]]]]),
            [[[[7, 0], [7, 7]], [[7, 7], [7, 8]]], [[[7, 7], [8, 8]], [[7, 7], [8, 7]]]])
        self.assertEqual(
            myobj.add([7, [5, [[3, 8], [1, 4]]]]),
            [[[[7, 7], [7, 8]], [[9, 5], [8, 7]]], [[[6, 8], [0, 8]], [[9, 9], [9, 0]]]])
        self.assertEqual(
            myobj.add([[2, [2, 2]], [8, [8, 1]]]),
            [[[[6, 6], [6, 6]], [[6, 0], [6, 7]]], [[[7, 7], [8, 9]], [8, [8, 1]]]])
        self.assertEqual(
            myobj.add([2, 9]),
            [[[[6, 6], [7, 7]], [[0, 7], [7, 7]]], [[[5, 5], [5, 6]], 9]])
        self.assertEqual(
            myobj.add([1, [[[9, 3], 9], [[9, 0], [0, 7]]]]),
            [[[[7, 8], [6, 7]], [[6, 8], [0, 8]]], [[[7, 7], [5, 0]], [[5, 5], [5, 6]]]])
        self.assertEqual(
            myobj.add([[[5, [7, 4]], 7], 1]),
            [[[[7, 7], [7, 7]], [[8, 7], [8, 7]]], [[[7, 0], [7, 7]], 9]])
        self.assertEqual(
            myobj.add([[[[4, 2], 2], 6], [8, 7]]),
            [[[[8, 7], [7, 7]], [[8, 6], [7, 7]]], [[[0, 7], [6, 6]], [8, 7]]])


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ n u m b e r . p y                  end
# ======================================================================
