# ======================================================================
# High-Entropy Passphrases
#   Advent of Code 2017 Day 04 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                       p a s s p h r a s e s . p y
# ======================================================================
"A solver for High-Entropy Passphrases for Advent of Code 2017 Day 04"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from collections import Counter

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                            PassPhrases
# ======================================================================


class PassPhrases(object):
    """Object representing a PassPhrases solver"""

    def __init__(self, part2=False, text=None):

        # 1. Set the initial values
        self.part2 = part2
        if text is not None:
            self.phrases = text
        else:
            self.phrases = []

    def is_valid(self, phrase):
        "Return if a phrase is valid or not"

        # 1. For parts one and two we need to check uniqueness of words
        words = phrase.split()
        unique = set(words)
        if len(words) != len(unique):
            return False

        # 2. But that's all we need for part one
        if not self.part2:
            return True

        # 3. Words must have unique letter counts for part two
        letter_knts = [Counter(word) for word in words]
        for wnum, knt1 in enumerate(letter_knts[:-1]):
            for knt2 in letter_knts[wnum+1:]:
                if knt1 == knt2:
                    return False
        return True

    def knt_valid(self, verbose=False):
        "Return the highest square on the ring"

        result = 0
        total = 0
        for phrase in self.phrases:
            total += 1
            valid = self.is_valid(phrase)
            if verbose:
                if valid:
                    print("Phrase %s is valid" % (phrase))
                else:
                    print("Phrase %s is not valid" % (phrase))
            if valid:
                result += 1
        if verbose:
            print("There are %d valid phrases out of %d total" %
                  (result, total))
        return result

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                  p a s s p h r a s e s . p y                   end
# ======================================================================
