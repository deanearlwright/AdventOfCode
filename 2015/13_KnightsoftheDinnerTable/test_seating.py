# ======================================================================
# Knights of the Dinner Table
#   Advent of Code 2015 Day 13 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ s e a t i n g . p y
# ======================================================================
"Test solver for Advent of Code 2015 day 13, Knights of the Dinner Table"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_13
import seating

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 330
PART_TWO_RESULT = 286

# ======================================================================
#                                                            TestSeating
# ======================================================================


class TestSeating(unittest.TestCase):  # pylint: disable=R0904
    "Test Seating object"

    def test_empty_init(self):
        "Test the default Seating creation"

        # 1. Create default Seating object
        myobj = seating.Seating()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.people), 0)
        self.assertEqual(len(myobj.preferences), 0)

    def test_text_init(self):
        "Test the Seating object creation from text"

        # 1. Create Seating object from text
        myobj = seating.Seating(text=aoc_13.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 12)
        self.assertEqual(len(myobj.people), 4)
        self.assertEqual(len(myobj.preferences), 12)

    def test_part_one(self):
        "Test part one example of Seating object"

        # 1. Create Seating object from text
        myobj = seating.Seating(text=aoc_13.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Seating object"

        # 1. Create Seating object from text
        myobj = seating.Seating(part2=True, text=aoc_13.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                  t e s t _ s e a t i n g . p y                 end
# ======================================================================
