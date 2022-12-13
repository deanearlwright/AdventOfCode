
# ======================================================================
# Hill Climbing Algorithm
#   Advent of Code 2022 Day 12 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ d e v i c e . p y
# ======================================================================
"Test Device for Advent of Code 2022 day 12, Hill Climbing Algorithm"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import device

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = [
    "Sabqponm",
    "abcryxxl",
    "accszExk",
    "acctuvwj",
    "abdefghi"
]

# ======================================================================
#                                                             TestDevice
# ======================================================================


class TestDevice(unittest.TestCase):  # pylint: disable=R0904
    "Test Device object"

    def test_empty_init(self):
        "Test the default Device creation"

        # 1. Create default Device object
        myobj = device.Device()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.map, {})
        self.assertEqual(myobj.start, None)
        self.assertEqual(myobj.goal, None)

    def test_text_init(self):
        "Test the Device object creation from text"

        # 1. Create Device object from text
        myobj = device.Device(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 5)
        self.assertEqual(len(myobj.map), 40)
        self.assertEqual(myobj.start, (0, 0))
        self.assertEqual(myobj.goal, (5, 2))
        self.assertEqual(myobj.map[(0, 0)], 0)
        self.assertEqual(myobj.map[(1, 0)], 0)
        self.assertEqual(myobj.map[(2, 0)], 1)
        self.assertEqual(myobj.map[(0, 1)], 0)
        self.assertEqual(myobj.map[(1, 1)], 1)
        self.assertEqual(myobj.map[(2, 1)], 2)

        # 3. Check methods
        self.assertEqual(myobj.one_away((0, 0)),
                         [(1, 0), (0, 1)])
        self.assertEqual(myobj.one_away((3, 3)),
                         [(4, 3), (2, 3), (3, 4), (3, 2)])
        self.assertEqual(myobj.is_reachable((0, 0), (1, 0)), True)
        self.assertEqual(myobj.is_reachable((1, 0), (2, 0)), True)
        self.assertEqual(myobj.is_reachable((2, 0), (3, 0)), False)
        self.assertEqual(myobj.reachable((0, 0)),
                         [(1, 0), (0, 1)])
        self.assertEqual(myobj.reachable((2, 2)),
                         [(1, 2), (2, 3), (2, 1)])
        self.assertEqual(myobj.reachable((3, 3)),
                         [(4, 3), (2, 3), (3, 4), (3, 2)])
        self.assertEqual(myobj.best_path(), 31)

        self.assertEqual(len(myobj.find_starts()), 6)
        self.assertEqual(myobj.best_trail(), 29)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ d e v i c e . p y                  end
# ======================================================================
