# ======================================================================
# Rucksack Reorganization
#   Advent of Code 2022 Day 03 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ r u c k s a c k . p y
# ======================================================================
"Test Rucksack for Advent of Code 2022 day 03, Rucksack Reorganization"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import rucksack

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = "vJrwpWtwJgWrhcsFMMfFFhFp"

# ======================================================================
#                                                           TestRucksack
# ======================================================================


class TestRucksack(unittest.TestCase):  # pylint: disable=R0904
    "Test Rucksack object"

    def test_empty_init(self):
        "Test the default Rucksack creation"

        # 1. Create default Rucksack object
        myobj = rucksack.Rucksack()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.pockets), 0)

    def test_text_init(self):
        "Test the Rucksack object creation from text"

        # 1. Create Rucksack object from text
        myobj = rucksack.Rucksack(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 24)
        self.assertEqual(len(myobj.pockets), 2)
        self.assertEqual(myobj.pockets[0], "vJrwpWtwJgWr")
        self.assertEqual(myobj.pockets[1], "hcsFMMfFFhFp")

        # 3. Check methods
        self.assertEqual(myobj.both(), "p")
        self.assertEqual(myobj.priority("p"), 16)
        self.assertEqual(myobj.priority("L"), 38)
        self.assertEqual(myobj.priority("P"), 42)
        self.assertEqual(myobj.priority("v"), 22)
        self.assertEqual(myobj.priority("t"), 20)
        self.assertEqual(myobj.priority("s"), 19)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ r u c k s a c k . p y                end
# ======================================================================
