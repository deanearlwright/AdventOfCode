# ======================================================================
# Giant Squid
#   Advent of Code 2021 Day 04 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         c a r d . p y
# ======================================================================
"Card for the Advent of Code 2021 Day 04 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
WINS = [
  [0, 1, 2, 3, 4],
  [5, 6, 7, 8, 9],
  [10, 11, 12, 13, 14],
  [15, 16, 17, 18, 19],
  [20, 21, 22, 23, 24],
  [0, 5, 10, 15, 20],
  [1, 6, 11, 16, 21],
  [2, 7, 12, 17, 22],
  [3, 8, 13, 18, 23],
  [4, 9, 14, 19, 24],
]

# ======================================================================
#                                                                   Card
# ======================================================================


class Card(object):   # pylint: disable=R0902, R0205
    "Object for Giant Squid"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.numbers = None
        self.called = None
        self.last = None
        self.has_won = False

        # 2. Process text (if any)
        if text is not None and len(text) == 5:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        # 1. Start with nothing
        self.numbers = []
        self.called = []

        # 1. Loop for rows of text
        for line in text:

            # 2. Convert the row to numbers
            row = [int(x) for x in line.split()]

            # 3. Add the numbers
            self.numbers.extend(row)

            # 4. And the called
            self.called.extend([False, False, False, False, False])

    def call(self, number):
        "Call a number -- return True if board wins"

        # 1. Remember the last number called
        self.last = number

        # 2. We are done if the number wasn't on the card
        if not self.has_number(number):
            return False

        # 3. Set the position as called
        self.set_called(number)

        # 4. Return true if card is a winner
        return self.is_winner()

    def has_number(self, number):
        "Returns True if card has the number"

        return number in self.numbers

    def set_called(self, number):
        "Set the corresponding called item to True"
        self.called[self.numbers.index(number)] = True

    def is_winner(self):
        "Returns True if there is a complete row or column"

        # 1. Loop for all of the possible rows and columns
        for win in WINS:

            # 2. Loop for all of the positions
            winner = True
            for index in win:

                # 3. If any are not called, this row/col isn't a winner
                if not self.called[index]:
                    winner = False
                    break

            # 4. If this row/col is a winner, return True
            if winner:
                self.has_won = True
                return True

        # 5. Better luck next time
        return False

    def score(self):
        "Store this winning card"

        # 1. Start with nothing
        result = 0

        # 2. Loop for all of numbers on the card
        for index, number in enumerate(self.numbers):

            # 3. If it wasn't called, add it to the total
            if not self.called[index]:
                result += number

        # 4. Return the score
        return self.last * result

    def covered(self):
        "Return the number of covered squares"
        return sum([1 for _ in self.called if _])


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                          c a r d . p y                         end
# ======================================================================
