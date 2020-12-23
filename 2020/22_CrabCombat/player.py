# ======================================================================
# Crab Combat
#   Advent of Code 2020 Day 22 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         p l a y e r . p y
# ======================================================================
"A player for the Advent of Code 2020 Day 22 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                 Player
# ======================================================================


class Player(object):   # pylint: disable=R0902, R0205
    "Object for Crab Combat"

    def __init__(self, number=0, cards=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.number = number
        self.cards = []

        # 2. Process text (if any)
        if cards is not None:
            self.cards = cards

    def add_card(self, card):
        "Add a single card"
        self.cards.append(int(card))

    def get_top_card(self):
        "Returns the top card or None if the player has no cards"
        if self.cards:
            return self.cards.pop(0)
        return None

    def keep(self, card0, card1):
        "Add winning cards"
        self.cards.append(card0)
        self.cards.append(card1)

    def score(self):
        "Score the player's cards"

        # 1. Start with nothing
        result = 0
        multiplier = len(self.cards)

        # 2. Loop for all of the cards in the hand
        for card in self.cards:

            # 3. Add in the score for this card
            result += card * multiplier

            # 4. The next card is worth less
            multiplier -= 1

        # 5. Return the score
        return result

    def lost(self):
        "Returns true if the player has no cards"
        return len(self.cards) == 0

    def clone(self, card):
        "Return a copy of the player for use in recursion"

        # 1. Create a new player
        return Player(number=self.number, cards=self.cards[:card].copy())


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         p l a y e r . p y                      end
# ======================================================================
