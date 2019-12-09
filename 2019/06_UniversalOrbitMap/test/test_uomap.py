# ======================================================================
# Universal Orbit Map
#   Advent of Code 2019 Day 06 -- Eric Wastl -- https://adventofcode.com
#
# codeuter simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                        t e s t _ u a m a p . p y
# ======================================================================
"Test orbit map for Advent of Code 2019 day 6, Universal Orbit Map"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import uomap

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
PAIRS = [('COM', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'),
         ('E', 'F'), ('B', 'G'), ('G', 'H'), ('D', 'I'),
         ('E', 'J'), ('J', 'K'), ('K', 'L')]

TEXT = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L""".split('\n')

PART2 = ['K)YOU', 'I)SAN']

# ======================================================================
#                                                              TestUOMap
# ======================================================================


class TestUOMap(unittest.TestCase):  # pylint: disable=R0904
    """Test TestUOMap object"""

    def test_empty_init(self):
        """Test default UOMap object creation"""

        # 1. Create default UOMap object
        mymap = uomap.UOMap()

        # 2. Check methods
        self.assertEqual(len(mymap.nodes()), 0)
        self.assertEqual(mymap.direct_links(), 0)
        self.assertEqual(mymap.total_orbits(), 0)

    def test_pairs_init(self):
        """Test UOMap object creation with text"""

    #         G - H       J - K - L
    #        /           /
    # COM - B - C - D - E - F
    #                \
    #                 I

        # 1. Create Wire obhect with values
        mymap = uomap.UOMap(pairs=PAIRS)

        # 2. Check methods
        self.assertEqual(len(mymap.nodes()), 12)
        self.assertTrue(uomap.COM in mymap.dag)
        self.assertTrue('A' not in mymap.nodes())
        self.assertTrue('B' in mymap.nodes())
        self.assertTrue('C' in mymap.nodes())
        self.assertTrue('D' in mymap.nodes())
        self.assertEqual(mymap.direct_links(), 11)
        self.assertEqual(mymap.orbits('B'), 1)
        self.assertEqual(mymap.orbits('C'), 2)
        self.assertEqual(mymap.orbits('D'), 3)
        self.assertEqual(mymap.orbits('E'), 4)
        self.assertEqual(mymap.orbits('F'), 5)
        self.assertEqual(mymap.orbits('G'), 2)
        self.assertEqual(mymap.orbits('H'), 3)
        self.assertEqual(mymap.orbits('I'), 4)
        self.assertEqual(mymap.orbits('J'), 5)
        self.assertEqual(mymap.orbits('K'), 6)
        self.assertEqual(mymap.orbits('L'), 7)
        self.assertEqual(mymap.total_orbits(), 42)

    def test_text_init(self):
        """Test UOMap object creation with text"""

        #         G - H       J - K - L
        #        /           /
        # COM - B - C - D - E - F
        #                \
        #                 I

        # 1. Create Wire obhect with values
        mymap = uomap.UOMap(text=TEXT)

        # 2. Check methods
        self.assertEqual(len(mymap.nodes()), 12)
        self.assertTrue(uomap.COM in mymap.dag)
        self.assertTrue('A' not in mymap.nodes())
        self.assertTrue('B' in mymap.nodes())
        self.assertTrue('C' in mymap.nodes())
        self.assertTrue('D' in mymap.nodes())
        self.assertEqual(mymap.direct_links(), 11)
        self.assertEqual(mymap.orbits('B'), 1)
        self.assertEqual(mymap.orbits('C'), 2)
        self.assertEqual(mymap.orbits('D'), 3)
        self.assertEqual(mymap.orbits('E'), 4)
        self.assertEqual(mymap.orbits('F'), 5)
        self.assertEqual(mymap.orbits('G'), 2)
        self.assertEqual(mymap.orbits('H'), 3)
        self.assertEqual(mymap.orbits('I'), 4)
        self.assertEqual(mymap.orbits('J'), 5)
        self.assertEqual(mymap.orbits('K'), 6)
        self.assertEqual(mymap.orbits('L'), 7)
        self.assertEqual(mymap.total_orbits(), 42)

    def test_part_two(self):
        """Test part2 minimum_transfers"""

        #                           YOU
        #                          /
        #         G - H       J - K - L
        #        /           /
        # COM - B - C - D - E - F
        #                \
        #                 I - SAN

        # 1. Create Wire obhect with values
        mymap = uomap.UOMap(text=TEXT + PART2)

        # 2. Check methods
        self.assertEqual(len(mymap.nodes()), 14)
        self.assertTrue('YOU' in mymap.nodes())
        self.assertTrue('SAN' in mymap.nodes())
        self.assertEqual(mymap.find_shortest_path(uomap.COM, 'I'),
                         ['COM', 'B', 'C', 'D', 'I'])
        self.assertEqual(mymap.find_shortest_path(uomap.COM, 'K'),
                         ['COM', 'B', 'C', 'D', 'E', 'J', 'K'])
        self.assertEqual(mymap.minimum_transfers('I', 'K'), 4)
        self.assertEqual(mymap.minimum_transfers(uomap.YOU, uomap.SANTA), 4)
        self.assertEqual(mymap.minimum_transfers(uomap.SANTA, uomap.YOU), 4)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ u o m a p . p y                   end
# ======================================================================
