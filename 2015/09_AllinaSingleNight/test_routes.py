# ======================================================================
# All in a Single Night
#   Advent of Code 2015 Day 09 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ r o u t e s . p y
# ======================================================================
"Test solver for Advent of Code 2015 day 09, All in a Single Night"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_09
import routes

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 605
PART_TWO_RESULT = 982

# ======================================================================
#                                                             TestRoutes
# ======================================================================


class TestRoutes(unittest.TestCase):  # pylint: disable=R0904
    "Test Routes object"

    def test_empty_init(self):
        "Test the default Routes creation"

        # 1. Create default Routes object
        myobj = routes.Routes()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.nodes), 0)
        self.assertEqual(len(myobj.links), 0)

    def test_text_init(self):
        "Test the Routes object creation from text"

        # 1. Create Routes object from text
        myobj = routes.Routes(text=aoc_09.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 3)
        self.assertEqual(len(myobj.nodes), 3)
        self.assertEqual(len(myobj.links), 6)
        self.assertEqual('London' in myobj.nodes, True)
        self.assertEqual('Bristal' in myobj.nodes, False)
        self.assertEqual(('London', 'Belfast') in myobj.links, True)
        self.assertEqual(('Belfast', 'London') in myobj.links, True)
        self.assertEqual(('London', 'Bristal') in myobj.links, False)
        self.assertEqual(myobj.links[('London', 'Belfast')], 518)
        self.assertEqual(myobj.links[('Belfast', 'London')], 518)

    def test_part_one(self):
        "Test part one example of Routes object"

        # 1. Create Routes object from text
        myobj = routes.Routes(text=aoc_09.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Routes object"

        # 1. Create Routes object from text
        myobj = routes.Routes(part2=True, text=aoc_09.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ r o u t e s . p y                  end
# ======================================================================
