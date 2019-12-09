# ======================================================================
# Space Image Format
#   Advent of Code 2019 Day 08 -- Eric Wastl -- https://adventofcode.com
#
# codeuter simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                        t e s t _ i m a g e . p y
# ======================================================================
"Test image objects for Advent of Code 2019 day 08, Space Image Format"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import image

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                              TestImage
# ======================================================================


class TestImage(unittest.TestCase):  # pylint: disable=R0904
    """Test image object"""

    def test_empty_init(self):
        """Test default image object creation"""

        # 1. Create default image object
        myimage = image.Image()

        # 2. Make sure it has the default values
        self.assertEqual(myimage.width, 0)
        self.assertEqual(myimage.height, 0)
        self.assertEqual(len(myimage.layers), 0)

        # 3. Check methods
        self.assertEqual(myimage.check_layers(), None)
        self.assertEqual(myimage.part_one(), None)

    def test_value_init(self):
        """Test image object creation with values"""

        # 1. Create image objhect with values
        myimage = image.Image(width=3, height=2, layers=['123456','789012'])

        # 2. Make sure it has the specified values
        self.assertEqual(myimage.width, 3)
        self.assertEqual(myimage.height, 2)
        self.assertEqual(len(myimage.layers), 2)

        # 3. Check methods
        self.assertEqual(myimage.check_layers(), None)
        self.assertEqual(myimage.part_one(), 1)

    def test_text_init(self):
        """Test image object creation with texts"""

        # 1. Create image objhect with values
        myimage = image.Image(width=3, height=2, text='123456789012')

        # 2. Make sure it has the specified values
        self.assertEqual(myimage.width, 3)
        self.assertEqual(myimage.height, 2)
        self.assertEqual(len(myimage.layers), 2)

        # 3. Check methods
        self.assertEqual(myimage.check_layers(), None)
        self.assertEqual(myimage.part_one(), 1)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ i m a g e . p y                   end
# ======================================================================
