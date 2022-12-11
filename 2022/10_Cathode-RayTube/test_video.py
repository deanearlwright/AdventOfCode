# ======================================================================
# Cathode-Ray Tube
#   Advent of Code 2022 Day 10 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                    t e s t _ v i d e o . p y
# ======================================================================
"Test Video for Advent of Code 2022 day 10, Cathode-Ray Tube"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import video

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EXAMPLE_TEXT = ["noop", "addx 3", "addx -5"]

# ======================================================================
#                                                              TestVideo
# ======================================================================


class TestVideo(unittest.TestCase):  # pylint: disable=R0904
    "Test Video object"

    def test_empty_init(self):
        "Test the default Video creation"

        # 1. Create default Video object
        myobj = video.Video()

        # 2. Make sure it has the default values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(myobj.text, None)
        self.assertEqual(myobj.pc, 0)
        self.assertEqual(myobj.cycle, 0)
        self.assertEqual(myobj.x, 1)

    def test_text_init(self):
        "Test the Video object creation from text"

        # 1. Create Video object from text
        myobj = video.Video(text=EXAMPLE_TEXT)

        # 2. Make sure it has the expected values
        self.assertEqual(myobj.part2, False)
        self.assertEqual(len(myobj.text), 3)
        self.assertEqual(myobj.pc, 0)
        self.assertEqual(myobj.cycle, 0)
        self.assertEqual(myobj.x, 1)

        # 3. Check methods
        self.assertEqual(myobj.step(), [1])
        self.assertEqual(myobj.step(), [1, 4])
        self.assertEqual(myobj.step(), [4, -1])
        self.assertEqual(myobj.pc, 3)
        self.assertEqual(myobj.cycle, 5)
        self.assertEqual(myobj.x, -1)

        myobj.reset()
        self.assertEqual(myobj.pc, 0)
        self.assertEqual(myobj.cycle, 0)
        self.assertEqual(myobj.x, 1)
        self.assertEqual(myobj.run(), [1, 1, 1, 4, 4, -1])


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ v i d e o . p y                   end
# ======================================================================
