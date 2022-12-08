# ======================================================================
# No Space Left On Device
#   Advent of Code 2022 Day 07 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ d i r e c t o r y . p y
# ======================================================================
"Test Directory for Advent of Code 2022 day 07, No Space Left On Device"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import directory

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = ""

# ======================================================================
#                                                          TestDirectory
# ======================================================================


class TestDirectory(unittest.TestCase):  # pylint: disable=R0904
    "Test Directory object"

    def test_init(self):
        "Test the default Directory creation"

        # 1. Create default Directory object
        myobj = directory.Directory()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.name, None)
        self.assertEqual(myobj.out, None)
        self.assertEqual(len(myobj.files), 0)
        self.assertEqual(len(myobj.dirs), 0)

        # 3. Check methods
        myobj.add_file("foo", 100)
        myobj.add_file("goo", 200)
        self.assertEqual(len(myobj.files), 2)
        self.assertEqual(myobj.size(), 300)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                t e s t _ d i r e c t o r y . p y               end
# ======================================================================
