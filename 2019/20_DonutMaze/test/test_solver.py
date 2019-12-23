# ======================================================================
# Donut Maze
#   Advent of Code 2019 Day 18 -- Eric Wastl -- https://adventofcode.com
#
# codeuter simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                     t e s t _ s o l v e r . p y
# ======================================================================
"Test donut maze solver Advent of Code 2019 day 18, Donut Maze"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import solver
import test_donut
from aoc_dm import from_text

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------


# ======================================================================
#                                                             TestSolver
# ======================================================================


class TestSolver(unittest.TestCase):  # pylint: disable=R0904
    """Test Asteroids object"""

    def test_empty_init(self):
        """Test default Solver object creation"""

        # 1. Create default Astroids object
        mysolver = solver.Solver()

        # 2. Make sure it has the default values
        self.assertEqual(mysolver.vault.text, None)
        self.assertEqual(mysolver.vault.origin, None)
        self.assertEqual(mysolver.vault.origins, None)
        self.assertEqual(len(mysolver.key_paths), 0)

        # 3. Check methods
        solution = mysolver.get_all_keys()
        self.assertEqual(solution[0], 0)
        self.assertEqual(solution[1], [solver.ORIGIN_KEY])

    def test_p1e0_solve(self):
        "Test Solver object creation with text of part 1 example 0"

        # 1. Create Intcode obhect with values
        mysolver = solver.Solver(text=from_text(test_vault.EXAMPLES[0]))

        # 2. Make sure it has the specified values
        self.assertEqual(mysolver.vault.rows, 3)
        self.assertEqual(mysolver.vault.cols, 9)
        self.assertEqual(len(mysolver.key_paths), 3)

        # 3. Check methods
        solution = mysolver.get_all_keys()
        self.assertEqual(solution[0], 8)
        self.assertEqual(solution[1], [solver.ORIGIN_KEY, 'a', 'b'])

    def test_p1e1_solve(self):
        "Test Solver object creation with text of part 1 example 1"

        # 1. Create Intcode obhect with values
        mysolver = solver.Solver(text=from_text(test_vault.EXAMPLES[1]))

        # 2. Make sure it has the specified values
        self.assertEqual(mysolver.vault.rows, 5)
        self.assertEqual(mysolver.vault.cols, 24)
        self.assertEqual(len(mysolver.key_paths), 7)

        # 3. Check methods
        solution = mysolver.get_all_keys()
        self.assertEqual(solution[0], 86)
        self.assertEqual(solution[1], [solver.ORIGIN_KEY, 'a', 'b', 'c', 'd', 'e', 'f'])

    def test_p1e2_init(self):
        "Test Solver object creation with text of part 1 example 2"

        # 1. Create Intcode obhect with values
        mysolver = solver.Solver(text=from_text(test_vault.EXAMPLES[2]))

        # 2. Make sure it has the specified values
        self.assertEqual(mysolver.vault.rows, 5)
        self.assertEqual(mysolver.vault.cols, 24)
        self.assertEqual(len(mysolver.key_paths), 8)

        # 3. Check methods
        solution = mysolver.get_all_keys()
        self.assertEqual(solution[0], 132)
        self.assertEqual(solution[1], [solver.ORIGIN_KEY, 'b', 'a', 'c', 'd', 'f', 'e', 'g'])

    def test_p1e3_init(self):
        "Test Solver object creation with text of part 1 example 3"

        # 1. Create Intcode obhect with values
        mysolver = solver.Solver(text=from_text(test_vault.EXAMPLES[3]))

        # 2. Make sure it has the specified values
        self.assertEqual(mysolver.vault.rows, 9)
        self.assertEqual(mysolver.vault.cols, 17)
        self.assertEqual(len(mysolver.key_paths), 17)

        # 3. Check methods
        solution = mysolver.get_all_keys()
        self.assertEqual(solution[0], 136)
        self.assertEqual(len(solution[1]), 17)

    def test_p1e4_init(self):
        "Test Solver object creation with text of part 1 example 4"

        # 1. Create Intcode obhect with values
        mysolver = solver.Solver(text=from_text(test_vault.EXAMPLES[4]))

        # 2. Make sure it has the specified values
        self.assertEqual(mysolver.vault.rows, 6)
        self.assertEqual(mysolver.vault.cols, 24)
        self.assertEqual(len(mysolver.key_paths), 10)

        # 3. Check methods
        solution = mysolver.get_all_keys()
        self.assertEqual(solution[0], 81)
        self.assertEqual(len(solution[1]), 10)

    def test_p2e0_solve(self):
        "Test Solver object creation with text of part 2 example 0"

        # 1. Create Intcode obhect with values
        mysolver = solver.Solver(text=from_text(test_vault.EXAMPLES_PART2[0]),
                                 part2=True)

        # 2. Make sure it has the specified values
        self.assertEqual(mysolver.vault.rows, 7)
        self.assertEqual(mysolver.vault.cols, 7)
        self.assertEqual(len(mysolver.key_paths), 8)

        # 3. Check methods
        solution = mysolver.get_all_keys()
        self.assertEqual(solution[0], 8)
        self.assertEqual(solution[1], [solver.ORIGIN_KEY, 'a', 'b', 'c', 'd'])

    def test_p2e1_solve(self):
        "Test Solver object creation with text of part 2 example 1"

        # 1. Create Intcode obhect with values
        mysolver = solver.Solver(text=from_text(test_vault.EXAMPLES_PART2[1]),
                                 part2=True)
        #print(mysolver.key_paths.keys())

        # 2. Make sure it has the specified values
        self.assertEqual(mysolver.vault.rows, 7)
        self.assertEqual(mysolver.vault.cols, 15)
        self.assertEqual(len(mysolver.key_paths), 8)

        # 3. Check methods
        solution = mysolver.get_all_keys()
        self.assertEqual(solution[0], 24)

    def test_p2e2_solve(self):
        "Test Solver object creation with text of part 2 example 2"

        # 1. Create Intcode obhect with values
        mysolver = solver.Solver(text=from_text(test_vault.EXAMPLES_PART2[2]),
                                 part2=True)
        #print(mysolver.key_paths.keys())

        # 2. Make sure it has the specified values
        self.assertEqual(mysolver.vault.rows, 7)
        self.assertEqual(mysolver.vault.cols, 13)
        self.assertEqual(len(mysolver.key_paths), 16)

        # 3. Check methods
        solution = mysolver.get_all_keys()
        self.assertEqual(solution[0], 32)

    def test_p2e3_solve(self):
        "Test Solver object creation with text of part 2 example 3"

        # 1. Create Intcode obhect with values
        mysolver = solver.Solver(text=from_text(test_vault.EXAMPLES_PART2[3]),
                                 part2=True)
        #print(mysolver.key_paths.keys())

        # 2. Make sure it has the specified values
        self.assertEqual(mysolver.vault.rows, 9)
        self.assertEqual(mysolver.vault.cols, 13)
        self.assertEqual(len(mysolver.key_paths), 19)

        # 3. Check methods
        solution = mysolver.get_all_keys()
        self.assertEqual(solution[0], 72)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                  t e s t _ s o l v e r . p y                   end
# ======================================================================
