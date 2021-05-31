# ======================================================================
# Signals and Noise
#   Advent of Code 2016 Day 06 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         m e s s a g e . p y
# ======================================================================
"A solver for the Advent of Code 2016 Day 06 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
from collections import Counter

# ======================================================================
#                                                                Message
# ======================================================================


class Message(object):   # pylint: disable=R0902, R0205
    "Object for Signals and Noise"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.columns = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Count the characters in each column"

        # 1. Start with nothing
        numcols = len(text[0])
        for _ in range(numcols):
            self.columns.append(Counter())

        # 2. Count the characters in each column in each row
        for row in text:
            assert len(row) == numcols
            for indx, char in enumerate(row):
                self.columns[indx].update(char)

    def most_common(self):
        "Return the messsage made from the most common character"

        # 1. Start with nothing
        result = []

        # 2. Loop for each column
        for col in self.columns:

            # 3. Add most common character to the result
            letter = col.most_common()[0][0]
            result.append(letter)

        # 4. Return the message
        return ''.join(result)

    def least_common(self):
        "Return the messsage made from the most common character"

        # 1. Start with nothing
        result = []

        # 2. Loop for each column
        for col in self.columns:

            # 3. Add least common character to the result
            letter = col.most_common()[-1][0]
            result.append(letter)

        # 4. Return the message
        return ''.join(result)

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.most_common()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.least_common()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                       m e s s a g e . p y                      end
# ======================================================================
