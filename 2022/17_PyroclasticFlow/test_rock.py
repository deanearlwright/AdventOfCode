
# ======================================================================
# Pyroclastic Flow
#   Advent of Code 2022 Day 17 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ r o c k . p y
# ======================================================================
"Test Rock for Advent of Code 2022 day 17, Pyroclastic Flow"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import rock

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = "1,4,1,####"

# ======================================================================
#                                                               TestRock
# ======================================================================


class TestRock(unittest.TestCase):  # pylint: disable=R0904
    "Test Rock object"

    def test_empty_init(self):
        "Test the default Rock creation"

        # 1. Create default Rock object
        myobj = rock.Rock()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.type, 0)
        self.assertEqual(myobj.width, 0)
        self.assertEqual(myobj.height, 0)
        self.assertEqual(len(myobj.shape), 0)

    def test_text_init(self):
        "Test the Rock object creation from text"

        # 1. Create Rock object from text
        myobj = rock.Rock(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 10)
        self.assertEqual(myobj.type, 1)
        self.assertEqual(myobj.width, 4)
        self.assertEqual(myobj.height, 1)
        self.assertEqual(len(myobj.shape), 1)
        self.assertEqual(myobj.shape[0], "####")

        # 3. Check methods
        self.assertEqual(myobj.go_down(), -1)
        self.assertEqual(myobj.go_right(), 4)
        self.assertEqual(myobj.go_right(), 5)
        self.assertEqual(myobj.go_right(), 6)
        self.assertEqual(myobj.go_left(), 2)
        self.assertEqual(myobj.go_left(), 1)
        self.assertEqual(myobj.go_left(), 0)
        self.assertEqual(myobj.box(), ((0, -1), (3, -1)))


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                     t e s t _ r o c k . p y                    end
# ======================================================================
