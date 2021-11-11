# ======================================================================
# It Hangs in the Balance
#   Advent of Code 2015 Day 24 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ p a c k a g e s . p y
# ======================================================================
"Test solver for Advent of Code 2015 day 24, It Hangs in the Balance"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_24
import packages

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
1
2
3
4
5
7
8
9
10
11
"""

PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 99
PART_TWO_RESULT = 44

# ======================================================================
#                                                           TestPackages
# ======================================================================


class TestPackages(unittest.TestCase):  # pylint: disable=R0904
    "Test Packages object"

    def test_empty_init(self):
        "Test the default Packages creation"

        # 1. Create default Packages object
        myobj = packages.Packages()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.weights), 0)
        self.assertEqual(myobj.compartments, 3)
        self.assertEqual(myobj.balance, 0)

        # 3. Test methods
        self.assertEqual(myobj.quantum_entanglement([7, 5, 4, 3, 1]), 420)

    def test_text_init(self):
        "Test the Packages object creation from text"

        # 1. Create Packages object from text
        myobj = packages.Packages(text=aoc_24.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 10)
        self.assertEqual(len(myobj.weights), 10)
        self.assertEqual(myobj.compartments, 3)
        self.assertEqual(myobj.balance, 20)

        # 3. Test methods
        self.assertEqual(myobj.min_max_helper(myobj.weights, myobj.balance), 6)
        myobj.weights.reverse()
        self.assertEqual(myobj.min_max_helper(myobj.weights, myobj.balance), 2)
        self.assertEqual(myobj.find_min_max_packages(myobj.weights, myobj.balance), (2, 6))

        self.assertEqual(len(myobj.get_weighted(myobj.weights, myobj.balance, 2)), 1)
        self.assertEqual(len(myobj.get_weighted(myobj.weights, myobj.balance, 3)), 9)
        self.assertEqual(len(myobj.get_weighted(myobj.weights, myobj.balance, 4)), 11)
        self.assertEqual(len(myobj.get_weighted(myobj.weights, myobj.balance, 5)), 4)

        self.assertEqual(myobj.is_remainder_balanced(myobj.weights, [9, 11], myobj.balance, 2),
                         True)
        self.assertEqual(myobj.is_remainder_balanced(myobj.weights, [1, 8, 11], myobj.balance, 2),
                         True)
        self.assertEqual(myobj.is_remainder_balanced(myobj.weights, [1, 9, 10], myobj.balance, 2),
                         True)

        self.assertEqual(myobj.find_best_legroom(), 99)

    def test_part_one(self):
        "Test part one example of Packages object"

        # 1. Create Packages object from text
        myobj = packages.Packages(text=aoc_24.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Packages object"

        # 1. Create Packages object from text
        myobj = packages.Packages(part2=True, text=aoc_24.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ p a c k a g e s . p y                end
# ======================================================================
