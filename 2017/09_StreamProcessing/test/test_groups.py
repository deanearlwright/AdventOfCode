# ======================================================================
# Stream Processing
#   Advent of Code 2017 Day 09 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ g r o u p s . p y
# ======================================================================
"Test solver for Advent of Code 2017 day 9, Stream Processing"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import groups

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

P1_GROUP_EXAMPLES = [
    "{}", # 1 group.
    "{{{}}}",  # 3 groups.
    "{{},{}}", # also 3 groups.
    "{{{},{},{{}}}}", # 6 groups.
    "{<{},{},{{}}>}", # 1 group (which itself contains garbage).
    "{<a>,<a>,<a>,<a>}", #1 group.
    "{{<a>},{<a>},{<a>},{<a>}}", # 5 groups.
    "{{<!>},{<!>},{<!>},{<a>}}", # 2 groups (since all but the last > are
]
P1_GROUP_NUMBERS = [1, 3, 3, 6, 1, 1, 5, 2]

P1_SCORE_EXAMPLES = [
    "{}", # score of 1.
    "{{{}}}", # score of 1 + 2 + 3 = 6.
    "{{},{}}", # score of 1 + 2 + 2 = 5.
    "{{{},{},{{}}}}", # score of 1 + 2 + 3 + 3 + 3 + 4 = 16.
    "{<a>,<a>,<a>,<a>}", # score of 1.
    "{{<ab>},{<ab>},{<ab>},{<ab>}}", # score of 1 + 2 + 2 + 2 + 2 = 9.
    "{{<!!>},{<!!>},{<!!>},{<!!>}}", # score of 1 + 2 + 2 + 2 + 2 = 9.
    "{{<a!>},{<a!>},{<a!>},{<ab>}}", # score of 1 + 2 = 3.
]
P1_SCORE_NUMBERS = [1, 6, 5, 16, 1, 9, 9, 3]

P2_EXAMPLES = [
    "{<>}", # 0 characters.
    "{<random characters>}", # 17 characters.
    "{<<<<>}", # 3 characters.
    "{<{!>}>}", # 2 characters.
    "{<!!>}", # 0 characters.
    "{<!!!>>}", # 0 characters.
    '{<{o"i!a,<{i<a>}', # 10 characters.
]
P2_NUMBERS = [0, 17, 3, 2, 0, 0, 10]

# ======================================================================
#                                                             TestGroups
# ======================================================================


class TestGroups(unittest.TestCase):  # pylint: disable=R0904
    """Test Register object"""

    def test_empty_init(self):
        """Test default Groups creation"""

        # 1. Create default Groups object
        mygrp = groups.Groups()

        # 2. Make sure it has the default values
        self.assertEqual(mygrp.part2, False)
        self.assertEqual(mygrp.state, 0)
        self.assertEqual(mygrp.level, 0)
        self.assertEqual(mygrp.group, 0)
        self.assertEqual(mygrp.score, 0)
        self.assertEqual(str(mygrp), "s=0 l=0 g=0 s=0")


    def test_text_init(self):
        """Test Groups creation from text"""

        # 1. Create Instruction object from text
        mygrp = groups.Groups(text="{<a>,<a>,<a>,<a>}")

        # 2. Make sure it has the specified values
        self.assertEqual(mygrp.part2, False)
        self.assertEqual(mygrp.state, 1)
        self.assertEqual(mygrp.level, 0)
        self.assertEqual(mygrp.group, 1)
        self.assertEqual(mygrp.score, 1)
        self.assertEqual(str(mygrp), "s=1 l=0 g=1 s=1")

    def test_part_one_groups(self):
        """Check the part one group examples"""

        # 1. Loop for all the part one group examples
        for enum, etext in enumerate(P1_GROUP_EXAMPLES):

            # 2. Create the group example
            mygrp = groups.Groups(text=etext)

            # 3. Verifty the results
            self.assertEqual(mygrp.group, P1_GROUP_NUMBERS[enum])

    def test_part_one_scores(self):
        """Check the part one score examples"""

        # 1. Loop for all the part one score examples
        for enum, etext in enumerate(P1_SCORE_EXAMPLES):

            # 2. Create the score example
            mygrp = groups.Groups(text=etext)

            # 3. Verifty the results
            self.assertEqual(mygrp.score, P1_SCORE_NUMBERS[enum])

    def test_part_two(self):
        """Check the part two examples"""

        # 1. Loop for all the part one score examples
        for enum, etext in enumerate(P2_EXAMPLES):

            # 2. Create the score example
            mygrp = groups.Groups(text=etext, part2=True)

            # 3. Verifty the results
            self.assertEqual(mygrp.trash, P2_NUMBERS[enum])

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ g r o u p s . p y                 end
# ======================================================================
