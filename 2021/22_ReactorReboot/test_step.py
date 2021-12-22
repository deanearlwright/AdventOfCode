# ======================================================================
# Reactor Reboot
#   Advent of Code 2021 Day 22 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ s t e p . p y
# ======================================================================
"Test Step for Advent of Code 2021 day 22, Reactor Reboot"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import step

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = "off x=10..12,y=-1..2,z=-60..60"

# ======================================================================
#                                                               TestStep
# ======================================================================


class TestStep(unittest.TestCase):  # pylint: disable=R0904
    "Test Step object"

    def test_empty_init(self):
        "Test the default Step creation"

        # 1. Create default Step object
        myobj = step.Step()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.turn_on, True)
        self.assertEqual(myobj.x_beg_end, (0, 0))
        self.assertEqual(myobj.y_beg_end, (0, 0))
        self.assertEqual(myobj.z_beg_end, (0, 0))

    def test_text_init(self):
        "Test the Step object creation from text"

        # 1. Create Step object from text
        myobj = step.Step(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 30)
        self.assertEqual(myobj.turn_on, False)
        self.assertEqual(myobj.x_beg_end, (10, 12))
        self.assertEqual(myobj.y_beg_end, (-1, 2))
        self.assertEqual(myobj.z_beg_end, (-60, 60))

        # 3. Check methods
        self.assertEqual(myobj.limited(), ((10, 12), (-1, 2), (-50, 50)))
        self.assertEqual(myobj.size(), 3 * 4 * 101)

        self.assertEqual(myobj.dim_overlap((0, 3), (4, 7)), None)
        self.assertEqual(myobj.dim_overlap((0, 3), (-2, -1)), None)
        self.assertEqual(myobj.dim_overlap((0, 3), (2, 7)), (2, 3))
        self.assertEqual(myobj.dim_overlap((4, 7), (0, 3)), None)
        self.assertEqual(myobj.dim_overlap((-2, -1), (0, 3)), None)
        self.assertEqual(myobj.dim_overlap((2, 7), (0, 3)), (2, 3))

        other = step.Step(text="off x=10..12,y=-1..2,z=-60..60")
        self.assertEqual(myobj.overlap(other), ((10, 12), (-1, 2), (-50, 50)))
        other = step.Step(text="off x=8..9,y=-1..2,z=-60..60")
        self.assertEqual(myobj.overlap(other), None)
        other = step.Step(text="off x=10..14,y=5..9,z=-60..60")
        self.assertEqual(myobj.overlap(other), None)
        other = step.Step(text="off x=11..14,y=-1..3,z=-60..40")
        self.assertEqual(myobj.overlap(other), ((11, 12), (-1, 2), (-50, 40)))

    def test_ranges_init(self):
        "Test the Step object creation from ranges"

        # 1. Create Step object from range values
        myobj = step.Step(on=False, ranges=((10, 12), (-1, 2), (-60, 60)))

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.turn_on, False)
        self.assertEqual(myobj.x_beg_end, (10, 12))
        self.assertEqual(myobj.y_beg_end, (-1, 2))
        self.assertEqual(myobj.z_beg_end, (-60, 60))
        self.assertEqual(myobj.size(), 3 * 4 * 101)

    def test_text_init_out_of_bounds(self):
        "Test the Step object creation from ranges"

        # 1. Create Step object from text
        myobj = step.Step(text="on x=-54112..-39298,y=-85059..-49293,z=-27449..7877")

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 51)
        self.assertEqual(myobj.turn_on, True)
        self.assertEqual(myobj.x_beg_end, (-54112, -39298))
        self.assertEqual(myobj.y_beg_end, (-85059, -49293))
        self.assertEqual(myobj.z_beg_end, (-27449, 7877))
        self.assertEqual(myobj.size(), 0)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                     t e s t _ s t e p . p y                    end
# ======================================================================
