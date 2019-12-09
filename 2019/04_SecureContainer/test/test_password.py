# ======================================================================
# Secure Container
#   Advent of Code 2019 Day 04 -- Eric Wastl -- https://adventofcode.com
#
# codeuter simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                     t e s t _ p a s s w o r d . p y
# ======================================================================
"Test password objects for Advent of Code 2019 day 4, Secure Container"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import password

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                            TestUtility
# ======================================================================

class TestUtility(unittest.TestCase):  # pylint: disable=R0904
    """Test utilty function"""

    def test_sequential(self):
        """Test sequental checking function"""

        self.assertEqual(password.sequential("111111"), True)
        self.assertEqual(password.sequential("122345"), True)
        self.assertEqual(password.sequential("111123"), True)
        self.assertEqual(password.sequential("135679"), True)
        self.assertEqual(password.sequential("223450"), False)
        self.assertEqual(password.sequential("123789"), True)

        self.assertEqual(password.sequential("112233"), True)
        self.assertEqual(password.sequential("123444"), True)
        self.assertEqual(password.sequential("111122"), True)

    def test_pair(self):
        """Test pair checking function"""

        self.assertEqual(password.pair("111111"), True)
        self.assertEqual(password.pair("122345"), True)
        self.assertEqual(password.pair("111123"), True)
        self.assertEqual(password.pair("135679"), False)
        self.assertEqual(password.pair("223450"), True)
        self.assertEqual(password.pair("123789"), False)

        self.assertEqual(password.pair("112233"), True)
        self.assertEqual(password.pair("123444"), True)
        self.assertEqual(password.pair("111122"), True)

    def test_pair_only(self):
        """Test pair checking function"""

        self.assertEqual(password.pair_only("111111"), False)
        self.assertEqual(password.pair_only("122345"), True)
        self.assertEqual(password.pair_only("111123"), False)
        self.assertEqual(password.pair_only("135679"), False)
        self.assertEqual(password.pair_only("223450"), True)
        self.assertEqual(password.pair_only("123789"), False)

        self.assertEqual(password.pair_only("112233"), True)
        self.assertEqual(password.pair_only("123444"), False)
        self.assertEqual(password.pair_only("111122"), True)

# ======================================================================
#                                                           TestPassword
# ======================================================================


class TestPassword(unittest.TestCase):  # pylint: disable=R0904
    """Test password object"""

    def test_empty_init(self):
        """Test default password object creation"""

        # 1. Create default password object
        mypswd = password.Password()

        # 2. Make sure it has the default values
        self.assertEqual(mypswd.start, 111111)
        self.assertEqual(mypswd.finish, 999999)

        # 3. Check methods
        self.assertEqual(mypswd.check(111111), True)
        self.assertEqual(mypswd.check(122345), True)
        self.assertEqual(mypswd.check(111123), True)
        self.assertEqual(mypswd.check(135679), False)
        self.assertEqual(mypswd.check(223450), False)
        self.assertEqual(mypswd.check(123789), False)

    def test_value_init(self):
        """Test password object creation with values"""

        # 1. Create Wire obhect with values
        mypswd = password.Password(start=123444, finish=123455)

        # 2. Make sure it has the specified values
        self.assertEqual(mypswd.start, 123444)
        self.assertEqual(mypswd.finish, 123455)

        # 3. Check methods
        self.assertEqual(mypswd.check(111111), False)
        self.assertEqual(mypswd.check(123449), True)
        self.assertEqual(mypswd.check(222222), False)

        # Check iterator
        self.assertEqual(list(mypswd),
                         [123444, 123445, 123446, 123447,
                          123448, 123449, 123455])

# ======================================================================
#                                                          TestPassword2
# ======================================================================


class TestPassword2(unittest.TestCase):  # pylint: disable=R0904
    """Test password object"""

    def test_empty_init(self):
        """Test default password object creation"""

        # 1. Create default password object
        mypswd = password.Password2()

        # 2. Make sure it has the default values
        self.assertEqual(mypswd.start, 111111)
        self.assertEqual(mypswd.finish, 999999)

        # 3. Check methods
        self.assertEqual(mypswd.check(111111), False)
        self.assertEqual(mypswd.check(122345), True)
        self.assertEqual(mypswd.check(111123), False)
        self.assertEqual(mypswd.check(135679), False)
        self.assertEqual(mypswd.check(223450), False)
        self.assertEqual(mypswd.check(123789), False)

        self.assertEqual(mypswd.check(112233), True)
        self.assertEqual(mypswd.check(123444), False)
        self.assertEqual(mypswd.check(111122), True)

    def test_value_init(self):
        """Test password object creation with values"""

        # 1. Create Wire obhect with values
        mypswd = password.Password2(start=123444, finish=123455)

        # 2. Make sure it has the specified values
        self.assertEqual(mypswd.start, 123444)
        self.assertEqual(mypswd.finish, 123455)

        # 3. Check methods
        self.assertEqual(mypswd.check(111111), False)
        self.assertEqual(mypswd.check(123449), True)
        self.assertEqual(mypswd.check(222222), False)

        self.assertEqual(mypswd.check(123444), False)
        self.assertEqual(mypswd.check(123445), True)
        self.assertEqual(mypswd.check(123455), True)

        # Check iterator
        self.assertEqual(list(mypswd),
                         [123445, 123446, 123447,
                          123448, 123449, 123455])


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                t e s t _ p a s s w o r d . p y                 end
# ======================================================================
