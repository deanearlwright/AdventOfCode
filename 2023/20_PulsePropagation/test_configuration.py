
# ======================================================================
# Pulse Propagation
#   Advent of Code 2023 Day 20 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                t e s t _ c o n f i g u r a t i o n . p y
# ======================================================================
"Test Configuration for Advent of Code 2023 day 20, Pulse Propagation"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import configuration

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_ONE = [
    "broadcaster -> a, b, c",
    "%a -> b",
    "%b -> c",
    "%c -> inv",
    "&inv -> a",
] # l=8000, h=4000, p=32000000

EXAMPLE_TWO = [
    "broadcaster -> a",
    "%a -> inv, con",
    "&inv -> b",
    "%b -> con",
    "&con -> output",
] # l=4250, h=2750, p=11687500

EXAMPLE_RX = [
    "broadcaster -> a",
    "%a -> inv, con",
    "&inv -> b",
    "%b -> con",
    "&con -> rx",
]

# ======================================================================
#                                                      TestConfiguration
# ======================================================================


class TestConfiguration(unittest.TestCase):  # pylint: disable=R0904
    "Test Configuration object"

    def test_empty_init(self):
        "Test the default Configuration creation"

        # 1. Create default Configuration object
        myobj = configuration.Configuration()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.modules, {})

    def test_text_init(self):
        "Test the Configuration object creation from text"

        # 1. Create Configuration object from text
        myobj = configuration.Configuration(text=EXAMPLE_ONE)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 5)
        self.assertEqual(len(myobj.modules), 6)

        # 3. Check methods
        self.assertEqual(myobj.press_button(), (8, 4))
        myobj.reset_all()
        self.assertEqual(myobj.multiple_presses(), 32000000)

    def test_text_rx(self):
        "Test the Configuration object creation from text"

        # 1. Create Configuration object from text
        myobj = configuration.Configuration(text=EXAMPLE_RX)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 5)
        self.assertEqual(len(myobj.modules), 7)

        # 3. Check methods
        self.assertEqual(myobj.inputs_to_rx(), ["a", "b"])
        self.assertEqual(myobj.low_pulse_to_rx(), 0)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end            t e s t _ c o n f i g u r a t i o n . p y           end
# ======================================================================
