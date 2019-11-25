# ======================================================================
# Mine Cart Madness
#   Advent of Code 2018 Day 13 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                       t e s t _ t r a c k . p y
# ======================================================================
"Test Tracks for day 13 of Advent of Code 2018, Mine Cart Madness"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import track

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

VERTICAL_TRACK = """
# Mine Cart Madness - day 13 of Advent of Code 2018

# Vertical line example from instructions

|
v
|
|
|
^
|

# Solution is 0,3
"""

SAMPLE_TRACK = """
# Mine Cart Madness - day 13 of Advent of Code 2018

# A longer example from the instructions

/->-\
|   |  /----\
| /-+--+-\  |
| | |  | v  |
\-+-/  \-+--/
  \------/

# Solution is 7,3
"""

# ======================================================================
#                                                                  Track
# ======================================================================


class TestTrack(unittest.TestCase):  # pylint: disable=R0904
    """Test Track object"""

    def test_empty_init(self):
        """Test default Track object creation"""

        # 1. Create default Track object
        mytrack = track.Track()

        # 2. Make sure it has the default values
        #self.assertEqual(mycoin.side, '?')
        #self.assertEqual(mycoin.value, 0)
        #self.assertEqual(mycoin.name, 'C0')

        # 3. Check methods
        #self.assertEqual(mycoin.letter(), 'C')
        #self.assertEqual(str(mycoin), 'Coin: C0?')
        #self.assertEqual(mycoin.csv_header(), 'Coin')
        #elf.assertEqual(mycoin.csv(), 'C0?')


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ t r a c k . p y                    end
# ======================================================================
