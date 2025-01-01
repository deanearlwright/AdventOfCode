
# ======================================================================
# Keypad Conundrum
#   Advent of Code 2024 Day 21 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ k e y p a d . p y
# ======================================================================
"Test solver for Advent of Code 2024 day 21, Keypad Conundrum"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_21
import keypad

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
029A
980A
179A
456A
379A
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 126384
PART_TWO_RESULT = 154115708116294

# ======================================================================
#                                                             TestKeypad
# ======================================================================


class TestKeypad(unittest.TestCase):  # pylint: disable=R0904
    "Test Keypad object"

    def test_empty_init(self):
        "Test the default Keypad creation"

        # 1. Create default Keypad object
        myobj = keypad.Keypad()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.codes), 0)
        self.assertEqual(myobj.robots, 3)
        self.assertEqual(len(myobj.presses), 0)

    def test_text_init(self):
        "Test the Keypad object creation from text"

        # 1. Create Keypad object from text
        myobj = keypad.Keypad(text=aoc_21.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 5)
        self.assertEqual(len(myobj.codes), 5)
        self.assertEqual(myobj.robots, 3)
        self.assertEqual(len(myobj.presses), 0)

        # 3. Check methods
        self.assertEqual(myobj.complexity(68, "029A"), 1972)
        self.assertEqual(myobj.key_to_key(0, "A", "A"), [""])
        self.assertEqual(myobj.key_to_key(0, "A", "0"), ["<"])
        self.assertEqual(myobj.key_to_key(0, "0", "A"), [">"])
        self.assertEqual(myobj.key_to_key(0, "A", "3"), ["^"])
        self.assertEqual(myobj.key_to_key(0, "3", "A"), ["v"])
        self.assertEqual(myobj.key_to_key(0, "A", "2"), ["^<", "<^"])
        self.assertEqual(myobj.key_to_key(0, "A", "1"), ["^<<", "<^<"])

        self.assertEqual(myobj.min_seq_len(0, "A", 0), 1)
        self.assertEqual(myobj.min_seq_len(0, "A", 1), 1)
        self.assertEqual(myobj.min_seq_len(0, "0A", 1), 4)
        self.assertEqual(myobj.min_seq_len(0, "029A", 1), 12)
        self.assertEqual(myobj.min_seq_len(0, "029A", 2), 28)
        self.assertEqual(myobj.min_seq_len(0, "029A", 3), 68)

        self.assertEqual(myobj.min_seq_len(0, "029A", 3), 68)
        self.assertEqual(myobj.min_seq_len(0, "980A", 3), 60)
        self.assertEqual(myobj.min_seq_len(0, "179A", 3), 68)
        self.assertEqual(myobj.min_seq_len(0, "456A", 3), 64)
        self.assertEqual(myobj.min_seq_len(0, "379A", 3), 64)

        self.assertEqual(myobj.sum_complexity(), 126384)

    def test_part_one(self):
        "Test part one example of Keypad object"

        # 1. Create Keypad object from text
        text = aoc_21.from_text(PART_ONE_TEXT)
        myobj = keypad.Keypad(text=text)

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Keypad object"

        # 1. Create Keypad object from text
        text = aoc_21.from_text(PART_TWO_TEXT)
        myobj = keypad.Keypad(part2=True, text=text)

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ k e y p a d . p y                  end
# ======================================================================
