# ======================================================================
# Chronal Classification
#   Advent of Code 2018 Day 16 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                 t e s t _ o b s e r v a t i o n s . p y
# ======================================================================
"Tester for Advent of Code 2018 day 16, Chronal Classification"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_16
import observations

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT_SINGLE = """
Before: [3, 2, 1, 1]
9 2 1 2
After:  [3, 2, 2, 1]"""

EXAMPLE_TEXT_MULTIPLE = """
Before: [3, 2, 1, 1]
9 2 1 2
After:  [3, 2, 2, 1]

Before: [2, 0, 0, 1]
15 3 1 3
After:  [2, 0, 0, 1]

Before: [3, 2, 3, 3]
4 3 3 0
After:  [3, 2, 3, 3]


"""

# ======================================================================
#                                                        TestObservation
# ======================================================================


class TestObservation(unittest.TestCase):  # pylint: disable=R0904
    "Test Single Observation object"

    def test_empty_init(self):
        "Test the default Observation creation"

        # 1. Create default Device object
        myobj = observations.Observation()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.before), 0)
        self.assertEqual(len(myobj.instruction), 0)
        self.assertEqual(len(myobj.after), 0)

    def test_text_init(self):
        "Test the Device object creation from text"

        # 1. Create Device object from text
        myobj = observations.Observation(text=aoc_16.from_text(EXAMPLE_TEXT_SINGLE))

        # 2. Make sure it has the expected values
        self.assertEqual(len(myobj.text), 3)
        self.assertEqual(len(myobj.before), 4)
        self.assertEqual(len(myobj.instruction), 4)
        self.assertEqual(len(myobj.after), 4)
        self.assertEqual(myobj.before, [3, 2, 1, 1])
        self.assertEqual(myobj.instruction, [9, 2, 1, 2])
        self.assertEqual(myobj.after, [3, 2, 2, 1])

# ======================================================================
#                                                        TestObservation
# ======================================================================


class TestObservations(unittest.TestCase):  # pylint: disable=R0904
    "Test Multiple Observation object"

    def test_empty_init(self):
        "Test the default Observations creation"

        # 1. Create default Device object
        myobj = observations.Observations()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.data), 0)

    def test_text_init(self):
        "Test the Device object creation from text"

        # 1. Create Device object from text
        myobj = observations.Observations(text=aoc_16.from_text(EXAMPLE_TEXT_MULTIPLE))

        # 2. Make sure it has the expected values
        self.assertEqual(len(myobj.text), 14)
        self.assertEqual(len(myobj.data), 3)
        self.assertEqual(myobj.data[0].before, [3, 2, 1, 1])
        self.assertEqual(myobj.data[0].instruction, [9, 2, 1, 2])
        self.assertEqual(myobj.data[0].after, [3, 2, 2, 1])

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end            t e s t _ o b s e r v a t i o n s . p y             end
# ======================================================================

