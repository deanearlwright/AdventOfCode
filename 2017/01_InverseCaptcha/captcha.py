# ======================================================================
# Inverse Captcha
#   Advent of Code 2019 Day 12 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                             c a p t c h a . p y
# ======================================================================
"A single moon for Inverse Captcha for Advent of Code 2017 Day 01"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import re

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
DUPS_RE = re.compile(r'([0-9])\1')

# ======================================================================
#                                                                Captcha
# ======================================================================


class Captcha():
    """Object representing a Captcha solver"""

    def __init__(self, text=None):

        # 1. Set the initial values
        self.text = text

    def solve(self, verbose=False):
        "Solve the captcha"

        # 1. If we have nothing, that's what you get.
        if self.text is None:
            return None

        # 2. Start with no digits
        digits = []
        start = 0
        wrap = self.text + self.text[0]

        # 3. Loop for all the matches
        while True:
            if verbose:
                print("Searching %s at %d" % (wrap, start))
            dup_match = DUPS_RE.search(wrap, start)
            if dup_match is None:
                break

            if verbose:
                print("Match from %s at %d %s of %s" % (
                    start, dup_match.start(),
                                          dup_match.group(1),
                                          dup_match.group(0)))
            # 4. Add the digit to the digits
            digits.append(int(dup_match.group(1)))

            # 5. Advance the start
            start = 1 + dup_match.start()

        # 6. Return the sum of the digits
        if verbose:
            print(digits)
        return sum(digits)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                        c a p t c h a . p y                     end
# ======================================================================
