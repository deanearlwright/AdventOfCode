
# ======================================================================
# Unstable Diffusion
#   Advent of Code 2022 Day 23 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ p r o c e s s . p y
# ======================================================================
"Test Process for Advent of Code 2022 day 23, Unstable Diffusion"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import process

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = [
    ".....",
    "..##.",
    "..#..",
    ".....",
    "..##.",
    "....."
]
# ======================================================================
#                                                            TestProcess
# ======================================================================


class TestProcess(unittest.TestCase):  # pylint: disable=R0904
    "Test Process object"

    def test_empty_init(self):
        "Test the default Process creation"

        # 1. Create default Process object
        myobj = process.Process()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.grove, None)
        self.assertEqual(len(myobj.rules), 4)

    def test_text_init(self):
        "Test the Process object creation from text"

        # 1. Create Process object from text
        myobj = process.Process(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 6)
        self.assertNotEqual(myobj.grove, None)
        self.assertEqual(len(myobj.rules), 4)

        # 3. Check methods
        self.assertEqual(myobj.next_rule(), 'N')
        self.assertEqual(myobj.next_rule(), 'S')
        self.assertEqual(myobj.next_rule(), 'W')
        self.assertEqual(myobj.next_rule(), 'E')
        self.assertEqual(myobj.next_rule(), 'N')
        self.assertEqual(myobj.next_rule(), 'S')
        self.assertEqual(myobj.next_rule(), 'W')
        self.assertEqual(myobj.next_rule(), 'E')

        self.assertEqual(myobj.one_round(), 3)
        self.assertEqual(myobj.one_round(), 5)
        self.assertEqual(myobj.one_round(), 3)
        self.assertEqual(myobj.one_round(), 0)
        self.assertEqual(myobj.one_round(), 0)

        self.assertEqual(myobj.grove.rectangle(), ((0, 0), (4, 5)))
        self.assertEqual(myobj.grove.empty_ground_tiles(), 25)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------

if __name__ == '__main__':
    pass

# ======================================================================
# end                  t e s t _ p r o c e s s . p y                 end
# ======================================================================
