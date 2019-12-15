# ======================================================================
# Space Stoichiometry
#   Advent of Code 2019 Day 14 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ n a n o f a c t o r y . p y
# ======================================================================
"Test ships' hull for Advent of Code 2019 day 14, Space Stoichiometry"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import nanofactory

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXP1_TEXT = [
    '10 ORE => 10 A',
    '1 ORE => 1 B',
    '7 A, 1 B => 1 C',
    '7 A, 1 C => 1 D',
    '7 A, 1 D => 1 E',
    '7 A, 1 E => 1 FUEL'
]
EXP1_ORE = 31

EXP2_TEXT = [
    '9 ORE => 2 A',
    '8 ORE => 3 B',
    '7 ORE => 5 C',
    '3 A, 4 B => 1 AB',
    '5 B, 7 C => 1 BC',
    '4 C, 1 A => 1 CA',
    '2 AB, 3 BC, 4 CA => 1 FUEL'
]
EXP2_ORE = 165

EXP3_TEXT = [
    '157 ORE => 5 NZVS',
    '165 ORE => 6 DCFZ',
    '44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL',
    '12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ',
    '179 ORE => 7 PSHF',
    '177 ORE => 5 HKGWZ',
    '7 DCFZ, 7 PSHF => 2 XJWVT',
    '165 ORE => 2 GPVTF',
    '3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT'
]
EXP3_ORE = 13312
EXP3_TRILLION = 82892753

EXP4_TEXT = [
    '2 VPVL, 7 FWMGM, 2 CXFTF, 11 MNCFX => 1 STKFG',
    '17 NVRVD, 3 JNWZP => 8 VPVL',
    '53 STKFG, 6 MNCFX, 46 VJHF, 81 HVMC, 68 CXFTF, 25 GNMV => 1 FUEL',
    '22 VJHF, 37 MNCFX => 5 FWMGM',
    '139 ORE => 4 NVRVD',
    '144 ORE => 7 JNWZP',
    '5 MNCFX, 7 RFSQX, 2 FWMGM, 2 VPVL, 19 CXFTF => 3 HVMC',
    '5 VJHF, 7 MNCFX, 9 VPVL, 37 CXFTF => 6 GNMV',
    '145 ORE => 6 MNCFX',
    '1 NVRVD => 8 CXFTF',
    '1 VJHF, 6 MNCFX => 4 RFSQX',
    '176 ORE => 6 VJHF'
]
EXP4_ORE = 180697
EXP3_TRILLION = 82892753

EXP5_TEXT = [
    '171 ORE => 8 CNZTR',
    '7 ZLQW, 3 BMBT, 9 XCVML, 26 XMNCP, 1 WPTQ, 2 MZWV, 1 RJRHP => 4 PLWSL',
    '7 ORE => 5 C',
    '114 ORE => 4 BHXH',
    '14 VRPVC => 6 BMBT',
    '6 BHXH, 18 KTJDG, 12 WPTQ, 7 PLWSL, 31 FHTLT, 37 ZDVW => 1 FUEL',
    '6 WPTQ, 2 BMBT, 8 ZLQW, 18 KTJDG, 1 XMNCP, 6 MZWV, 1 RJRHP => 6 FHTLT',
    '15 XDBXC, 2 LTCX, 1 VRPVC => 6 ZLQW',
    '13 WPTQ, 10 LTCX, 3 RJRHP, 14 XMNCP, 2 MZWV, 1 ZLQW => 1 ZDVW',
    '5 BMBT => 4 WPTQ',
    '189 ORE => 9 KTJDG',
    '1 MZWV, 17 XDBXC, 3 XCVML => 2 XMNCP',
    '12 VRPVC, 27 CNZTR => 2 XDBXC',
    '15 KTJDG, 12 BHXH => 5 XCVML',
    '3 BHXH, 2 VRPVC => 7 MZWV',
    '121 ORE => 7 VRPVC',
    '7 XCVML => 6 RJRHP',
    '5 BHXH, 4 VRPVC => 5 LTCX'
]
EXP5_ORE = 2210736

# ======================================================================
#                                                        TestNanoFactory
# ======================================================================


