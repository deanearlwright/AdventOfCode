
# ======================================================================
# Camel Cards
#   Advent of Code 2023 Day 07 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         h a n d s . p y
# ======================================================================
"Hands for the Advent of Code 2023 Day 07 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from hand import Hand

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                  Hands
# ======================================================================


class Hands(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Camel Cards"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.hands = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        # 0. Preconditions
        assert text is not None and len(text) > 0

        # 1. Loop for all of the lines of text
        for line in text:

            # 2. Create a hand
            a_hand = Hand(text=line, part2=self.part2)

            # 3. And save it
            self.hands.append(a_hand)

    def winnings(self):
        "Determing the total winnings for the hands"

        # 1. Start with nothing
        result = 0

        # 2. Sort the hands
        sorted_hands = sorted(self.hands, key=lambda h: h.key)

        # 3. Collect the winnings hand by hand
        for rank, one_hand in enumerate(sorted_hands):

            # 4. Add in the winnings for this hand
            result += one_hand.winnings(rank + 1)

        # 5. Return the total winnings
        return result


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------

if __name__ == '__main__':
    pass

# ======================================================================
# end                      h a n d s . p y                     end
# ======================================================================
