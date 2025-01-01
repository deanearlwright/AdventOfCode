
# ======================================================================
# Garden Groups
#   Advent of Code 2024 Day 12 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ r e g i o n . p y
# ======================================================================
"Test Region for Advent of Code 2024 day 12, Garden Groups"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import region

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = ""

# ======================================================================
#                                                             TestRegion
# ======================================================================


class TestRegion(unittest.TestCase):  # pylint: disable=R0904
    "Test Region object"

    def test_empty_init(self):
        "Test the default Region creation"

        # 1. Create default Region object
        myobj = region.Region()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.label, None)
        self.assertEqual(len(myobj.plots), 0)

    def test_text_init(self):
        "Test the Region object creation from text"

        # 1. Create Region object from text
        myobj = region.Region(label="A", plot=(0, 0))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.label, "A")
        self.assertEqual(len(myobj.plots), 1)

        # 3. Check methods
        self.assertEqual(myobj.area(), 1)
        self.assertEqual(myobj.touches(), 0)
        self.assertEqual(myobj.perimeter(), 4)
        self.assertEqual(myobj.price(), 4)

    def test_region_a(self):
        "Test a Region object from the first example"

        # 1. Create the Region object
        myobj = region.Region(label="A", plot=(0, 0))
        myobj.expand((0, 1))
        myobj.expand((0, 2))
        myobj.expand((0, 3))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.label, "A")
        self.assertEqual(len(myobj.plots), 4)

        # 3. Check methods
        self.assertEqual(myobj.area(), 4)
        self.assertEqual(myobj.touches(), 6)
        self.assertEqual(myobj.perimeter(), 10)
        self.assertEqual(myobj.price(), 40)
        self.assertEqual(myobj.sides(), 4)
        self.assertEqual(myobj.price2(), 16)

    def test_region_b(self):
        "Test a Region object from the first example"

        # 1. Create the Region object
        myobj = region.Region(label="B", plot=(1, 0))
        myobj.expand((1, 1))
        myobj.expand((2, 0))
        myobj.expand((2, 1))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.label, "B")
        self.assertEqual(len(myobj.plots), 4)

        # 3. Check methods
        self.assertEqual(myobj.area(), 4)
        self.assertEqual(myobj.touches(), 8)
        self.assertEqual(myobj.perimeter(), 8)
        self.assertEqual(myobj.price(), 32)
        self.assertEqual(myobj.sides(), 4)
        self.assertEqual(myobj.price2(), 16)

    def test_region_c(self):
        "Test a Region object from the first example"

        # 1. Create the Region object
        myobj = region.Region(label="C", plot=(1, 3))
        myobj.expand((2, 3))
        myobj.expand((2, 4))
        myobj.expand((3, 4))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.label, "C")
        self.assertEqual(len(myobj.plots), 4)

        # 3. Check methods
        self.assertEqual(myobj.area(), 4)
        self.assertEqual(myobj.touches(), 6)
        self.assertEqual(myobj.perimeter(), 10)
        self.assertEqual(myobj.price(), 40)
        self.assertEqual(myobj.sides(), 8)
        self.assertEqual(myobj.price2(), 32)

    def test_region_d(self):
        "Test a Region object from the first example"

        # 1. Create the Region object
        myobj = region.Region(label="D", plot=(0, 4))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.label, "D")
        self.assertEqual(len(myobj.plots), 1)

        # 3. Check methods
        self.assertEqual(myobj.area(), 1)
        self.assertEqual(myobj.touches(), 0)
        self.assertEqual(myobj.perimeter(), 4)
        self.assertEqual(myobj.price(), 4)
        self.assertEqual(myobj.sides(), 4)
        self.assertEqual(myobj.price2(), 4)

    def test_region_e(self):
        "Test a Region object from the first example"

        # 1. Create the Region object
        myobj = region.Region(label="E", plot=(3, 0))
        myobj.expand((3, 1))
        myobj.expand((3, 2))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.label, "E")
        self.assertEqual(len(myobj.plots), 3)

        # 3. Check methods
        self.assertEqual(myobj.area(), 3)
        self.assertEqual(myobj.touches(), 4)
        self.assertEqual(myobj.perimeter(), 8)
        self.assertEqual(myobj.price(), 24)
        self.assertEqual(myobj.sides(), 4)
        self.assertEqual(myobj.price2(), 12)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ r e g i o n . p y                  end
# ======================================================================
