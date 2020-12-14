# ======================================================================
# Shuttle Search
#   Advent of Code 2020 Day 13 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ b u s e s . p y
# ======================================================================
"Test solver for Advent of Code 2020 day 13, Shuttle Search"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_13
import buses

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
939
7,13,x,x,59,x,31,19
"""

EXAMPLES = [
   {'text': '17,x,13,19', 'at': 3417},
   {'text': '67,7,59,61', 'at': 754018},
   {'text': '67,x,7,59,61', 'at': 779210},
   {'text': '67,7,x,59,61', 'at': 1261476},
   {'text': '1789,37,47,1889', 'at': 1202161486},
]
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 295
PART_TWO_RESULT = 1068781

# ======================================================================
#                                                              TestBuses
# ======================================================================


class TestBuses(unittest.TestCase):  # pylint: disable=R0904
    "Test Buses object"

    def test_empty_init(self):
        "Test the default Buses creation"

        # 1. Create default Buses object
        myobj = buses.Buses()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.earliest, 0)
        self.assertEqual(len(myobj.buses), 0)

    def test_text_init(self):
        "Test the Buses object creation from text"

        # 1. Create Buses object from text
        myobj = buses.Buses(text=aoc_13.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 2)
        self.assertEqual(myobj.earliest, 939)
        self.assertEqual(len(myobj.buses), 5)

    def test_part_one(self):
        "Test part one example of Buses object"

        # 1. Create Buses object from text
        myobj = buses.Buses(text=aoc_13.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two_examples(self):
        "Test part two examples of Buses object"

        # 1. Loop for all of the examples
        for example in EXAMPLES:

            # 2. Create Buses object from text
            myobj = buses.Buses(part2=True, text=['999', example['text']])

            # 2. Check the part two result
            self.assertEqual(myobj.part_two(verbose=False), example['at'])

    def test_part_two(self):
        "Test part two example of Buses object"

        # 1. Create Buses object from text
        myobj = buses.Buses(part2=True, text=aoc_13.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ b u s e s . p y                   end
# ======================================================================
