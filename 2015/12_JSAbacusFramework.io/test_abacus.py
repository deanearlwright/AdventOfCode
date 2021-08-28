# ======================================================================
# JSAbacusFramework.io
#   Advent of Code 2015 Day 12 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ n u m b e r s . p y
# ======================================================================
"Test solver for Advent of Code 2015 day 12, JSAbacusFramework.io"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_12
import abacus

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
[1,{"c":"red","b":2},3]
"""

PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 6
PART_TWO_RESULT = 4

# ======================================================================
#                                                             TestAbacus
# ======================================================================


class TestAbacus(unittest.TestCase):  # pylint: disable=R0904
    "Test Abacus object"

    def test_empty_init(self):
        "Test the default Numbers creation"

        # 1. Create default Abacus object
        myobj = abacus.Abacus()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)

    def test_text_init(self):
        "Test the Abacus object creation from text"

        # 1. Create Abacus object from text
        myobj = abacus.Abacus(text=aoc_12.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 1)

        # 3. Check methods
        self.assertEqual(myobj.total_line('[1,2,3]'), 6)
        self.assertEqual(myobj.total_line('{"a":2,"b":4}'), 6)
        self.assertEqual(myobj.total_line('[[[3]]]'), 3)
        self.assertEqual(myobj.total_line('{"a":{"b":4},"c":-1}'), 3)
        self.assertEqual(myobj.total_line('{"a":[-1,1]}'), 0)
        self.assertEqual(myobj.total_line('[-1,{"a":1}]'), 0)
        self.assertEqual(myobj.total_line('[]'), 0)
        self.assertEqual(myobj.total_line('{}'), 0)
        self.assertEqual(myobj.total_json(), 6)

    def test_text_two(self):
        "Test the Abacus object creation from text for part two"

        # 1. Create Abacus object from text
        myobj = abacus.Abacus(text=aoc_12.from_text(EXAMPLE_TEXT), part2=True)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, True)
        self.assertEqual(len(myobj.text), 1)

        # 3. Check methods
        self.assertEqual(myobj.total_line('[1,2,3]'), 6)
        self.assertEqual(myobj.total_line('{"a":2,"b":4}'), 6)
        self.assertEqual(myobj.total_line('[[[3]]]'), 3)
        self.assertEqual(myobj.total_line('{"a":{"b":4},"c":-1}'), 3)
        self.assertEqual(myobj.total_line('{"a":[-1,1]}'), 0)
        self.assertEqual(myobj.total_line('[-1,{"a":1}]'), 0)
        self.assertEqual(myobj.total_line('[]'), 0)
        self.assertEqual(myobj.total_line('{}'), 0)
        self.assertEqual(myobj.total_json(), 4)

    def test_two_two(self):
        "Test the Abacus object creation from text two for part two"

        # 1. Create Abacus object from text
        myobj = abacus.Abacus(text=aoc_12.from_text(EXAMPLE_TEXT), part2=True)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, True)
        self.assertEqual(len(myobj.text), 1)

        # 3. Check methods
        self.assertEqual(myobj.find_left_brace('[1,{"c":"red","b":2},3]', 9), 3)
        self.assertEqual(myobj.find_right_brace('[1,{"c":"red","b":2},3]', 9), 19)
        self.assertEqual(myobj.find_left_brace('[{"a":1},{"c":"red","b":2},3]', 15), 9)
        self.assertEqual(myobj.find_right_brace('[{"a":1},{"c":"red","b":2},3]', 3), 7)
        self.assertEqual(myobj.find_left_brace('[1,{"z":{"a":[1,2]},c:"red","b":2},3]', 23), 3)
        self.assertEqual(myobj.find_right_brace('[1,{"z":{"a":[1,2]},c:"red","b":2},3]', 5), 33)

        self.assertEqual(myobj.eliminate_red('[1,2,3]'), '[1,2,3]')
        self.assertEqual(myobj.eliminate_red('[1,{"c":"red","b":2},3]'), '[1,,3]')
        self.assertEqual(myobj.eliminate_red('{"d":"red","e":[1,2,3,4],"f":5}'), '')
        self.assertEqual(myobj.eliminate_red('[{"d":"red","e":[1,2,3,4],"f":5},1]'), '[,1]')
        self.assertEqual(myobj.eliminate_red('[{"d":"red","e":[1,2,3,4],"f":5,"g":"red"},1]'),
                         '[,1]')
        self.assertEqual(myobj.eliminate_red(
            '{"e":"red","c":2,"a":1,"g":"blue","b":"green","d":"violet","f":170}'), '')
        self.assertEqual(myobj.eliminate_red(
            '[{"d":"red","e":{"a":"red","b":[1,2,3,4]},"f":5,"g":"red"},1]'), '[,1]')
        self.assertEqual(myobj.eliminate_red(
            '[{"d":"tan","e":{"a":"red","b":[1,2,3,4]},"f":5,"g":"red"},1]'), '[,1]')
        self.assertEqual(myobj.eliminate_red(
            '[{"d":"tan","e":{"a":"red","b":[1,2,3,4]},"f":5,"g":"tan"},1]'),
            '[{"d":"tan","e":,"f":5,"g":"tan"},1]')
        self.assertEqual(myobj.eliminate_red('[1,"red",5]'), '[1,"red",5]')
        self.assertEqual(myobj.total_json(), 4)

    def test_part_one(self):
        "Test part one example of Abacus object"

        # 1. Create Numbers object from text
        myobj = abacus.Abacus(text=aoc_12.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Abacus object"

        # 1. Create Numbers object from text
        myobj = abacus.Abacus(part2=True, text=aoc_12.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ a b a c u s . p y                 end
# ======================================================================
