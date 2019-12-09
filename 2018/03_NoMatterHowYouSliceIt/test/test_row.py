# ======================================================================
# No Matter How You Slice It
#   Advent of Code 2018 Day 03 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                          t e s t _ r o w . p y
# ======================================================================
"Test Row for day 3 of Advent of Code 2018, No Matter How You Slice It"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import claim
import row

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------


# ======================================================================
#                                                                TestRow
# ======================================================================


class TestRow(unittest.TestCase):  # pylint: disable=R0904
    """Test Row object"""

    def test_empty_init(self):
        """Test default Row object creation"""

        # 1. Create default claim object
        myrow = row.Row()

        # 2. Make sure it has the default values
        self.assertEqual(myrow.number, 0)
        self.assertEqual(len(myrow.counts), 0)

        # 3. Check methods
        claim1 = claim.Claim(text='#1 @ 1,3: 4x4')
        myrow.add_claim(claim1)
        self.assertEqual(len(myrow.counts), 0)
        self.assertEqual(myrow.claimed(), 0)
        self.assertEqual(myrow.overlap(), 0)

        claim2 = claim.Claim(text='#2 @ 0,0: 4x4')
        myrow.add_claim(claim2)
        self.assertEqual(len(myrow.counts), 4)
        self.assertEqual(myrow.claimed(), 4)
        self.assertEqual(myrow.overlap(), 0)

        claim3 = claim.Claim(text='#3 @ 1,0: 2x2')
        myrow.add_claim(claim3)
        self.assertEqual(len(myrow.counts), 4)
        self.assertEqual(myrow.claimed(), 4)
        self.assertEqual(myrow.overlap(), 2)

    def test_value_init(self):
        """Test default Row object creation"""

        # 1. Create default claim object
        myrow = row.Row(number=4)

        # 2. Make sure it has the default values
        self.assertEqual(myrow.number, 4)
        self.assertEqual(len(myrow.counts), 0)

        # 3. Check methods
        claim1 = claim.Claim(text='#1 @ 1,3: 4x4')
        myrow.add_claim(claim1)
        self.assertEqual(len(myrow.counts), 4)
        self.assertEqual(myrow.claimed(), 4)
        self.assertEqual(myrow.overlap(), 0)

        claim2 = claim.Claim(text='#2 @ 3,1: 4x4')
        myrow.add_claim(claim2)
        self.assertEqual(len(myrow.counts), 6)
        self.assertEqual(myrow.claimed(), 6)
        self.assertEqual(myrow.overlap(), 2)

        claim3 = claim.Claim(text='#3 @ 5,5: 2x2')
        myrow.add_claim(claim3)
        self.assertEqual(len(myrow.counts), 6)
        self.assertEqual(myrow.claimed(), 6)
        self.assertEqual(myrow.overlap(), 2)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      t e s t _ r o w . p y                     end
# ======================================================================
