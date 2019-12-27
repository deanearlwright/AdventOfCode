# ======================================================================
# Donut Maze
#   Advent of Code 2019 Day 20 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ d o n u t . p y
# ======================================================================
"Test donut maze for Advent of Code 2019 day 20, Donut Maze"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

from aoc_dm import from_text
import donut

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLES = ["""
! 8 labels, 23 steps
         A
         A
  #######.#########
  #######.........#
  #######.#######.#
  #######.#######.#
  #######.#######.#
  #####  B    ###.#
BC...##  C    ###.#
  ##.##       ###.#
  ##...DE  F  ###.#
  #####    G  ###.#
  #########.#####.#
DE..#######...###.#
  #.#########.###.#
FG..#########.....#
  ###########.#####
             Z
             Z       """, """
! 22 labels, 58 steps

                   A
                   A
  #################.#############
  #.#...#...................#.#.#
  #.#.#.###.###.###.#########.#.#
  #.#.#.......#...#.....#.#.#...#
  #.#########.###.#####.#.#.###.#
  #.............#.#.....#.......#
  ###.###########.###.#####.#.#.#
  #.....#        A   C    #.#.#.#
  #######        S   P    #####.#
  #.#...#                 #......VT
  #.#.#.#                 #.#####
  #...#.#               YN....#.#
  #.###.#                 #####.#
DI....#.#                 #.....#
  #####.#                 #.###.#
ZZ......#               QG....#..AS
  ###.###                 #######
JO..#.#.#                 #.....#
  #.#.#.#                 ###.#.#
  #...#..DI             BU....#..LF
  #####.#                 #.#####
YN......#               VT..#....QG
  #.###.#                 #.###.#
  #.#...#                 #.....#
  ###.###    J L     J    #.#.###
  #.....#    O F     P    #.#...#
  #.###.#####.#.#####.#####.###.#
  #...#.#.#...#.....#.....#.#...#
  #.#####.###.###.#.#.#########.#
  #...#.#.....#...#.#.#.#.....#.#
  #.###.#####.###.###.#.#.#######
  #.#.........#...#.............#
  #########.###.###.#############
           B   J   C
           U   P   P               """, """

! For part 1, takes 11 levels for 396 steps

             Z L X W       C
             Z P Q B       K
  ###########.#.#.#.#######.###############
  #...#.......#.#.......#.#.......#.#.#...#
  ###.#.#.#.#.#.#.#.###.#.#.#######.#.#.###
  #.#...#.#.#...#.#.#...#...#...#.#.......#
  #.###.#######.###.###.#.###.###.#.#######
  #...#.......#.#...#...#.............#...#
  #.#########.#######.#.#######.#######.###
  #...#.#    F       R I       Z    #.#.#.#
  #.###.#    D       E C       H    #.#.#.#
  #.#...#                           #...#.#
  #.###.#                           #.###.#
  #.#....OA                       WB..#.#..ZH
  #.###.#                           #.#.#.#
CJ......#                           #.....#
  #######                           #######
  #.#....CK                         #......IC
  #.###.#                           #.###.#
  #.....#                           #...#.#
  ###.###                           #.#.#.#
XF....#.#                         RF..#.#.#
  #####.#                           #######
  #......CJ                       NM..#...#
  ###.#.#                           #.###.#
RE....#.#                           #......RF
  ###.###        X   X       L      #.#.#.#
  #.....#        F   Q       P      #.#.#.#
  ###.###########.###.#######.#########.###
  #.....#...#.....#.......#...#.....#.#...#
  #####.#.###.#######.#######.###.###.#.#.#
  #.......#.......#.#.#.#.#...#...#...#.#.#
  #####.###.#####.#.#.#.#.###.###.#.###.###
  #.......#.....#.#...#...............#...#
  #############.#.#.###.###################
               A O F   N
               A A D   M """]

# ======================================================================
#                                                              TestDonut
# ======================================================================


