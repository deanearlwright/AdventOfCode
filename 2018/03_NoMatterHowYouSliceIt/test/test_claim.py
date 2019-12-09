# ======================================================================
# No Matter How You Slice It
#   Advent of Code 2018 Day 03 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                        t e s t _ c l a i m . p y
# ======================================================================
"Test Carts for day 3 of Advent of Code 2018, No Matter How You Slice It"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import claim

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------


# ======================================================================
#                                                              TestClaim
# ======================================================================


class TestClaim(unittest.TestCase):  # pylint: disable=R0904
    """Test Claimk object"""

    def test_empty_init(self):
        """Test default Claim object creation"""

        # 1. Create default claim object
        myclaim = claim.Claim()

        # 2. Make sure it has the default values
        self.assertEqual(myclaim.number, 0)
        self.assertEqual(myclaim.left, 0)
        self.assertEqual(myclaim.top, 0)
        self.assertEqual(myclaim.width, 1)
        self.assertEqual(myclaim.height, 1)
        self.assertEqual(myclaim.right, 0)
        self.assertEqual(myclaim.bottom, 0)

        # 3. Check methods
        self.assertEqual(str(myclaim), '#0 @ 0,0: 1x1')

    def test_values_init(self):
        """Test Claim object creation with values"""

        # 1. Create default claim object
        myclaim = claim.Claim(number=2,
                              left=3,
                              top=1,
                              width=4,
                              height=4)

        # 2. Make sure it has the default values
        self.assertEqual(myclaim.number, 2)
        self.assertEqual(myclaim.left, 3)
        self.assertEqual(myclaim.top, 1)
        self.assertEqual(myclaim.width, 4)
        self.assertEqual(myclaim.height, 4)
        self.assertEqual(myclaim.right, 6)
        self.assertEqual(myclaim.bottom, 4)

        # 3. Check methods
        self.assertEqual(str(myclaim), '#2 @ 3,1: 4x4')

    def test_text_init(self):
        """Test Claim object creation with text"""

        # 1. Create default claim object
        myclaim = claim.Claim(text='#1 @ 1,3: 4x4')

        # 2. Make sure it has the default values
        self.assertEqual(myclaim.number, 1)
        self.assertEqual(myclaim.left, 1)
        self.assertEqual(myclaim.top, 3)
        self.assertEqual(myclaim.width, 4)
        self.assertEqual(myclaim.height, 4)
        self.assertEqual(myclaim.right, 4)
        self.assertEqual(myclaim.bottom, 6)

        # 3. Check methods
        self.assertEqual(str(myclaim), '#1 @ 1,3: 4x4')
        
    def test_does_overlap(self):
        """Test Claim overlap detection"""

        # 1. Create some claim objects
        claim1 = claim.Claim(text='#1 @ 1,3: 4x4')
        claim2 = claim.Claim(text='#2 @ 3,1: 4x4')
        claim3 = claim.Claim(text='#3 @ 5,5: 2x2')
        
        # 2. Check for overlaps
        self.assertEqual(claim1.does_overlap(claim1), True)
        self.assertEqual(claim1.does_overlap(claim2), True)
        self.assertEqual(claim1.does_overlap(claim3), False)
        self.assertEqual(claim2.does_overlap(claim1), True)
        self.assertEqual(claim2.does_overlap(claim2), True)
        self.assertEqual(claim2.does_overlap(claim3), False)
        self.assertEqual(claim3.does_overlap(claim1), False)
        self.assertEqual(claim3.does_overlap(claim2), False)
        self.assertEqual(claim3.does_overlap(claim3), True)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ c l a i m . p y                   end
# ======================================================================
