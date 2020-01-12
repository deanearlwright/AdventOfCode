# ======================================================================
# Hex Ed
#   Advent of Code 2017 Day 11 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ h e x e s . p y
# ======================================================================
"Test solver for Advent of Code 2017 day 11, Hex Ed"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import hexes

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

EXAMPLES = [
    ('ne,ne,ne', 3, 3),
    ('ne,ne,sw,sw', 0, 2),
    ('ne,ne,s,s', 2, 2),
    ('se,sw,se,sw,sw', 3, 3)
    ]

# ======================================================================
#                                                              TestHexes
# ======================================================================


class TestHexes(unittest.TestCase):  # pylint: disable=R0904
    """Test Knots object"""

    def test_empty_init(self):
        """Test default Hexes creation"""

        # 1. Create default Hexes object
        myhex = hexes.Hexes()

        # 2. Make sure it has the default values
        self.assertEqual(myhex.part2, False)


    def test_examples(self):
        """Test hexes part one examples"""

        # 1. Loop for all of the part two examples
        for example in EXAMPLES:

            # 2. Create the hexes object
            myhex = hexes.Hexes()

            # 3. Knot it up, and check result
            self.assertEqual(myhex.steps(text=example[0], verbose=False),
                             example[1])
    def test_part2(self):
        """Test hexes part two examples"""

        # 1. Loop for all of the part two examples
        for example in EXAMPLES:

            # 2. Create the hexes object
            myhex = hexes.Hexes(part2=True)

            # 3. Knot it up, and check result
            self.assertEqual(myhex.furthest(text=example[0], verbose=False),
                             example[2])

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                     t e s t _ h e x e s . p y                  end
# ======================================================================