class TestDonut(unittest.TestCase):  # pylint: disable=R0904
    """Test Donut object"""

    def test_empty_init(self):
        """Test default donut mazet object creation"""

        # 1. Create default Vault object
        mydonut = donut.Donut()

        # 2. Make sure it has the default values
        self.assertEqual(mydonut.text, None)
        self.assertEqual(mydonut.rows, 0)
        self.assertEqual(mydonut.cols, 0)
        self.assertEqual(mydonut.portals, {})
        self.assertEqual(mydonut.start, donut.START)
        self.assertEqual(mydonut.finish, donut.FINISH)
        self.assertEqual(mydonut.portals_at, {})
        self.assertEqual(mydonut.part2, False)
        self.assertEqual(mydonut.locs, {})

    def test_text_0_init(self):
        """Test vault object creation with text"""

        # 1. Create default donut object
        mydonut = donut.Donut(text=from_text(EXAMPLES[0]))

        # 2. Make sure it has the expected values
        self.assertEqual(len(mydonut.text), 19)
        self.assertEqual(mydonut.rows, 19)
        self.assertEqual(mydonut.cols, 19)
        self.assertEqual(mydonut.portals, {
            'AA': {(9, 2)},
            'BC': {(2, 8), (9, 6)},
            'DE': {(2, 13), (6, 10)},
            'FG': {(2, 15), (11, 12)},
            'ZZ': {(13, 16)}})
        self.assertEqual(mydonut.finish, donut.FINISH)
        self.assertEqual(mydonut.portals_at, {
            (2, 8): 'BC',
            (2, 13): 'DE',
            (2, 15): 'FG',
            (6, 10): 'DE',
            (9, 2): 'AA',
            (9, 6): 'BC',
            (11, 12): 'FG',
            (13, 16): 'ZZ'})
        self.assertEqual(mydonut.part2, False)
        self.assertEqual(len(mydonut.locs), 47)

        # 3. Check methods (not used by init)
        self.assertEqual(mydonut.exit_dirs(9, 2), ['S'])
        self.assertEqual(mydonut.exit_dirs(9, 3), ['N', 'S', 'E'])
        self.assertEqual(mydonut.exit_dirs(9, 4), ['N', 'S'])
        self.assertEqual(mydonut.exit_dirs(9, 5), ['N', 'S'])
        self.assertEqual(mydonut.exit_dirs(9, 6), ['N', 'S'])
        self.assertEqual(mydonut.non_portals(9, 2), ['S'])
        self.assertEqual(mydonut.non_portals(9, 3), ['S', 'E'])
        self.assertEqual(mydonut.non_portals(9, 4), ['N', 'S'])
        self.assertEqual(mydonut.non_portals(9, 5), ['N'])
        self.assertEqual(mydonut.non_portals(9, 6), ['N', 'S'])
        self.assertEqual(mydonut.exit_locs(9, 2), [(9, 3)])
        self.assertEqual(mydonut.exit_locs(9, 3), [(9, 2), (9, 4), (10, 3)])
        self.assertEqual(mydonut.exit_locs(9, 4), [(9, 3), (9, 5)])
        self.assertEqual(mydonut.exit_locs(9, 5), [(9, 4), (9, 6)])
        self.assertEqual(mydonut.exit_locs(9, 6), [(9, 5)])

        self.assertEqual(mydonut.inner_portal((2, 8)), False)
        self.assertEqual(mydonut.inner_portal((2, 13)), False)
        self.assertEqual(mydonut.inner_portal((2, 15)), False)
        self.assertEqual(mydonut.inner_portal((6, 10)), True)
        self.assertEqual(mydonut.inner_portal((9, 2)), False)
        self.assertEqual(mydonut.inner_portal((9, 6)), True)
        self.assertEqual(mydonut.inner_portal((11, 12)), True)
        self.assertEqual(mydonut.inner_portal((13, 16)), False)

    def test_text_1_init(self):
        """Test vault object creation with text"""

        # 1. Create default donut object
        mydonut = donut.Donut(text=from_text(EXAMPLES[1]))

        # 2. Make sure it has the expected values
        self.assertEqual(len(mydonut.text), 37)
        self.assertEqual(mydonut.rows, 37)
        self.assertEqual(mydonut.cols, 35)
        self.assertEqual(mydonut.portals, {
            'AA': {(19, 2)},
            'AS': {(32, 17), (17, 8)},
            'BU': {(26, 21), (11, 34)},
            'CP': {(19, 34), (21, 8)},
            'DI': {(2, 15), (8, 21)},
            'JO': {(13, 28), (2, 19)},
            'JP': {(21, 28), (15, 34)},
            'LF': {(15, 28), (32, 21)},
            'QG': {(32, 23), (26, 17)},
            'VT': {(26, 23), (32, 11)},
            'YN': {(2, 23), (26, 13)},
            'ZZ': {(2, 17)}})
        self.assertEqual(mydonut.start, donut.START)
        self.assertEqual(mydonut.finish, donut.FINISH)
        self.assertEqual(mydonut.portals_at, {
            (2, 15): 'DI',
            (2, 17): 'ZZ',
            (2, 19): 'JO',
            (2, 23): 'YN',
            (8, 21): 'DI',
            (11, 34): 'BU',
            (13, 28): 'JO',
            (15, 28): 'LF',
            (15, 34): 'JP',
            (17, 8): 'AS',
            (19, 2): 'AA',
            (19, 34): 'CP',
            (21, 8): 'CP',
            (21, 28): 'JP',
            (26, 13): 'YN',
            (26, 17): 'QG',
            (26, 21): 'BU',
            (26, 23): 'VT',
            (32, 11): 'VT',
            (32, 17): 'AS',
            (32, 21): 'LF',
            (32, 23): 'QG'})
        self.assertEqual(mydonut.part2, False)
        self.assertEqual(len(mydonut.locs), 313)

        self.assertEqual(mydonut.outer_portal((2, 15)), True)
        self.assertEqual(mydonut.outer_portal((2, 17)), True)
        self.assertEqual(mydonut.outer_portal((2, 19)), True)
        self.assertEqual(mydonut.outer_portal((2, 23)), True)
        self.assertEqual(mydonut.outer_portal((8, 21)), False)
        self.assertEqual(mydonut.outer_portal((11, 34)), True)
        self.assertEqual(mydonut.outer_portal((13, 28)), False)
        self.assertEqual(mydonut.outer_portal((15, 28)), False)
        self.assertEqual(mydonut.outer_portal((15, 34)), True)
        self.assertEqual(mydonut.outer_portal((17, 8)), False)
        self.assertEqual(mydonut.outer_portal((19, 2)), True)
        self.assertEqual(mydonut.outer_portal((19, 34)), True)
        self.assertEqual(mydonut.outer_portal((21, 8)), False)
        self.assertEqual(mydonut.outer_portal((21, 28)), False)
        self.assertEqual(mydonut.outer_portal((26, 13)), False)
        self.assertEqual(mydonut.outer_portal((26, 17)), False)
        self.assertEqual(mydonut.outer_portal((26, 21)), False)
        self.assertEqual(mydonut.outer_portal((26, 23)), False)
        self.assertEqual(mydonut.outer_portal((32, 11)), True)
        self.assertEqual(mydonut.outer_portal((32, 17)), True)
        self.assertEqual(mydonut.outer_portal((32, 21)), True)
        self.assertEqual(mydonut.outer_portal((32, 23)), True)

    def test_text_2_init(self):
        """Test vault object creation with text"""

        # 1. Create default donut object
        mydonut = donut.Donut(text=from_text(EXAMPLES[2]), part2=True)

        # 2. Make sure it has the expected values
        self.assertEqual(len(mydonut.text), 37)
        self.assertEqual(mydonut.rows, 37)
        self.assertEqual(mydonut.cols, 45)
        self.assertEqual(mydonut.portals, {
            'OA': {(17, 34), (8, 13)},
            'WB': {(36, 13), (19, 2)},
            'ZH': {(42, 13), (31, 8)},
            'CJ': {(2, 15), (8, 23)},
            'CK': {(8, 17), (27, 2)},
            'IC': {(23, 8), (42, 17)},
            'XF': {(2, 21), (17, 28)},
            'RF': {(36, 21), (42, 25)},
            'NM': {(36, 23), (23, 34)},
            'RE': {(21, 8), (2, 25)},
            'ZZ': {(13, 2)},
            'FD': {(19, 34), (13, 8)},
            'LP': {(29, 28), (15, 2)},
            'AA': {(15, 34)},
            'XQ': {(17, 2), (21, 28)}})
        self.assertEqual(mydonut.start, donut.START)
        self.assertEqual(mydonut.finish, donut.FINISH)
        self.assertEqual(mydonut.portals_at, {
            (8, 13): 'OA',
            (36, 13): 'WB',
            (42, 13): 'ZH',
            (2, 15): 'CJ',
            (8, 17): 'CK',
            (42, 17): 'IC',
            (2, 21): 'XF',
            (36, 21): 'RF',
            (8, 23): 'CJ',
            (36, 23): 'NM',
            (2, 25): 'RE',
            (42, 25): 'RF',
            (13, 2): 'ZZ',
            (13, 8): 'FD',
            (15, 2): 'LP',
            (15, 34): 'AA',
            (17, 2): 'XQ',
            (17, 28): 'XF',
            (17, 34): 'OA',
            (19, 2): 'WB',
            (19, 34): 'FD',
            (21, 8): 'RE',
            (21, 28): 'XQ',
            (23, 8): 'IC',
            (23, 34): 'NM',
            (27, 2): 'CK',
            (29, 28): 'LP',
            (31, 8): 'ZH'})
        self.assertEqual(mydonut.part2, True)
        self.assertEqual(len(mydonut.locs), 376)
        self.assertEqual(mydonut.outer_portal((8, 13)), False)
        self.assertEqual(mydonut.outer_portal((36, 13)), False)
        self.assertEqual(mydonut.outer_portal((42, 13)), True)
        self.assertEqual(mydonut.outer_portal((2, 15)), True)
        self.assertEqual(mydonut.outer_portal((8, 17)), False)
        self.assertEqual(mydonut.outer_portal((42, 17)), True)
        self.assertEqual(mydonut.outer_portal((2, 21)), True)
        self.assertEqual(mydonut.outer_portal((36, 21)), False)
        self.assertEqual(mydonut.outer_portal((8, 23)), False)
        self.assertEqual(mydonut.outer_portal((36, 23)), False)
        self.assertEqual(mydonut.outer_portal((2, 25)), True)
        self.assertEqual(mydonut.outer_portal((42, 25)), True)

        self.assertEqual(mydonut.inner_portal((13, 2)), False)
        self.assertEqual(mydonut.inner_portal((13, 8)), True)
        self.assertEqual(mydonut.inner_portal((15, 2)), False)
        self.assertEqual(mydonut.inner_portal((15, 24)), True)
        self.assertEqual(mydonut.inner_portal((17, 2)), False)
        self.assertEqual(mydonut.inner_portal((17, 28)), True)
        self.assertEqual(mydonut.inner_portal((17, 34)), False)
        self.assertEqual(mydonut.inner_portal((19, 2)), False)
        self.assertEqual(mydonut.inner_portal((19, 34)), False)
        self.assertEqual(mydonut.inner_portal((21, 8)), True)
        self.assertEqual(mydonut.inner_portal((23, 8)), True)
        self.assertEqual(mydonut.inner_portal((23, 34)), False)
        self.assertEqual(mydonut.inner_portal((27, 2)), False)
        self.assertEqual(mydonut.inner_portal((29, 28)), True)
        self.assertEqual(mydonut.inner_portal((31, 8)), True)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ v a u l t . p y                    end
# ======================================================================
