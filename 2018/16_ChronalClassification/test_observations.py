# ======================================================================
# Chronal Classification
#   Advent of Code 2018 Day 16 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                 t e s t _ o b s e r v a t i o n s . p y
# ======================================================================
"Tester for Advent of Code 2018 day 16, Chronal Classification"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_16
import observations
import device

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT_SINGLE = """
Before: [3, 2, 1, 1]
9 2 1 2
After:  [3, 2, 2, 1]"""

EXAMPLE_TEXT_MULTIPLE = """
Before: [3, 2, 1, 1]
9 2 1 2
After:  [3, 2, 2, 1]

Before: [2, 0, 0, 1]
15 3 1 3
After:  [2, 0, 0, 1]

Before: [3, 2, 3, 3]
4 3 3 0
After:  [3, 2, 3, 3]

Before: [3, 0, 1, 1]
15 3 1 3
After:  [3, 0, 1, 1]

Before: [0, 0, 2, 1]
15 3 1 3
After:  [0, 0, 2, 1]

Before: [3, 0, 3, 1]
15 3 1 0
After:  [1, 0, 3, 1]

Before: [2, 0, 1, 3]
15 2 1 0
After:  [1, 0, 1, 3]

Before: [1, 0, 2, 0]
15 0 1 1
After:  [1, 1, 2, 0]

Before: [1, 0, 2, 1]
15 0 1 0
After:  [1, 0, 2, 1]

Before: [1, 0, 2, 3]
15 0 1 2
After:  [1, 0, 1, 3]

Before: [1, 0, 2, 3]
15 0 1 1
After:  [1, 1, 2, 3]

Before: [0, 0, 1, 1]
15 2 1 0
After:  [1, 0, 1, 1]

Before: [2, 0, 1, 3]
15 2 1 1
After:  [2, 1, 1, 3]



"""


def inst_true(inst, regs):
    regs[2] = 2


def inst_false(inst, regs):
    regs[2] = 4


# ======================================================================
#                                                        TestObservation
# ======================================================================


class TestObservation(unittest.TestCase):  # pylint: disable=R0904
    "Test Single Observation object"

    def test_empty_init(self):
        "Test the default Observation creation"

        # 1. Create default Device object
        myobj = observations.Observation()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.before), 0)
        self.assertEqual(len(myobj.instruction), 0)
        self.assertEqual(len(myobj.after), 0)
        self.assertEqual(len(myobj.names), 0)

    def test_text_init(self):
        "Test the Device object creation from text"

        # 1. Create Device object from text
        myobj = observations.Observation(text=aoc_16.from_text(EXAMPLE_TEXT_SINGLE))

        # 2. Make sure it has the expected values
        self.assertEqual(len(myobj.text), 3)
        self.assertEqual(len(myobj.before), 4)
        self.assertEqual(len(myobj.instruction), 4)
        self.assertEqual(len(myobj.after), 4)
        self.assertEqual(myobj.before, [3, 2, 1, 1])
        self.assertEqual(myobj.instruction, [9, 2, 1, 2])
        self.assertEqual(myobj.after, [3, 2, 2, 1])
        self.assertEqual(len(myobj.names), 0)

        # 3. Test with instructions
        self.assertEqual(myobj.try_inst('true', inst_true), True)
        self.assertEqual(myobj.try_inst('false', inst_false), False)
        self.assertEqual(len(myobj.names), 1)
        self.assertEqual(myobj.names, set(['true']))

# ======================================================================
#                                                        TestObservation
# ======================================================================


class TestObservations(unittest.TestCase):  # pylint: disable=R0904
    "Test Multiple Observation object"

    def test_empty_init(self):
        "Test the default Observations creation"

        # 1. Create default Device object
        myobj = observations.Observations()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.data), 0)

    def test_text_init(self):
        "Test the Observation object creation from text"

        # 1. Create Device object from text
        myobj = observations.Observations(text=aoc_16.from_text(EXAMPLE_TEXT_MULTIPLE))

        # 2. Make sure it has the expected values
        self.assertEqual(len(myobj.text), 55)
        self.assertEqual(len(myobj.data), 13)
        self.assertEqual(myobj.data[0].before, [3, 2, 1, 1])
        self.assertEqual(myobj.data[0].instruction, [9, 2, 1, 2])
        self.assertEqual(myobj.data[0].after, [3, 2, 2, 1])

    def test_opcodes(self):
        "Test determining opcodes"
        # 1. Create Device object from text
        myobj = observations.Observations(text=aoc_16.from_text(EXAMPLE_TEXT_MULTIPLE))
        # 2. Make sure it has the expected values
        self.assertEqual(len(myobj.text), 55)
        self.assertEqual(len(myobj.data), 13)

        # 3. Process the observations
        myobj.process_observations(device.INSTS)
        self.assertEqual(myobj.data[0].names, set(['seti', 'addi', 'mulr']))
        self.assertEqual(myobj.data[1].names, set(['bani', 'eqri', 'gtrr', 'muli',
                                                   'borr', 'bori', 'addr', 'setr', 'gtir']))
        self.assertEqual(myobj.data[2].names, set(['seti', 'banr', 'borr', 'setr', 'bani', 'bori']))

        # 4. Evaluate the opcodes
        self.assertEqual(myobj.determine_opcodes(device.INSTS)[15], None)
        #                 set(['bori', 'gtrr', 'bani', 'setr', 'addr', 'borr', 'muli', 'eqri']))


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end            t e s t _ o b s e r v a t i o n s . p y             end
# ======================================================================

