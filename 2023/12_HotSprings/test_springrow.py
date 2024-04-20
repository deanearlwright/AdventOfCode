
# ======================================================================
# Hot Springs
#   Advent of Code 2023 Day 12 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ s p r i n g r o w . p y
# ======================================================================
"Test Springrow for Advent of Code 2023 day 12, Hot Springs"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import springrow

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = "???.### 1,1,3"

SIMPLE_TEXT = {
    "# 1": 1,
    "? 1": 1,
    "#. 1": 1,
    ".# 1": 1,
    "## 2": 1,
    "?. 1": 1,
    "?# 1": 1,
    "?# 2": 1,
    ".? 1": 1,
    "#? 1": 1,
    "#? 2": 1,
    "?? 1": 2,
    "?? 2": 1,
    "??? 1": 3,
    "??? 1,1": 1,
    "??? 2": 2,
    "??? 3": 1,
}

COMPLEX_TEXT = {
    "???.### 1,1,3": 1,
    ".??..??...?##. 1,1,3": 4,
    "?#?#?#?#?#?#?#? 1,3,1,6": 1,
    "????.#...#... 4,1,1": 1,
    "????.######..#####. 1,6,5": 4,
    "?###???????? 3,2,1": 10,
}

# ======================================================================
#                                                          TestSpringrow
# ======================================================================


class TestSpringrow(unittest.TestCase):  # pylint: disable=R0904
    "Test Springrow object"

    def test_empty_init(self):
        "Test the default Springrow creation"

        # 1. Create default Springrow object
        myobj = springrow.Springrow()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.individuals, "")
        self.assertEqual(myobj.groups, None)

    def test_text_init(self):
        "Test the Springrow object creation from text"

        # 1. Create Springrow object from text
        myobj = springrow.Springrow(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 13)
        self.assertEqual(myobj.individuals, "???.###")
        self.assertEqual(len(myobj.groups), 3)

        # 3. Check methods
        self.assertEqual(myobj.arrangements(), 1)

    def test_simple_text(self):
        "Test the Springrow object solving simple text"

        # 1. Loop for all of the tests
        for text, answer in SIMPLE_TEXT.items():

            # 2. Create Springrow object from text
            myobj = springrow.Springrow(text=text)

            # 3. Check number of arrangements
            self.assertEqual(myobj.arrangements(), answer)

    def test_complex_text(self):
        "Test the Springrow object solving simple text"

        # 1. Loop for all of the tests
        for text, answer in COMPLEX_TEXT.items():

            # 2. Create Springrow object from text
            myobj = springrow.Springrow(text=text)

            # 3. Check number of arrangements
            self.assertEqual(myobj.arrangements(), answer)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                t e s t _ s p r i n g r o w . p y               end
# ======================================================================
