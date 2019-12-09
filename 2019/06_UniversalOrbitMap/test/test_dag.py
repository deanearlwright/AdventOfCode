# ======================================================================
# Universal Orbit Map
#   Advent of Code 2019 Day 06 -- Eric Wastl -- https://adventofcode.com
#
# codeuter simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                          t e s t _ d a g . p y
# ======================================================================
"Test DAG for Advent of Code 2019 day 5, Universal Orbit Map"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import dag

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                            TestUtility
# ======================================================================


class TestDAG(unittest.TestCase):  # pylint: disable=R0904
    """Test directed acylcic grapg"""

    def test_empty_init(self):
        """Test default dag object creation"""

        # 1. Create default dag object
        mydag = dag.DAG()

        # 2. Make sure it has the default values
        self.assertEqual(len(mydag.dag), 0)

        # 3. Check methods
        self.assertEqual(len(mydag.nodes()), 0)
        self.assertEqual(mydag.direct_links(), 0)
        self.assertEqual(mydag.find_path('A', 'B'), None)

    def test_value_init(self):
        """Test dag object creation with values"""

        # 1. Create default dag object
        mydag = dag.DAG(pairs=[('A', 'B'), ('A', 'C'),
                               ('B', 'C'), ('B', 'D'),
                               ('C', 'D'), ('D', 'C'),
                               ('E', 'F'), ('F', 'C')])

        # 2. Make sure it has the default values
        self.assertEqual(len(mydag.dag), 6)

        # 3. Check methods
        self.assertEqual(len(mydag.nodes()), 6)
        self.assertEqual(mydag.direct_links(), 8)
        self.assertEqual(mydag.find_path('A', 'A'), ['A'])
        self.assertEqual(mydag.find_path('A', 'B'), ['A', 'B'])
        self.assertEqual(mydag.find_path('A', 'D'),
                         ['A', 'B', 'C', 'D'])
        self.assertEqual(mydag.find_shortest_path('A', 'D'),
                         ['A', 'B', 'D'])

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                     t e s t _ d a g . p y                      end
# ======================================================================
