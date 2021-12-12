# ======================================================================
# Passage Pathing
#   Advent of Code 2021 Day 12 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ c a v e s . p y
# ======================================================================
"Test solver for Advent of Code 2021 day 12, Passage Pathing"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import aoc_12
import caves

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_ONE = """
start-A
start-b
A-c
A-b
b-d
A-end
b-end
"""
EXAMPLE_TWO = """
dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
"""
EXAMPLE_THREE = """
fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
"""
PART_ONE_TEXT = EXAMPLE_THREE
PART_TWO_TEXT = EXAMPLE_THREE

PART_ONE_RESULT = 226
PART_TWO_RESULT = 3509

# ======================================================================
#                                                              TestCaves
# ======================================================================


class TestCaves(unittest.TestCase):  # pylint: disable=R0904
    "Test Caves object"

    def test_empty_init(self):
        "Test the default Caves creation"

        # 1. Create default Caves object
        myobj = caves.Caves()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(len(myobj.caves), 0)

    def test_text_init_one(self):
        "Test the Caves object creation from text"

        # 1. Create Caves object from text
        myobj = caves.Caves(text=aoc_12.from_text(EXAMPLE_ONE))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 7)
        self.assertEqual(len(myobj.caves), 6)
        self.assertEqual(len(myobj.caves['start']), 2)
        self.assertEqual(len(myobj.caves['A']), 4)
        self.assertEqual(len(myobj.caves['b']), 4)
        self.assertEqual(myobj.caves['c'], ['A'])
        self.assertEqual(myobj.caves['d'], ['b'])
        self.assertEqual(len(myobj.caves['end']), 2)

        # 3. Check methods
        self.assertEqual(len(myobj.filter_options([], 'start')), 2)
        self.assertEqual(len(myobj.filter_options(['A'], 'start')), 2)
        self.assertEqual(len(myobj.filter_options(['b'], 'start')), 1)
        self.assertEqual(len(myobj.filter_options(['a', 'b', 'c'], 'start')), 1)

        self.assertEqual(len(myobj.find_paths('start', 'end')), 10)

        # 4. Check methods for part 2
        myobj.part2 = True

        self.assertEqual(len(myobj.small_caves()), 3)

        self.assertEqual(myobj.times_occurs([], 'b'), 0)
        self.assertEqual(myobj.times_occurs(['b'], 'b'), 1)
        self.assertEqual(myobj.times_occurs(['A', 'b', 'C'], 'b'), 1)
        self.assertEqual(myobj.times_occurs(['A', 'b', 'C', 'b', 'D'], 'b'), 2)

        self.assertEqual(len(myobj.filter_options([], 'start')), 2)
        self.assertEqual(len(myobj.filter_options([], 'start', twice='')), 2)
        self.assertEqual(len(myobj.filter_options([], 'start', twice='x')), 2)
        self.assertEqual(len(myobj.filter_options(['b'], 'start', twice='d')), 1)
        self.assertEqual(len(myobj.filter_options(['b'], 'start', twice='b')), 2)
        self.assertEqual(len(myobj.filter_options(['b'], 'start', twice='d')), 1)

        self.assertEqual(len(myobj.find_paths('start', 'end')), 36)

    def test_text_init_two(self):
        "Test the Caves object creation from text using example two"

        # 1. Create Caves object from text
        myobj = caves.Caves(text=aoc_12.from_text(EXAMPLE_TWO))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 10)
        self.assertEqual(len(myobj.caves), 7)

        # 3. Check methods
        self.assertEqual(len(myobj.find_paths('start', 'end')), 19)

        self.assertEqual(len(myobj.small_caves()), 3)

        # 4. Check methods for part 2
        myobj.part2 = True
        self.assertEqual(len(myobj.find_paths('start', 'end')), 103)

    def test_text_init_three(self):
        "Test the Caves object creation from text using example three"

        # 1. Create Caves object from text
        myobj = caves.Caves(text=aoc_12.from_text(EXAMPLE_THREE))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 18)
        self.assertEqual(len(myobj.caves), 10)

        # 3. Check methods
        self.assertEqual(len(myobj.find_paths('start', 'end')), 226)

        self.assertEqual(len(myobj.small_caves()), 5)

        # 4. Check methods for part 2
        myobj.part2 = True
        self.assertEqual(len(myobj.find_paths('start', 'end')), 3509)

    def test_part_one(self):
        "Test part one example of Caves object"

        # 1. Create Caves object from text
        myobj = caves.Caves(text=aoc_12.from_text(PART_ONE_TEXT))

        # 2. Check the part one result
        self.assertEqual(myobj.part_one(verbose=False), PART_ONE_RESULT)

    def test_part_two(self):
        "Test part two example of Caves object"

        # 1. Create Caves object from text
        myobj = caves.Caves(part2=True, text=aoc_12.from_text(PART_TWO_TEXT))

        # 2. Check the part two result
        self.assertEqual(myobj.part_two(verbose=False), PART_TWO_RESULT)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ c a v e s . p y                   end
# ======================================================================
