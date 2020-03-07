# ======================================================================
# The Halting Problem
#   Advent of Code 2017 Day 25 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                     t e s t _ t u r i n g . p y
# ======================================================================
"Test solver for Advent of Code 2017 day 25, The Halting Problem"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_25
import turing

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
Begin in state A.
Perform a diagnostic checksum after 6 steps.

In state A:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state B.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state B.

In state B:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state A.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state A.
    """
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 3
PART_TWO_RESULT = None

# ======================================================================
#                                                             TestTuring
# ======================================================================


class TestTuring(unittest.TestCase):  # pylint: disable=R0904
    "Test Turing object"

    def test_empty_init(self):
        "Test the default Turing creation"

        # 1. Create default Turing object
        myobj = turing.Turing()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.tape), 0)
        self.assertEqual(myobj.position, 0)
        self.assertEqual(myobj.state, None)
        self.assertEqual(myobj.steps, 0)
        self.assertEqual(len(myobj.rules), 0)

        # 3. Check methods
        self.assertEqual(myobj.ones(), 0)

    def test_text_init(self):
        "Test the Turing object creation from text"

        # 1. Create Turing object from text
        myobj = turing.Turing(text=aoc_25.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 20)
        self.assertEqual(len(myobj.tape), 0)
        self.assertEqual(myobj.position, 0)
        self.assertEqual(myobj.state, 'A')
        self.assertEqual(myobj.steps, 6)
        self.assertEqual(len(myobj.rules), 2)

        # 3. Check the rules
        self.assertTrue('A' in myobj.rules)
        self.assertTrue('B' in myobj.rules)
        self.assertEqual(len(myobj.rules['A']), 2)
        self.assertEqual(len(myobj.rules['B']), 2)
        self.assertEqual(myobj.rules['A'][0],
                         turing.Rule('A', 0, 1, turing.RIGHT, 'B'))
        self.assertEqual(myobj.rules['A'][1],
                         turing.Rule('A', 1, 0, turing.LEFT, 'B'))
        self.assertEqual(myobj.rules['B'][0],
                         turing.Rule('B', 0, 1, turing.LEFT, 'A'))
        self.assertEqual(myobj.rules['B'][1],
                         turing.Rule('B', 1, 1, turing.RIGHT, 'A'))

        # 3. Check the step and ones methods
        self.assertEqual(myobj.position, 0)
        self.assertEqual(myobj.state, 'A')
        self.assertEqual(myobj.ones(), 0)
        myobj.step()
        self.assertEqual(myobj.position, 1)
        self.assertEqual(myobj.state, 'B')
        self.assertEqual(myobj.ones(), 1)
        myobj.step()
        self.assertEqual(myobj.position, 0)
        self.assertEqual(myobj.state, 'A')
        self.assertEqual(myobj.ones(), 2)
        myobj.step()
        self.assertEqual(myobj.position, -1)
        self.assertEqual(myobj.state, 'B')
        self.assertEqual(myobj.ones(), 1)
        myobj.step()
        self.assertEqual(myobj.position, -2)
        self.assertEqual(myobj.state, 'A')
        self.assertEqual(myobj.ones(), 2)
        myobj.step()
        self.assertEqual(myobj.position, -1)
        self.assertEqual(myobj.state, 'B')
        self.assertEqual(myobj.ones(), 3)
        myobj.step()
        self.assertEqual(myobj.position, 0)
        self.assertEqual(myobj.state, 'A')
        self.assertEqual(myobj.ones(), 3)

    def test_part_one(self):
        "Test part one example of Turing object"

        # 1. Create Turing object from text
        myobj = turing.Turing(text=aoc_25.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Turing object"

        # 1. Create Turing object from text
        myobj = turing.Turing(part2=True, text=aoc_25.from_text(PART_TWO_TEXT))

        # 2. Check the part two
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ t u r i n g . p y                  end
# ======================================================================
