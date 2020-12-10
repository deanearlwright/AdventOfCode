# ======================================================================
# Encoding Error
#   Advent of Code 2020 Day 09 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ c y p h e r . p y
# ======================================================================
"Test solver for Advent of Code 2020 day 09, Encoding Error"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_09
import cypher

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 127
PART_TWO_RESULT = 62

# ======================================================================
#                                                             TestCypher
# ======================================================================


class TestCypher(unittest.TestCase):  # pylint: disable=R0904
    "Test Cypher object"

    def test_empty_init(self):
        "Test the default Cypher creation"

        # 1. Create default Cypher object
        myobj = cypher.Cypher()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.numbers, None)
        self.assertEqual(myobj.previous, None)

    def test_text_init(self):
        "Test the Cypher object creation from text"

        # 1. Create Cypher object from text
        myobj = cypher.Cypher(text=aoc_09.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 20)
        self.assertEqual(len(myobj.numbers), 20)
        self.assertEqual(myobj.previous, None)

        # 3. Test methods
        original_numbers = myobj.numbers.copy()
        myobj.preamble(limit=5)
        self.assertEqual(len(myobj.numbers), 15)
        self.assertEqual(len(myobj.previous), 5)

        self.assertEqual(myobj.get_pair(40), (15, 25))
        self.assertEqual(myobj.get_pair(62), (15, 47))
        self.assertEqual(myobj.get_pair(55), (35, 20))
        self.assertEqual(myobj.get_pair(56), (None, None))

        self.assertEqual(myobj.is_weak(40), False)
        self.assertEqual(myobj.is_weak(62), False)
        self.assertEqual(myobj.is_weak(55), False)
        self.assertEqual(myobj.is_weak(56), True)

        myobj.numbers = original_numbers
        self.assertEqual(myobj.find_first_weakness(limit=5), 127)

    def test_part_one(self):
        "Test part one example of Cypher object"

        # 1. Create Cypher object from text
        myobj = cypher.Cypher(text=aoc_09.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False, limit=5), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Cypher object"

        # 1. Create Cypher object from text
        myobj = cypher.Cypher(part2=True, text=aoc_09.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False, limit=5), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ c y p h e r . p y                  end
# ======================================================================
