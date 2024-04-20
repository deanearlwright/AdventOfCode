
# ======================================================================
# Mirage Maintenance
#   Advent of Code 2023 Day 09 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         h i s t o r y . p y
# ======================================================================
"History for the Advent of Code 2023 Day 09 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                History
# ======================================================================


class History(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Mirage Maintenance"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.values = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.values = [int(x) for x in text.split()]

    def next_value(self):
        "Detmine the next value in the history"

        return self.nxt_value(self.values)

    def prev_value(self):
        "Backwards and in heels"

        # 1. Return the next value of the reversed list
        return self.nxt_value(self.values[::-1])

    @staticmethod
    def nxt_value(values):
        "Go down the rabbit hole to determine the next value"

        # 1. Base case, numbers are all zero
        if History.all_zeroes(values):
            return 0

        # 2. Determine the differences
        diffs = History.differences(values)
        assert len(diffs) == len(values) - 1

        # 3. And recurse
        return values[-1] + History.nxt_value(diffs)

    @staticmethod
    def differences(values):
        "Return the differences in the values"

        return [values[i + 1] - values[i] for i in range(len(values) - 1)]

    @staticmethod
    def all_zeroes(values):
        "Are all the values 0?"

        return all(x == 0 for x in values)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                        h i s t o r y . p y                     end
# ======================================================================
