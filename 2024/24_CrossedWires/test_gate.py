
# ======================================================================
# Crossed Wires
#   Advent of Code 2024 Day 24 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ g a t e . p y
# ======================================================================
"Test Gate for Advent of Code 2024 day 24, Crossed Wires"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import gate

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_AND = "x00 AND y00 -> z00"
EXAMPLE_XOR = "x01 XOR y01 -> z01"
EXAMPLE_OR = "x02 OR y02 -> z02"

WIRES = {
    "x00": 1,
    "x01": 1,
    "x02": 1,
    "y00": 0,
    "y01": 1,
    "y02": 0,
}
NO_INTUIT = {
    "x00": 1,
    "x01": 1,
    "x02": 0,
}
INTUIT = {
    "x00": 0,
    "x01": 0,
    "x02": 1,
}

# ======================================================================
#                                                               TestGate
# ======================================================================


class TestGate(unittest.TestCase):  # pylint: disable=R0904
    "Test Gate object"

    def test_empty_init(self):
        "Test the default Gate creation"

        # 1. Create default Gate object
        myobj = gate.Gate()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.name, None)
        self.assertEqual(myobj.type, None)
        self.assertEqual(myobj.inputs, {})
        self.assertEqual(myobj.output, None)

    def test_text_and(self):
        "Test AND Gate object creation from text"

        # 1. Create Gate object from text
        myobj = gate.Gate(text=EXAMPLE_AND)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 18)
        self.assertEqual(myobj.name, "z00")
        self.assertEqual(myobj.type, "AND")
        self.assertEqual(myobj.inputs, {"x00": None, "y00": None})
        self.assertEqual(myobj.output, None)

        # 3. Check methods
        self.assertEqual(myobj.waiting_on({}), set(["x00", "y00"]))
        self.assertEqual(myobj.process(WIRES), 0)
        self.assertEqual(myobj.process({}), 0)
        self.assertEqual(myobj.waiting_on({}), set())
        self.assertTrue(myobj.has_inputs("x00", "y00"))
        self.assertTrue(myobj.has_inputs("y00", "x00"))
        self.assertFalse(myobj.has_inputs("x00", "y01"))
        self.assertFalse(myobj.has_inputs("x00", None))

    def test_text_xor(self):
        "Test XOR Gate object creation from text"

        # 1. Create Gate object from text
        myobj = gate.Gate(text=EXAMPLE_XOR)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 18)
        self.assertEqual(myobj.name, "z01")
        self.assertEqual(myobj.type, "XOR")
        self.assertEqual(myobj.inputs, {"x01": None, "y01": None})
        self.assertEqual(myobj.output, None)

        # 3. Check methods
        self.assertEqual(myobj.waiting_on({}), set(["x01", "y01"]))
        self.assertEqual(myobj.process(WIRES), 0)
        self.assertEqual(myobj.process({}), 0)
        self.assertEqual(myobj.waiting_on({}), set())

    def test_text_or(self):
        "Test OR Gate object creation from text"

        # 1. Create Gate object from text
        myobj = gate.Gate(text=EXAMPLE_OR)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 17)
        self.assertEqual(myobj.name, "z02")
        self.assertEqual(myobj.type, "OR")
        self.assertEqual(myobj.inputs, {"x02": None, "y02": None})
        self.assertEqual(myobj.output, None)

        # 3. Check methods
        self.assertEqual(myobj.waiting_on({}), set(["x02", "y02"]))
        self.assertEqual(myobj.process(WIRES), 1)
        self.assertEqual(myobj.process({}), 1)
        self.assertEqual(myobj.waiting_on({}), set())

    def test_no_intuit_and(self):
        "Test AND Gate object without intuition"

        # 1. Create Gate object from text
        myobj = gate.Gate(text=EXAMPLE_AND)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 18)
        self.assertEqual(myobj.name, "z00")
        self.assertEqual(myobj.type, "AND")
        self.assertEqual(myobj.inputs, {"x00": None, "y00": None})
        self.assertEqual(myobj.output, None)

        # 3. Check methods
        self.assertEqual(myobj.waiting_on({}), set(["x00", "y00"]))
        self.assertEqual(myobj.process(NO_INTUIT), None)
        self.assertEqual(myobj.intuit(NO_INTUIT), None)
        self.assertEqual(myobj.process({}), None)
        self.assertEqual(myobj.waiting_on({}), set(["y00"]))

    def test_no_intuit_xor(self):
        "Test XOR Gate object without intuition"

        # 1. Create Gate object from text
        myobj = gate.Gate(text=EXAMPLE_XOR)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 18)
        self.assertEqual(myobj.name, "z01")
        self.assertEqual(myobj.type, "XOR")
        self.assertEqual(myobj.inputs, {"x01": None, "y01": None})
        self.assertEqual(myobj.output, None)

        # 3. Check methods
        self.assertEqual(myobj.waiting_on({}), set(["x01", "y01"]))
        self.assertEqual(myobj.process(NO_INTUIT), None)
        self.assertEqual(myobj.intuit(NO_INTUIT), None)
        self.assertEqual(myobj.process({}), None)
        self.assertEqual(myobj.waiting_on({}), set(["y01"]))

    def test_no_intuit_or(self):
        "Test OR Gate object without intuition"

        # 1. Create Gate object from text
        myobj = gate.Gate(text=EXAMPLE_OR)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 17)
        self.assertEqual(myobj.name, "z02")
        self.assertEqual(myobj.type, "OR")
        self.assertEqual(myobj.inputs, {"x02": None, "y02": None})
        self.assertEqual(myobj.output, None)

        # 3. Check methods
        self.assertEqual(myobj.waiting_on({}), set(["x02", "y02"]))
        self.assertEqual(myobj.process(NO_INTUIT), None)
        self.assertEqual(myobj.intuit(NO_INTUIT), None)
        self.assertEqual(myobj.process({}), None)
        self.assertEqual(myobj.waiting_on({}), set(["y02"]))

    def test_intuit_and(self):
        "Test AND Gate object with intuition"

        # 1. Create Gate object from text
        myobj = gate.Gate(text=EXAMPLE_AND)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 18)
        self.assertEqual(myobj.name, "z00")
        self.assertEqual(myobj.type, "AND")
        self.assertEqual(myobj.inputs, {"x00": None, "y00": None})
        self.assertEqual(myobj.output, None)

        # 3. Check methods
        self.assertEqual(myobj.waiting_on({}), set(["x00", "y00"]))
        self.assertEqual(myobj.process(INTUIT), None)
        self.assertEqual(myobj.intuit(INTUIT), 0)
        self.assertEqual(myobj.process({}), 0)
        self.assertEqual(myobj.waiting_on({}), set())

    def test_intuit_xor(self):
        "Test XOR Gate object with intuition"

        # 1. Create Gate object from text
        myobj = gate.Gate(text=EXAMPLE_XOR)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 18)
        self.assertEqual(myobj.name, "z01")
        self.assertEqual(myobj.type, "XOR")
        self.assertEqual(myobj.inputs, {"x01": None, "y01": None})
        self.assertEqual(myobj.output, None)

        # 3. Check methods
        self.assertEqual(myobj.waiting_on({}), set(["x01", "y01"]))
        self.assertEqual(myobj.process(INTUIT), None)
        self.assertEqual(myobj.intuit(INTUIT), None)
        self.assertEqual(myobj.process({}), None)
        self.assertEqual(myobj.waiting_on({}), set(["y01"]))

    def test_intuit_or(self):
        "Test OR Gate object with intuition"

        # 1. Create Gate object from text
        myobj = gate.Gate(text=EXAMPLE_OR)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 17)
        self.assertEqual(myobj.name, "z02")
        self.assertEqual(myobj.type, "OR")
        self.assertEqual(myobj.inputs, {"x02": None, "y02": None})
        self.assertEqual(myobj.output, None)

        # 3. Check methods
        self.assertEqual(myobj.waiting_on({}), set(["x02", "y02"]))
        self.assertEqual(myobj.process(INTUIT), None)
        self.assertEqual(myobj.intuit(INTUIT), 1)
        self.assertEqual(myobj.process({}), 1)
        self.assertEqual(myobj.waiting_on({}), set())

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                     t e s t _ g a t e . p y                    end
# ======================================================================
