# ======================================================================
# Repose Record
#   Advent of Code 2018 Day 04 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                        t e s t _ s h i f t . p y
# ======================================================================
"Test Shift for day 04 of Advent of Code 2018, Repose Record"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import unittest

import shift

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------


# ======================================================================
#                                                              TestShift
# ======================================================================


class TestShift(unittest.TestCase):  # pylint: disable=R0904
    """Test Shift object"""

    def test_empty_init(self):
        """Test default Shift object creation"""

        # 1. Create default shift object
        myshift = shift.Shift()

        # 2. Make sure it has the default values
        self.assertEqual(myshift.number, 0)
        self.assertEqual(myshift.month, 1)
        self.assertEqual(myshift.day, 1)
        self.assertEqual(myshift.falls, 0)
        self.assertEqual(myshift.wakes, 0)
        self.assertEqual(len(myshift.minutes), 0)

        # 3. Check methods
        self.assertEqual(myshift.asleep(), 0)
        self.assertEqual(str(myshift),
                         '01-01  #0000  '
                         '............................................................')


    def test_value_init(self):
        """Test valued Shift object creation"""

        # 1. Create valued claim object
        myshift = shift.Shift(number=10, month=11, day=1)

        # 2. Make sure it has the specified values
        self.assertEqual(myshift.number, 10)
        self.assertEqual(myshift.month, 11)
        self.assertEqual(myshift.day, 1)
        self.assertEqual(myshift.falls, 0)
        self.assertEqual(myshift.wakes, 0)
        self.assertEqual(len(myshift.minutes), 0)

        # 3. Check methods
        self.assertEqual(myshift.asleep(), 0)
        self.assertEqual(str(myshift),
                         '11-01  #0010  '
                         '............................................................')
        myshift.add_fall(falls=5)
        myshift.add_wake(wakes=25)
        myshift.add_fall(falls=30)
        myshift.add_wake(wakes=55)
        self.assertEqual(myshift.asleep(), 20+25)
        self.assertEqual(str(myshift),
                         '11-01  #0010  '
                         '.....####################.....#########################.....')

    def test_text_init(self):
        """Test text Shift object creation"""

        # 1. Create text shift object
        myshift = shift.Shift(text='[1518-11-01 23:58] Guard #99 begins shift')

        # 2. Make sure it has the specified values
        self.assertEqual(myshift.number, 99)
        self.assertEqual(myshift.month, 11)
        self.assertEqual(myshift.day, 2)
        self.assertEqual(myshift.falls, 0)
        self.assertEqual(myshift.wakes, 0)
        self.assertEqual(len(myshift.minutes), 0)

        # 3. Check methods
        self.assertEqual(myshift.asleep(), 0)
        self.assertEqual(str(myshift),
                         '11-02  #0099  '
                         '............................................................')
        myshift.add_fall(text='[1518-11-02 00:40] falls asleep')
        myshift.add_wake(text='[1518-11-02 00:50] wakes up')
        self.assertEqual(myshift.asleep(), 10)
        self.assertEqual(str(myshift),
                         '11-02  #0099  '
                         '........................................##########..........')

    def test_often(self):
        """Test Shift object often function"""

        # 1. Create test shift object and record events
        myshift = shift.Shift(text='[1518-11-01 00:00] Guard #10 begins shift')
        myshift.add_fall(text='[1518-11-01 00:05] falls asleep')
        myshift.add_wake(text='[1518-11-01 00:25] wakes up')
        myshift.add_fall(text='[1518-11-01 00:30] falls asleep')
        myshift.add_wake(text='[1518-11-01 00:55] wakes up')
        myshift.add_fall(text='[1518-11-03 00:24] falls asleep')
        myshift.add_wake(text='[1518-11-03 00:29] wakes up')

        # 2. Make sure it has the specified values
        self.assertEqual(myshift.number, 10)
        self.assertEqual(myshift.month, 11)
        self.assertEqual(myshift.day, 3)
        self.assertEqual(myshift.falls, 0)
        self.assertEqual(myshift.wakes, 0)

        # 3. Check methods
        self.assertEqual(myshift.asleep(), 50)
        self.assertEqual(str(myshift),
                         '11-03  #0010  '
                         '.....########################.#########################.....')
        self.assertEqual(myshift.often(), (24, 2))

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    t e s t _ s h i f t . p y                   end
# ======================================================================
