# ======================================================================
# Repose Record
#   Advent of Code 2018 Day 04 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                             s h i f t . p y
# ======================================================================
"Shift for Repose Record problem for day 04 of Advent of Code"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from collections import Counter
import re

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
YMDHM = r'^\[1518-([0-9][0-9])-([0-9][0-9]) ([0-9][0-9]):([0-9][0-9])]'
GUARD = re.compile(YMDHM + r' Guard #([0-9]+) begins shift$')
FALLS = re.compile(YMDHM + r' falls asleep$')
WAKES = re.compile(YMDHM + r' wakes up$')

#               JAN FEB MAR APR MAY JUN JUL AUG SEP OCT NOV DEC
DAYSMONTH = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]



# ======================================================================
#                                                                  Shift
# ======================================================================


class Shift():
    """Object representing a single row of fabric"""

    def __init__(self,                          # pylint: disable=R0913
                 number=0, month=1, day=1, hour=0, text=None):

        # 1. Set the values
        self.number = number
        self.month = month
        self.day = day
        self.falls = 0
        self.wakes = 0
        self.minutes = Counter()

        # 2. Process text (if any)
        if text:
            match = GUARD.match(text)
            assert match is not None
            self.month = int(match.group(1))
            self.day = int(match.group(2))
            hour = int(match.group(3))
            self.number = int(match.group(5))

        # 3. Tweak month and day (if needed)
        if hour == 23:
            self.day += 1
            if self.day > DAYSMONTH[self.month]:
                self.day = 1
                self.month += 1
                if self.month > 12:
                    self.month = 1

        # 4. Postconditions
        assert self.month >= 1 and month <= 12
        assert self.day >= 1 and day <= 31
        assert self.falls == 0
        assert self.wakes == 0

    def add_fall(self, falls=0, text=None):
        "Record time of falling asleep"

        # 0. Preconditions
        assert self.falls == 0
        assert self.wakes == 0

        # 1. Save the value
        self.falls = falls

        # 2. Process text (if any)
        if text:
            match = FALLS.match(text)
            assert match is not None
            self.month = int(match.group(1))
            self.day = int(match.group(2))
            hour = int(match.group(3))
            assert hour == 0
            self.falls = int(match.group(4))

        # 9. Postconditions
        assert self.falls >= 0
        assert self.wakes == 0

    def add_wake(self, wakes=0, text=None):
        "Record time of falling asleep"

        # 0. Preconditions
        assert self.falls >= 0

        # 1. Save the value
        self.wakes = wakes

        # 2. Process text (if any)
        if text:
            match = WAKES.match(text)
            assert match is not None
            self.month = int(match.group(1))
            self.day = int(match.group(2))
            hour = int(match.group(3))
            assert hour == 0
            self.wakes = int(match.group(4))

        # 3. Make claims to squares in this row
        assert self.falls < self.wakes
        self.minutes.update(range(self.falls, self.wakes))

        # 4. Reset for next time
        self.falls = 0
        self.wakes = 0

    def asleep(self):
        "Total minutes asleep this shift"

        return sum(self.minutes.values())


    def often(self):
        "Return the minute and times most often asleep"

        if len(self.minutes) > 0:
            return self.minutes.most_common(1)[0]
        return (0, 0)

    def __str__(self):

        view = []
        for minute in range(60):
            if minute in self.minutes:
                view.append('#')
            else:
                view.append('.')
        return "%02d-%02d  #%04d  %s" % (self.month, self.day, self.number, ''.join(view))


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                        s h i f t . p y                         end
# ======================================================================
