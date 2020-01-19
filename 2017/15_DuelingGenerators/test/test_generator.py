# ======================================================================
# Dueling Generators
#   Advent of Code 2017 Day 15 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                     t e s t _ g e n e r a t o r . p y
# ======================================================================
"Test solver for Advent of Code 2017 day 15, Dueling Generators"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import generator
import aoc_15

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
START_A = 65
START_B = 8921

EXAMPLE_INPUT = """
Generator A starts with 65
Generator B starts with 8921
"""

EXAMPLE_VALUES = """
--Gen. A--  --Gen. B--
   1092455   430625591
1181022009  1233683848
 245556042  1431495498
1744312007   137874439
1352636452   285222916
"""

EXAMPLE_JUDGE_6 = 1

EXAMPLE_JUDGE_40M = 588

PART_TWO_VALUES = """
--Gen. A--  --Gen. B--
1352636452  1233683848
1992081072   862516352
 530830436  1159784568
1980017072  1616057672
 740335192   412269392
"""

PART_TWO_JUDGE_6 = 0

PART_TWO_JUDGE_5M = 309

# ======================================================================
#                                                          TestGenerator
# ======================================================================


class TestGenerator(unittest.TestCase):  # pylint: disable=R0904
    """Test Hash Knot for Disk Defragmenter object"""

    def test_empty_init(self):
        """Test the default generator creation"""

        # 1. Create default disk deframenter object
        mygen = generator.Generator()

        # 2. Make sure it has the default values
        self.assertEqual(mygen.factor, generator.FACTOR_A)
        self.assertEqual(mygen.modulo, generator.MODULO)
        self.assertEqual(mygen.start, None)
        self.assertEqual(mygen.value, None)
        self.assertEqual(mygen.count, 0)
        self.assertEqual(mygen.name, None)
        self.assertEqual(mygen.part2, False)

    def test_values_init(self):
        """Test the generator creation with values"""

        # 1. Create default disk deframenter object
        mygen = generator.Generator(factor=12345, modulo=67890, start=START_A, name='George')

        # 2. Make sure it has the default values
        self.assertEqual(mygen.factor, 12345)
        self.assertEqual(mygen.modulo, 67890)
        self.assertEqual(mygen.start, START_A)
        self.assertEqual(mygen.value, START_A)
        self.assertEqual(mygen.count, 0)
        self.assertEqual(mygen.name, 'George')
        self.assertEqual(mygen.part2, False)

    def test_text_init(self):
        """Test the generator creation with text"""

        # 1. Create default disk deframenter object
        mygen = generator.Generator(text='Generator B starts with 8921')

        # 2. Make sure it has the default values
        self.assertEqual(mygen.factor, generator.FACTOR_B)
        self.assertEqual(mygen.modulo, generator.MODULO)
        self.assertEqual(mygen.start, 8921)
        self.assertEqual(mygen.value, 8921)
        self.assertEqual(mygen.count, 0)
        self.assertEqual(mygen.name, 'B')
        self.assertEqual(mygen.part2, False)

        # 3. Check next value generation
        self.assertEqual(mygen.next_value(), 430625591)
        self.assertEqual(mygen.next_value(), 1233683848)
        self.assertEqual(mygen.next_value(), 1431495498)
        self.assertEqual(mygen.next_value(), 137874439)
        self.assertEqual(mygen.next_value(), 285222916)

# ======================================================================
#                                                         TestGenerators
# ======================================================================


