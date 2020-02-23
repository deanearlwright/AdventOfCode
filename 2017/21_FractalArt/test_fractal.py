# ======================================================================
# Fractal Art
#   Advent of Code 2017 Day 21 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ f r a c t a l . p y
# ======================================================================
"Test solver for Advent of Code 2017 day 21, Fractal Art"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_21
import fractal

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#

"""

ENANCEMENT_ONE = "#..#........#..#"
ENANCEMENT_TWO = "##.##.#..#........##.##.#..#........"

SIZE_ZERO = 3
SIZE_ONE = 4
SIZE_TWO = 6

PIXELS_ZERO = 5
PIXELS_ONE = 4
PIXELS_TWO = 12

PART_ONE_TEXT = EXAMPLE_TEXT

PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = PIXELS_TWO
PART_TWO_RESULT = PIXELS_TWO

# ======================================================================
#                                                               TestRule
# ======================================================================


class TestRule(unittest.TestCase):  # pylint: disable=R0904
    "Test Fractal Art Rule object"

    def test_empty_init(self):
        "Test the default Fractal Art Rule creation"

        # 1. Create default Fractal object
        myobj = fractal.Rule()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.size, 0)
        self.assertEqual(myobj.base, [])
        self.assertEqual(myobj.matches, set())
        self.assertEqual(myobj.replace, "")

        # 3. Check methods
        self.assertEqual(myobj.match(".#...####"), None)

    def test_text_init2(self):
        "Test the Fractal Art Rule object creation from text"

        # 1. Create Fractal object from text
        myobj = fractal.Rule("../.# => ##./#../...")

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.text, "../.# => ##./#../...")
        self.assertEqual(myobj.size, 2)
        self.assertEqual(myobj.replace, "##.#.....")
        self.assertEqual(myobj.base, ['.', '.', '.', '#'])
        #print(myobj.matches)
        self.assertEqual(len(myobj.matches), 4)

        # 3. Check methods
        self.assertEqual(myobj.match(".#...####"), None)
        self.assertEqual(myobj.match("#..."), "##.#.....")
        self.assertEqual(myobj.match("...#"), "##.#.....")
        self.assertEqual(myobj.match("..##"), None)

    def test_text_init3(self):
        "Test the Fractal Art Rule object creation from text"

        # 1. Create Fractal object from text
        myobj = fractal.Rule(".#./..#/### => #..#/..../..../#..#")

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.text, ".#./..#/### => #..#/..../..../#..#")
        self.assertEqual(myobj.size, 3)
        self.assertEqual(myobj.replace, "#..#........#..#")
        self.assertEqual(myobj.base, ['.', '#', '.', '.', '.', '#', '#', '#', '#'])
        #print(myobj.matches)
        self.assertEqual(len(myobj.matches), 8)

        # 3. Check methods
        self.assertEqual(myobj.match(".#...####"), "#..#........#..#")

# ======================================================================
#                                                            TestFractal
# ======================================================================


class TestFractal(unittest.TestCase):  # pylint: disable=R0904
    "Test Fractal object"

    def test_empty_init(self):
        "Test the default Fractal creation"

        # 1. Create default Fractal object
        myobj = fractal.Fractal()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.art, fractal.INITIAL_PATTERN)
        self.assertEqual(myobj.art_size, fractal.INITIAL_SIZE)
        self.assertEqual(myobj.rules, {2: [], 3: []})

        # 3. Check methods
        self.assertEqual(myobj.pixels(), PIXELS_ZERO)
        self.assertEqual(len(list(myobj.squares())), 1)
        self.assertEqual(list(myobj.squares())[0], fractal.INITIAL_PATTERN)

    def test_text_init(self):
        "Test the Fractal object creation from text"

        # 1. Create Fractal object from text
        myobj = fractal.Fractal(text=aoc_21.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 2)
        self.assertEqual(myobj.art, fractal.INITIAL_PATTERN)
        self.assertEqual(myobj.art_size, fractal.INITIAL_SIZE)
        self.assertEqual(len(myobj.rules), 2)
        self.assertEqual(len(myobj.rules[2]), 1)
        self.assertEqual(len(myobj.rules[3]), 1)

        # 3. Check methods
        self.assertEqual(myobj.pixels(), PIXELS_ZERO)
        self.assertEqual(len(list(myobj.squares())), 1)
        self.assertEqual(list(myobj.squares())[0], fractal.INITIAL_PATTERN)
        self.assertEqual(myobj.transform(fractal.INITIAL_PATTERN), ENANCEMENT_ONE)

        # 4. Do one enhancement step
        #print("Step one")
        myobj.step()
        self.assertEqual(myobj.art, ENANCEMENT_ONE)
        self.assertEqual(myobj.art_size, SIZE_ONE)
        self.assertEqual(myobj.pixels(), PIXELS_ONE)

        # 5. And then another enhancement step
        #print("Step two")
        myobj.step()
        self.assertEqual(myobj.art, ENANCEMENT_TWO)
        self.assertEqual(myobj.art_size, SIZE_TWO)
        self.assertEqual(myobj.pixels(), PIXELS_TWO)

    def test_part_one(self):
        "Test part one example of Fractal object"

        # 1. Create Spinlock object from text
        myobj = fractal.Fractal(text=aoc_21.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False, limit=2), PART_ONE_RESULT)


    def test_part_two(self):
        "Test part two example of Fractal object"

        # 1. Create Spinlock object from text
        myobj = fractal.Fractal(part2=True, text=aoc_21.from_text(PART_TWO_TEXT))

        # 2. Check the part two
        self.assertEqual(myobj.part_two(verbose=False, limit=2), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                  t e s t _ f r a c t a l . p y                 end
# ======================================================================
