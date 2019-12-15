# ======================================================================
# Space Stoichiometry
#   Advent of Code 2019 Day 14 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ r e a c t i o n . p y
# ======================================================================
"Test reaction for Advent of Code 2019 day 14, Space Stoichiometry"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import reaction

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                           TestReaction
# ======================================================================


class TestReaction(unittest.TestCase):  # pylint: disable=R0904
    """Test Reaction object"""

    def test_empty_init(self):
        """Test default Reaction object creation"""

        # 1. Create default Reaction object
        myrecipe = reaction.Reaction()

        # 2. Make sure it has the default values
        self.assertEqual(myrecipe.produces, None)
        self.assertEqual(myrecipe.quanity, 1)
        self.assertEqual(myrecipe.requires, [])

        # 3. Check methods
        self.assertEqual(str(myrecipe), " => 1 None")

    def test_value_init(self):
        "Test Moon object creation with values"

        # 1. Create Reaction object with values
        myrecipe = reaction.Reaction(produces='C', quanity=1, requires=['7 A', '1 B'])

        # 2. Make sure it has the specified values
        self.assertEqual(myrecipe.produces, 'C')
        self.assertEqual(myrecipe.quanity, 1)
        self.assertEqual(myrecipe.requires, ['7 A', '1 B'])

        # 3. Check methods
        self.assertEqual(str(myrecipe), "7 A, 1 B => 1 C")

    def test_text_single_init(self):
        """Test Moon object creation from text"""

        # 1. Create Reaction object from test with a single ingrediant
        myrecipe = reaction.Reaction(text='10 ORE => 10 A')

        # 2. Make sure it has the default values
        self.assertEqual(myrecipe.produces, 'A')
        self.assertEqual(myrecipe.quanity, 10)
        self.assertEqual(myrecipe.requires, ['10 ORE'])

        # 3. Check methods
        self.assertEqual(str(myrecipe), "10 ORE => 10 A")

    def test_text_multiple_init(self):
        """Test Moon object creation from text"""

        # 1. Create Reaction object from text with multiple ingrediants
        myrecipe = reaction.Reaction(text='7 A, 1 E => 1 FUEL')

        # 2. Make sure it has the default values
        self.assertEqual(myrecipe.produces, 'FUEL')
        self.assertEqual(myrecipe.quanity, 1)
        self.assertEqual(myrecipe.requires, ['7 A', '1 E'])

        # 3. Check methods
        self.assertEqual(str(myrecipe), "7 A, 1 E => 1 FUEL")


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                  t e s t _ r e a c t i o n . p y               end
# ======================================================================
