
# ======================================================================
# Pipe Maze
#   Advent of Code 2023 Day 10 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ p i p e m a z e . p y
# ======================================================================
"Test Pipemaze for Advent of Code 2023 day 10, Pipe Maze"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import pipemaze

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = [
    "..F7.",
    ".FJ|.",
    "SJ.L7",
    "|F--J",
    "LJ...",
]
EXAMPLE_TWO = [
    "...........",
    ".S-------7.",
    ".|F-----7|.",
    ".||.....||.",
    ".||.....||.",
    ".|L-7.F-J|.",
    ".|..|.|..|.",
    ".L--J.L--J.",
    "...........",
]

# ======================================================================
#                                                           TestPipemaze
# ======================================================================


class TestPipemaze(unittest.TestCase):  # pylint: disable=R0904
    "Test Pipemaze object"

    def test_empty_init(self):
        "Test the default Pipemaze creation"

        # 1. Create default Pipemaze object
        myobj = pipemaze.Pipemaze()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.start, None)

    def test_text_init(self):
        "Test the Pipemaze object creation from text"

        # 1. Create Pipemaze object from text
        myobj = pipemaze.Pipemaze(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 5)
        self.assertEqual(myobj.start, (2, 0))

        # 3. Check methods
        self.assertEqual(myobj.step((2, 0), pipemaze.EAST), ((2, 1), pipemaze.NORTH))
        self.assertEqual(myobj.step((2, 0), pipemaze.SOUTH), ((3, 0), pipemaze.SOUTH))

        self.assertEqual(myobj.furthest(), 8)
        self.assertEqual(len(myobj.loop_locations()), 16)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ p i p e m a z e . p y                end
# ======================================================================
