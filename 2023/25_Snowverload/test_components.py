
# ======================================================================
# Snowverload
#   Advent of Code 2023 Day 25 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                   t e s t _ c o m p o n e n t s . p y
# ======================================================================
"Test Components for Advent of Code 2023 day 25, Snowverload"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import components

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = [
    "jqt: rhn xhk nvd",
    "rsh: frs pzl lsr",
    "xhk: hfx",
    "cmg: qnr nvd lhk bvb",
    "rhn: xhk bvb hfx",
    "bvb: xhk hfx",
    "pzl: lsr hfx nvd",
    "qnr: nvd",
    "ntq: jqt hfx bvb xhk",
    "nvd: lhk",
    "lsr: lhk",
    "rzs: qnr cmg lsr rsh",
    "frs: qnr lhk lsr",
]

# ======================================================================
#                                                         TestComponents
# ======================================================================


class TestComponents(unittest.TestCase):  # pylint: disable=R0904
    "Test Components object"

    def test_empty_init(self):
        "Test the default Components creation"

        # 1. Create default Components object
        myobj = components.Components()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.components), 0)

    def test_text_init(self):
        "Test the Components object creation from text"

        # 1. Create Components object from text
        myobj = components.Components(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 13)
        self.assertEqual(len(myobj.components), 15)
        self.assertEqual(myobj.components["jqt"].name, "jqt")
        self.assertEqual(myobj.components["jqt"].connections,
                         set(["rhn", "xhk", "nvd", "ntq"]))
        self.assertEqual(myobj.components["frs"].name, "frs")
        self.assertEqual(myobj.components["frs"].connections,
                         set(["qnr", "lhk", "lsr", "rsh"]))
# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end               t e s t _ c o m p o n e n t s . p y              end
# ======================================================================
