# ======================================================================
# Signals and Noise
#   Advent of Code 2016 Day 06 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ m e s s a g e . p y
# ======================================================================
"Test solver for Advent of Code 2016 day 06, Signals and Noise"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_06
import message

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = "easter"
PART_TWO_RESULT = "advent"

# ======================================================================
#                                                            TestMessage
# ======================================================================


class TestMessage(unittest.TestCase):  # pylint: disable=R0904
    "Test Message object"

    def test_empty_init(self):
        "Test the default Message creation"

        # 1. Create default Message object
        myobj = message.Message()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.columns), 0)

    def test_text_init(self):
        "Test the Message object creation from text"

        # 1. Create Message object from text
        myobj = message.Message(text=aoc_06.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 16)
        self.assertEqual(len(myobj.columns), 6)
        self.assertEqual(myobj.columns[0].most_common()[0][0], 'e')
        self.assertEqual(myobj.columns[1].most_common()[0][0], 'a')

        # 3. Check methods
        self.assertEqual(myobj.most_common(), 'easter')
        self.assertEqual(myobj.least_common(), 'advent')

    def test_part_one(self):
        "Test part one example of Message object"

        # 1. Create Message object from text
        myobj = message.Message(text=aoc_06.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Message object"

        # 1. Create Message object from text
        myobj = message.Message(part2=True, text=aoc_06.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                  t e s t _ m e s s a g e . p y                 end
# ======================================================================
