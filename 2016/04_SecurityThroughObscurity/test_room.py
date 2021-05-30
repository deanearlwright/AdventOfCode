
# ======================================================================
# Security Through Obscurity
#   Advent of Code 2016 Day 04 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                        t e s t _ l i s t . p y
# ======================================================================
"Test Room object for Advent of Code 2016 day 04, Security Through Obscurity"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import room

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
aaaaa-bbb-z-y-x-123[abxyz]
a-b-c-d-e-f-g-h-987[abcde]
not-a-real-room-404[oarel]
totally-real-room-200[decoy]
"""

# ======================================================================
#                                                               TestRoom
# ======================================================================


class TestRoom(unittest.TestCase):  # pylint: disable=R0904
    "Test Room object"

    def test_empty_init(self):
        "Test the default List creation"

        # 1. Create default Room object
        myobj = room.Room()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, '')
        self.assertEqual(myobj.name, '')
        self.assertEqual(myobj.id, 0)
        self.assertEqual(myobj.checksum, '')
        self.assertEqual(myobj.valid, False)

    def test_text_init(self):
        "Test the Room object creation from text"

        # 1. Create Room object from text
        myobj = room.Room("aaaaa-bbb-z-y-x-123[abxyz]")

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 26)
        self.assertEqual(myobj.name, "aaaaa-bbb-z-y-x")
        self.assertEqual(myobj.id, 123)
        self.assertEqual(myobj.checksum, "abxyz")
        self.assertEqual(myobj.valid, True)

        # 3. Create another Room object from text
        myobj = room.Room("a-b-c-d-e-f-g-h-987[abcde]")

        # 4. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 26)
        self.assertEqual(myobj.name, "a-b-c-d-e-f-g-h")
        self.assertEqual(myobj.id, 987)
        self.assertEqual(myobj.checksum, "abcde")
        self.assertEqual(myobj.valid, True)

        # 5. Create yet another Room object from text
        myobj = room.Room("not-a-real-room-404[oarel]")

        # 6. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 26)
        self.assertEqual(myobj.name, "not-a-real-room")
        self.assertEqual(myobj.id, 404)
        self.assertEqual(myobj.checksum, "oarel")
        self.assertEqual(myobj.valid, True)

        # 7. Create last Room object from text
        myobj = room.Room("totally-real-room-200[decoy]")

        # 8. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 28)
        self.assertEqual(myobj.name, "totally-real-room")
        self.assertEqual(myobj.id, 200)
        self.assertEqual(myobj.checksum, "decoy")
        self.assertEqual(myobj.valid, False)

    def test_decryption(self):
        "Test the Room object decryption"

        # 1. Create Room object from text
        myobj = room.Room("qzmt-zixmtkozy-ivhz-343[xxxxx]")

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 30)
        self.assertEqual(myobj.name, "qzmt-zixmtkozy-ivhz")
        self.assertEqual(myobj.id, 343)

        # 3. Test decryption
        self.assertEqual(myobj.decrypt(), "very encrypted name")


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                       t e s t _ r o o m . p y                  end
# ======================================================================
