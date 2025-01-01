
# ======================================================================
# LAN Party
#   Advent of Code 2024 Day 23 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ n e t w o r k . p y
# ======================================================================
"Test solver for Advent of Code 2024 day 23, LAN Party"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_23
import network

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn
"""
PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 7
PART_TWO_RESULT = "co,de,ka,ta"

# ======================================================================
#                                                            TestNetwork
# ======================================================================


class TestNetwork(unittest.TestCase):  # pylint: disable=R0904
    "Test Network object"

    def test_empty_init(self):
        "Test the default Network creation"

        # 1. Create default Network object
        myobj = network.Network()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.computers), 0)

    def test_text_init(self):
        "Test the Network object creation from text"

        # 1. Create Network object from text
        myobj = network.Network(text=aoc_23.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 32)
        self.assertEqual(len(myobj.computers), 16)

        # 3. Check methods
        no_ingrp = (set(), set(["yn", "wq", "vc", "cg"]))
        self.assertEqual(myobj.fill_set([no_ingrp], 3), set())
        xx_ingrp = (set(["xx"]), set(["yn", "wq", "vc", "cg"]))
        self.assertEqual(myobj.fill_set([xx_ingrp], 3), set())
        aq_ingrp = (set(["aq"]), set(["yn", "wq", "vc", "cg"]))
        self.assertEqual(len(myobj.fill_set([aq_ingrp], 3)), 2)
        co_ingrp = (set(["co"]), myobj.computers["co"])
        self.assertEqual(len(myobj.fill_set([co_ingrp], 3)), 3)

        self.assertEqual(len(myobj.all_sets()), 12)
        self.assertEqual(len(myobj.only_prefix()), 7)

        self.assertEqual(len(myobj.lan_sized(5)), 0)
        self.assertEqual(len(myobj.lan_sized(4)), 4)
        self.assertEqual(len(myobj.largest_subnet()), 4)
        self.assertEqual(myobj.password(frozenset({'de', 'co', 'ka', 'ta'})),
                         "co,de,ka,ta")
        self.assertEqual(myobj.password(myobj.largest_subnet()),
                         "co,de,ka,ta")

    def test_part_one(self):
        "Test part one example of Network object"

        # 1. Create Network object from text
        text = aoc_23.from_text(PART_ONE_TEXT)
        myobj = network.Network(text=text)

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Network object"

        # 1. Create Network object from text
        text = aoc_23.from_text(PART_TWO_TEXT)
        myobj = network.Network(part2=True, text=text)

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                  t e s t _ n e t w o r k . p y                 end
# ======================================================================
