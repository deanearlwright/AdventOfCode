
# ======================================================================
# Mirage Maintenance
#   Advent of Code 2023 Day 09 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         r e p o r t . p y
# ======================================================================
"Report for the Advent of Code 2023 Day 09 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from history import History

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                 Report
# ======================================================================


class Report(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Mirage Maintenance"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.histories = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.histories = [History(text=line, part2=part2) for line in text]

    def next_values(self):
        "Return the sum of the next values for all of the histories"

        return sum(hist.next_value() for hist in self.histories)

    def prev_values(self):
        "Return the sum of the previous values for all of the histories"

        return sum(hist.prev_value() for hist in self.histories)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                        r e p o r t . p y                       end
# ======================================================================
