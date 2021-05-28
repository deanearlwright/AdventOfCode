# ======================================================================
# No Time for a Taxicab
#   Advent of Code 2016 Day 01 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ t a x i c a b . p y
# ======================================================================
"Test solver for Advent of Code 2016 day 01, No Time for a Taxicab"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_01
import taxicab

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
R2, L3"""

EXAMPLE_TWO = """
R2, R2, R2
"""

EXAMPLE_THREE = """
R5, L5, R5, R3
"""

EXAMPLE_FOUR = """
R8, R4, R4, R8
"""

PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_FOUR

PART_ONE_RESULT = 5
PART_TWO_RESULT = 4

# ======================================================================
#                                                              TestTaxicab
# ======================================================================


class TestTaxicab(unittest.TestCase):  # pylint: disable=R0904
    "Test Taxicab object"

    def test_empty_init(self):
        "Test the default Taxicab creation"

        # 1. Create default Taxicab object
        myobj = taxicab.Taxicab()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.instructions, [])
        self.assertEqual(myobj.location, [0, 0])
        self.assertEqual(myobj.facing, "N")

        # 3. Check methods
        self.assertEqual(myobj.from_start(), 0)
        myobj.follow_instructions()
        self.assertEqual(myobj.from_start(), 0)

    def test_text_init(self):
        "Test the Taxicab object creation from text"

        # 1. Create Taxicab object from text
        myobj = taxicab.Taxicab(text=aoc_01.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 1)
        self.assertEqual(myobj.instructions, ['R2', 'L3'])
        self.assertEqual(myobj.location, [0, 0])
        self.assertEqual(myobj.facing, "N")

        # 3. Check methods
        self.assertEqual(myobj.from_start(), 0)
        myobj.follow_instructions()
        self.assertEqual(myobj.location, [2, 3])
        self.assertEqual(myobj.facing, "N")
        self.assertEqual(myobj.from_start(), 5)

        # 4. Example 2
        myobj = taxicab.Taxicab(text=aoc_01.from_text(EXAMPLE_TWO))
        myobj.follow_instructions()
        self.assertEqual(myobj.from_start(), 2)
        self.assertEqual(myobj.location, [0, -2])

        # 5. Example 3
        myobj = taxicab.Taxicab(text=aoc_01.from_text(EXAMPLE_THREE))
        myobj.follow_instructions()
        self.assertEqual(myobj.from_start(), 12)

        # 6. Example 4
        myobj = taxicab.Taxicab(text=aoc_01.from_text(EXAMPLE_FOUR))
        myobj.find_hq()
        self.assertEqual(myobj.from_start(), 4)

    def test_part_one(self):
        "Test part one example of Taxicab object"

        # 1. Create Taxicab object from text
        myobj = taxicab.Taxicab(text=aoc_01.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Taxicab object"

        # 1. Create Taxicab object from text
        myobj = taxicab.Taxicab(part2=True, text=aoc_01.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ t a x i c a b . p y                end
# ======================================================================
