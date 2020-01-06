# ======================================================================
# Recursive Circus
#   Advent of Code 2017 Day 07 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                       t e s t _ d i s c s . p y
# ======================================================================
"Test solver for Advent of Code 2017 day 7, Recursive Circus"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_07
import discs

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

P1_EXAMPLES_TEXT = """
pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)

! In this example, the disc on the bottom is tknk.
"""

# ======================================================================
#                                                               TestDisc
# ======================================================================


class TestDisc(unittest.TestCase):  # pylint: disable=R0904
    """Test Disc object"""

    def test_empty_init(self):
        """Test default Disc creation"""

        # 1. Create default Jumps object
        mydisc = discs.Disc()

        # 2. Make sure it has the default values
        self.assertEqual(mydisc.name, None)
        self.assertEqual(mydisc.weight, 0)
        self.assertEqual(mydisc.above, [])


    def test_value_init(self):
        """Test Disc creation with values"""

        # 1. Create Memory object with values
        #    fwft (72) -> ktlj, cntj, xhth
        mydisc = discs.Disc(name="fwft", weight=72,
                           above=["ktlj", "cntj", "xhth"])

        # 2. Make sure it has the specified values
        self.assertEqual(mydisc.name, "fwft")
        self.assertEqual(mydisc.weight, 72)
        self.assertEqual(mydisc.above, ["ktlj", "cntj", "xhth"])


    def test_text_init(self):
        """Test Disc creation from text"""

        # 1. Create Jumps object from text
        #    fwft (72) -> ktlj, cntj, xhth
        mydisc = discs.Disc(text="fwft (72) -> ktlj, cntj, xhth")

        # 2. Make sure it has the specified values
        self.assertEqual(mydisc.name, "fwft")
        self.assertEqual(mydisc.weight, 72)
        self.assertEqual(mydisc.above, ["ktlj", "cntj", "xhth"])


# ======================================================================
#                                                              TestDiscs
# ======================================================================


class TestDiscs(unittest.TestCase):  # pylint: disable=R0904
    """Test Memory object"""

    def test_empty_init(self):
        """Test default Discs creation"""

        # 1. Create default Jumps object
        mydiscs = discs.Discs()

        # 2. Make sure it has the default values
        self.assertEqual(mydiscs.part2, False)
        self.assertEqual(mydiscs.discs, {})


    def test_value_init(self):
        """Test Discs creation with values"""

        # 1. Create Discs object with values
        mydiscs = discs.Discs(text=["pbga (66)", "xhth (57)"])

        # 2. Make sure it has the specified values
        self.assertEqual(mydiscs.part2, False)
        self.assertEqual(len(mydiscs.discs), 2)
        self.assertEqual("pbga" in mydiscs.discs, True)
        self.assertEqual("xxxx" in mydiscs.discs, False)
        self.assertEqual(mydiscs.discs["pbga"].weight, 66)
        self.assertEqual(mydiscs.discs["xhth"].weight, 57)

        # 3. Check methods
        self.assertEqual(mydiscs.number_above("pbga"), 0)
        self.assertEqual(mydiscs.number_above("xhth"), 0)

    def test_text_init(self):
        """Test Discs creation from text"""

        # 1. Create Jumps object from text
        mydiscs = discs.Discs(text=aoc_07.from_text(P1_EXAMPLES_TEXT))

        # 2. Make sure it has the specified values
        self.assertEqual(mydiscs.part2, False)
        self.assertEqual(len(mydiscs.discs), 13)
        self.assertEqual("pbga" in mydiscs.discs, True)
        self.assertEqual("xxxx" in mydiscs.discs, False)
        self.assertEqual(mydiscs.discs["pbga"].name, "pbga")
        self.assertEqual(mydiscs.discs["pbga"].weight, 66)
        self.assertEqual(mydiscs.discs["pbga"].above, [])
        self.assertEqual(mydiscs.discs["fwft"].name, "fwft")
        self.assertEqual(mydiscs.discs["fwft"].weight, 72)
        self.assertEqual(mydiscs.discs["fwft"].above, ["ktlj", "cntj", "xhth"])

        # 3. Check methods
        self.assertEqual(mydiscs.number_above("pbga"), 0)
        self.assertEqual(mydiscs.number_above("xhth"), 0)
        self.assertEqual(mydiscs.number_above("fwft"), 3)
        self.assertEqual(mydiscs.number_above("tknk"), 12)
        self.assertEqual(mydiscs.bottom(), "tknk")

    def test_part_two(self):
        """Test Discs creation from text"""

        # 1. Create Jumps object from text
        mydiscs = discs.Discs(text=aoc_07.from_text(P1_EXAMPLES_TEXT),
                              part2=True)

        # 2. Make sure it has the specified values
        self.assertEqual(mydiscs.part2, True)
        self.assertEqual(len(mydiscs.discs), 13)
        self.assertEqual("pbga" in mydiscs.discs, True)
        self.assertEqual("xxxx" in mydiscs.discs, False)
        self.assertEqual(mydiscs.discs["pbga"].name, "pbga")
        self.assertEqual(mydiscs.discs["pbga"].weight, 66)
        self.assertEqual(mydiscs.discs["pbga"].above, [])
        self.assertEqual(mydiscs.discs["fwft"].name, "fwft")
        self.assertEqual(mydiscs.discs["fwft"].weight, 72)
        self.assertEqual(mydiscs.discs["fwft"].above, ["ktlj", "cntj", "xhth"])

        # 3. Check methods
        self.assertEqual(mydiscs.number_above("pbga"), 0)
        self.assertEqual(mydiscs.number_above("xhth"), 0)
        self.assertEqual(mydiscs.number_above("fwft"), 3)
        self.assertEqual(mydiscs.number_above("tknk"), 12)
        self.assertEqual(mydiscs.bottom(), "tknk")

        # 4. Check part two methods
        # ugml + (gyxo + ebii + jptl) = 68 + (61 + 61 + 61) = 251
        # padx + (pbga + havc + qoyq) = 45 + (66 + 66 + 66) = 243
        # fwft + (ktlj + cntj + xhth) = 72 + (57 + 57 + 57) = 243
        self.assertEqual(mydiscs.weight_above("gyxo"), 61)
        self.assertEqual(mydiscs.weight_above("ugml"), 251)
        self.assertEqual(mydiscs.weight_above("padx"), 243)
        self.assertEqual(mydiscs.weight_above("fwft"), 243)

        self.assertEqual(mydiscs.adjustment("tknk"), 243 - 251)
        self.assertEqual(mydiscs.adjustment("ugml"), 0)
        self.assertEqual(mydiscs.balance(), 60)



# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                     t e s t _ d i s c s . p y                  end
# ======================================================================
