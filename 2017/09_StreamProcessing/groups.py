# ======================================================================
# Stream Processing
#   Advent of Code 2017 Day 09 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                       g r o u p s . p y
# ======================================================================
"A solver for Stream Processing for Advent of Code 2017 Day 09"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

from collections import namedtuple

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

StateTableRow = namedtuple('StateTableRow',
                           'state, inchr, nxtst, delta, trash')

STATE_TABLE = [
    StateTableRow(0, '{', 1, 1, 0),
    StateTableRow(1, '{', 1, 1, 0),
    StateTableRow(1, '}', 1, -1, 0),
    StateTableRow(1, '<', 2, 0, 0),
    StateTableRow(2, '>', 1, 0, 0),
    StateTableRow(2, '!', 3, 0, 0),
    StateTableRow(2, None, 2, 0, 1),  # To count garbage characters
    StateTableRow(3, None, 2, 0, 0)
]

# ======================================================================
#                                                                 Groups
# ======================================================================


class Groups(object):
    """Object processing group / garbage stream"""

    def __init__(self, part2=False, text=None, verbose=False, limit=0):

        # 1. Set the initial values
        self.part2 = part2
        self.state = 0
        self.level = 0
        self.group = 0
        self.score = 0
        self.trash = 0

        # 2. If text is not None, process it
        if text is not None:
            self.process_stream(text=text, verbose=verbose, limit=limit)

    def __str__(self):
        return "s=%d l=%d g=%d s=%d" % (
            self.state, self.level, self.group, self.score)


    def process_stream(self, text=None, verbose=False, limit=0):
        "Process the text of a stream"

        # 1. If no text, not much to do
        if text is None:
            return

        # 2. Loop for all of the character
        for cnum, char in enumerate(text):

            # 3. Process the character
            self.process_character(char, verbose=verbose)

            # 4. Check if processing limit reached
            if cnum > limit > 0:
                break

    def process_character(self, char, verbose=False):
        "Process the text of a stream"

        # 1. Loop for the all of the rows in the state table
        for row in STATE_TABLE:

            # 2. Ignore row if state does not match
            if self.state != row.state:
                continue

            # 3. Ignore row if character does not match
            if row.inchr is not None and row.inchr != char:
                continue

            # 4. Set up adjustments
            next_state = row.nxtst
            next_level = self.level + row.delta
            if row.delta == -1:
                self.group += 1
                self.score += self.level
            self.trash += row.trash

            # 5. Describe the state (if desired)
            if verbose:
                print("state %d, char %s -> next %d, level %d, group %d score %d" %
                      (self.state, char, next_state, next_level, self.group, self.score))

            # 6. Set the next state and level
            self.state = next_state
            self.level = next_level

            # 7. Character processed, exit loop
            break

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         g r o u p s . p y                      end
# ======================================================================
