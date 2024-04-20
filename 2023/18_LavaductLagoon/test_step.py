
# ======================================================================
# Lavaduct Lagoon
#   Advent of Code 2023 Day 18 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                        t e s t _ s t e p . p y
# ======================================================================
"Test Step for Advent of Code 2023 day 18, Lavaduct Lagoon"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import step

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = "R 6 (#70c710)"

# ======================================================================
#                                                               TestStep
# ======================================================================


class TestStep(unittest.TestCase):  # pylint: disable=R0904
    "Test Step object"

    def test_empty_init(self):
        "Test the default Step creation"

        # 1. Create default Step object
        myobj = step.Step()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.action, "")
        self.assertEqual(myobj.meters, 0)
        self.assertEqual(myobj.hex_color, "")

    def test_text_init(self):
        "Test the Step object creation from text"

        # 1. Create Step object from text
        myobj = step.Step(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 13)
        self.assertEqual(myobj.action, "R")
        self.assertEqual(myobj.meters, 6)
        self.assertEqual(myobj.hex_color, "70c710")

        # 3. Check methods
        self.assertEqual(myobj.specs(), ("R", 6, "70c710"))

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                     t e s t _ s t e p . p y                    end
# ======================================================================
