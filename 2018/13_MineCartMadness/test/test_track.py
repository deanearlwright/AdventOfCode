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

SAMPLE = r"""
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

ROUND = [r"""/->--\
v    |
|    |
\----/""", r"""/-->-\
|    |
v    |
\----/""", r"""/--->\
|    |
|    |
>----/""", r"""/----v
|    |
|    |
\>---/""", r"""/----\
|    v
|    |
\->--/""", r"""/----\
|    |
|    v
\-->-/""", r"""/----\
|    |
|    |
\---><""", r"""/----\
|    |
|    |
\----X"""]

EXAMPLE = [r"""/->-\
|   |  /----\
| /-+--+-\  |
| | |  | v  |
\-+-/  \-+--/
  \------/""", r"""/-->\
|   |  /----\
| /-+--+-\  |
| | |  | |  |
\-+-/  \->--/
  \------/""", r"""/---v
|   |  /----\
| /-+--+-\  |
| | |  | |  |
\-+-/  \-+>-/
  \------/""", r"""/---\
|   v  /----\
| /-+--+-\  |
| | |  | |  |
\-+-/  \-+->/
  \------/""", r"""/---\
|   |  /----\
| /->--+-\  |
| | |  | |  |
\-+-/  \-+--^
  \------/""", r"""/---\
|   |  /----\
| /-+>-+-\  |
| | |  | |  ^
\-+-/  \-+--/
  \------/""", r"""/---\
|   |  /----\
| /-+->+-\  ^
| | |  | |  |
\-+-/  \-+--/
  \------/""", r"""/---\
|   |  /----<
| /-+-->-\  |
| | |  | |  |
\-+-/  \-+--/
  \------/""", r"""/---\
|   |  /---<\
| /-+--+>\  |
| | |  | |  |
\-+-/  \-+--/
  \------/""", r"""/---\
|   |  /--<-\
| /-+--+-v  |
| | |  | |  |
\-+-/  \-+--/
  \------/""", r"""/---\
|   |  /-<--\
| /-+--+-\  |
| | |  | v  |
\-+-/  \-+--/
  \------/""", r"""/---\
|   |  /<---\
| /-+--+-\  |
| | |  | |  |
\-+-/  \-<--/
  \------/""", r"""/---\
|   |  v----\
| /-+--+-\  |
| | |  | |  |
\-+-/  \<+--/
  \------/""", r"""/---\
|   |  /----\
| /-+--v-\  |
| | |  | |  |
\-+-/  ^-+--/
  \------/""", r"""/---\
