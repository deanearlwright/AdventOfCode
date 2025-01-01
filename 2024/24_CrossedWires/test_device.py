
# ======================================================================
# Crossed Wires
#   Advent of Code 2024 Day 24 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ d e v i c e . p y
# ======================================================================
"Test solver for Advent of Code 2024 day 24, Crossed Wires"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_24
import device

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_ONE = """
x00: 1
x01: 1
x02: 1
y00: 0
y01: 1
y02: 0

x00 AND y00 -> z00
x01 XOR y01 -> z01
x02 OR y02 -> z02
"""
EXAMPLE_ONE_VALUES = {
    "z00": 0,
    "z01": 0,
    "z02": 1,
}

EXAMPLE_TWO = """
x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj
"""
EXAMPLE_TWO_VALUES = {
    "bfw": 1,
    "bqk": 1,
    "djm": 1,
    "ffh": 0,
    "fgs": 1,
    "frj": 1,
    "fst": 1,
    "gnj": 1,
    "hwm": 1,
    "kjc": 0,
    "kpj": 1,
    "kwq": 0,
    "mjb": 1,
    "nrd": 1,
    "ntg": 0,
    "pbm": 1,
    "psh": 1,
    "qhw": 1,
    "rvg": 0,
    "tgd": 0,
    "tnw": 1,
    "vdt": 1,
    "wpb": 0,
    "z00": 0,
    "z01": 0,
    "z02": 0,
    "z03": 1,
    "z04": 0,
    "z05": 1,
    "z06": 1,
    "z07": 1,
    "z08": 1,
    "z09": 1,
    "z10": 1,
    "z11": 0,
    "z12": 0,
}

EXAMPLE_THREE = """
x00: 0
x01: 1
x02: 0
x03: 1
x04: 0
x05: 1
y00: 0
y01: 0
y02: 1
y03: 1
y04: 0
y05: 1

x00 AND y00 -> z05
x01 AND y01 -> z02
x02 AND y02 -> z01
x03 AND y03 -> z03
x04 AND y04 -> z04
x05 AND y05 -> z00
"""
GOOD_ADDER = """
x00: 1
x01: 1
x02: 0
y00: 1
y01: 0
y02: 1

x00 AND y00 -> c00
x01 AND y01 -> a01
x02 AND y02 -> a02
x00 XOR y00 -> z00
x01 XOR y01 -> h01
x02 XOR y02 -> h02
h01 XOR c00 -> z01
h02 XOR c01 -> z02
h01 AND c00 -> b01
h02 AND c01 -> b02
b01 OR a01 -> c01
b02 OR a02 -> z03
"""
BAD_ADDER_ONE = """
x00: 1
x01: 1
x02: 0
y00: 1
y01: 0
y02: 1

x00 AND y00 -> c00
x01 AND y01 -> a01
x02 AND y02 -> a02
x00 XOR y00 -> z00
x01 XOR y01 -> h01
x02 XOR y02 -> h02
h01 XOR c00 -> c01
h02 XOR c01 -> z02
h01 AND c00 -> b01
h02 AND c01 -> b02
b01 OR a01 -> z01
b02 OR a02 -> z03
"""
BAD_ADDER_TWO = """
x00: 1
x01: 1
x02: 0
y00: 1
y01: 0
y02: 1

x00 AND y00 -> c00
x01 AND y01 -> a01
x02 AND y02 -> a02
x00 XOR y00 -> z00
x01 XOR y01 -> h01
x02 XOR y02 -> h02
h01 XOR c00 -> z01
h02 XOR c01 -> z03
h01 AND c00 -> b01
h02 AND c01 -> b02
b01 OR a01 -> c01
b02 OR a02 -> z02
"""


EXAMPLE_TEXT = EXAMPLE_ONE
PART_ONE_TEXT = EXAMPLE_TWO
PART_TWO_TEXT = BAD_ADDER_ONE

PART_ONE_RESULT = 2024
PART_TWO_RESULT = "c01,z01"

# ======================================================================
#                                                             TestDevice
# ======================================================================


