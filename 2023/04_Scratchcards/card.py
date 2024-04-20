
# ======================================================================
# Scratchcards
#   Advent of Code 2023 Day 04 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         c a r d . p y
# ======================================================================
"Card for the Advent of Code 2023 Day 04 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                   Card
# ======================================================================


class Card(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Scratchcards"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.id = 0
        self.winning = frozenset()
        self.having = frozenset()

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        assert text is not None and len(text) > 0

        # 1. Ensure valid card
        if not text.startswith('Card '):
            print(f"Invalid card ->{card}")
            return

        # 2. Get the card number
        parts = text.split(':')
        self.id = int(parts[0][4:])

        # 3. Get the winning and having numbers
        parts = parts[1].split("|")
        self.winning = frozenset([int(x) for x in parts[0].split()])
        self.having = frozenset([int(x) for x in parts[1].split()])

    def matches(self):
        "Return the matching numbers"

        return self.winning.intersection(self.having)

    def score(self):
        "Return the score for the card"

        # 1. Card with no matches are worth nothing
        matched = self.matches()
        if len(matched) == 0:
            return 0

        # 2. Else one for the first match, and doubled for the rest
        return pow(2, len(matched) - 1)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                          c a r d . p y                         end
# ======================================================================
