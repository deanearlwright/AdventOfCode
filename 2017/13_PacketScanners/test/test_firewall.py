# ======================================================================
# Packet Scanners
#   Advent of Code 2017 Day 13 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ f i r e w a l l . p y
# ======================================================================
"Test solver for Advent of Code 2017 day 13, Packet Scanners"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import firewall
import aoc_13

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

EXAMPLE_TEXT = """
0: 3
1: 2
4: 4
6: 4
"""
# ======================================================================
#                                                            TestScanner
# ======================================================================


class TestScanner(unittest.TestCase):  # pylint: disable=R0904
    """Test Scanner object"""

    def test_empty_init(self):
        """Test default Scanner creation"""

        # 1. Create default Scanner object
        myscan = firewall.Scanner()

        # 2. Make sure it has the default values
        self.assertEqual(myscan.level, 0)
        self.assertEqual(myscan.depth, 0)
        self.assertEqual(myscan.position, 0)
        self.assertEqual(myscan.direction, 1)

    def test_value_init(self):
        """Test Scanner creation with values"""

        # 1. Create Scanner objects with values
        myscan = firewall.Scanner(level=0, depth=3)

        # 2. Make sure it has the expected values
        self.assertEqual(myscan.level, 0)
        self.assertEqual(myscan.depth, 3)
        self.assertEqual(myscan.position, 0)
        self.assertEqual(myscan.direction, 1)

        # 3. Test advance method
        myscan.advance()
        self.assertEqual(myscan.level, 0)
        self.assertEqual(myscan.depth, 3)
        self.assertEqual(myscan.position, 1)
        self.assertEqual(myscan.direction, 1)

        myscan.advance()
        self.assertEqual(myscan.level, 0)
        self.assertEqual(myscan.depth, 3)
        self.assertEqual(myscan.position, 2)
        self.assertEqual(myscan.direction, 1)

        myscan.advance()
        self.assertEqual(myscan.level, 0)
        self.assertEqual(myscan.depth, 3)
        self.assertEqual(myscan.position, 1)
        self.assertEqual(myscan.direction, -1)

# ======================================================================
#                                                           TestFirewall
# ======================================================================


class TestFirewall(unittest.TestCase):  # pylint: disable=R0904
    """Test Firewall object"""

    def test_empty_init(self):
        """Test default Firewall creation"""

        # 1. Create default Pipes object
        myfw = firewall.Firewall()

        # 2. Make sure it has the default values
        self.assertEqual(myfw.part2, False)
        self.assertEqual(myfw.levels, {})
        self.assertEqual(myfw.picosecond, 0)
        self.assertEqual(myfw.final, 0)


    def test_text_init(self):
        """Test firewall creation from text"""

        # 1. Create default Pipes object
        myfw = firewall.Firewall(text=aoc_13.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the specified values
        self.assertEqual(myfw.part2, False)
        self.assertEqual(len(myfw.levels), 4)
        self.assertEqual(myfw.picosecond, 0)
        self.assertEqual(myfw.final, 6)

        self.assertEqual(myfw.levels[0].level, 0)
        self.assertEqual(myfw.levels[0].depth, 3)
        self.assertEqual(myfw.levels[0].position, 0)
        self.assertEqual(myfw.levels[0].direction, 1)

        self.assertEqual(myfw.levels[1].depth, 2)
        self.assertEqual(myfw.levels[4].depth, 4)
        self.assertEqual(myfw.levels[6].depth, 4)

        # 3. Test advance method
        myfw.advance()
        self.assertEqual(myfw.levels[0].position, 1)
        self.assertEqual(myfw.levels[1].position, 1)
        self.assertEqual(myfw.levels[4].position, 1)
        self.assertEqual(myfw.levels[6].position, 1)
        self.assertEqual(myfw.picosecond, 1)

        myfw.advance()
        self.assertEqual(myfw.levels[0].position, 2)
        self.assertEqual(myfw.levels[1].position, 0)
        self.assertEqual(myfw.levels[4].position, 2)
        self.assertEqual(myfw.levels[6].position, 2)
        self.assertEqual(myfw.picosecond, 2)

        myfw.advance()
        self.assertEqual(myfw.levels[0].position, 1)
        self.assertEqual(myfw.levels[1].position, 1)
        self.assertEqual(myfw.levels[4].position, 3)
        self.assertEqual(myfw.levels[6].position, 3)
        self.assertEqual(myfw.picosecond, 3)

    def test_part_one(self):
        """Test the part one example"""

        # 1. Create default Pipes object
        myfw = firewall.Firewall(text=aoc_13.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the specified values
        self.assertEqual(myfw.part2, False)
        self.assertEqual(len(myfw.levels), 4)
        self.assertEqual(myfw.picosecond, 0)
        self.assertEqual(myfw.final, 6)

        # 3. Test the trip methos
        self.assertEqual(myfw.trip(verbose=False), 24)

    def test_part_two_sim(self):
        """Test the part two example with simulation"""

        # 1. Create default Pipes object
        myfw = firewall.Firewall(part2=True, text=aoc_13.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the specified values
        self.assertEqual(myfw.part2, True)
        self.assertEqual(len(myfw.levels), 4)
        self.assertEqual(myfw.picosecond, 0)
        self.assertEqual(myfw.final, 6)

        # 3. Test the trip methos
        self.assertEqual(myfw.part_two_sim(verbose=False, limit=20), 10)

    def test_part_two_mod(self):
        """Test the part two example with modulo"""

        # 1. Create default Pipes object
        myfw = firewall.Firewall(part2=True, text=aoc_13.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the specified values
        self.assertEqual(myfw.part2, True)
        self.assertEqual(len(myfw.levels), 4)
        self.assertEqual(myfw.picosecond, 0)
        self.assertEqual(myfw.final, 6)

        # 3. Test the trip methos
        self.assertEqual(myfw.part_two_mod(verbose=False, limit=20), 10)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                t e s t _ f i r e w a l l . p y                 end
# ======================================================================
