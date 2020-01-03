# ======================================================================
# High-Entropy Passphrases
#   Advent of Code 2017 Day 04 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                t e s t _ p a s s p h r a s e s . p y
# ======================================================================
"Test solver for Advent of Code 2017 day 3, High-Entropy Passphrases"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_04
import passphrases

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

P1_EXAMPLES_TEXT = """
aa bb cc dd ee
aa bb cc dd aa
aa bb cc dd aaa

! The first and third are valid but the second is not.
"""

# ======================================================================
#                                                        TestPassPhrases
# ======================================================================


class TestPassPhrases(unittest.TestCase):  # pylint: disable=R0904
    """Test PassPhrases object"""

    def test_empty_init(self):
        """Test default PassPhrases creation"""

        # 1. Create default PassPhrases object
        mypass = passphrases.PassPhrases()

        # 2. Make sure it has the default values
        self.assertEqual(mypass.part2, False)
        self.assertEqual(mypass.phrases, [])

        # 3. Check methods
        self.assertEqual(mypass.knt_valid(), 0)

    def test_value_init(self):
        """Test PassPhrases creation with values"""

        # 1. Create default PassPhrases object
        mypass = passphrases.PassPhrases(text=["aa bb cc dd ee",
                                               "aa bb cc dd aa",
                                               "aa bb cc dd aaa"])

        # 2. Make sure it has the default values
        self.assertEqual(mypass.part2, False)
        self.assertEqual(len(mypass.phrases), 3)

        # 3. Check methods
        self.assertEqual(mypass.knt_valid(), 2)

    def test_text_init(self):
        """Test PassPhrases creation from text"""

        # 1. Create default PassPhrases object
        mypass = passphrases.PassPhrases(text=aoc_04.from_text(P1_EXAMPLES_TEXT))

        # 2. Make sure it has the default values
        self.assertEqual(mypass.part2, False)
        self.assertEqual(len(mypass.phrases), 3)

        # 3. Check methods
        self.assertEqual(mypass.knt_valid(), 2)

    def test_is_valid(self):
        """Test if individual phrase is valid"""

        # 1. Create default PassPhrases object
        mypass = passphrases.PassPhrases()

        # 2. Make sure it has the default values
        self.assertEqual(mypass.part2, False)
        self.assertEqual(mypass.phrases, [])

        # 3. Check methods
        self.assertEqual(mypass.is_valid("aa bb cc dd ee"), True)
        self.assertEqual(mypass.is_valid("aa bb cc dd aa"), False)
        self.assertEqual(mypass.is_valid("aa bb cc dd aaa"), True)

    def test_is_valid_two(self):
        """Test if individual phrase is valid"""

        # 1. Create default PassPhrases object
        mypass = passphrases.PassPhrases(part2=True)

        # 2. Make sure it has the default values
        self.assertEqual(mypass.part2, True)
        self.assertEqual(mypass.phrases, [])

        # 3. Check methods
        self.assertEqual(mypass.is_valid("abcde fghij"), True)
        self.assertEqual(mypass.is_valid("abcde xyz ecdab"), False)
        self.assertEqual(mypass.is_valid("a ab abc abd abf abj"), True)
        self.assertEqual(mypass.is_valid("iiii oiii ooii oooi oooo"), True)
        self.assertEqual(mypass.is_valid("oiii ioii iioi iiio"), False)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end               t e s t _ p a s s p h r a s e s . p y            end
# ======================================================================
