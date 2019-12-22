# ======================================================================
# Many-Worlds Interpretation
#   Advent of Code 2019 Day 18 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ v a u l t . p y
# ======================================================================
"Test vault for Advent of Code 2019 day 18, Many-Worlds Interpretation"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

from aoc_mw import from_text
import vault

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLES = ["""
!0: 8 steps
#########
#b.A.@.a#
#########""", """
!1: 86 steps
########################
#f.D.E.e.C.b.A.@.a.B.c.#
######################.#
#d.....................#
########################""", """
!2: 132 steps
########################
#...............b.C.D.f#
#.######################
#.....@.a.B.c.d.A.e.F.g#
########################""", """
!3: 136 steps
#################
#i.G..c...e..H.p#
########.########
#j.A..b...f..D.o#
########@########
#k.E..a...g..B.n#
########.########
#l.F..d...h..C.m#
#################""", """
!4: 81 steps
########################
#@..............ac.GI.b#
###d#e#f################
###A#B#C################
###g#h#i################
########################"""]

EXAMPLES_PART2 = ["""
!0: 8 steps
#######
#a.#Cd#
##...##
##.@.##
##...##
#cB#Ab#
#######""", """
!1: 24 steps
###############
#d.ABC.#.....a#
######...######
######.@.######
######...######
#b.....#.....c#
###############""", """
!2: 32 steps
#############
#DcBa.#.GhKl#
#.###...#I###
#e#d#.@.#j#k#
###C#...###J#
#fEbA.#.FgHi#
#############""", """
!3: 72 steps
#############
#g#f.D#..h#l#
#F###e#E###.#
#dCba...BcIJ#
#####.@.#####
#nK.L...G...#
#M###N#H###.#
#o#m..#i#jk.#
#############"""]

# ======================================================================
#                                                              TestVault
# ======================================================================


class TestVault(unittest.TestCase):  # pylint: disable=R0904
    """Test Hull object"""

    def test_empty_init(self):
        """Test default vault object creation"""

        # 1. Create default Vault object
        myvault = vault.Vault()

        # 2. Make sure it has the default values
        self.assertEqual(myvault.text, None)
        self.assertEqual(myvault.clean, None)
        self.assertEqual(myvault.rows, 0)
        self.assertEqual(myvault.cols, 0)
        self.assertEqual(myvault.keys, {})
        self.assertEqual(myvault.doors, {})
        self.assertEqual(myvault.key_at, {})
        self.assertEqual(myvault.door_at, {})
        self.assertEqual(myvault.origin, None)
        self.assertEqual(myvault.origins, None)
        self.assertEqual(myvault.locs, {})


    def test_text_init(self):
        """Test vault object creation with text"""

        # 1. Create default Vault object
        myvault = vault.Vault(text=from_text(EXAMPLES[3]))

        # 2. Make sure it has the expected values
        self.assertEqual(len(myvault.text), 9)
        self.assertEqual(len(myvault.clean), 9)
        self.assertEqual(myvault.rows, 9)
        self.assertEqual(myvault.cols, 17)
        self.assertEqual(len(myvault.keys), 16)
        self.assertEqual(len(myvault.doors), 8)
        self.assertEqual(len(myvault.key_at), 16)
        self.assertEqual(len(myvault.door_at), 8)
        self.assertEqual(myvault.origin, (8, 4))
        self.assertEqual(myvault.origins, None)
        self.assertEqual(len(myvault.locs), 4*15+3)

    def test_text_init_part2(self):
        """Test vault object creation with text"""

        # 1. Create default Vault object
        myvault = vault.Vault(text=from_text(EXAMPLES_PART2[0]), part2=True)

        # 2. Make sure it has the expected values
        self.assertEqual(len(myvault.text), 7)
        self.assertEqual(len(myvault.clean), 7)
        self.assertEqual(myvault.rows, 7)
        self.assertEqual(myvault.cols, 7)
        self.assertEqual(len(myvault.keys), 4)
        self.assertEqual(len(myvault.doors), 3)
        self.assertEqual(len(myvault.key_at), 4)
        self.assertEqual(len(myvault.door_at), 3)
        #self.assertEqual(myvault.origin, (3, 3))
        self.assertEqual(myvault.origins, [(2, 2), (4, 2), (2, 4), (4, 4)])
        self.assertEqual(len(myvault.locs), 12)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ v a u l t . p y                    end
# ======================================================================