|   |  /----\
| /-+--+-\  |
| | |  X |  |
\-+-/  \-+--/
  \------/"""]

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
        self.assertEqual(len(mytrack.tracks), 0)
        self.assertEqual(len(mytrack.carts), 0)
        self.assertEqual(mytrack.time, 0)
        self.assertEqual(mytrack.size(), (0, 0))
        self.assertEqual(mytrack.crashed, None)

        # 3. Check methods
        self.assertEqual(mytrack.get_track((0, 0)), ' ')
        self.assertRaises(AssertionError, mytrack.get_track, (3, 3))
        mytrack.add_track((1, 2), '-')
        self.assertEqual(len(mytrack.tracks), 1)
        self.assertEqual(mytrack.size(), (1, 2))
        mytrack.add_track((1, 3), '+')
        self.assertEqual(mytrack.size(), (1, 3))
        self.assertEqual(len(mytrack.tracks), 2)
        self.assertEqual(mytrack.get_track((1, 1)), ' ')
        self.assertEqual(mytrack.get_track((1, 2)), '-')
        self.assertEqual(mytrack.get_track((1, 3)), '+')
        self.assertRaises(AssertionError, mytrack.get_track, (1, 4))
        mytrack.set_crashed((0, 0))
        self.assertEqual(mytrack.crashed, (0, 0))

        # 4. Once last check of values
        self.assertEqual(len(mytrack.tracks), 3)
        self.assertEqual(len(mytrack.carts), 0)
        self.assertEqual(mytrack.time, 0)
        self.assertEqual(mytrack.size(), (1, 3))

    def test_vertical(self):
        """Test vertical track"""

        # 1. Create default Track object
        mytrack = track.Track()

        # 2. Add the vertical track
        mytrack.add_track((0, 0), '|')
        mytrack.add_track((0, 1), 'v')
        mytrack.add_track((0, 2), '|')
        mytrack.add_track((0, 3), '|')
        mytrack.add_track((0, 4), '|')
        mytrack.add_track((0, 5), '^')
        mytrack.add_track((0, 6), '|')

        # 3. Check a few things
        self.assertEqual(len(mytrack.tracks), 7)
        self.assertEqual(len(mytrack.carts), 2)
        self.assertEqual(mytrack.time, 0)
        self.assertEqual(mytrack.size(), (0, 6))
        self.assertEqual(str(mytrack), "|\nv\n|\n|\n|\n^\n|")

        # 4. Advance the clock by one
        self.assertEqual(mytrack.tick(), False)
        self.assertEqual(mytrack.crashed, None)
        self.assertEqual(str(mytrack), "|\n|\nv\n|\n^\n|\n|")

        # 5. Advance the clock by one more
        self.assertEqual(mytrack.tick(), True)
        self.assertEqual(mytrack.crashed, (0, 3))
        self.assertEqual(str(mytrack), "|\n|\n|\nX\n|\n|\n|")

    def test_vertical_text(self):
        """Test vertical track using from_text()"""

        # 1. Create default Track object
        mytrack = track.Track()

        # 2. Add the track from text
        mytrack.from_text(VERTICAL_TRACK)

        # 3. Check a few things
        self.assertEqual(len(mytrack.tracks), 7)
        self.assertEqual(len(mytrack.carts), 2)
        self.assertEqual(mytrack.time, 0)
        self.assertEqual(mytrack.size(), (0, 6))
        self.assertEqual(str(mytrack), "|\nv\n|\n|\n|\n^\n|")

        # 4. Advance the clock by one
        self.assertEqual(mytrack.tick(), False)
        self.assertEqual(mytrack.crashed, None)
        self.assertEqual(str(mytrack), "|\n|\nv\n|\n^\n|\n|")

        # 5. Advance the clock by one more
        self.assertEqual(mytrack.tick(), True)
        self.assertEqual(mytrack.crashed, (0, 3))
        self.assertEqual(str(mytrack), "|\n|\n|\nX\n|\n|\n|")

    def test_round_tick(self):
        """Test round track using tick()"""

        # 1. Create default Track object
        mytrack = track.Track()

        # 2. Add the track from text
        mytrack.from_text(ROUND[0])

        # 3. Check a few things
        self.assertEqual(len(mytrack.tracks), 16)
        self.assertEqual(len(mytrack.carts), 2)
        self.assertEqual(mytrack.time, 0)
        self.assertEqual(mytrack.size(), (5, 3))
        self.assertEqual(str(mytrack), ROUND[0])

        # 4. Loop for all but last iteration
        for i in range(1, len(ROUND)-1):

            # 5. Advance the clock by one each loop
            self.assertEqual(mytrack.tick(), False)
            self.assertEqual(mytrack.crashed, None)
            self.assertEqual(str(mytrack), ROUND[i])

        # 6. Advance the clock by one last time
        self.assertEqual(mytrack.tick(), True)
        self.assertEqual(mytrack.crashed, (5, 3))
        self.assertEqual(str(mytrack), ROUND[len(ROUND)-1])

    def test_example_tick(self):
        """Test example track using tick()"""

        # 1. Create default Track object
        mytrack = track.Track()

        # 2. Add the track from text
        mytrack.from_text(EXAMPLE[0])

        # 3. Check a few things
        self.assertEqual(len(mytrack.carts), 2)
        self.assertEqual(mytrack.time, 0)
        self.assertEqual(mytrack.size(), (12, 5))
        self.assertEqual(str(mytrack), EXAMPLE[0])

        # 4. Loop for all but last iteration
        for i in range(1, len(EXAMPLE)-1):

            # 5. Advance the clock by one each loop
            self.assertEqual(mytrack.tick(), False)
            self.assertEqual(mytrack.crashed, None)
            #print("........... actual %d" % i)
            #print(str(mytrack))
            #print("........... expected %d" % i)
            #print(EXAMPLE[i])
            self.assertEqual(str(mytrack), EXAMPLE[i])

        # 6. Advance the clock by one last time
        self.assertEqual(mytrack.tick(), True)
        self.assertEqual(mytrack.crashed, (7, 3))
        self.assertEqual(str(mytrack), EXAMPLE[len(EXAMPLE)-1])

    def test_round_solve(self):
        """Test round track example using solve()"""

        # 1. Create default Track object
        mytrack = track.Track()

        # 2. Add the track from text
        mytrack.from_text(ROUND[0])

        # 3. Check a few things
        self.assertEqual(len(mytrack.tracks), 16)
        self.assertEqual(len(mytrack.carts), 2)
        self.assertEqual(mytrack.time, 0)
        self.assertEqual(mytrack.size(), (5, 3))
        self.assertEqual(str(mytrack), ROUND[0])

        # 4. Solve this puzzle
        self.assertEqual(mytrack.solve(), (5, 3))
        self.assertEqual(str(mytrack), ROUND[len(ROUND)-1])

    def test_sample_solve(self):
        """Test sample track using solve()"""

        # 1. Create default Track object
        mytrack = track.Track()

        # 2. Add the track from text
        mytrack.from_text(SAMPLE)

        # 3. Solve this puzzle
        self.assertEqual(mytrack.solve(), (7, 3))

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                   t e s t _ t r a c k . p y                    end
# ======================================================================
