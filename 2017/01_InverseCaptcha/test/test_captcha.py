# ======================================================================
# The Inverse Captcha
#   Advent of Code 2017 Day 01 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ c a p t c h a . p y
# ======================================================================
"Test captcha solver for Advent of Code 2019 day 12, The N-Body Problem"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import captcha
import aoc_01

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

P1_EXAMPLE_TEXT = """
! Example 1 from part 1

1122

! Solution = 3  (1 + 2)
"""

P1_EXAMPLES = ["1122", "1111", "1234", "91212129"]

P1_SOLUTIONS = [3, 4, 0, 9]

P2_EXAMPLE_TEXT = """
! Example 1 from part 2

1212

! Solution = 6, the list contains 4 items,
! and all four digits match the digit 2 items ahead
"""

P2_EXAMPLES = ["1212", "1221", "123425", "123123", "12131415"]

P2_SOLUTIONS = [6, 0, 4, 12, 4]

# ======================================================================
#                                                            TestCaptcha
# ======================================================================


class TestCaptcha(unittest.TestCase):  # pylint: disable=R0904
    """Test Captcha object"""

    def test_empty_init(self):
        """Test default Captcha object creation"""

        # 1. Create default Captcha object
        mycap = captcha.Captcha()

        # 2. Make sure it has the default values
        self.assertEqual(mycap.text, None)
        self.assertEqual(mycap.part2, False)
        self.assertEqual(mycap.offset, 1)

        # 3. Check methods
        self.assertEqual(mycap.solve(), None)
        self.assertEqual(mycap.re_solve(), None)

    def test_value_init(self):
        "Test Captcha object creation with values"

        # 1. Create Captcha object with values
        mycap = captcha.Captcha(text="1122", offset=1)

        # 2. Make sure it has the specified values
        self.assertEqual(mycap.text, "1122")
        self.assertEqual(mycap.part2, False)
        self.assertEqual(mycap.offset, 1)

        # 3. Check methods
        self.assertEqual(mycap.solve(), 3)
        self.assertEqual(mycap.re_solve(), 3)

    def test_text_init(self):
        """Test Captcha object creation from text"""

        # 1. Create Captcha object from text
        mycap = captcha.Captcha(text=aoc_01.from_text(P1_EXAMPLE_TEXT)[0])

        # 2. Make sure it has the specified values
        self.assertEqual(mycap.text, "1122")
        self.assertEqual(mycap.part2, False)
        self.assertEqual(mycap.offset, 1)

        # 3. Check methods
        self.assertEqual(mycap.solve(), 3)
        self.assertEqual(mycap.re_solve(), 3)

    def test_part_one_examples(self):
        """Test Chaptcha examples for Part One"""

        # 1. Loop for the examples
        for enum, text in enumerate(P1_EXAMPLES):

            # 2. Create the Captcha object
            mycap = captcha.Captcha(text=text)

            # 3. Check methods
            self.assertEqual(mycap.solve(verbose=False), P1_SOLUTIONS[enum])
            self.assertEqual(mycap.re_solve(verbose=False), P1_SOLUTIONS[enum])

    def test_part_two_text_init(self):
        """Test Captcha object creation from text"""

        # 1. Create Captcha object from text
        mycap = captcha.Captcha(part2=True, text=aoc_01.from_text(P2_EXAMPLE_TEXT)[0])

        # 2. Make sure it has the specified values
        self.assertEqual(mycap.text, "1212")
        self.assertEqual(mycap.part2, True)
        self.assertEqual(mycap.offset, 2)

        # 3. Check methods
        self.assertEqual(mycap.solve(verbose=False), 6)

    def test_part_two_examples(self):
        """Test Chaptcha examples for Part Two"""

        # 1. Loop for the examples
        for enum, text in enumerate(P2_EXAMPLES):

            # 2. Create the Captcha object
            mycap = captcha.Captcha(part2=True, text=text)

            # 3. Check methods
            self.assertEqual(mycap.solve(verbose=False), P2_SOLUTIONS[enum])

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ m o o n . p y                     end
# ======================================================================
