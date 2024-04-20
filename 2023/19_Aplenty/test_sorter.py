
# ======================================================================
# Aplenty
#   Advent of Code 2023 Day 19 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                      t e s t _ s o r t e r . p y
# ======================================================================
"Test Sorter for Advent of Code 2023 day 19, Aplenty"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import sorter

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = [
    "px{a<2006:qkq,m>2090:A,rfg}",
    "pv{a>1716:R,A}",
    "lnx{m>1548:A,A}",
    "rfg{s<537:gd,x>2440:R,A}",
    "qs{s>3448:A,lnx}",
    "qkq{x<1416:A,crn}",
    "crn{x>2662:A,R}",
    "in{s<1351:px,qqz}",
    "qqz{s>2770:qs,m<1801:hdj,R}",
    "gd{a>3333:R,R}",
    "hdj{m>838:A,pv}",
    "{x=787,m=2655,a=1222,s=2876}",
    "{x=1679,m=44,a=2067,s=496}",
    "{x=2036,m=264,a=79,s=2244}",
    "{x=2461,m=1339,a=466,s=291}",
    "{x=2127,m=1623,a=2188,s=1013}",
]

# ======================================================================
#                                                             TestSorter
# ======================================================================


class TestSorter(unittest.TestCase):  # pylint: disable=R0904
    "Test Sorter object"

    def test_empty_init(self):
        "Test the default Sorter creation"

        # 1. Create default Sorter object
        myobj = sorter.Sorter()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.workflows, None)
        self.assertEqual(myobj.parts, [])

    def test_text_init(self):
        "Test the Sorter object creation from text"

        # 1. Create Sorter object from text
        myobj = sorter.Sorter(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 16)
        self.assertNotEqual(myobj.workflows, None)
        self.assertEqual(len(myobj.parts), 5)
        self.assertEqual(len(myobj.workflows.workflows), 11)

        # 3. Check methods
        self.assertEqual(myobj.evaluate_all(), 19114)

        self.assertEqual(myobj.combinations(), 167409079868000)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ s o r t e r . p y                  end
# ======================================================================
