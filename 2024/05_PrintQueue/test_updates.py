
# ======================================================================
# Print Queue
#   Advent of Code 2024 Day 05 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ u p d a t e s . p y
# ======================================================================
"Test solver for Advent of Code 2024 day 05, Print Queue"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_05
import updates

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 143
PART_TWO_RESULT = 123

# ======================================================================
#                                                            TestUpdates
# ======================================================================


class TestUpdates(unittest.TestCase):  # pylint: disable=R0904
    "Test Updates object"

    def test_empty_init(self):
        "Test the default Updates creation"

        # 1. Create default Updates object
        myobj = updates.Updates()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.rules), 0)
        self.assertEqual(len(myobj.pages), 0)

        # 3. Check utilities
        self.assertEqual(updates.middle([75, 47, 61, 53, 29]), 61)
        self.assertEqual(updates.middle([97, 61, 53, 29, 13]), 53)
        self.assertEqual(updates.middle([75, 29, 13]), 29)

        self.assertEqual(updates.is_afters([75, 29, 13], 75, [29, 53, 47, 13]), True)
        self.assertEqual(updates.is_afters([47, 75, 29, 13], 75, [29, 53, 47, 13]), False)

        self.assertEqual(updates.correct_afters([47, 75, 29, 13], 75, [29, 53, 47, 13]),
                         [75, 47, 29, 13])

    def test_text_init(self):
        "Test the Updates object creation from text"

        # 1. Create Updates object from text
        myobj = updates.Updates(text=aoc_05.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 27)
        self.assertEqual(len(myobj.rules), 6)
        self.assertEqual(len(myobj.pages), 6)

        # 3. Check methods
        self.assertEqual(myobj.is_ordered([75, 29, 13]), True)
        self.assertEqual(myobj.is_ordered([47, 75, 29, 13]), False)
        self.assertEqual(myobj.is_ordered(myobj.pages[0]), True)
        self.assertEqual(myobj.is_ordered(myobj.pages[1]), True)
        self.assertEqual(myobj.is_ordered(myobj.pages[2]), True)
        self.assertEqual(myobj.is_ordered(myobj.pages[3]), False)
        self.assertEqual(myobj.is_ordered(myobj.pages[4]), False)
        self.assertEqual(myobj.is_ordered(myobj.pages[5]), False)

        self.assertEqual(myobj.correct_order_multiple(myobj.pages[3]), [97, 75, 47, 61, 53])
        self.assertEqual(myobj.correct_order_multiple(myobj.pages[4]), [61, 29, 13])
        self.assertEqual(myobj.correct_order_multiple(myobj.pages[5]), [97, 75, 47, 29, 13])

    def test_part_one(self):
        "Test part one example of Updates object"

        # 1. Create Updates object from text
        text = aoc_05.from_text(PART_ONE_TEXT)
        myobj = updates.Updates(text=text)

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Updates object"

        # 1. Create Updates object from text
        text = aoc_05.from_text(PART_TWO_TEXT)
        myobj = updates.Updates(part2=True, text=text)

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                  t e s t _ u p d a t e s . p y                 end
# ======================================================================
