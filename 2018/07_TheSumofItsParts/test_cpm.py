# ======================================================================
# The Sum of Its Parts
#   Advent of Code 2018 Day 07 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ c p m . p y
# ======================================================================
"Test solver for Advent of Code 2018 day 07, The Sum of Its Parts"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_07
import cpm

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = "CABDFE"
PART_TWO_RESULT = 15

# ======================================================================
#                                                                TestCpm
# ======================================================================


class TestCpm(unittest.TestCase):  # pylint: disable=R0904
    "Test Cpm object"

    def test_empty_init(self):
        "Test the default Cpm creation"

        # 1. Create default Cpm object
        myobj = cpm.Cpm()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.letters), 0)
        self.assertEqual(len(myobj.steps), 0)
        self.assertEqual(len(myobj.completed), 0)
        self.assertEqual(len(myobj.ordered), 0)

    def test_text_init(self):
        "Test the Cpm object creation from text"

        # 1. Create Cpm object from text
        myobj = cpm.Cpm(text=aoc_07.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 7)
        self.assertEqual(len(myobj.letters), 6)
        self.assertEqual(len(myobj.steps), 5)
        self.assertEqual(len(myobj.completed), 0)
        self.assertEqual(len(myobj.ordered), 0)
        self.assertTrue('A' in myobj.steps)
        self.assertEqual(myobj.steps['A'].letter, 'A')
        self.assertEqual(myobj.steps['A'].before, set('C'))
        self.assertTrue('E' in myobj.steps)
        self.assertEqual(myobj.steps['E'].letter, 'E')
        self.assertEqual(myobj.steps['E'].before, set(['B', 'D', 'F']))
        self.assertTrue('C' not in myobj.steps)

        # 3. Get the starting letter
        self.assertEqual(myobj.get_start(), set(['C']))
        self.assertEqual(myobj.next_step(), set(['C']))

        # 4. Walk through the steps
        myobj.complete('C')
        self.assertEqual(myobj.next_step(), set(['A', 'F']))
        myobj.complete('A')
        self.assertEqual(myobj.next_step(), set(['B', 'D', 'F']))
        myobj.complete('B')
        self.assertEqual(myobj.next_step(), set(['D', 'F']))
        myobj.complete('D')
        self.assertEqual(myobj.next_step(), set(['F']))
        myobj.complete('F')
        self.assertEqual(myobj.next_step(), set(['E']))
        myobj.complete('E')
        self.assertEqual(myobj.ordered, ['C', 'A', 'B', 'D', 'F', 'E'])


    def test_part_one(self):
        "Test part one example of Cpm object"

        # 1. Create Cpm object from text
        myobj = cpm.Cpm(text=aoc_07.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)


    def test_part_two(self):
        "Test part two example of Cpm object"

        # 1. Create Cpm object from text
        myobj = cpm.Cpm(part2=True, text=aoc_07.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(number=2, seconds=0, verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      t e s t _ c p m . p y                     end
# ======================================================================
