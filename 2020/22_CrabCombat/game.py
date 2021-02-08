# ======================================================================
# Crab Combat
#   Advent of Code 2020 Day 22 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         g a m e . p y
# ======================================================================
"A solver for the Advent of Code 2020 Day 22 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import player

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                   Game
# ======================================================================


class Game(object):   # pylint: disable=R0902, R0205
    "Object for Crab Combat"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.players = []
        self.previous = set()
        self.winner = None
        self.rounds = 0

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Read the input text and create the players"

        # 1. We don't have a player yet
        plyr = None

        # 2. Loop for all of the lines of the text
        for line in text:

            # 3. If this is a player line, create them
            if line.startswith('Player'):
                plyr = player.Player(part2=self.part2, number=int(line[:-1].split()[1]))
                self.players.append(plyr)

            # 4. Else add the card to the current player
            else:
                plyr.add_card(int(line))

    def who_is_the_winner(self):
        "Returns the winning player or None if there is none"
        if self.winner is None:
            if self.players[0].lost():
                self.winner = 1
            elif self.players[1].lost():
                self.winner = 0
        return self.winner

    def round_one(self):
        "Play a round with the part 1 rules"

        # 1. Get cards from both players
        card0 = self.players[0].get_top_card()
        card1 = self.players[1].get_top_card()

        # 2. Determine the winner who gets to keep both cards
        if card0 > card1:
            self.players[0].keep(card0, card1)
        else:
            self.players[1].keep(card1, card0)

        # 3. Update the number of rounds
        self.rounds += 1

    def get_game_hash(self):
        "Returns the hash for this game"

        # 1. Get all of the cards
        cards = []
        cards.extend(self.players[0].cards)
        cards.append(0)
        cards.extend(self.players[1].cards)

        # 2. And return the string representation of that as the hash
        return str(cards)

    def round_two(self, limit=0):
        "Play a round with the part 2 rules"

        # 1. Infinate game prevention
        game_hash = self.get_game_hash()
        #print(game_hash, self.players[0].cards, self.players[1].cards)
        if game_hash in self.previous:
            self.winner = 0
            self.rounds += 1
            return
        self.previous.add(game_hash)

        # 2. Get cards from both players
        card0 = self.players[0].get_top_card()
        card1 = self.players[1].get_top_card()
        #print(card0, card1, len(self.players[0].cards), len(self.players[0].cards))

        # 3. Check for recursion
        if card0 > len(self.players[0].cards) or card1 > len(self.players[1].cards):

            # 4. Someone (or both) has too few cards to recuse, just play like part 1
            #print("not recursing")
            if card0 > card1:
                self.players[0].keep(card0, card1)
            else:
                self.players[1].keep(card1, card0)
            self.rounds += 1

        # 6. And now we (and now we (and now we (recurse)))
        else:

            # 7. Start a new game
            #print("starting a new game")
            new_game = self.clone([card0, card1])

            # 8. Get the winner of the new game
            winner = new_game.play(limit=limit)
            self.rounds += new_game.rounds

            # 9. Give the cards to the winner
            if winner is not None:
                if winner == 0:
                    self.players[0].keep(card0, card1)
                else:
                    print("player 2 wins the recursion")
                    self.players[1].keep(card1, card0)

    def play(self, limit=0):
        "play the game until there is a winner"

        # 1. Keep track of the number of rounds
        max_rounds = limit
        if max_rounds == 0:
            max_rounds = 9999999

        # 2. Loop until there is a winner
        while self.who_is_the_winner() is None and self.rounds < max_rounds:

            # 3. Play a round
            if self.part2:
                self.round_two(limit=max_rounds - self.rounds)
            else:
                self.round_one()

        # 4. Return the winning player
        if self.rounds >= max_rounds:
            return None
        return self.who_is_the_winner()

    def clone(self, cards):
        "Create a copy of the current game for recurion"

        # 1. Create a new empty game
        other = Game(part2=self.part2)

        # 2. Add the players to it
        for card, plyr in zip(cards, self.players):
            other.players.append(plyr.clone(card))

        # 3. Return a new game that is ready for recursion
        return other

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        assert verbose in [True, False]
        assert limit >= 0

        # 1. Play the game until there is a winner
        winner = self.play()
        if winner is None:
            return None

        # 1. Return the solution for part one
        return self.players[winner].score()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        assert verbose in [True, False]
        assert limit >= 0

        # 1. Play the game until there is a winner
        winner = self.play(limit=limit)
        if winner is None:
            return None

        # 1. Return the solution for part two
        print("Played %d rounds" % self.rounds)
        return self.players[winner].score()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                          g a m e . p y                         end
# ======================================================================
