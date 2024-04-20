
# ======================================================================
# Scratchcards
#   Advent of Code 2023 Day 04 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         s o l v e r . p y
# ======================================================================
"A solver for the Advent of Code 2023 Day 04 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from card import Card

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                 Solver
# ======================================================================


class Solver(object):   # pylint: disable=R0902, R0205
    "Object for Scratchcards"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.cards = []
        self.memory = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        assert text is not None and len(text) > 0

        # 1. Loop for all of the cards
        for line in text:

            # 2. Add the card
            self.cards.append(Card(text=line, part2=self.part2))

            # 3. And a part2 memory slot
            self.memory.append(0)

        assert len(self.cards) == len(self.memory)

    def cards_for_card(self, indx):
        "Returns (and remembers) the number of cards you get for this card"

        # 1. If we already know, return that knowledge
        if self.memory[indx] > 0:
            return self.memory[indx]

        # 2. If this card has no matches, return 0
        matched = len(self.cards[indx].matches())
        if matched == 0:
            return 1

        # 3. Start with just this card
        result = 1

        # 4. Loop for the number of matches
        for delta in range(matched):

            # 5. Add in the number of cards for this card
            result += self.cards_for_card(indx + 1 + delta)

        # 6. Remember this number of cards
        self.memory[indx] = result

        # 7. Return the number of cards you get for this one
        return result

    def cards_for_all_cards(self):
        "Get the total number of cards - original and earned"

        # 1. Start with nothing
        result = 0

        # 2. Loop for all the cards, setting memory
        for indx in range(len(self.cards)):
            result += self.cards_for_card(indx)

        # 3. Return total number of cards
        return result

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        if self.text:
            return sum([c.score() for c in self.cards])
        return None

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        if self.text:
            return self.cards_for_all_cards()
        return None

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                        s o l v e r . p y                       end
# ======================================================================