class TestDevice(unittest.TestCase):  # pylint: disable=R0904
    "Test Device object"

    def test_empty_init(self):
        "Test the default Device creation"

        # 1. Create default Device object
        myobj = device.Device()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.wires), 0)
        self.assertEqual(len(myobj.gates), 0)

    def test_text_one(self):
        "Test the Device object creation from text"

        # 1. Create Device object from text
        myobj = device.Device(text=aoc_24.from_text(EXAMPLE_ONE))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 9)
        self.assertEqual(len(myobj.wires), 6)
        self.assertEqual(len(myobj.gates), 3)
        self.assertEqual(len(myobj.ands), 1)
        self.assertEqual(len(myobj.xors), 1)
        self.assertEqual(len(myobj.ors), 1)

        # 3. Check methods
        self.assertEqual(myobj.unknown_gates(), set())
        self.assertEqual(myobj.solve_unkowns(), set())
        self.assertEqual(myobj.unknown_gates(), set())
        for name, value in EXAMPLE_ONE_VALUES.items():
            self.assertTrue(name in myobj.wires, f"{name} is not in wires")
            self.assertEqual(myobj.wires[name], value,
                             f"wire {name} has value {myobj.wires[name]} not {value}")
        self.assertEqual(myobj.z_number(), 4)

        self.assertEqual(myobj.has_inputs("x00", "y00", myobj.ands), "z00")
        self.assertEqual(myobj.has_inputs("y00", "x00", myobj.ands), "z00")
        self.assertEqual(myobj.has_inputs("x00", "y00", myobj.ors), None)
        self.assertEqual(myobj.has_inputs("x02", "y02", myobj.ors), "z02")
        self.assertEqual(myobj.get_largest_z(), 2)

    def test_text_two(self):
        "Test the Device object creation from text"

        # 1. Create Device object from text
        myobj = device.Device(text=aoc_24.from_text(EXAMPLE_TWO))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 46)
        self.assertEqual(len(myobj.wires), 10)
        self.assertEqual(len(myobj.gates), 36)
        self.assertEqual(len(myobj.ands), 9)
        self.assertEqual(len(myobj.xors), 10)
        self.assertEqual(len(myobj.ors), 17)

        # 3. Check methods
        self.assertEqual(len(myobj.unknown_gates()), 13)
        self.assertEqual(myobj.solve_unkowns(), set())
        self.assertEqual(myobj.unknown_gates(), set())
        for name, value in EXAMPLE_TWO_VALUES.items():
            self.assertTrue(name in myobj.wires, f"{name} is not in wires")
            self.assertEqual(myobj.wires[name], value,
                             f"wire {name} has value {myobj.wires[name]} not {value}")
        self.assertEqual(myobj.z_number(), 2024)

    def test_text_three(self):
        "Test the Device object creation from text"

        # 1. Create Device object from text
        myobj = device.Device(text=aoc_24.from_text(EXAMPLE_THREE))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 18)
        self.assertEqual(len(myobj.wires), 12)
        self.assertEqual(len(myobj.gates), 6)
        self.assertEqual(len(myobj.ands), 6)
        self.assertEqual(len(myobj.xors), 0)
        self.assertEqual(len(myobj.ors), 0)

        # 3. Check methods
        self.assertEqual(len(myobj.unknown_gates()), 0)
        self.assertEqual(myobj.solve_unkowns(), set())
        self.assertEqual(myobj.unknown_gates(), set())
        self.assertEqual(myobj.z_number(), 9)  # 01001
        self.assertEqual(myobj.z_number(prefix="x"), 42)  # 101010
        self.assertEqual(myobj.z_number(prefix="y"), 44)  # 101100

        self.assertEqual(myobj.check_adder(), False)
        # self.assertEqual(myobj.fix_adder(), [])
        # self.assertEqual(myobj.check_adder(), True)

    def test_text_good_adder(self):
        "Test the Device object creation from text"

        # 1. Create Device object from text
        myobj = device.Device(text=aoc_24.from_text(GOOD_ADDER))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 18)
        self.assertEqual(len(myobj.wires), 6)
        self.assertEqual(len(myobj.gates), 12)
        self.assertEqual(len(myobj.ands), 5)
        self.assertEqual(len(myobj.xors), 5)
        self.assertEqual(len(myobj.ors), 2)

        # 3. Check methods
        self.assertEqual(myobj.solve_unkowns(), set())
        self.assertEqual(myobj.unknown_gates(), set())
        self.assertEqual(myobj.z_number(prefix="x"), 3)
        self.assertEqual(myobj.z_number(prefix="y"), 5)
        self.assertEqual(myobj.wires["c00"], 1)
        self.assertEqual(myobj.wires["a01"], 0)
        self.assertEqual(myobj.wires["a02"], 0)
        self.assertEqual(myobj.wires["z00"], 0)
        self.assertEqual(myobj.wires["h01"], 1)
        self.assertEqual(myobj.wires["h02"], 1)
        self.assertEqual(myobj.wires["b01"], 1)
        self.assertEqual(myobj.wires["b02"], 1)
        self.assertEqual(myobj.wires["c01"], 1)
        self.assertEqual(myobj.wires["z01"], 0)
        self.assertEqual(myobj.wires["z02"], 0)
        self.assertEqual(myobj.wires["z03"], 1)
        self.assertEqual(myobj.z_number(), 8)

        self.assertEqual(myobj.check_adder(), True)
        self.assertEqual(myobj.fix_adder(), set())
        self.assertEqual(myobj.check_adder(), True)

    def test_text_bad_adder_one(self):
        "Test the Device object creation from text"

        # 1. Create Device object from text
        myobj = device.Device(text=aoc_24.from_text(BAD_ADDER_ONE))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 18)
        self.assertEqual(len(myobj.wires), 6)
        self.assertEqual(len(myobj.gates), 12)
        self.assertEqual(len(myobj.ands), 5)
        self.assertEqual(len(myobj.xors), 5)
        self.assertEqual(len(myobj.ors), 2)

        # 3. Check methods
        self.assertEqual(myobj.solve_unkowns(), set())
        self.assertEqual(myobj.unknown_gates(), set())
        self.assertEqual(myobj.z_number(prefix="x"), 3)
        self.assertEqual(myobj.z_number(prefix="y"), 5)
        self.assertEqual(myobj.z_number(), 6)

        self.assertEqual(myobj.check_adder(), False)
        self.assertEqual(set(myobj.fix_adder()), set(["c01", "z01"]))
        self.assertEqual(myobj.check_adder(), True)

    def test_text_bad_adder_two(self):
        "Test the Device object creation from text"

        # 1. Create Device object from text
        myobj = device.Device(text=aoc_24.from_text(BAD_ADDER_TWO))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 18)
        self.assertEqual(len(myobj.wires), 6)
        self.assertEqual(len(myobj.gates), 12)
        self.assertEqual(len(myobj.ands), 5)
        self.assertEqual(len(myobj.xors), 5)
        self.assertEqual(len(myobj.ors), 2)

        # 3. Check methods
        self.assertEqual(myobj.solve_unkowns(), set())
        self.assertEqual(myobj.unknown_gates(), set())
        self.assertEqual(myobj.z_number(prefix="x"), 3)
        self.assertEqual(myobj.z_number(prefix="y"), 5)
        self.assertEqual(myobj.z_number(), 4)

        self.assertEqual(myobj.check_adder(), False)
        self.assertEqual(set(myobj.fix_adder()), set(["z02", "z03"]))
        self.assertEqual(myobj.check_adder(), True)

    def test_part_one(self):
        "Test part one example of Device object"

        # 1. Create Device object from text
        text = aoc_24.from_text(PART_ONE_TEXT)
        myobj = device.Device(text=text)

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Device object"

        # 1. Create Device object from text
        text = aoc_24.from_text(PART_TWO_TEXT)
        myobj = device.Device(part2=True, text=text)

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ d e v i c e . p y                  end
# ======================================================================
