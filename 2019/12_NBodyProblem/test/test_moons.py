# ======================================================================
# Space Police
#   Advent of Code 2019 Day 11 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ h u l l . p y
# ======================================================================
"Test ships' hull for Advent of Code 2019 day 11, Space Police"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import hull
import panel

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                               TestHull
# ======================================================================


class TestHull(unittest.TestCase):  # pylint: disable=R0904
    """Test Hull object"""

    def test_empty_init(self):
        """Test default Hull object creation"""

        # 1. Create default Hull object
        myhull = hull.Hull()

        # 2. Make sure it has the default values
        self.assertEqual(myhull.panels, {})

        # 3. Check methods
        self.assertEqual(myhull.at_least_once(), 0)
        self.assertEqual(myhull.color((7, 11)), panel.COLOR_BLACK)

    def test_painting(self):
        "Test Asteroids object creation with text"

        # 1. Create default Hull object
        myhull = hull.Hull()

        # 2. Do what the robot did part one of the problem
        # 2a. Starts at (0,0), input 0 -> 1, 0
        self.assertEqual(myhull.color((0, 0)), panel.COLOR_BLACK)
        myhull.paint((0, 0), panel.COLOR_WHITE)
        self.assertEqual(myhull.color((0, 0)), panel.COLOR_WHITE)

        # 2b. input 0 -> 0, 0
        self.assertEqual(myhull.color((0, -1)), panel.COLOR_BLACK)
        myhull.paint((0, -1), panel.COLOR_BLACK)
        self.assertEqual(myhull.color((0, -1)), panel.COLOR_BLACK)

        # 2c. input 0 -> 1, 0
        self.assertEqual(myhull.color((-1, -1)), panel.COLOR_BLACK)
        myhull.paint((-1, -1), panel.COLOR_WHITE)
        self.assertEqual(myhull.color((-1, -1)), panel.COLOR_WHITE)

        # 2d. input 0 -> 1, 0
        self.assertEqual(myhull.color((-1, 0)), panel.COLOR_BLACK)
        myhull.paint((-1, 0), panel.COLOR_WHITE)
        self.assertEqual(myhull.color((-1, 0)), panel.COLOR_WHITE)

        # 2e. Back at the start, input 1 -> 0, 1
        self.assertEqual(myhull.color((0, 0)), panel.COLOR_WHITE)
        myhull.paint((0, 0), panel.COLOR_BLACK)
        self.assertEqual(myhull.color((0, 0)), panel.COLOR_BLACK)

        # 2f. input 0 -> 1, 0
        self.assertEqual(myhull.color((0, 1)), panel.COLOR_BLACK)
        myhull.paint((0, 1), panel.COLOR_WHITE)
        self.assertEqual(myhull.color((0, 1)), panel.COLOR_WHITE)

        # 2g. input 0 -> 1, 0
        self.assertEqual(myhull.color((1, 1)), panel.COLOR_BLACK)
        myhull.paint((1, 1), panel.COLOR_WHITE)
        self.assertEqual(myhull.color((1, 1)), panel.COLOR_WHITE)

        # 3. Check the results
        self.assertEqual(myhull.at_least_once(), 6)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ h u l l . p y                     end
# ======================================================================
