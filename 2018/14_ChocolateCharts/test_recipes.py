# ======================================================================
# Chocolate Charts
#   Advent of Code 2018 Day 14 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ r e c i p e s . p y
# ======================================================================
"Test solver for Advent of Code 2018 day 14, Chocolate Charts"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_14
import recipes

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = "\n9\n"
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = "\n51589\n"

PART_ONE_RESULT = '5158916779'
PART_TWO_RESULT = 9


#   (3)[7]
#   (3)[7] 1  0
#    3  7  1 [0](1) 0
#    3  7  1  0 [1] 0 (1)
#   (3) 7  1  0  1  0 [1] 2
#    3  7  1  0 (1) 0  1  2 [4]
#    3  7  1 [0] 1  0 (1) 2  4  5
#    3  7  1  0 [1] 0  1  2 (4) 5  1
#    3 (7) 1  0  1  0 [1] 2  4  5  1  5
#    3  7  1  0  1  0  1  2 [4](5) 1  5  8
#    3 (7) 1  0  1  0  1  2  4  5  1  5  8 [9]
#    3  7  1  0  1  0  1 [2] 4 (5) 1  5  8  9  1  6
#    3  7  1  0  1  0  1  2  4  5 [1] 5  8  9  1 (6) 7
#    3  7  1  0 (1) 0  1  2  4  5  1  5 [8] 9  1  6  7  7
#    3  7 [1] 0  1  0 (1) 2  4  5  1  5  8  9  1  6  7  7  9
#    3  7  1  0 [1] 0  1  2 (4) 5__1__5__8__9__1__6__7__7__9  2
EXAMPLE_LAST = [7, 0, 0, 1, 2, 4, 5, 1, 5, 8, 9, 6, 7, 7, 9, 2]
EXAMPLE_ELF1 = [0, 0, 4, 6, 0, 4, 6, 8, 1, 9, 1, 9, 15, 4, 6, 8]
EXAMPLE_ELF2 = [1, 1, 3, 4, 6, 8, 3, 4, 6, 8, 13, 7, 10, 12, 2, 4]

# - If the Elves think their skill will improve after making 9 recipes,
#   the scores of the ten recipes after the first nine on the scoreboard
#   would be 5158916779 (highlighted in the last line of the diagram).
# - After 5 recipes, the scores of the next ten would be 0124515891.
# - After 18 recipes, the scores of the next ten would be 9251071085.
# - After 2018 recipes, the scores of the next ten would be 5941429882.
EXAMPLE_AFTER = [9, 5, 18, 2018]
EXAMPLE_NXT10 = ['5158916779', '0124515891', '9251071085', '5941429882']
EXAMPLE_PART2 = ['51589', '01245', '92510', '59414']

EXAMPLE_PART2_PARTS = ['2', '21', '121', '0121', '30121', '330121']
EXAMPLE_PART2_AFTER = [7, 79, 78, 922, 22018, 20216138]

# ======================================================================
#                                                            TestRecipes
# ======================================================================


class TestRecipes(unittest.TestCase):  # pylint: disable=R0904
    "Test Recipes object"

    def test_empty_init(self):
        "Test the default Recipes creation"

        # 1. Create default Recipes object
        myobj = recipes.Recipes()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.scores, [3, 7])
        self.assertEqual(myobj.elves, [0, 1])
        self.assertEqual(myobj.after, None)


    def test_text_init(self):
        "Test the Recipes object creation from text"

        # 1. Create Recipes object from text
        myobj = recipes.Recipes(text=aoc_14.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 1)
        self.assertEqual(myobj.scores, [3, 7])
        self.assertEqual(myobj.elves, [0, 1])
        self.assertEqual(myobj.after, 9)

    def test_steps(self):
        "Test the Recipes object steps"

        # 1. Check lengths of EXAMPLE DATA
        self.assertEqual(len(EXAMPLE_LAST), len(EXAMPLE_ELF1))
        self.assertEqual(len(EXAMPLE_LAST), len(EXAMPLE_ELF2))

        # 2. Create Recipes object from text
        myobj = recipes.Recipes(text=aoc_14.from_text(EXAMPLE_TEXT))

        # 3. Loop for several steps
        for step in range(len(EXAMPLE_LAST)):
            self.assertEqual(myobj.scores[-1], EXAMPLE_LAST[step])
            self.assertEqual(myobj.elves[0], EXAMPLE_ELF1[step])
            self.assertEqual(myobj.elves[1], EXAMPLE_ELF2[step])
            myobj.step()

    def test_next_ten(self):
        "Test the Recipes object next_ten"

        # 1. Check lengths of EXAMPLE DATA
        self.assertEqual(len(EXAMPLE_AFTER), len(EXAMPLE_NXT10))

        # 2. Loop for the examples
        for index in range(len(EXAMPLE_AFTER)):

            # 3. Create Recipes object from text
            myobj = recipes.Recipes(text=aoc_14.from_text(EXAMPLE_TEXT))

            # 4. Checkout next 10 scores
            self.assertEqual(myobj.next_ten(EXAMPLE_AFTER[index]), EXAMPLE_NXT10[index])

    def test_first_appears(self):
        "Test the Recipes object first_appears"

        # 1. Check lengths of EXAMPLE DATA
        self.assertEqual(len(EXAMPLE_AFTER), len(EXAMPLE_PART2))

        # 2. Loop for the examples
        for index in range(len(EXAMPLE_AFTER)):

            # 3. Create Recipes object from text
            myobj = recipes.Recipes([EXAMPLE_PART2[index]])

            # 4. Checkout next 10 scores
            self.assertEqual(myobj.first_appears(EXAMPLE_PART2[index]), EXAMPLE_AFTER[index])

    def test_first_appears_by_parts(self):
        "Test the Recipes object first_appears"

        # 1. Check lengths of EXAMPLE DATA
        self.assertEqual(len(EXAMPLE_PART2_PARTS), len(EXAMPLE_PART2_AFTER))

        # 2. Loop for the examples
        for index in range(len(EXAMPLE_PART2_PARTS)):

            # 3. Create Recipes object from text
            myobj = recipes.Recipes([EXAMPLE_PART2_PARTS[index]])

            # 4. Checkout next 10 scores
            self.assertEqual(myobj.first_appears(EXAMPLE_PART2_PARTS[index]), EXAMPLE_PART2_AFTER[index])


    def test_part_one(self):
        "Test part one example of Recipes object"

        # 1. Create Recipes object from text
        myobj = recipes.Recipes(text=aoc_14.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)


    def test_part_two(self):
        "Test part two example of Recipes object"

        # 1. Create Recipes object from text
        myobj = recipes.Recipes(part2=True, text=aoc_14.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)



# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ r e c i p e s . p y                end
# ======================================================================
