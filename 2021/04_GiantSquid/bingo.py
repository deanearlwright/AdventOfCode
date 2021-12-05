# ======================================================================
# Giant Squid
#   Advent of Code 2021 Day 04 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         b i n g o . p y
# ======================================================================
"A solver for the Advent of Code 2021 Day 04 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import card

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                  Bingo
# ======================================================================


class Bingo(object):   # pylint: disable=R0902, R0205
    "Object for Giant Squid"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.numbers = []
        self.cards = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        # 1. Get the numbers to be called
        self.numbers = [int(x) for x in text[0].split(',')]

        # 2. Loop for the cards
        for index in range(1, len(text), 5):

            # 3. Build a card
            lines = text[index:index + 5]
            new_card = card.Card(text=lines)

            # 4. Add the card
            self.cards.append(new_card)

    def call_numbers_until_a_card_wins(self):
        "Like is says in the name of the method"

        # 1. Loop for all of the numbers
        for number in self.numbers:

            # 2. Loop for all of the cards
            for this_card in self.cards:

                # 3. Call the number for that card
                wins = this_card.call(number)

                # 4. If the card is a winner return the score
                if wins:
                    return this_card.score()

        # 5. We ran out of numbers without a winner
        return None

    def call_numbers_until_the_last_card_wins(self):
        "Like is says in the name of the method"

        # 1. Keep track of the number of winning cards
        cards_won = 0

        # 2. Loop for all of the numbers
        for number in self.numbers:

            # 3. Loop for all of the cards
            for this_card in self.cards:

                # 4. Ignore the card if it has already won
                if this_card.has_won:
                    continue

                # 5. Call the number for that card
                wins = this_card.call(number)

                # 6. If the card is a winner and it is the last one return the score
                if wins:
                    cards_won += 1
                    if cards_won == len(self.cards):
                        return this_card.score()

        # 7. We ran out of numbers without everyone being a winner
        return None

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.call_numbers_until_a_card_wins()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.call_numbers_until_the_last_card_wins()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         b i n g o . p y                        end
# ======================================================================
