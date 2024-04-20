
# ======================================================================
# Snowverload
#   Advent of Code 2023 Day 25 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ a p p a r a t u s . p y
# ======================================================================
"Test Apparatus for Advent of Code 2023 day 25, Snowverload"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import apparatus

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
#                                                          TestApparatus
# ======================================================================


class TestApparatus(unittest.TestCase):  # pylint: disable=R0904
    "Test Apparatus object"

    def test_empty_init(self):
        "Test the default Apparatus creation"

        # 1. Create default Apparatus object
        myobj = apparatus.Apparatus()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.components, None)
        self.assertEqual(myobj.connections, None)

    def test_text_init(self):
        "Test the Apparatus object creation from text"

        # 1. Create Apparatus object from text
        myobj = apparatus.Apparatus(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 13)
        self.assertNotEqual(myobj.components, None)
        self.assertNotEqual(myobj.connections, None)

        # 3. Check methods
        self.assertEqual(myobj.split(), 54)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                t e s t _ a p p a r a t u s . p y               end
# ======================================================================
