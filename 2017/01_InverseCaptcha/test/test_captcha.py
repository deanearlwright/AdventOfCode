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

EXAMPLE_TEXT = """
! Example 1

1122

! Solution = 3  (1 + 2)
"""

EXAMPLES = ["1122", "1111", "1234", "91212129"]

SOLUTIONS = [3, 4, 0, 9]

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

        # 3. Check methods
        self.assertEqual(mycap.solve(), None)

    def test_value_init(self):
        "Test Captcha object creation with values"

        # 1. Create Captcha object with values
        mycap = captcha.Captcha(text="1122")

        # 2. Make sure it has the specified values
        self.assertEqual(mycap.text, "1122")

        # 3. Check methods
        self.assertEqual(mycap.solve(), 3)

    def test_text_init(self):
        """Test Captcha object creation from text"""

        # 1. Create Captcha object from text
        mycap = captcha.Captcha(text=aoc_01.from_text(EXAMPLE_TEXT)[0])

        # 2. Make sure it has the specified values
        self.assertEqual(mycap.text, "1122")

        # 3. Check methods
        self.assertEqual(mycap.solve(), 3)

    def test_examples(self):
        """Test Chaptcha examples"""

        # 1. Loop for the examples
        for enum, text in enumerate(EXAMPLES):

            # 2. Create the Captcha object
            mycap = captcha.Captcha(text=text)

            # 3. Check methods
            self.assertEqual(mycap.solve(verbose=False), SOLUTIONS[enum])

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ m o o n . p y                     end
# ======================================================================
