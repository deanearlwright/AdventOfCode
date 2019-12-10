# ======================================================================
# Sensor Boost
#   Advent of Code 2019 Day 09 -- Eric Wastl -- https://adventofcode.com
#
# codeuter simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                       t e s t _ i n t c o d e . p y
# ======================================================================
"Test computer for Advent of Code 2019 day 09, Sensor Boost"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import intcode

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                            TestUtility
# ======================================================================

class TestUtility(unittest.TestCase):  # pylint: disable=R0904
    """Test Utility Functions"""

    def test_op_name(self):
        """Test op_name function"""

        self.assertEqual(intcode.op_name(None), '<->')
        self.assertEqual(intcode.op_name(-1), '???')
        self.assertEqual(intcode.op_name(1), 'ADD')
        self.assertEqual(intcode.op_name(2), 'MUL')
        self.assertEqual(intcode.op_name(3), 'INP')
        self.assertEqual(intcode.op_name(4), 'OUT')
        self.assertEqual(intcode.op_name(99), 'HLT')

    def test_split_op(self):
        """Test split_op function"""

        self.assertEqual(intcode.split_op(None), (None, []))
        self.assertEqual(intcode.split_op(44), (44, []))
        self.assertEqual(intcode.split_op(1), (1, [0, 0, 0]))
        self.assertEqual(intcode.split_op(101), (1, [1, 0, 0]))
        self.assertEqual(intcode.split_op(1001), (1, [0, 1, 0]))
        self.assertEqual(intcode.split_op(10001), (1, [0, 0, 1]))
        self.assertEqual(intcode.split_op(3), (3, [0]))
        self.assertEqual(intcode.split_op(103), (3, [1]))


# ======================================================================
#                                                            TestIntcode
# ======================================================================


