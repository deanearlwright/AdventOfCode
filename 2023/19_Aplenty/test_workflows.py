
# ======================================================================
# Aplenty
#   Advent of Code 2023 Day 19 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                   t e s t _ w o r k f l o w s . p y
# ======================================================================
"Test Workflows for Advent of Code 2023 day 19, Aplenty"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import workflows
from part import Part

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
    "qqz{s>2770:qs,m<1801:hdj,R}",
    "gd{a>3333:R,R}",
    "hdj{m>838:A,pv}",
]
EXAMPLE_IN = "in{s<1351:px,qqz}"

EXAMPLE_PARTS = {
    "{x=787,m=2655,a=1222,s=2876}": "A",
    "{x=1679,m=44,a=2067,s=496}": "R",
    "{x=2036,m=264,a=79,s=2244}": "A",
    "{x=2461,m=1339,a=466,s=291}": "R",
    "{x=2127,m=1623,a=2188,s=1013}": "A",
}

# ======================================================================
#                                                          TestWorkflows
# ======================================================================


class TestWorkflows(unittest.TestCase):  # pylint: disable=R0904
    "Test Workflows object"

    def test_empty_init(self):
        "Test the default Workflows creation"

        # 1. Create default Workflows object
        myobj = workflows.Workflows()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, [])
        self.assertEqual(myobj.workflows, {})

    def test_text_init(self):
        "Test the Workflows object creation from text"

        # 1. Create Workflows object from text
        myobj = workflows.Workflows(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 10)
        self.assertEqual(len(myobj.workflows), 10)

        # 3. Check methods
        self.assertEqual(myobj.add_workflow(EXAMPLE_IN), "in")
        for part, result in EXAMPLE_PARTS.items():
            self.assertEqual(myobj.evaluate(Part(part)), result)

        self.assertEqual(myobj.combinations(), 167409079868000)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                t e s t _ w o r k f l o w s . p y               end
# ======================================================================
