
# ======================================================================
# A Long Walk
#   Advent of Code 2023 Day 23 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                      t e s t _ t r a i l s . p y
# ======================================================================
"Test Trails for Advent of Code 2023 day 23, A Long Walk"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import trails

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = [
    "#.#####################",
    "#.......#########...###",
    "#######.#########.#.###",
    "###.....#.>.>.###.#.###",
    "###v#####.#v#.###.#.###",
    "###.>...#.#.#.....#...#",
    "###v###.#.#.#########.#",
    "###...#.#.#.......#...#",
    "#####.#.#.#######.#.###",
    "#.....#.#.#.......#...#",
    "#.#####.#.#.#########v#",
    "#.#...#...#...###...>.#",
    "#.#.#v#######v###.###v#",
    "#...#.>.#...>.>.#.###.#",
    "#####v#.#.###v#.#.###.#",
    "#.....#...#...#.#.#...#",
    "#.#########.###.#.#.###",
    "#...###...#...#...#.###",
    "###.###.#.###v#####v###",
    "#...#...#.#.>.>.#.>.###",
    "#.###.###.#.###.#.#v###",
    "#.....###...###...#...#",
    "#####################.#",
]

# ======================================================================
#                                                             TestTrails
# ======================================================================


class TestTrails(unittest.TestCase):  # pylint: disable=R0904
    "Test Trails object"

    def test_empty_init(self):
        "Test the default Trails creation"

        # 1. Create default Trails object
        myobj = trails.Trails()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.start, None)
        self.assertEqual(myobj.exit, None)

    def test_text_init(self):
        "Test the Trails object creation from text"

        # 1. Create Trails object from text
        myobj = trails.Trails(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 23)
        self.assertEqual(myobj.start, (0, 1))
        self.assertEqual(myobj.exit, (22, 21))

        # 3. Check methods
        self.assertEqual(myobj.longest_hike(), 94)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ t r a i l s . p y                  end
# ======================================================================
