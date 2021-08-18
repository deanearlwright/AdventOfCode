# ======================================================================
# Doesn't He Have Intern-Elves For This
#   Advent of Code 2015 Day 05 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         t h e l i s t . p y
# ======================================================================
"A solver for the Advent of Code 2015 Day 05 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import re
# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
HAS_THREE_VOWELS = re.compile('[aeiou][a-z]*[aeiou][a-z]*[aeiou]')
HAS_PAIR = re.compile('aa|bb|cc|dd|ee|ff|gg|hh|ii|jj|kk|ll|'
                      'mm|nn|oo|pp|qq|rr|ss|tt|uu|vv|ww|xx|yy|zz')
HAS_EVIL = re.compile('ab|cd|pq|xy')

HAS_TWO_PAIR = re.compile(r'([a-z][a-z])[a-z]*\1')
HAS_ONE_ONE_ONE = re.compile(r'([a-z])[a-z]\1')

# ======================================================================
#                                                                Thelist
# ======================================================================


class Thelist(object):   # pylint: disable=R0902, R0205
    "Object for Doesn't He Have Intern-Elves For This"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text

    def is_nice(self, string):
        "Returns true if the string is nice"

        # 1. Part one is differnt than part two
        if not self.part2:

            # 2. Check the string for part one
            has_three_vowels = HAS_THREE_VOWELS.search(string) is not None
            has_pair = HAS_PAIR.search(string) is not None
            has_evil = HAS_EVIL.search(string) is not None

            # 3. Return True of the first two are True but not the third
            return has_three_vowels and has_pair and not has_evil

        # 4. Check the string for part two
        has_two_pair = HAS_TWO_PAIR.search(string) is not None
        has_one_one_one = HAS_ONE_ONE_ONE.search(string) is not None

        # 5. Return True if both are True
        return has_two_pair and has_one_one_one

    def count_nice(self):
        "Return the number of nice strings in the list"

        # 1. Start with nothing
        result = 0

        # 2. Loop for all of the strings
        for string in self.text:

            # 3. If it is nice, increment count
            if self.is_nice(string):
                result += 1

        # 4, Return the number of nice strings
        return result

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.count_nice()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.count_nice()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                       t h e l i s t . p y                      end
# ======================================================================
