
# ======================================================================
# Hot Springs
#   Advent of Code 2023 Day 12 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ s p r i n g s . p y
# ======================================================================
"Test Springs for Advent of Code 2023 day 12, Hot Springs"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import springs

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = [
    "???.### 1,1,3",
    ".??..??...?##. 1,1,3",
    "?#?#?#?#?#?#?#? 1,3,1,6",
    "????.#...#... 4,1,1",
    "????.######..#####. 1,6,5",
    "?###???????? 3,2,1",
]

# ======================================================================
#                                                            TestSprings
# ======================================================================


class TestSprings(unittest.TestCase):  # pylint: disable=R0904
    "Test Springs object"

    def test_empty_init(self):
        "Test the default Springs creation"

        # 1. Create default Springs object
        myobj = springs.Springs()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.rows), 0)

    def test_text_init(self):
        "Test the Springs object creation from text"

        # 1. Create Springs object from text
        myobj = springs.Springs(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 6)
        self.assertEqual(len(myobj.rows), 6)

        # 3. Check methods
        self.assertEqual(myobj.rows[0].arrangements(), 1)
        self.assertEqual(myobj.rows[1].arrangements(), 4)
        self.assertEqual(myobj.rows[2].arrangements(), 1)
        self.assertEqual(myobj.rows[3].arrangements(), 1)
        self.assertEqual(myobj.rows[4].arrangements(), 4)
        self.assertEqual(myobj.rows[5].arrangements(), 10)
        self.assertEqual(myobj.total_arrangements(), 21)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                  t e s t _ s p r i n g s . p y                 end
# ======================================================================
