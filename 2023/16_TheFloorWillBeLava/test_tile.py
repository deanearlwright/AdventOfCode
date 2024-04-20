
# ======================================================================
# The Floor Will Be Lava
#   Advent of Code 2023 Day 16 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ t i l e . p y
# ======================================================================
"Test Tile for Advent of Code 2023 day 16, The Floor Will Be Lava"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import tile

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                               TestTile
# ======================================================================


class TestTile(unittest.TestCase):  # pylint: disable=R0904
    "Test Tile object"

    def test_default_init(self):
        "Test the default Tile creation"

        # 1. Create default Tile object
        myobj = tile.Tile()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.row, 0)
        self.assertEqual(myobj.col, 0)
        self.assertEqual(myobj.char, tile.EMPTY)
        self.assertEqual(myobj.activated, False)
        self.assertEqual(len(myobj.directions), 0)

    def test_empty_init(self):
        "Test the Tile object creation from text"

        # 1. Create Tile object from text
        myobj = tile.Tile(row=1, col=5, char=tile.EMPTY)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.row, 1)
        self.assertEqual(myobj.col, 5)
        self.assertEqual(myobj.char, tile.EMPTY)
        self.assertEqual(myobj.activated, False)
        self.assertEqual(len(myobj.directions), 0)

        # 3. Check methods
        self.assertEqual(myobj.next(tile.NORTH), (0, 5))
        self.assertEqual(myobj.next(tile.SOUTH), (2, 5))
        self.assertEqual(myobj.next(tile.EAST), (1, 6))
        self.assertEqual(myobj.next(tile.WEST), (1, 4))

        self.assertEqual(myobj.is_activated(), False)
        self.assertEqual(myobj.entered(tile.NORTH), [tile.NORTH])
        self.assertEqual(myobj.is_activated(), True)
        self.assertEqual(len(myobj.directions), 1)
        self.assertEqual(myobj.entered(tile.NORTH), [])
        self.assertEqual(myobj.is_activated(), True)
        self.assertEqual(len(myobj.directions), 1)
        self.assertEqual(myobj.entered(tile.SOUTH), [tile.SOUTH])
        self.assertEqual(myobj.entered(tile.EAST), [tile.EAST])
        self.assertEqual(myobj.entered(tile.WEST), [tile.WEST])
        self.assertEqual(len(myobj.directions), 4)

    def test_left_init(self):
        "Test the Tile object creation from text"

        # 1. Create Tile object from text
        myobj = tile.Tile(row=1, col=5, char=tile.LEFT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.row, 1)
        self.assertEqual(myobj.col, 5)
        self.assertEqual(myobj.char, tile.LEFT)
        self.assertEqual(myobj.activated, False)
        self.assertEqual(len(myobj.directions), 0)

        # 3. Check methods
        self.assertEqual(myobj.is_activated(), False)
        self.assertEqual(myobj.entered(tile.NORTH), [tile.EAST])
        self.assertEqual(myobj.is_activated(), True)
        self.assertEqual(len(myobj.directions), 1)
        self.assertEqual(myobj.entered(tile.NORTH), [])
        self.assertEqual(myobj.is_activated(), True)
        self.assertEqual(len(myobj.directions), 1)
        self.assertEqual(myobj.entered(tile.SOUTH), [tile.WEST])
        self.assertEqual(myobj.entered(tile.EAST), [tile.NORTH])
        self.assertEqual(myobj.entered(tile.WEST), [tile.SOUTH])
        self.assertEqual(len(myobj.directions), 4)

    def test_flat_init(self):
        "Test the Tile object creation from text"

        # 1. Create Tile object from text
        myobj = tile.Tile(row=1, col=5, char=tile.FLAT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.row, 1)
        self.assertEqual(myobj.col, 5)
        self.assertEqual(myobj.char, tile.FLAT)
        self.assertEqual(myobj.activated, False)
        self.assertEqual(len(myobj.directions), 0)

        # 3. Check methods
        self.assertEqual(myobj.is_activated(), False)
        self.assertEqual(myobj.entered(tile.NORTH), [tile.EAST, tile.WEST])
        self.assertEqual(myobj.is_activated(), True)
        self.assertEqual(len(myobj.directions), 1)
        self.assertEqual(myobj.entered(tile.NORTH), [])
        self.assertEqual(myobj.is_activated(), True)
        self.assertEqual(len(myobj.directions), 1)
        self.assertEqual(myobj.entered(tile.SOUTH), [tile.EAST, tile.WEST])
        self.assertEqual(myobj.entered(tile.EAST), [tile.EAST])
        self.assertEqual(myobj.entered(tile.WEST), [tile.WEST])
        self.assertEqual(len(myobj.directions), 4)

    def test_vert_init(self):
        "Test the Tile object creation from text"

        # 1. Create Tile object from text
        myobj = tile.Tile(row=1, col=5, char=tile.VERT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.row, 1)
        self.assertEqual(myobj.col, 5)
        self.assertEqual(myobj.char, tile.VERT)
        self.assertEqual(myobj.activated, False)
        self.assertEqual(len(myobj.directions), 0)

        # 3. Check methods
        self.assertEqual(myobj.is_activated(), False)
        self.assertEqual(myobj.entered(tile.NORTH), [tile.NORTH])
        self.assertEqual(myobj.is_activated(), True)
        self.assertEqual(len(myobj.directions), 1)
        self.assertEqual(myobj.entered(tile.NORTH), [])
        self.assertEqual(myobj.is_activated(), True)
        self.assertEqual(len(myobj.directions), 1)
        self.assertEqual(myobj.entered(tile.SOUTH), [tile.SOUTH])
        self.assertEqual(myobj.entered(tile.EAST), [tile.NORTH, tile.SOUTH])
        self.assertEqual(myobj.entered(tile.WEST), [tile.NORTH, tile.SOUTH])
        self.assertEqual(len(myobj.directions), 4)

    def test_right_init(self):
        "Test the Tile object creation from text"

        # 1. Create Tile object from text
        myobj = tile.Tile(row=1, col=5, char=tile.RIGHT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.row, 1)
        self.assertEqual(myobj.col, 5)
        self.assertEqual(myobj.char, tile.RIGHT)
        self.assertEqual(myobj.activated, False)
        self.assertEqual(len(myobj.directions), 0)

        # 3. Check methods
        self.assertEqual(myobj.is_activated(), False)
        self.assertEqual(myobj.entered(tile.NORTH), [tile.WEST])
        self.assertEqual(myobj.is_activated(), True)
        self.assertEqual(len(myobj.directions), 1)
        self.assertEqual(myobj.entered(tile.NORTH), [])
        self.assertEqual(myobj.is_activated(), True)
        self.assertEqual(len(myobj.directions), 1)
        self.assertEqual(myobj.entered(tile.SOUTH), [tile.EAST])
        self.assertEqual(myobj.entered(tile.EAST), [tile.SOUTH])
        self.assertEqual(myobj.entered(tile.WEST), [tile.NORTH])
        self.assertEqual(len(myobj.directions), 4)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                     t e s t _ t i l e . p y                    end
# ======================================================================