class TestIntcode(unittest.TestCase):  # pylint: disable=R0904
    """Test Intcode object"""

    def test_empty_init(self):
        """Test default intcode object creation"""

        # 1. Create default Intcode object
        mycode = intcode.IntCode()

        # 2. Make sure it has the default values
        self.assertEqual(mycode.counter, 0)
        self.assertEqual(mycode.rbase, 0)
        self.assertEqual(len(mycode.positions), 0)
        self.assertEqual(len(mycode.inp), 0)
        self.assertEqual(len(mycode.out), 0)

        # 3. Check methods
        self.assertEqual(mycode.fetch(0), 0)
        self.assertEqual(mycode.alter(0, 0), 0)
        self.assertEqual(mycode.step(), intcode.STOP_BAD)
        mycode.reset()
        self.assertEqual(mycode.run(), intcode.STOP_BAD)

    def test_value_init(self):
        """Test Intcode object creation with values"""

        # 1. Create Intcode obhect with values
        mycode = intcode.IntCode(counter=0, positions=[99, 30, 40, 50])

        # 2. Make sure it has the specified values
        self.assertEqual(mycode.counter, 0)
        self.assertEqual(len(mycode.positions), 4)
        self.assertEqual(mycode.positions, [99, 30, 40, 50])

        # 3. Check methods
        self.assertEqual(mycode.fetch(0), 99)
        self.assertEqual(mycode.alter(0, 99), 99)
        self.assertEqual(mycode.step(), intcode.STOP_HLT)
        mycode.reset()
        self.assertEqual(mycode.run(), intcode.STOP_HLT)

    def test_text_init(self):
        """Test Intcode object creation with text"""

        # 1. Create Intcode obhect with values
        mycode = intcode.IntCode(text='1,0,4,3,99')

        # 2. Make sure it has the specified values
        self.assertEqual(mycode.counter, 0)
        self.assertEqual(len(mycode.positions), 5)
        self.assertEqual(mycode.positions, [1, 0, 4, 3, 99])

        # 3. Check methods
        self.assertEqual(mycode.fetch(0), 1)
        self.assertEqual(mycode.alter(0, 1), 1)
        self.assertEqual(mycode.step(), intcode.STOP_RUN)
        self.assertEqual(mycode.positions, [1, 0, 4, 100, 99])
        self.assertEqual(mycode.alter(3, 3), 100)
        self.assertEqual(mycode.positions, [1, 0, 4, 3, 99])
        mycode.reset()
        self.assertEqual(mycode.run(), intcode.STOP_HLT)
        self.assertEqual(mycode.positions, [1, 0, 4, 100, 99])

    def test_samples(self):
        """Test Intcode object with samples from problem description"""

        # 1. 1,0,0,0,99 becomes 2,0,0,0,99 (1 + 1 = 2)
        mycode = intcode.IntCode(text='1,0,0,0,99')
        self.assertEqual(mycode.run(), intcode.STOP_HLT)
        self.assertEqual(mycode.positions, [2, 0, 0, 0, 99])

        # 2. 2,3,0,3,99 becomes 2,3,0,6,99 (3 * 2 = 6)
        mycode = intcode.IntCode(text='2,3,0,3,99')
        self.assertEqual(mycode.run(), intcode.STOP_HLT)
        self.assertEqual(mycode.positions, [2, 3, 0, 6, 99])

        # 3. 2,4,4,5,99,0 becomes 2,4,4,5,99,9801 (99 * 99 = 9801)
        mycode = intcode.IntCode(text='2,4,4,5,99,0')
        self.assertEqual(mycode.run(), intcode.STOP_HLT)
        self.assertEqual(mycode.positions, [2, 4, 4, 5, 99, 9801])

        # 4. 1,1,1,4,99,5,6,0,99 becomes 30,1,1,4,2,5,6,0,99
        mycode = intcode.IntCode(text='1,1,1,4,99,5,6,0,99')
        self.assertEqual(mycode.run(), intcode.STOP_HLT)
        self.assertEqual(mycode.positions, [30, 1, 1, 4, 2, 5, 6, 0, 99])

        # 5. 1,9,10,3,2,3,11,0,99,30,40,50 becomes 3500,9,10,70,2,3,11,0,99,30,40,50
        mycode = intcode.IntCode(text='1,9,10,3,2,3,11,0,99,30,40,50')
        self.assertEqual(mycode.run(), intcode.STOP_HLT)
        self.assertEqual(mycode.positions,
                         [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50])

        # 6. 3,5,3,6,1101,0,0,9,104,0,99 becomes 3,5,3,6,1101,127,32,9,104,0,99
        #    Inputs two numbers (127 and 32) and output the sum as 159
        mycode = intcode.IntCode(text='3,5,3,6,1101,0,0,9,104,159,99')
        self.assertEqual(mycode.run(inp=[127, 32]), intcode.STOP_HLT)
        self.assertEqual(mycode.positions,
                         [3, 5, 3, 6, 1101, 127, 32, 9, 104, 159, 99])
        self.assertEqual(mycode.outputs(), [159])

    def test_part_two_samples(self):
        """Test Intcode object with samples from part two description"""

        # 1. 3,9,8,9,10,9,4,9,99,-1,8 outputs 1 if input is 8 else 0
        mycode = intcode.IntCode(text='3,9,8,9,10,9,4,9,99,-1,8')
        self.assertEqual(mycode.run(inp=[8]), intcode.STOP_HLT)
        self.assertEqual(mycode.outputs(), [1])
        mycode = intcode.IntCode(text='3,9,8,9,10,9,4,9,99,-1,8')
        self.assertEqual(mycode.run(inp=[4]), intcode.STOP_HLT)
        self.assertEqual(mycode.outputs(), [0])

        # 2. 3,9,7,9,10,9,4,9,99,-1,8 outputs 1 if input less than 8 else 0
        mycode = intcode.IntCode(text='3,9,7,9,10,9,4,9,99,-1,8')
        self.assertEqual(mycode.run(inp=[4]), intcode.STOP_HLT)
        self.assertEqual(mycode.outputs(), [1])
        mycode = intcode.IntCode(text='3,9,7,9,10,9,4,9,99,-1,8')
        self.assertEqual(mycode.run(inp=[9]), intcode.STOP_HLT)
        self.assertEqual(mycode.outputs(), [0])

        # 3. 3,3,1108,-1,8,3,4,3,99 outputs 1 if input is 8 else 0
        mycode = intcode.IntCode(text='3,3,1108,-1,8,3,4,3,99')
        self.assertEqual(mycode.run(inp=[8]), intcode.STOP_HLT)
        self.assertEqual(mycode.outputs(), [1])
        mycode = intcode.IntCode(text='3,3,1108,-1,8,3,4,3,99')
        self.assertEqual(mycode.run(inp=[4]), intcode.STOP_HLT)
        self.assertEqual(mycode.outputs(), [0])

        # 4. 3,3,1107,-1,8,3,4,3,99 outputs 1 if input less than 8 else 0
        mycode = intcode.IntCode(text='3,3,1107,-1,8,3,4,3,99')
        self.assertEqual(mycode.run(inp=[4]), intcode.STOP_HLT)
        self.assertEqual(mycode.outputs(), [1])
        mycode = intcode.IntCode(text='3,3,1107,-1,8,3,4,3,99')
        self.assertEqual(mycode.run(inp=[9]), intcode.STOP_HLT)
        self.assertEqual(mycode.outputs(), [0])
        # 5. 3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9 outputs 0 if input is 0 else 1
        mycode = intcode.IntCode(text='3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9')
        self.assertEqual(mycode.run(inp=[0]), intcode.STOP_HLT)
        self.assertEqual(mycode.outputs(), [0])
        mycode = intcode.IntCode(text='3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9')
        self.assertEqual(mycode.run(inp=[42]), intcode.STOP_HLT)
        self.assertEqual(mycode.outputs(), [1])

        # 6. 3,3,1105,-1,9,1101,0,0,12,4,12,99,1 outputs 0 if input is 0 else 1
        mycode = intcode.IntCode(text='3,3,1105,-1,9,1101,0,0,12,4,12,99,1')
        self.assertEqual(mycode.run(inp=[0]), intcode.STOP_HLT)
        self.assertEqual(mycode.outputs(), [0])
        mycode = intcode.IntCode(text='3,3,1105,-1,9,1101,0,0,12,4,12,99,1')
        self.assertEqual(mycode.run(inp=[666]), intcode.STOP_HLT)
        self.assertEqual(mycode.outputs(), [1])

        # 7. Larger example, output 999 if input < 0, 1000 if 0, 1001 if > 0
        prog = ''.join([
            '3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,',
            '1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,',
            '999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99',])
        mycode = intcode.IntCode(text=prog)
        self.assertEqual(mycode.run(inp=[8]), intcode.STOP_HLT)
        self.assertEqual(mycode.outputs(), [1000])
        mycode = intcode.IntCode(text=prog)
        self.assertEqual(mycode.run(inp=[3]), intcode.STOP_HLT)
        self.assertEqual(mycode.outputs(), [999])
        mycode = intcode.IntCode(text=prog)
        self.assertEqual(mycode.run(inp=[666]), intcode.STOP_HLT)
        self.assertEqual(mycode.outputs(), [1001])

    def test_sensor_boost(self):
        """Test Intcode object with samples from day 9"""

        # 1. Takes no input and produces a copy of itself as output.
        mycode = intcode.IntCode(text='109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99')
        self.assertEqual(mycode.run(), intcode.STOP_HLT)
        self.assertEqual(mycode.outputs(), [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99])

        # 2. 1102,34915192,34915192,7,4,7,99,0 should output a 16-digit number.
        mycode = intcode.IntCode(text='1102,34915192,34915192,7,4,7,99,0')
        self.assertEqual(mycode.run(), intcode.STOP_HLT)
        self.assertEqual(mycode.outputs(), [1219070632396864])

        # 3. 104,1125899906842624,99 should output the large number in the middle.
        mycode = intcode.IntCode(text='104,1125899906842624,99')
        self.assertEqual(mycode.run(), intcode.STOP_HLT)
        self.assertEqual(mycode.outputs(), [1125899906842624])

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ i n t c o d e . p y                  end
# ======================================================================
