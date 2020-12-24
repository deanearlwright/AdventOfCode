# ======================================================================
# Ticket Translation
#   Advent of Code 2020 Day 16 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ t i c k e t s . p y
# ======================================================================
"Test solver for Advent of Code 2020 day 16, Ticket Translation"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_16
import tickets

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
"""
EXAMPLE_TWO = """
class: 0-1 or 4-19
departure row: 0-5 or 8-19
departure seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,99
3,9,18
15,1,5
5,14,9
"""

PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TWO

PART_ONE_RESULT = 71
PART_TWO_RESULT = 11 * 13

# ======================================================================
#                                                            TestTickets
# ======================================================================


class TestTickets(unittest.TestCase):  # pylint: disable=R0904
    "Test Tickets object"

    def test_empty_init(self):
        "Test the default Tickets creation"

        # 1. Create default Tickets object
        myobj = tickets.Tickets()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.rules, [])
        self.assertEqual(myobj.mine, None)
        self.assertEqual(myobj.nearby, [])

    def test_text_init(self):
        "Test the Tickets object creation from text"

        # 1. Create Tickets object from text
        myobj = tickets.Tickets(text=aoc_16.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 10)
        self.assertEqual(len(myobj.rules), 3)
        self.assertNotEqual(myobj.mine, None)
        self.assertEqual(len(myobj.nearby), 4)

    def test_part_one(self):
        "Test part one example of Tickets object"

        # 1. Create Tickets object from text
        myobj = tickets.Tickets(text=aoc_16.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Tickets object"

        # 1. Create Tickets object from text
        myobj = tickets.Tickets(part2=True, text=aoc_16.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ t i c k e t s . p y                end
# ======================================================================
