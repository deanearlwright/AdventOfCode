# ======================================================================
# Sporifica Virus
#   Advent of Code 2017 Day 22 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ v i r u s . p y
# ======================================================================
"Test solver for Advent of Code 2017 day 22, Sporifica Virus"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_22
import virus

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
..#
#..
...
"""

V = virus.VIRUS_CHAR
GRID_ZERO = {(1, -1): V, (-1, 0): V}
GRID_ONE = {(1, -1): V, (-1, 0): V, (0, 0): V}
GRID_TWO = {(1, -1): V, (0, 0): V}
GRID_SIX = {(1, -1): V, (0, 0): V, (-1, -1): V, (-2, -1): V, (-2, 0): V, (-1, 0): V}
GRID_SEVEN = {(1, -1): V, (0, 0): V, (-2, -1): V, (-2, 0): V, (-1, 0): V}

W = virus.WEAK_CHAR
F = virus.FLAG_CHAR
C = virus.CLEAN_CHAR
GRID2_ONE = {(1, -1): V, (-1, 0): V, (0, 0): W}
GRID2_TWO = {(1, -1): V, (-1, 0): F, (0, 0): W}
GRID2_THREE = {(1, -1): V, (-1, 0): F, (0, 0): W, (-1, -1): W}
GRID2_FIVE = {(1, -1): V, (-1, 0): F, (0, 0): W, (-1, -1): W, (-2, -1): W, (-2, 0): W}
GRID2_SIX = {(1, -1): V, (-1, 0): C, (0, 0): W, (-1, -1): W, (-2, -1): W, (-2, 0): W}
GRID2_SEVEN = {(1, -1): V, (-1, 0): C, (0, 0): W, (-1, -1): W, (-2, -1): W, (-2, 0): V}


PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 5587
PART_TWO_RESULT = 2511944

# ======================================================================
#                                                              TestVirus
# ======================================================================


class TestVirus(unittest.TestCase):  # pylint: disable=R0904
    "Test Virus object"

    def test_empty_init(self):
        "Test the default Virus creation"

        # 1. Create default Virus object
        myobj = virus.Virus()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.grid, {})
        self.assertEqual(myobj.activities, 0)
        self.assertEqual(myobj.infections, 0)
        self.assertEqual(myobj.virus_loc, virus.INITIAL_VIRUS_LOC)
        self.assertEqual(myobj.virus_dir, virus.INITIAL_VIRUS_DIR)

    def test_text_init(self):
        "Test the Virus object creation from text"

        # 1. Create Virus object from text
        myobj = virus.Virus(text=aoc_22.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, ['..#', '#..', '...'])
        self.assertEqual(myobj.grid, GRID_ZERO)
        self.assertEqual(myobj.activities, 0)
        self.assertEqual(myobj.infections, 0)
        self.assertEqual(myobj.virus_loc, virus.INITIAL_VIRUS_LOC)
        self.assertEqual(myobj.virus_dir, virus.INITIAL_VIRUS_DIR)

        # 3. Let the clock run a few ticks
        myobj.burst()
        self.assertEqual(myobj.activities, 1)
        self.assertEqual(myobj.infections, 1)
        self.assertEqual(myobj.virus_loc, (-1, 0))
        self.assertEqual(myobj.virus_dir, virus.DIR_W)
        self.assertEqual(myobj.grid, GRID_ONE)
        myobj.burst()
        self.assertEqual(myobj.activities, 2)
        self.assertEqual(myobj.infections, 1)
        self.assertEqual(myobj.virus_loc, (-1, -1))
        self.assertEqual(myobj.virus_dir, virus.DIR_N)
        self.assertEqual(myobj.grid, GRID_TWO)
        myobj.burst()
        myobj.burst()
        myobj.burst()
        myobj.burst()
        self.assertEqual(myobj.activities, 6)
        self.assertEqual(myobj.infections, 5)
        self.assertEqual(myobj.virus_loc, (-1, -1))
        self.assertEqual(myobj.virus_dir, virus.DIR_N)
        self.assertEqual(myobj.grid, GRID_SIX)
        myobj.burst()
        self.assertEqual(myobj.activities, 7)
        self.assertEqual(myobj.infections, 5)
        self.assertEqual(myobj.virus_loc, (0, -1))
        self.assertEqual(myobj.virus_dir, virus.DIR_E)
        self.assertEqual(myobj.grid, GRID_SEVEN)

        # 4. And now the big one
        while myobj.activities < 70:
            myobj.burst()
        self.assertEqual(myobj.activities, 70)
        self.assertEqual(myobj.infections, 41)
        self.assertEqual(myobj.virus_loc, (1, -1))
        self.assertEqual(myobj.virus_dir, virus.DIR_N)
        self.assertEqual(len(myobj.grid), 14)

    def test_text_init_two(self):
        "Test the Virus object creation from text for part two"

        # 1. Create Virus object from text
        myobj = virus.Virus(text=aoc_22.from_text(EXAMPLE_TEXT),
                            part2=True)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, True)
        self.assertEqual(myobj.text, ['..#', '#..', '...'])
        self.assertEqual(myobj.grid, GRID_ZERO)
        self.assertEqual(myobj.activities, 0)
        self.assertEqual(myobj.infections, 0)
        self.assertEqual(myobj.virus_loc, virus.INITIAL_VIRUS_LOC)
        self.assertEqual(myobj.virus_dir, virus.INITIAL_VIRUS_DIR)

        # 3. Let the clock run a few ticks
        myobj.burst_two()
        self.assertEqual(myobj.activities, 1)
        self.assertEqual(myobj.infections, 0)
        self.assertEqual(myobj.virus_loc, (-1, 0))
        self.assertEqual(myobj.virus_dir, virus.DIR_W)
        self.assertEqual(myobj.grid, GRID2_ONE)
        myobj.burst_two()
        self.assertEqual(myobj.activities, 2)
        self.assertEqual(myobj.infections, 0)
        self.assertEqual(myobj.virus_loc, (-1, -1))
        self.assertEqual(myobj.virus_dir, virus.DIR_N)
        self.assertEqual(myobj.grid, GRID2_TWO)
        myobj.burst_two()
        self.assertEqual(myobj.activities, 3)
        self.assertEqual(myobj.infections, 0)
        self.assertEqual(myobj.virus_loc, (-2, -1))
        self.assertEqual(myobj.virus_dir, virus.DIR_W)
        self.assertEqual(myobj.grid, GRID2_THREE)
        myobj.burst_two()
        myobj.burst_two()
        self.assertEqual(myobj.activities, 5)
        self.assertEqual(myobj.infections, 0)
        self.assertEqual(myobj.virus_loc, (-1, 0))
        self.assertEqual(myobj.virus_dir, virus.DIR_E)
        self.assertEqual(myobj.grid, GRID2_FIVE)
        myobj.burst_two()
        self.assertEqual(myobj.activities, 6)
        self.assertEqual(myobj.infections, 0)
        self.assertEqual(myobj.virus_loc, (-2, 0))
        self.assertEqual(myobj.virus_dir, virus.DIR_W)
        self.assertEqual(myobj.grid, GRID2_SIX)
        myobj.burst_two()
        self.assertEqual(myobj.activities, 7)
        self.assertEqual(myobj.infections, 1)
        self.assertEqual(myobj.virus_loc, (-3, 0))
        self.assertEqual(myobj.virus_dir, virus.DIR_W)
        self.assertEqual(myobj.grid, GRID2_SEVEN)

        # 4. And now the big one
        while myobj.activities < 100:
            myobj.burst_two()
        self.assertEqual(myobj.activities, 100)
        self.assertEqual(myobj.infections, 26)


    def test_part_one(self):
        "Test part one example of Virus object"

        # 1. Create Spinlock object from text
        myobj = virus.Virus(text=aoc_22.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)


    def test_part_two(self):
        "Test part two example of Virus object"

        # 1. Create Spinlock object from text
        myobj = virus.Virus(part2=True, text=aoc_22.from_text(PART_TWO_TEXT))

        # 2. Check the part two
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ v i r u s . p y                   end
# ======================================================================
