
# ======================================================================
# Aplenty
#   Advent of Code 2023 Day 19 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ w o r k f l o w . p y
# ======================================================================
"Test Workflow for Advent of Code 2023 day 19, Aplenty"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import workflow
from part import Part

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = "px{a<2006:qkq,m>2090:A,rfg}"

# ======================================================================
#                                                           TestWorkflow
# ======================================================================


class TestWorkflow(unittest.TestCase):  # pylint: disable=R0904
    "Test Workflow object"

    def test_empty_init(self):
        "Test the default Workflow creation"

        # 1. Create default Workflow object
        myobj = workflow.Workflow()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.name, "")
        self.assertEqual(myobj.rules, [])

    def test_text_init(self):
        "Test the Workflow object creation from text"

        # 1. Create Workflow object from text
        myobj = workflow.Workflow(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 27)
        self.assertEqual(myobj.name, "px")
        self.assertEqual(len(myobj.rules), 3)

        # 3. Check methods
        self.assertEqual(myobj.evaluate(Part("{x=787,m=2655,a=1222,s=2876}")), "qkq")
        self.assertEqual(myobj.evaluate(Part("{x=787,m=2655,a=2222,s=2876}")), "A")

        self.assertEqual(len(myobj.get_rules()), 3)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                 t e s t _ w o r k f l o w . p y                end
# ======================================================================
