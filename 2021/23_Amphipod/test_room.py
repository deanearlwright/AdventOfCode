# ======================================================================
# Amphipod
#   Advent of Code 2021 Day 23 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ r o o m . p y
# ======================================================================
"Test Room for Advent of Code 2021 day 23, Amphipod"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import room

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                               TestRoom
# ======================================================================


class TestRoom(unittest.TestCase):  # pylint: disable=R0904
    "Test Room object"

    def test_empty_init(self):
        "Test the default Room creation"

        # 1. Create default Room object
        myobj = room.Room()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.doorway, 0)
        self.assertEqual(myobj.homeroom, None)
        self.assertEqual(myobj.contents, [])

    def test_text_init(self):
        "Test the Room object creation from text"

        # 1. Create Room object from text
        myobj = room.Room(doorway=2, homeroom='A', contents=['B', 'A'])

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.doorway, 2)
        self.assertEqual(myobj.homeroom, 'A')
        self.assertEqual(myobj.contents, ['B', 'A'])

        # 3. Check methods
        self.assertEqual(str(myobj), 'BA')
        self.assertEqual(myobj.is_homey(), False)
        self.assertEqual(myobj.is_my_room('A'), True)
        self.assertEqual(myobj.is_my_room('B'), False)
        myobj.contents[0] = 'A'
        self.assertEqual(myobj.is_homey(), True)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                     t e s t _ r o o m . p y                    end
# ======================================================================
