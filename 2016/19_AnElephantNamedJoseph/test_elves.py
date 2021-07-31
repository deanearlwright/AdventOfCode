# ======================================================================
# An Elephant Named Joseph
#   Advent of Code 2016 Day 19 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                       t e s t _ e l v e s . p y
# ======================================================================
"Test solver for Advent of Code 2016 day 19, An Elephant Named Joseph"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_19
import elves

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
5
"""

PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 3
PART_TWO_RESULT = 2

# ======================================================================
#                                                              TestElves
# ======================================================================


class TestElves(unittest.TestCase):  # pylint: disable=R0904
    "Test Elves object"

    def test_empty_init(self):
        "Test the default Elves creation"

        # 1. Create default Elves object
        myobj = elves.Elves()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.number, 0)
        self.assertEqual(len(myobj.elves), 0)

    def test_text_init(self):
        "Test the Elves object creation from text"

        # 1. Create Elves object from text
        myobj = elves.Elves(text=aoc_19.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 1)
        self.assertEqual(myobj.number, 5)
        self.assertEqual(len(myobj.elves), 5)

        # 3. Check methods
        self.assertEqual(myobj.on_left(1), 2)
        self.assertEqual(myobj.on_left(2), 3)
        self.assertEqual(myobj.on_left(3), 4)
        self.assertEqual(myobj.on_left(4), 5)
        self.assertEqual(myobj.on_left(5), 1)

        self.assertEqual(myobj.across(1, 5), 3)

        myobj.takes(1, 2)
        myobj.takes(3, 4)
        myobj.takes(5, 1)
        self.assertEqual(myobj.on_left(3), 5)
        myobj.takes(3, 5)
        self.assertEqual(myobj.presents(3), 5)

    def test_part_two_science(self):
        "Output the result of a whole bunch of part2 runs"

        for number in range(2, 200):
            myobj = elves.Elves(text=[str(number)])
            two = myobj.party_on_two()
            dude = myobj.party_on_dude()
            #print("%d,%d,%d" % (number, two, dude))
            self.assertEqual(two, dude)

    def test_part_one(self):
        "Test part one example of Elves object"

        # 1. Create Elves object from text
        myobj = elves.Elves(text=aoc_19.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Elves object"

        # 1. Create Elves object from text
        myobj = elves.Elves(part2=True, text=aoc_19.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ e l v e s . p y                   end
# ======================================================================
