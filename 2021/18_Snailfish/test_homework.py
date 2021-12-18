# ======================================================================
# Snailfish
#   Advent of Code 2021 Day 18 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ h o m e w o r k . p y
# ======================================================================
"Test solver for Advent of Code 2021 day 18, Snailfish"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_18
import homework

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_ONE = """
[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
[7,[5,[[3,8],[1,4]]]]
[[2,[2,2]],[8,[8,1]]]
[2,9]
[1,[[[9,3],9],[[9,0],[0,7]]]]
[[[5,[7,4]],7],1]
[[[[4,2],2],6],[8,7]]
"""
EXAMPLE_TWO = """
[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
"""
PART_ONE_TEXT = EXAMPLE_TWO
PART_TWO_TEXT = EXAMPLE_TWO

PART_ONE_RESULT = 4140
PART_TWO_RESULT = 3993

# ======================================================================
#                                                           TestHomework
# ======================================================================


class TestHomework(unittest.TestCase):  # pylint: disable=R0904
    "Test Homework object"

    def test_empty_init(self):
        "Test the default Homework creation"

        # 1. Create default Homework object
        myobj = homework.Homework()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.pairs, [])
        self.assertEqual(myobj.sumation, [])

    def test_text_init_one(self):
        "Test the Homework object creation from text"

        # 1. Create Homework object from text
        myobj = homework.Homework(text=aoc_18.from_text(EXAMPLE_ONE))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 10)
        self.assertEqual(len(myobj.pairs), 10)
        self.assertEqual(myobj.sumation, [])

        # 3. Check addition
        myobj.sum_them_up()
        self.assertEqual(str(myobj.sumation),
                         "[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]")
        self.assertEqual(myobj.sumation.magnitude(), 3488)

    def test_text_init_two(self):
        "Test the Homework object creation from text"

        # 1. Create Homework object from text
        myobj = homework.Homework(text=aoc_18.from_text(EXAMPLE_TWO))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 10)
        self.assertEqual(len(myobj.pairs), 10)
        self.assertEqual(myobj.sumation, [])

        # 3. Check addition
        myobj.sum_them_up()
        self.assertEqual(str(myobj.sumation),
                         "[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]")
        self.assertEqual(myobj.sumation.magnitude(), 4140)
        self.assertEqual(myobj.largest_magnitude(), 3993)

    def test_part_one(self):
        "Test part one example of Homework object"

        # 1. Create Homework object from text
        myobj = homework.Homework(text=aoc_18.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Homework object"

        # 1. Create Homework object from text
        myobj = homework.Homework(part2=True, text=aoc_18.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ h o m e w o r k . p y                end
# ======================================================================
