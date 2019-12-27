# ======================================================================
# Donut Maze
#   Advent of Code 2019 Day 20 -- Eric Wastl -- https://adventofcode.com
#
# codeuter simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                     t e s t _ s o l v e r . p y
# ======================================================================
"Test donut maze solver Advent of Code 2019 day 20, Donut Maze"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import solver
import donut
import graph
import test_donut
from aoc_dm import from_text

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------


# ======================================================================
#                                                             TestSolver
# ======================================================================


class TestSolver(unittest.TestCase):  # pylint: disable=R0904
    """Test Solver for the Donut Maze object"""

    def test_empty_init(self):
        """Test default Solver object creation"""

        # 1. Create default Donut Maze Solver object object
        mysolver = solver.Solver()

        # 2. Make sure it has the default values
        self.assertNotEqual(mysolver.donut, None)
        self.assertEqual(mysolver.part2, False, None)
        self.assertEqual(len(mysolver.portal_paths), 0)
        self.assertEqual(len(mysolver.graph.edges), 0)
        self.assertEqual(mysolver.donut.text, None)
        self.assertEqual(mysolver.donut.rows, 0)
        self.assertEqual(mysolver.donut.cols, 0)
        self.assertEqual(mysolver.donut.portals, {})
        self.assertEqual(mysolver.donut.start, donut.START)
        self.assertEqual(mysolver.donut.finish, donut.FINISH)
        self.assertEqual(mysolver.donut.portals_at, {})
        self.assertEqual(mysolver.donut.part2, False)
        self.assertEqual(mysolver.donut.locs, {})

    def test_methods(self):
        "Test exploration between portal locations and other methods"

        # 1. Create an solver without a donut and then slap on a donut
        mysolver = solver.Solver()
        mysolver.donut = donut.Donut(text=from_text(test_donut.EXAMPLES[0]))

        # 2. Explore from all portal ends
        self.assertEqual(mysolver.explore_from((2, 8)), {(6, 10): 6})   # BC -> DE
        self.assertEqual(mysolver.explore_from((2, 13)), {(2, 15): 4})  # DE -> FG
        self.assertEqual(mysolver.explore_from((2, 15)), {(2, 13): 4})  # FG -> DE
        self.assertEqual(mysolver.explore_from((6, 10)), {(2, 8): 6})   # DE -> BC
        self.assertEqual(mysolver.explore_from((9, 2)), {(9, 6): 4,     # AA -> BC
                                                         (11, 12): 30,   # AA -> FG
                                                         (13, 16): 26})  # AA -> ZZ
        self.assertEqual(mysolver.explore_from((11, 12)), {(13, 16): 6,  # FG -> ZZ
                                                           (9, 2): 30,   # FG -> AA
                                                           (9, 6): 32})  # FG -> BC
        self.assertEqual(mysolver.explore_from((13, 16)), {(11, 12): 6,  # ZZ -> FG
                                                           (9, 2): 26,   # ZZ -> AA
                                                           (9, 6): 28})  # ZZ -> BC

        # 3. Compute and check direct portal paths
        mysolver.portal_paths = mysolver.get_direct_paths_between_portals()
        self.assertEqual(len(mysolver.portal_paths), 5)
        self.assertEqual(sorted(mysolver.portal_paths.keys()), ['AA', 'BC', 'DE', 'FG', 'ZZ'])
        self.assertEqual(len(mysolver.portal_paths['AA']), 3)
        self.assertEqual(sorted([path.steps for path in mysolver.portal_paths['AA']]), [4, 26, 30])
        self.assertEqual(sorted([path.steps for path in mysolver.portal_paths['BC']]), [1, 1, 4, 6, 28, 32])
        self.assertEqual(sorted([path.steps for path in mysolver.portal_paths['DE']]), [1, 1, 4, 6])
        self.assertEqual(sorted([path.steps for path in mysolver.portal_paths['FG']]), [1, 1, 4, 6, 30, 32])
        self.assertEqual(sorted([path.steps for path in mysolver.portal_paths['ZZ']]), [6, 26, 28])

        # 4. Compute and check graph
        mysolver.graph = mysolver.portal_paths_to_graph()
        self.assertEqual(len(mysolver.graph.edges), 22)

        # 5. Test solving the graph
        mysolver.solve_donut_maze()
        self.assertEqual(len(mysolver.path), 8)
        self.assertEqual(mysolver.cost, 23)

    def test_p1e0_solve(self):
        "Test Solver object creation with text of part 1 example 0"

        # 1. Create Donut Maze solver object from part one example 0
        mysolver = solver.Solver(text=from_text(test_donut.EXAMPLES[0]), verbose=True)  # verbose=True

        # 2. Make sure it has the specified values
        self.assertEqual(mysolver.donut.rows, 19)
        self.assertEqual(mysolver.donut.cols, 19)
        self.assertEqual(len(mysolver.portal_paths), 5)
        self.assertEqual(len(mysolver.graph.edges), 22)

        # 3. Solve the donut maze
        mysolver.solve_donut_maze()
        self.assertEqual(len(mysolver.path), 8)
        self.assertEqual(mysolver.cost, 23)

    def test_p1e1_solve(self):
        "Test Solver object creation with text of part 1 example 1"

        # 1. Test Solver object creation with text of part 1 example 1
        mysolver = solver.Solver(text=from_text(test_donut.EXAMPLES[1]))

        # 2. Make sure it has the specified values
        self.assertEqual(mysolver.donut.rows, 37)
        self.assertEqual(mysolver.donut.cols, 35)
        self.assertEqual(len(mysolver.portal_paths), 12)
        self.assertEqual(len(mysolver.graph.edges), 56)

        # 3. Solve the donut maze
        mysolver.solve_donut_maze()
        self.assertEqual(len(mysolver.path), 10)
        self.assertEqual(mysolver.cost, 58)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                  t e s t _ s o l v e r . p y                   end
# ======================================================================
