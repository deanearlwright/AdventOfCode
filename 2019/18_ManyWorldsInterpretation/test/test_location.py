# ======================================================================
# Space Police
#   Advent of Code 2019 Day 11 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ p a n e l . p y
# ======================================================================
"Test computer for Advent of Code 2019 day 11, Space Police"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import panel

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                              TestPanel
# ======================================================================


class TestPanels(unittest.TestCase):  # pylint: disable=R0904
    """Test Panels object"""

    def test_empty_init(self):
        """Test default Panel object creation"""

        # 1. Create default Panel object
        mypanel = panel.Panel()

        # 2. Make sure it has the default values
        self.assertEqual(mypanel.loc, (0, 0))
        self.assertEqual(mypanel.colored, panel.COLOR_BLACK)
        self.assertEqual(mypanel.history, [panel.COLOR_BLACK])

        # 3. Check methods
        self.assertEqual(len(mypanel), 0)
        self.assertEqual(mypanel.painted(), False)
        self.assertEqual(mypanel.color(), panel.COLOR_BLACK)
        self.assertEqual(str(mypanel), '.')

    def test_value_init(self):
        "Test Panel object creation with values"

        # 1. Create Panel object with values
        mypanel = panel.Panel(loc=(7, 11), color=panel.COLOR_WHITE)

        # 2. Make sure it has the specified values
        self.assertEqual(mypanel.loc, (7, 11))
        self.assertEqual(mypanel.colored, panel.COLOR_WHITE)
        self.assertEqual(mypanel.history, [panel.COLOR_WHITE])

        # 3. Check methods
        self.assertEqual(len(mypanel), 0)
        self.assertEqual(mypanel.painted(), False)
        self.assertEqual(mypanel.color(), panel.COLOR_WHITE)
        self.assertEqual(str(mypanel), '#')

    def test_painting(self):
        "Test painting the Panel object"

        # 1. Create default Panel object
        mypanel = panel.Panel()

        # 2. Paint it a couple of times
        mypanel.paint(panel.COLOR_WHITE)
        mypanel.paint(panel.COLOR_WHITE)
        mypanel.paint(panel.COLOR_BLACK)
        mypanel.paint(panel.COLOR_WHITE)
        mypanel.paint(panel.COLOR_WHITE)
        mypanel.paint(panel.COLOR_BLACK)

        # 3. Check the results
        self.assertEqual(len(mypanel), 6)
        self.assertEqual(mypanel.painted(), True)
        self.assertEqual(mypanel.color(), panel.COLOR_BLACK)
        self.assertEqual(str(mypanel), '.')

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ p a n e l . p y                    end
# ======================================================================