class TestGenerators(unittest.TestCase):  # pylint: disable=R0904
    """Test Generators object"""

    def test_empty_init(self):
        """Test the generators creation"""

        # 1. Create default generators object
        mygens = generator.Generators()

        # 2. Make sure it has the default values
        self.assertEqual(mygens.part2, False)
        self.assertEqual(mygens.text, None)
        self.assertEqual(mygens.judge, 16)
        self.assertEqual(mygens.modulo, 2**16)
        self.assertEqual(mygens.count, 0)
        self.assertEqual(mygens.generators, {})

    def test_text_init(self):
        """Test the generators object creation from text"""

        # 1. Create generators object from text
        mygens = generator.Generators(text=aoc_15.from_text(EXAMPLE_INPUT))

        # 2. Make sure it has the default values
        self.assertEqual(mygens.part2, False)
        self.assertEqual(len(mygens.text), 2)
        self.assertEqual(mygens.judge, 16)
        self.assertEqual(mygens.modulo, 2**16)
        self.assertEqual(mygens.count, 0)
        self.assertEqual(len(mygens.generators), 2)

        # 3. Check generator A
        self.assertEqual(mygens['A'].factor, generator.FACTOR_A)
        self.assertEqual(mygens['A'].modulo, generator.MODULO)
        self.assertEqual(mygens['A'].start, START_A)
        self.assertEqual(mygens['A'].value, START_A)
        self.assertEqual(mygens['A'].count, 0)
        self.assertEqual(mygens['A'].name, 'A')
        self.assertEqual(mygens['A'].part2, False)

        # 4. Check generator B
        self.assertEqual(mygens['B'].factor, generator.FACTOR_B)
        self.assertEqual(mygens['B'].modulo, generator.MODULO)
        self.assertEqual(mygens['B'].start, START_B)
        self.assertEqual(mygens['B'].value, START_B)
        self.assertEqual(mygens['B'].count, 0)
        self.assertEqual(mygens['B'].name, 'B')
        self.assertEqual(mygens['B'].part2, False)

    def test_part_one_values(self):
        """Test generators output from example"""

        # 1. Create the generator object
        mygens = generator.Generators(text=aoc_15.from_text(EXAMPLE_INPUT))

        # 2. Loop for all of the example output rows
        for row in aoc_15.from_text(EXAMPLE_VALUES):
            if row[0] == '-':
                continue

            # 3. Get the expected values
            expected = [int(_) for _ in row.split()]

            # 4. Advance the generators
            mygens.next_values()

            # 5. Check the values
            self.assertEqual(expected[0], mygens['A'].value)
            self.assertEqual(expected[1], mygens['B'].value)

    def test_part_one_judge_six(self):
        """Test generators matches from example"""

        # 1. Create the generator object
        mygens = generator.Generators(text=aoc_15.from_text(EXAMPLE_INPUT))

        # 2. Check the number of matches after six iterations
        self.assertEqual(mygens.part_one(verbose=False, limit=6),
                         EXAMPLE_JUDGE_6)

    def test_part_one_judge_40m(self):
        """Test generators matches from example"""

        # 1. Create the generator object
        mygens = generator.Generators(text=aoc_15.from_text(EXAMPLE_INPUT))

        # 2. Check the number of matches after six iterations
        self.assertEqual(mygens.part_one(verbose=False), EXAMPLE_JUDGE_40M)

class TestPartTwo(unittest.TestCase):  # pylint: disable=R0904
    """Test Generators object for part two"""

    def test_text_init(self):
        """Test the generators object creation from text"""

        # 1. Create generators object from text
        mygens = generator.Generators(text=aoc_15.from_text(EXAMPLE_INPUT),
                                      part2=True)

        # 2. Make sure it has the default values
        self.assertEqual(mygens.part2, True)
        self.assertEqual(len(mygens.text), 2)
        self.assertEqual(mygens.judge, 16)
        self.assertEqual(mygens.modulo, 2**16)
        self.assertEqual(mygens.count, 0)
        self.assertEqual(len(mygens.generators), 2)

        # 3. Check generator A
        self.assertEqual(mygens['A'].factor, generator.FACTOR_A)
        self.assertEqual(mygens['A'].modulo, generator.MODULO)
        self.assertEqual(mygens['A'].start, START_A)
        self.assertEqual(mygens['A'].value, START_A)
        self.assertEqual(mygens['A'].count, 0)
        self.assertEqual(mygens['A'].name, 'A')
        self.assertEqual(mygens['A'].part2, True)
        self.assertEqual(mygens['A'].multiple, generator.MULTIPLE_A)

        # 4. Check generator B
        self.assertEqual(mygens['B'].factor, generator.FACTOR_B)
        self.assertEqual(mygens['B'].modulo, generator.MODULO)
        self.assertEqual(mygens['B'].start, START_B)
        self.assertEqual(mygens['B'].value, START_B)
        self.assertEqual(mygens['B'].count, 0)
        self.assertEqual(mygens['B'].name, 'B')
        self.assertEqual(mygens['B'].part2, True)
        self.assertEqual(mygens['B'].multiple, generator.MULTIPLE_B)

    def test_part_two_values(self):
        """Test generators output from example"""

        # 1. Create the generator object
        mygens = generator.Generators(text=aoc_15.from_text(EXAMPLE_INPUT),
                                      part2=True)

        # 2. Loop for all of the example output rows
        for row in aoc_15.from_text(PART_TWO_VALUES):
            if row[0] == '-':
                continue

            # 3. Get the expected values
            expected = [int(_) for _ in row.split()]

            # 4. Advance the generators
            mygens.next_values()

            # 5. Check the values
            self.assertEqual(expected[0], mygens['A'].value)
            self.assertEqual(expected[1], mygens['B'].value)

    def test_part_two_judge_six(self):
        """Test generators matches from example"""

        # 1. Create the generator object
        mygens = generator.Generators(text=aoc_15.from_text(EXAMPLE_INPUT),
                                      part2=True)

        # 2. Check the number of matches after six iterations
        self.assertEqual(mygens.part_two(verbose=False, limit=6),
                         PART_TWO_JUDGE_6)

    def test_part_two_judge_5m(self):
        """Test generators matches from example"""

        # 1. Create the generator object
        mygens = generator.Generators(text=aoc_15.from_text(EXAMPLE_INPUT),
                                      part2=True)

        # 2. Check the number of matches after six iterations
        self.assertEqual(mygens.part_two(verbose=False), PART_TWO_JUDGE_5M)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                t e s t _ g e n e r a t o r . p y               end
# ======================================================================
