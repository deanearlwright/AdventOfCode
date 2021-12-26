# ======================================================================
# Arithmetic Logic Unit
#   Advent of Code 2021 Day 24 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ m o n a d . p y
# ======================================================================
"Test solver for Advent of Code 2021 day 24, Arithmetic Logic Unit"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_24
import monad

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
inp w
mul x 0
add x z
mod x 26
div z 1
add x 14
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 12
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 15
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 7
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 12
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 1
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 11
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 2
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -5
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 4
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 14
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 15
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 15
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 11
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -13
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 5
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -16
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 3
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -8
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 9
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 15
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 2
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -8
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 3
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x 0
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 3
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -4
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 11
mul y x
add z y
"""
EXAMPLE_DIGITS = "13579246899999"
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = "12996997829399"
PART_TWO_RESULT = "11841231117189"

# ======================================================================
#                                                              TestMonad
# ======================================================================


class TestMonad(unittest.TestCase):  # pylint: disable=R0904
    "Test Monad object"

    def test_empty_init(self):
        "Test the default Monad creation"

        # 1. Create default Monad object
        myobj = monad.Monad()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.alu, None)

    def test_text_init(self):
        "Test the Monad object creation from text"

        # 1. Create Monad object from text
        myobj = monad.Monad(text=aoc_24.from_text(EXAMPLE_TEXT), inp=EXAMPLE_DIGITS)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 252)
        self.assertEqual(len(myobj.alu.inst), 252)
        self.assertEqual(len(myobj.constants), 3)
        self.assertEqual(len(myobj.constants[0]), 14)
        self.assertEqual(myobj.constants[0][0], 1)
        self.assertEqual(myobj.constants[1][0], 14)
        self.assertEqual(myobj.constants[2][0], 12)
        self.assertEqual(myobj.constants[0][7], 26)
        self.assertEqual(myobj.constants[1][7], -13)
        self.assertEqual(myobj.constants[2][7], 5)
        self.assertEqual(myobj.constants[0][13], 26)
        self.assertEqual(myobj.constants[1][13], -4)
        self.assertEqual(myobj.constants[2][13], 11)
        self.assertEqual(len(myobj.alu.inp), 14)
        self.assertEqual(myobj.alu.inp[0], 1)
        self.assertEqual(myobj.alu.inp[13], 9)

        # 3. Check methods
        result = myobj.alu.run()
        self.assertEqual(myobj.run(EXAMPLE_DIGITS), result)

        self.assertEqual(myobj.unrun(digits=monad.DIGITS), PART_ONE_RESULT)
        self.assertEqual(myobj.unrun(digits=monad.STIGID), PART_TWO_RESULT)

    def test_part_one(self):
        "Test part one example of Monad object"

        # 1. Create Monad object from text
        myobj = monad.Monad(text=aoc_24.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Monad object"

        # 1. Create Monad object from text
        myobj = monad.Monad(part2=True, text=aoc_24.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ m o n a d . p y                   end
# ======================================================================
