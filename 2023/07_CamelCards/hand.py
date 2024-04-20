
# ======================================================================
# Camel Cards
#   Advent of Code 2023 Day 07 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         h a n d . p y
# ======================================================================
"Hand for the Advent of Code 2023 Day 07 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from collections import Counter

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
CARD_ORDER = "AKQJT08765432"
CARD_STRENGTH = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}
CARD_STRENGTH_PART_TWO = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 1,
    "Q": 12,
    "K": 13,
    "A": 14,
}
FIVE_OF_A_KIND = 7
FOUR_OF_A_KIND = 6
FULL_HOUSE = 5
THREE_OF_A_KIND = 4
TWO_PAIR = 3
ONE_PAIR = 2
HIGH_CARD = 1

# ======================================================================
#                                                                   Hand
# ======================================================================


class Hand(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Camel Cards"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.cards = ""
        self.bid = 0
        self.type = 0
        self.key = 0

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        assert text is not None and len(text) > 0

        # 1. Split into cards and bid
        parts = text.split()
        assert len(parts) == 2
        assert len(parts[0]) == 5

        # 2. Save them
        self.cards = parts[0]
        self.bid = int(parts[1])

        # 3. Determine the type and key
        if self.part2:
            self.type = self.determine_type_part_two(self.cards)
        else:
            self.type = self.determine_type(self.cards)
        self.key = self.determine_key()

    def determine_type(self, cards):  # pylint: disable=R0911
        "Return the type for this hand"

        # 1. If we already know it, return the stored value
        if self.type > 0:
            return self.type

        # 2. Count the cards
        knt = Counter(cards)
        oknt = knt.most_common()

        # 3. Is it five of a kind?
        if oknt[0][1] == 5:
            return FIVE_OF_A_KIND

        # 4. Is it four of a kind?
        if oknt[0][1] == 4:
            return FOUR_OF_A_KIND

        # 5. Is it three of a kind or full house?
        if oknt[0][1] == 3:
            if oknt[1][1] == 2:
                return FULL_HOUSE
            return THREE_OF_A_KIND

        # 6. Do we have one or two pairs?
        if oknt[0][1] == 2:
            if oknt[1][1] == 2:
                return TWO_PAIR
            return ONE_PAIR

        # 7. Which leaves only high card
        return HIGH_CARD

    def determine_type_part_two(self, cards):
        "Return the type for this hand part two hand"

        # 1. If we already know it, return the stored value
        if self.type > 0:
            return self.type

        # 2. If the hand has no jokers, evaluate it as normal
        if "J" not in cards:
            return self.determine_type(cards)

        # 3. Assume the least of the types
        result = 0

        # 4. Loop for all of the cards
        for card in cards:

            # 5. Set all the jokers to this value
            jcards = cards.replace("J", card)

            # 6. Determine the type with this hand of cards
            jtype = self.determine_type(jcards)

            # 7. Keep the highest type
            if jtype > result:
                result = jtype

        # 8. Return the highest type
        return result

    def determine_key(self):
        "Returns the sorting key of this hand"

        # 1. If we know the key, return it
        if self.key > 0:
            return self.key

        # 2. Get the card values
        if self.part2:
            values = [CARD_STRENGTH_PART_TWO[x] for x in self.cards]
        else:
            values = [CARD_STRENGTH[x] for x in self.cards]

        # 3. Combine the card values
        result = self.determine_type(self.cards)
        for value in values:
            result = result * 100 + value

        # 4. Return the computed key
        return result

    def winnings(self, rank):
        "Return the winnings for this hand"
        return rank * self.bid


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                          h a n d . p y                         end
# ======================================================================
