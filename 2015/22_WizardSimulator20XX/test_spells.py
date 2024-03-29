# ======================================================================
# Wizard Simulator 20XX
#   Advent of Code 2015 Day 22 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ s p e l l s . p y
# ======================================================================
"Test Spells for Advent of Code 2015 day 22, Wizard Simulator 20XX"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import spells

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = ""

# ======================================================================
#                                                             TestSpells
# ======================================================================


class TestSpells(unittest.TestCase):  # pylint: disable=R0904
    "Test Spells object"

    def test_empty_init(self):
        "Test the default Spells creation"

        # 1. Create default Shop object
        myobj = spells.Spells()

        # 2. Make sure it has the default values
        self.assertEqual(len(myobj.spells), 0)

        # 3. Check methods

    def test_text_init(self):
        "Test the Spells creation from text"

        # 1. Create default Shop object
        myobj = spells.Spells(text=spells.SPELLS)

        # 2. Make sure it has the default values
        self.assertEqual(len(myobj.spells), 5)

        # 3. Check methods


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ s p e l l s . p y                  end
# ======================================================================
