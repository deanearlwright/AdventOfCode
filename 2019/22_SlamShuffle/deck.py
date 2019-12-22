# ======================================================================
# Slam Shuffle
#   Advent of Code 2019 Day 22 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                            d e c k . p y
# ======================================================================
"A Space card deck for Advent of Code Day 22, Slam Shuffle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

DEFAULT_SIZE = 10007

PART2_SIZE = 119315717514047  # Don't create a deck with this size!!!
PART2_TIMES = 101741582076661 # Or execute the input this many times!!!

DISPLAY_SIZE = 10

# ======================================================================
#                                                                   Deck
# ======================================================================


class Deck():
    """Object representing a location in the Neptune vault"""

    def __init__(self, size=DEFAULT_SIZE):

        # 1. Set the initial values
        self.size = size

        # 2. Build the deck
        self.cards = self.factory_fresh()

    def __str__(self):

        # 1. If we can display them all, do so
        if self.size <= DISPLAY_SIZE:
            return str(self.cards)[1:-1].replace(',', '')

        # 2. Else just show some at either end
        return "%s ... %s" % (str(self.cards[:DISPLAY_SIZE // 2])[1:-1].replace(',', ''),
                              str(self.cards[-DISPLAY_SIZE // 2:])[1:-1].replace(',', ''))

    def factory_fresh(self):
        "Create a factor fresh deck of cards"

        return list(range(self.size))

    def factory_order(self):
        "Put the deck into the factor fresh order"

        self.cards = self.factory_fresh()

    def deal_into_new_stack(self):
        "Deal the Deck into a new stack (reverse order of the deck)"

        self.cards.reverse()

    def cut(self, number):
        "Move the top (bottom) cards to the bottom (top)"

        self.cards = self.cards[number:] + self.cards[:number]

    def deal_with_increment(self, number):
        "Set direction as leading to the origin"

        # 0. Preconditions
        assert number < self.size

        # 1. Initially the table is empty
        table = [-1 for _ in range(self.size)]
        position = 0

        # 2. Loop for all the cards in the deck
        for card in self.cards:

            # 3. Put the card on the table
            table[position] = card

            # 4. Advance by the increment
            position += number

            # 5. Handle wrapping past the end of the table
            position %= self.size

        # 6. Insure there are no unfilled positions
        try:
            loc = table.index(-1)
            print("Unfilled value found at %d doing increment %d on %d cards" %
                  (loc, number, self.size))
        except ValueError:
            pass

        # 6. The table becomes the new deck
        self.cards = table



    def position(self, number):
        "Return the position of the card with the specified value"

        return self.cards.index(number)

    def instructions(self, text, verbose=False, watch=None):
        "Follow a series of instructions"

        # 1. Loop for all of the instructions
        for inst in text:
            words = inst.split()

            # 2. Process deal into a new stack
            if words == ['deal', 'into', 'new', 'stack']:
                self.deal_into_new_stack()

            # 3. Process cut
            elif words[0] == 'cut':
                self.cut(int(words[1]))

            # 4. Process deal with increment
            elif words[0:3] == ['deal', 'with', 'increment']:
                self.deal_with_increment(int(words[3]))

            # 5. Huh?
            else:
                print("unknown instruction: %s" % (inst))

            # 6. Prattle on
            if verbose:
                print("%s ==> %s" % (inst, str(self)), end='')
                if watch is not None:
                    print(", [%d] = %d, [%d] = %d" %
                          (watch, self.cards[watch],
                           self.size-(watch+1), self.cards[self.size-(watch+1)]))
                else:
                    print()
            elif watch is not None:
                print('"%s", %d, %d' %
                      (inst, self.cards[watch], self.cards[self.size-(watch+1)]))

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                          d e c k . p y                         end
# ======================================================================
