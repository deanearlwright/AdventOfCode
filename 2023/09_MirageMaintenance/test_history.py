
# ======================================================================
# Mirage Maintenance
#   Advent of Code 2023 Day 09 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ h i s t o r y . p y
# ======================================================================
"Test History for Advent of Code 2023 day 09, Mirage Maintenance"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import history

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = "0 3 6 9 12 15"

# ======================================================================
#                                                            TestHistory
# ======================================================================


class TestHistory(unittest.TestCase):  # pylint: disable=R0904
    "Test History object"

    def test_empty_init(self):
        "Test the default History creation"

        # 1. Create default History object
        myobj = history.History()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.values), 0)

    def test_text_init(self):
        "Test the History object creation from text"

        # 1. Create History object from text
        myobj = history.History(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 13)
        self.assertEqual(len(myobj.values), 6)

        # 3. Check methods
        self.assertEqual(myobj.values, [0, 3, 6, 9, 12, 15])
        self.assertEqual(myobj.differences(myobj.values), [3, 3, 3, 3, 3])
        self.assertEqual(myobj.differences([3, 3, 3, 3, 3]), [0, 0, 0, 0])

        self.assertFalse(myobj.all_zeroes([0, 3, 6, 9, 12, 15]))
        self.assertFalse(myobj.all_zeroes([3, 3, 3, 3, 3]))
        self.assertTrue(myobj.all_zeroes([0, 0, 0, 0]))
        self.assertFalse(myobj.all_zeroes([0, 0, 7, 0]))

        self.assertEqual(myobj.nxt_value([0, 0, 0, 0]), 0)
        self.assertEqual(myobj.nxt_value([3, 3, 3, 3, 3]), 3)
        self.assertEqual(myobj.nxt_value([0, 3, 6, 9, 12, 15]), 18)

        self.assertEqual(myobj.next_value(), 18)
        self.assertEqual(myobj.prev_value(), -3)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                  t e s t _ h i s t o r y . p y                 end
# ======================================================================
