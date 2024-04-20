
# ======================================================================
# Snowverload
#   Advent of Code 2023 Day 25 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ c o n n e c t i o n s . p y
# ======================================================================
"Test Connections for Advent of Code 2023 day 25, Snowverload"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import connections
from components import Components

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
#                                                        TestConnections
# ======================================================================


class TestConnections(unittest.TestCase):  # pylint: disable=R0904
    "Test Connections object"

    def test_empty_init(self):
        "Test the default Connections creation"

        # 1. Create default Connections object
        myobj = connections.Connections()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.components, None)
        self.assertEqual(len(myobj.edges), 0)

    def test_text_init(self):
        "Test the Connections object creation from text"

        # 1. Create Connections object from text
        myobj = connections.Connections(Components(text=EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 13)
        self.assertEqual(myobj.components, None)
        self.assertEqual(len(myobj.edges), 33)

        # 3. Check methods
        self.assertEqual(myobj.karger(3), 54)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end              t e s t _ c o n n e c t i o n s . p y             end
# ======================================================================
