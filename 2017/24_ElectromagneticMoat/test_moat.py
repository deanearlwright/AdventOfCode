# ======================================================================
# Electromagnetic Moat
#   Advent of Code 2017 Day 24 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                        t e s t _ m o a t . p y
# ======================================================================
"Test solver for Advent of Code 2017 day 24, Electromagnetic Moat"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_24
import moat

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = """
0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10
"""


BRIDGES = [
    [5],  # - 0/1
    [5, 6],  # - 0/1--10/1
    [5, 6, 7],  # - 0/1--10/1--9/10
    [0],  # - 0/2
    [0, 2],  # - 0/2--2/3
    [0, 2, 3],  # - 0/2--2/3--3/4
    [0, 2, 4],  # - 0/2--2/3--3/5
    [0, 1],  # - 0/2--2/2
    [0, 1, 2],  # - 0/2--2/2--2/3
    [0, 1, 2, 3],  # - 0/2--2/2--2/3--3/4
    [0, 1, 2, 4],  # - 0/2--2/2--2/3--3/5
]
STRENGTHS = [1, 12, 31, 2, 7, 14, 15, 6, 11, 18, 19]
LAST = [1, 10, 9, 2, 3, 4, 5, 2, 3, 4, 5]


BAD_BRIDGES = [
    [],  # No components
    [0, 1, 0],  # Reuses a component
    [0, 1, 6],  # Non matching ports
]

PART_ONE_TEXT = EXAMPLE_TEXT
PART_TWO_TEXT = EXAMPLE_TEXT

PART_ONE_RESULT = 31
PART_TWO_RESULT = 19

# ======================================================================
#                                                               TestMoat
# ======================================================================


class TestMoat(unittest.TestCase):  # pylint: disable=R0904
    "Test Moat object"

    def test_empty_init(self):
        "Test the default Moat creation"

        # 1. Create default Moat object
        myobj = moat.Moat()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.components, [])
        self.assertEqual(myobj.ports, {})

    def test_text_init(self):
        "Test the Moat object creation from text"

        # 1. Create Moat object from text
        myobj = moat.Moat(text=aoc_24.from_text(EXAMPLE_TEXT))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 8)
        self.assertEqual(len(myobj.components), 8)
        self.assertEqual(myobj.components[0], (0, 2))
        self.assertEqual(len(myobj.ports), 8)
        self.assertEqual(myobj.ports[0], [0, 5])

    def test_strength(self):
        "Test the Moat.strength function"

        # 1. Create Moat object from text
        myobj = moat.Moat(text=aoc_24.from_text(EXAMPLE_TEXT))

        # 2. Loop for all of the example bridges
        for bnum, bridge in enumerate(BRIDGES):

            # 3. Compute and compare strengths
            self.assertEqual(myobj.strength(bridge), STRENGTHS[bnum])

    def test_check_bridge(self):
        "Test the Moat.strength function"

        # 1. Create Moat object from text
        myobj = moat.Moat(text=aoc_24.from_text(EXAMPLE_TEXT))

        # 2. Loop for all of the example bridges
        for bridge in BRIDGES:

            # 3. They should all pass the test
            self.assertEqual(myobj.check_bridge(bridge), True)

        # 4. Loop for all of the incorrectly assembled bridges
        for bridge in BAD_BRIDGES:

            # 5. They should all fail the test
            self.assertEqual(myobj.check_bridge(bridge), False)

    def test_simple_bridges(self):
        "Test build a couple of bridges"

        # 1. Create Moat object from text
        myobj = moat.Moat(text=aoc_24.from_text(EXAMPLE_TEXT))

        # 2. Build one bridge
        bridge = myobj.build_a_bridge(first=True)

        # 3. Validate it
        self.assertEqual(myobj.check_bridge(bridge), True)
        self.assertEqual(bridge, [0, 1, 2, 3])

        # 4. Build a couple of random bridges
        for _ in range(50):

            # 5. Build a bridge
            bridge = myobj.build_a_bridge()

            # 6. Validate it
            self.assertEqual(myobj.check_bridge(bridge), True)
            self.assertTrue(bridge in BRIDGES)

    def test_last_port(self):
        "Test the Moat last_port function"

        # 1. Create Moat object from text
        myobj = moat.Moat(text=aoc_24.from_text(EXAMPLE_TEXT))

        # 2. Loop for all of the example bridges
        for bnum, bridge in enumerate(BRIDGES):

            # 3. Verify that hey have the expected last port
            self.assertEqual(myobj.last_port(bridge), LAST[bnum])

    def test_all_components(self):
        "Test the Moat all_components function"

        # 1. Create Moat object from text
        myobj = moat.Moat(text=aoc_24.from_text(EXAMPLE_TEXT))

        # 2. Components that can start a bridge
        self.assertEqual(list(myobj.all_components()), [0, 5])

        # 3. Components that can be the used after 0/1 starts a bridge
        self.assertEqual(list(myobj.all_components(bridge=[5])), [6])

        # 4. Components that can be the used after 0/1--10/1 starts a bridge
        self.assertEqual(list(myobj.all_components(bridge=[5, 6])), [7])

        # 5. Components that can be the used after 0/1--10/1--9/10 starts a bridge
        self.assertEqual(list(myobj.all_components(bridge=[5, 6, 7])), [])

    def test_all_bridges(self):
        "Test the Moat all_components function"

        # 1. Create Moat object from text
        myobj = moat.Moat(text=aoc_24.from_text(EXAMPLE_TEXT))

        # 2. Loop for all the bridges
        knt_bridges = 0
        for bridge in myobj.all_bridges():

            # 3. Validate it
            self.assertEqual(myobj.check_bridge(bridge), True)
            self.assertTrue(bridge in BRIDGES)

            # 4. Keep track of the number of bridges generated
            knt_bridges += 1

        # 5. Verify that we generated them all
        self.assertEqual(knt_bridges, len(BRIDGES))

    def test_part_one(self):
        "Test part one example of Moat object"

        # 1. Create Moat object from text
        myobj = moat.Moat(text=aoc_24.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Moat object"

        # 1. Create Moat object from text
        myobj = moat.Moat(part2=True, text=aoc_24.from_text(PART_TWO_TEXT))

        # 2. Check the part two
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                     t e s t _ m o a t . p y                    end
# ======================================================================
