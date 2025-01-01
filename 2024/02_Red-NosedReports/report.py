
# ======================================================================
# Red-Nosed Reports
#   Advent of Code 2024 Day 02 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         r e p o r t . p y
# ======================================================================
"Report for the Advent of Code 2024 Day 02 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
MIN_DELTA = 1
MAX_DELTA = 3

# ----------------------------------------------------------------------
#                                                                utility
# ----------------------------------------------------------------------


def is_delta_safe(left, right, increasing):
    "Check the delta between two levels"
    delta = left - right
    if increasing:
        delta = -delta
    if MIN_DELTA <= delta <= MAX_DELTA:
        return True
    return False


def recursive_is_safe_determine_increasing(levels):
    "Determine if safe recursively with increasing determination"

    # 1. Always safe if only one (or no) levels
    if len(levels) < 2:
        return True

    # 2. Determine the delta
    delta = levels[0] - levels[1]
    if delta == 0:
        return False
    increasing = delta < 0

    # 3. Determine if the rest is good
    return recursive_is_safe(levels, increasing)


def recursive_is_safe(levels, increasing):
    "Determine if safe recursively"

    # 1. Always safe if only one (or no) levels
    if len(levels) < 2:
        return True

    # 2. Are the first two levels safe?
    initial = is_delta_safe(levels[0], levels[1], increasing)
    if not initial:
        return False

    # 3. They are, so check the rest
    return recursive_is_safe(levels[1:], increasing)

# ======================================================================
#                                                                 Report
# ======================================================================


class Report(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Red-Nosed Reports"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.levels = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        assert text is not None and len(text) > 0

        # 1. Break up the level numbers
        levels = text.split()

        # 2. Convert to integers
        self.levels = [int(l) for l in levels]

    def is_safe(self):
        "Returns true if the level is safe"

        # 1. Determine if increasing or decreasing
        delta = self.levels[0] - self.levels[1]
        if delta == 0:
            return False
        increasing = delta < 0

        # 2. Check each pair of levels
        for indx in range(0, len(self.levels) - 1):
            if not is_delta_safe(self.levels[indx], self.levels[indx + 1], increasing):
                return False

        # 3. All are good
        return True

    def is_safe_two(self):
        "Returns true if the level is safe for part 2"

        # 1. Is it good with no deletions?
        if self.is_safe():
            return True

        # 2. Loop for every index
        for indx in range(len(self.levels)):

            # 3. Make a copy of the list minus the element at this index
            cpy = self.levels[:]
            del cpy[indx]

            # 4. Are these levels safe?
            if recursive_is_safe_determine_increasing(cpy):
                return True

        # 5. At least we tried
        return False

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                        r e p o r t . p y                       end
# ======================================================================
