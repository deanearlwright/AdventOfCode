# ======================================================================
# Handy Haversacks
#   Advent of Code 2020 Day 07 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ r u l e s . p y
# ======================================================================
"Test single rule for Advent of Code 2020 day 07, Handy Haversacks"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import rule

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = "light red bags contain 1 bright white bag, 2 muted yellow bags."
EXAMPLES = [
    {'text': 'light red bags contain 1 bright white bag, 2 muted yellow bags.', 'sum': 3, 'can': None},
    {'text': 'dark orange bags contain 3 bright white bags, 4 muted yellow bags.', 'sum': 7, 'can': None},
    {'text': 'bright white bags contain 1 shiny gold bag.', 'sum': 1, 'can': True},
    {'text': 'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.', 'sum': 11, 'can': True},
    {'text': 'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.', 'sum': 3, 'can': None},
    {'text': 'dark olive bags contain 3 faded blue bags, 4 dotted black bags.', 'sum': 7, 'can': None},
    {'text': 'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.', 'sum': 11, 'can': None},
    {'text': 'faded blue bags contain no other bags.', 'sum': 0, 'can': False},
    {'text': 'dotted black bags contain no other bags.', 'sum': 0, 'can': False},
]

# ======================================================================
#                                                               TestRule
# ======================================================================


class TestRule(unittest.TestCase):  # pylint: disable=R0904
    "Test Rule object"

    def test_empty_init(self):
        "Test the default Rule creation"

        # 1. Create default Rule object
        myobj = rule.Rule()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.bag, None)
        self.assertEqual(myobj.bags, [])
        self.assertEqual(myobj.numbers, [])
        self.assertEqual(myobj.can_contain_shiny_gold, None)

    def test_text_init(self):
        "Test the Rule object creation from text"

        # 1. Create Rule object from text
        myobj = rule.Rule(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, EXAMPLE_TEXT)
        self.assertEqual(myobj.bag, 'light red')
        self.assertEqual(myobj.bags, ['bright white', 'muted yellow'])
        self.assertEqual(myobj.numbers, [1, 2])
        self.assertEqual(myobj.can_contain_shiny_gold, None)

        # 3. Check methods
        self.assertEqual(myobj.sumation(), 3)

    def test_part_one(self):
        "Test part one examples of Rule object"

        # 1. Loop for all the examples
        for example in EXAMPLES:

            # 2. Create Rule object from text
            myobj = rule.Rule(text=example['text'])

            # 3. Check the part one result
            self.assertEqual(myobj.sumation(), example['sum'])
            self.assertEqual(myobj.can_contain_shiny_gold, example['can'])


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                     t e s t _ r u l e . p y                    end
# ======================================================================
