# ======================================================================
# Permutation Promenade
#   Advent of Code 2017 Day 16 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ p r o m e n a d e . p y
# ======================================================================
"Test solver for Advent of Code 2017 day 16, Permutation Promenade"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import promenade

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

EXAMPLE_INPUT = "s1,x3/4,pe/b"
EXAMPLE_NUMBER = 5
EXAMPLE_RESULT = "baedc"
EXAMPLE_DANCERS = ["abcde", "eabcd", "eabdc", EXAMPLE_RESULT]

TWICE_INPUT = "s1,x3/4,pe/b,s1,x3/4,pe/b"
TWICE_RESULT = "ceadb"

PART_TWO_RESULT = "abcde"

# ======================================================================
#                                                              TestSteps
# ======================================================================


class TestSteps(unittest.TestCase):  # pylint: disable=R0904
    """Test Permutation Promenade Dance Steps"""

    def test_spin(self):
        """Test the spin step"""

        # 1. Test spin dance step from the part one examples
        self.assertEqual(promenade.spin('s3', list('abcde')), list('cdeab'))
        self.assertEqual(promenade.spin('s1', list('abcde')), list('eabcd'))

    def test_exchange(self):
        """Test the exchange step"""

        # 1. Test the exchange dance step from the part one examples
        self.assertEqual(promenade.exchange('x3/4', list('eabcd')), list('eabdc'))

    def test_partner(self):
        """Test the partner step"""

        # 1. Test the partment dance step from the part one examples
        self.assertEqual(promenade.partner('pe/b', list('eabdc')), list('baedc'))

# ======================================================================
#                                                          TestPromenade
# ======================================================================


class TestPromenade(unittest.TestCase):  # pylint: disable=R0904
    """Test Promenade object"""

    def test_empty_init(self):
        """Test the default Promenade creation"""

        # 1. Create default Promenade object
        myprom = promenade.Promenade()

        # 2. Make sure it has the default values
        self.assertEqual(myprom.part2, False)
        self.assertEqual(myprom.text, None)
        self.assertEqual(myprom.number, 16)
        self.assertEqual(myprom.dancers, list('abcdefghijklmnop'))
        self.assertEqual(myprom.steps, [])
        self.assertEqual(myprom.index, 0)

    def test_text_init(self):
        """Test the Promenade object creation from text"""

        # 1. Create Promenade object from text
        myprom = promenade.Promenade(number=EXAMPLE_NUMBER, text=EXAMPLE_INPUT)

        # 2. Make sure it has the default values
        self.assertEqual(myprom.part2, False)
        self.assertEqual(myprom.text, EXAMPLE_INPUT)
        self.assertEqual(myprom.number, EXAMPLE_NUMBER)
        self.assertEqual(myprom.dancers, list('abcde'))
        self.assertEqual(myprom.steps, ['s1', 'x3/4', 'pe/b'])
        self.assertEqual(myprom.index, 0)

    def test_part_one_dancers(self):
        """Test Promenade dancers step by step from example"""

        # 1. Create Promenade object from text
        myprom = promenade.Promenade(number=EXAMPLE_NUMBER, text=EXAMPLE_INPUT)

        # 2. Check the initial configuration
        self.assertEqual(myprom.index, 0)
        self.assertEqual(myprom.dancers, list(EXAMPLE_DANCERS[0]))

        # 3. Loop for all of the steps
        for num_step, one_step in enumerate(myprom.steps):

            # 4. Execute the step
            myprom.step(verbose=False)

            # 5. Verify the result of the dance step
            self.assertEqual(myprom.index, num_step + 1)
            self.assertEqual(myprom.dancers, list(EXAMPLE_DANCERS[num_step + 1]))

    def test_part_one(self):
        """Test final dancer configuration from example"""

        # 1. Create Promenade object from text
        myprom = promenade.Promenade(number=EXAMPLE_NUMBER, text=EXAMPLE_INPUT)

        # 2. Check the dancers after executing the steps
        self.assertEqual(myprom.part_one(verbose=False), EXAMPLE_RESULT)

    def test_part_one_twice(self):
        """Test final dancer configuration from example of part2"""

        # 1. Create Promenade object from text
        myprom = promenade.Promenade(number=EXAMPLE_NUMBER, text=TWICE_INPUT)

        # 2. Check the dancers after executing the steps
        self.assertEqual(myprom.part_one(verbose=False), TWICE_RESULT)

    def test_part_two(self):
        """Test final dancer configuration from example for part two"""

        # 1. Create Promenade object from text
        myprom = promenade.Promenade(number=EXAMPLE_NUMBER, text=EXAMPLE_INPUT,
                                     part2=True)

        # 2. Check the dancers after executing the steps
        self.assertEqual(myprom.part_two(verbose=True, limit=1), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                t e s t _ g e n e r a t o r . p y               end
# ======================================================================