class TestNanoFactory(unittest.TestCase):  # pylint: disable=R0904
    """Test NanoFactory object"""

    def test_empty_init(self):
        """Test default NanoFactory object creation"""

        # 1. Create a default factory
        myfactory = nanofactory.NanoFactory()

        # 2. Make sure it has the default values
        self.assertEqual(myfactory.resources, {})
        self.assertEqual(myfactory.recipes, {})
        self.assertEqual(myfactory.ore, 0)

        # 3. Test producing ore
        self.assertEqual(myfactory.produce('3 ORE'), True)
        self.assertEqual(myfactory.ore, 3)
        self.assertEqual(myfactory.produce('1 ORE'), True)
        self.assertEqual(myfactory.ore, 4)

    def test_text_init(self):
        """Test NanoFactory object creation with text"""

        # 1. Create a factory with reactions in text
        myfactory = nanofactory.NanoFactory(text=EXP1_TEXT)

        # 2. Make sure it has the default values
        self.assertEqual(len(myfactory.resources), 0)
        self.assertEqual(len(myfactory.recipes), 6)
        self.assertEqual(myfactory.ore, 0)

        # 3. Test producing ore
        self.assertEqual(myfactory.produce('3 ORE'), True)
        self.assertEqual(myfactory.ore, 3)
        self.assertEqual(myfactory.produce('1 ORE'), True)
        self.assertEqual(myfactory.ore, 4)
        myfactory.ore = 0

        # 4. Test a simple recipe
        self.assertEqual(myfactory.produce('1 B'), True)
        self.assertEqual(myfactory.resources['B'], 0)
        self.assertEqual(myfactory.ore, 1)
        myfactory.ore = 0

        # 5. Test a silightly mor complicated recipe
        self.assertEqual(myfactory.produce('1 C'), True)
        self.assertEqual(myfactory.resources['A'], 3)
        self.assertEqual(myfactory.ore, 11)
        myfactory.ore = 0

        # 6. And now try to make FUEL
        self.assertEqual(myfactory.produce('1 FUEL'), True)
        self.assertEqual(myfactory.resources['A'], 5)
        self.assertEqual(myfactory.ore, EXP1_ORE)
        myfactory.ore = 0

    def test_examples(self):
        """Test NanoFactory examples"""

        # 1. Create and run factory for example 1
        myfactory = nanofactory.NanoFactory(text=EXP1_TEXT)
        self.assertEqual(myfactory.produce('1 FUEL'), True)
        self.assertEqual(myfactory.ore, EXP1_ORE)

        # 2. Create and run factory for example 2
        myfactory = nanofactory.NanoFactory(text=EXP2_TEXT)
        self.assertEqual(myfactory.produce('1 FUEL'), True)
        self.assertEqual(myfactory.ore, EXP2_ORE)

        # 3. Create and run factory for example 3
        myfactory = nanofactory.NanoFactory(text=EXP3_TEXT)
        self.assertEqual(myfactory.produce('1 FUEL'), True)
        self.assertEqual(myfactory.ore, EXP3_ORE)

        # 4. Create and run factory for example 4
        myfactory = nanofactory.NanoFactory(text=EXP4_TEXT)
        self.assertEqual(myfactory.produce('1 FUEL'), True)
        self.assertEqual(myfactory.ore, EXP4_ORE)

        # 5. Create and run factory for example 5
        myfactory = nanofactory.NanoFactory(text=EXP5_TEXT)
        self.assertEqual(myfactory.produce('1 FUEL'), True)
        self.assertEqual(myfactory.ore, EXP5_ORE)

    def test_trillion(self):
        """Test NanoFactory fuel per one trillion ore"""

        # 1. Create and get fuel amount for example 3
        myfactory = nanofactory.NanoFactory(text=EXP3_TEXT)
        self.assertEqual(myfactory.fuel_per_trillion(), EXP3_TRILLION)

        # 2. Create and get fuel amount for example 4
        myfactory = nanofactory.NanoFactory(text=EXP4_TEXT)
        self.assertEqual(myfactory.fuel_per_trillion(), EXP4_TRILLION)

        # 3. Create and get fuel amount for example 5
        myfactory = nanofactory.NanoFactory(text=EXP5_TEXT)
        self.assertEqual(myfactory.fuel_per_trillion(), EXP5_TRILLION)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end             t e s t _ n a n o f a c t o r y . p y              end
# ======================================================================
