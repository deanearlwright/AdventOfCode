# ======================================================================
# Extended Polymerization
#   Advent of Code 2021 Day 14 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ p o l y m e r . p y
# ======================================================================
"Test solver for Advent of Code 2021 day 14, Extended Polymerization"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_14
import polymer

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 1588
PART_TWO_RESULT = 2188189693529

# ======================================================================
#                                                            TestPolymer
# ======================================================================


class TestPolymer(unittest.TestCase):  # pylint: disable=R0904
    "Test Polymer object"

    def test_empty_init(self):
        "Test the default Polymer creation"

        # 1. Create default Polymer object
        myobj = polymer.Polymer()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.template, '')
        self.assertEqual(myobj.rules, {})

    def test_text_init(self):
        "Test the Polymer object creation from text"

        # 1. Create Polymer object from text
        myobj = polymer.Polymer(text=aoc_14.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 17)
        self.assertEqual(myobj.template, 'NNCB')
        self.assertEqual(len(myobj.rules), 16)

        # 3. Check methods
        self.assertEqual(myobj.element_diff('NNCB'), 2 - 1)
        self.assertEqual(myobj.element_diff('NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB'),
                         23 - 5)

        self.assertEqual(myobj.expand_once('NNCB'), 'NCNBCHB')
        self.assertEqual(myobj.expand_once('NCNBCHB'), 'NBCCNBBBCBHCB')
        self.assertEqual(myobj.expand_once('NBCCNBBBCBHCB'), 'NBBBCNCCNBBNBNBBCHBHHBCHB')
        self.assertEqual(myobj.expand_once('NBBBCNCCNBBNBNBBCHBHHBCHB'),
                         'NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB')

        self.assertEqual(myobj.expand_template(4),
                         'NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB')

        self.assertEqual(len(myobj.expand_template(5)), 97)
        self.assertEqual(myobj.element_diff((myobj.expand_template(10))), 1588)

    def test_text_init_two(self):
        "Test the Polymer object creation from text for part two"

        # 1. Create Polymer object from text
        myobj = polymer.Polymer(text=aoc_14.from_text(EXAMPLE_TEXT), part2=True)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, True)
        self.assertEqual(len(myobj.text), 17)
        self.assertEqual(myobj.template, 'NNCB')
        self.assertEqual(len(myobj.rules), 16)

        # 3. Check methods
        self.assertEqual(myobj.element_diff((myobj.expand_template(1))), 1)
        self.assertEqual(myobj.element_diff((myobj.expand_template(2))), 5)
        self.assertEqual(myobj.element_diff((myobj.expand_template(3))), 7)
        self.assertEqual(myobj.element_diff((myobj.expand_template(10))), 1588)
        self.assertEqual(myobj.element_diff((myobj.expand_template(40))), 2188189693529)

    def test_part_one(self):
        "Test part one example of Polymer object"

        # 1. Create Polymer object from text
        myobj = polymer.Polymer(text=aoc_14.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Polymer object"

        # 1. Create Polymer object from text
        myobj = polymer.Polymer(part2=True, text=aoc_14.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                  t e s t _ p o l y m e r . p y                 end
# ======================================================================
