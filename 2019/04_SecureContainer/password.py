# ======================================================================
# Secure Container
#   Advent of Code 2019 Day 04 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                          p a s s w o r d  . p y
# ======================================================================
"Password for Secure Container problem for Advent of Code 2018 Day 04"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from collections import Counter

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                      Utility Functions
# ======================================================================

def sequential(digits):
    "Return True is the digits are sequential"

    return list(digits) == sorted(digits)

def pair(digits):
    "Return True is the digits have a pair or better"

    return any([v >= 2 for v in Counter(digits).values()])

def pair_only(digits):
    "Return True is the digits have a least one pair"

    return any([v == 2 for v in Counter(digits).values()])

# ======================================================================
#                                                               Password
# ======================================================================


class Password():
    """Object representing a password iterator"""

    def __init__(self, start=111111, finish=999999):


        # 0. preconditions
        assert start <= finish
        assert len(str(start)) == 6
        assert len(str(finish)) == 6

        # 1. Set the initial values
        self.start = start
        self.finish = finish
        self.number = start


    def __iter__(self):
        "Iterator for password"

        # 1. Restart at the very beginning
        self.number = self.start

        # 2. I am my own iterator
        return self

    def __next__(self):
        "Returns the next password"

        # 1. Start with no result
        result = None

        # 2. Loop until we get a result
        while result is None:

            # 3. The next password might be this number
            password = self.number

            # 4. Advance the number for next time
            self.number += 1

            # 5. If the password is too big, we are done
            if password > self.finish:
                raise StopIteration

            # 6. If this password passes the check, us
            if self.check(password):
                result = password

        # 7. Return the password we found
        return result


    def check(self, password):
        "Return True is valid password"

        # 1. Test that it is sequention
        if not sequential(str(password)):
            return False

        # 2. And that it comtains a pair
        if not pair(str(password)):
            return False

        # 3. Check limits
        if password < self.start or password > self.finish:
            return False

        # 4. Looks like a good password
        return True

# ======================================================================
#                                                              Password2
# ======================================================================


class Password2(Password):
    """Object representing a password iterator for part two"""

    def __init__(self, start=111111, finish=999999):

        # 1. Just use the Password initialization
        Password.__init__(self, start=start, finish=finish)

    def check(self, password):
        "Return True is valid password"

        # 1. Test that it passes the part one check
        if not Password.check(self, password):
            return False

        # 2. Test this it also passes our pair_only test
        if not pair_only(str(password)):
            return False

        # 3. Looks like a good password
        return True

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         w i r e . p y                          end
# ======================================================================
