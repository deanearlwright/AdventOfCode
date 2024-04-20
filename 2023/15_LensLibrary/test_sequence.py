
# ======================================================================
# Lens Library
#   Advent of Code 2023 Day 15 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ s e q u e n c e . p y
# ======================================================================
"Test Sequence for Advent of Code 2023 day 15, Lens Library"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import sequence

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"

# ======================================================================
#                                                           TestSequence
# ======================================================================


class TestSequence(unittest.TestCase):  # pylint: disable=R0904
    "Test Sequence object"

    def test_empty_init(self):
        "Test the default Sequence creation"

        # 1. Create default Sequence object
        myobj = sequence.Sequence()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.steps), 0)
        self.assertEqual(len(myobj.boxes), 256)

    def test_text_init(self):
        "Test the Sequence object creation from text"

        # 1. Create Sequence object from text
        myobj = sequence.Sequence(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 51)
        self.assertEqual(len(myobj.steps), 11)
        self.assertEqual(len(myobj.boxes), 256)

        # 3. Check methods
        self.assertEqual(sequence.Sequence.appendex1a("HASH"), 52)
        self.assertEqual(sequence.Sequence.appendex1a("rn=1"), 30)
        self.assertEqual(sequence.Sequence.appendex1a("cm-"), 253)
        self.assertEqual(sequence.Sequence.appendex1a("qp=3"), 97)

        self.assertEqual(myobj.steps_hash(), 1320)

        self.assertEqual(sequence.Sequence.appendex1a("rn"), 0)
        self.assertEqual(sequence.Sequence.appendex1a("cm"), 0)
        self.assertEqual(sequence.Sequence.appendex1a("qp"), 1)
        self.assertEqual(sequence.Sequence.appendex1a("pc"), 3)

        self.assertEqual(myobj.execute(), 145)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ s e q u e n c e . p y                end
# ======================================================================
