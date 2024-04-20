
# ======================================================================
# Pulse Propagation
#   Advent of Code 2023 Day 20 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                      t e s t _ m o d u l e . p y
# ======================================================================
"Test Module for Advent of Code 2023 day 20, Pulse Propagation"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import module

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = "broadcaster -> a, b, c"
EXAMPLE_BROADCASTER = "broadcaster -> a"
EXAMPLE_FLIP_FLOP = "%a -> inv, con"
EXAMPLE_CONJUNCTION = "&con -> output"
EXAMPLE_BUTTON = "button"

# ======================================================================
#                                                             TestModule
# ======================================================================


class TestModule(unittest.TestCase):  # pylint: disable=R0904
    "Test Module object"

    def test_empty_init(self):
        "Test the default Module creation"

        # 1. Create default Module object
        myobj = module.Module()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.name, None)
        self.assertEqual(myobj.type, None)
        self.assertEqual(myobj.outputs, [])
        self.assertEqual(len(myobj.inputs), 0)
        self.assertEqual(myobj.state, "Off")
        self.assertEqual(myobj.low_pulses, 0)
        self.assertEqual(myobj.high_pulses, 0)

    def test_text_init(self):
        "Test the Module object creation from text"

        # 1. Create Module object from text
        myobj = module.Module(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 22)
        self.assertEqual(myobj.name, "broadcaster")
        self.assertEqual(myobj.type, "B")
        self.assertEqual(myobj.outputs, ["a", "b", "c"])
        self.assertEqual(len(myobj.inputs), 0)
        self.assertEqual(myobj.state, "Off")
        self.assertEqual(myobj.low_pulses, 0)
        self.assertEqual(myobj.high_pulses, 0)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ m o d u l e . p y                  end
# ======================================================================
