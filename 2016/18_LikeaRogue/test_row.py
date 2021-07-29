# ======================================================================
# Like a Rogue
#   Advent of Code 2016 Day 18 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                        t e s t _ r o w . p y
# ======================================================================
"Test Row for Advent of Code 2016 day 18, Like a Rogue"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import row

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_FIVE = "..^^."
EXAMPLE_TEN = ".^^.^.^^^^"

# ======================================================================
#                                                                TestRow
# ======================================================================


class TestRow(unittest.TestCase):  # pylint: disable=R0904
    "Test Row object"

    def test_empty_init(self):
        "Test the default Row creation"

        # 1. Create default Row object
        myobj = row.Row()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.tiles, '')

        # 3. Check methods
        self.assertEqual(myobj.count_safe(), 0)

    def test_five_init(self):
        "Test the Row object creation from text with five tiles"

        # 1. Create Row object from text
        myobj = row.Row(text=EXAMPLE_FIVE)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 5)
        self.assertEqual(myobj.tiles, ":..^^.:")

        # 3. Check methods
        self.assertEqual(myobj.count_safe(), 3)
        self.assertEqual(myobj.next_tiles(), ':.^^^^:')

    def test_ten_init(self):
        "Test the Row object creation from text with ten tiles"

        # 1. Create Row object from text
        myobj = row.Row(text=EXAMPLE_TEN)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 10)
        self.assertEqual(myobj.tiles, ":.^^.^.^^^^:")

        # 3. Check methods
        self.assertEqual(myobj.count_safe(), 3)
        self.assertEqual(myobj.next_tiles(), ':^^^...^..^:')


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      t e s t _ r o w . p y                     end
# ======================================================================
