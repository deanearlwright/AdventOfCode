# ======================================================================
# Corporate Policy
#   Advent of Code 2015 Day 11 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         p a s s w o r d . p y
# ======================================================================
"A solver for the Advent of Code 2015 Day 11 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import re

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
TRIPLE = "abc|bcd|cde|def|efg|fgh|pqr|qrs|rst|stu|tuw|uvw|vwx|wxy|xyz"
RE_TRIPLE = re.compile(TRIPLE)
RE_CONFUSING = re.compile("[iol]")
PAIRS = "aa|bb|cc|dd|ee|ff|gg|hh|JJ|kk|mm|pp|qq|rr|ss|tt|uu|vv|ww|xx|yy|zz"
RE_PAIRS = re.compile(PAIRS)
NEXT_LETTER = {
  'a': 'b',
  'b': 'c',
  'c': 'd',
  'd': 'e',
  'e': 'f',
  'f': 'g',
  'g': 'h',
  'h': 'j',
  'i': 'j',
  'j': 'k',
  'k': 'm',
  'l': 'm',
  'm': 'n',
  'n': 'p',
  'o': 'p',
  'p': 'q',
  'q': 'r',
  'r': 's',
  's': 't',
  't': 'u',
  'u': 'v',
  'v': 'w',
  'w': 'x',
  'x': 'y',
  'y': 'z',
  'z': 'a',
}

# ======================================================================
#                                                               Password
# ======================================================================


class Password(object):   # pylint: disable=R0902, R0205
    "Object for Corporate Policy"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.current = ""

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.current = text[0]

    @staticmethod
    def valid_password(password):
        "Returns true of valid password"

        # 1. Must contain a triple
        match = RE_TRIPLE.search(password)
        if not match:
            return False

        # 2. Must not contain a confusing letter
        match = RE_CONFUSING.search(password)
        if match:
            return False

        # 3. Must contain two different pairs
        pairs = set(RE_PAIRS.findall(password))
        if len(pairs) < 2:
            return False

        # 4. Passes all the tests
        return True

    # staticmethod
    def increment_password(password):
        "Increment to the next (possibly invalid) password"

        # 1. Start with the current password
        result = list(password)

        # 1. Loop for all of the character position
        for indx in range(7, 0, -1):

            # 2. Increment this character
            this_letter = password[indx]
            next_letter = NEXT_LETTER[this_letter]

            # 3. Set it in the result
            result[indx] = next_letter

            # 4. If we didn't roll over, we are done
            if next_letter != 'a':
                break

        # 5. Return the updated password
        return ''.join(result)

    def next_password(self):
        "Returns the next password"

        # 1. Generate a new password
        new_password = Password.increment_password(self.current)

        # 2. Loop until we generate a valid password
        while not Password.valid_password(new_password):

            # 3. Generate another one
            new_password = Password.increment_password(new_password)

        # 4. Return the new password
        return new_password

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.next_password()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        self.current = self.next_password()
        return self.next_password()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      p a s s w o r d . p y                     end
# ======================================================================
