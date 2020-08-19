# ======================================================================
# Marble Mania
#   Advent of Code 2018 Day 09 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                            g a m e . p y
# ======================================================================
"A solver for the Advent of Code 2018 Day 09 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from collections import deque

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
CLOCKWISE = -1
COUNTER_CLOCKWISE = 1

# ======================================================================
#                                                                   Game
# ======================================================================


class Game(object):   # pylint: disable=R0902, R0205
    "Object for Marble Mania"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.num_players = 0
        self.last_marble = 0
        self.current_marble = 0
        self.current_player = None
        self.circle = deque([0])
        self.players = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            words = text[0].split()
            self.num_players = int(words[0])
            self.last_marble = int(words[6])
            self.players = [0] * self.num_players

    def highest_score(self):
        if len(self.players) > 0:
            return max(self.players)
        else:
            return 0

    def play_game(self):
        while self.game_turn() is not None:
            pass
        return self.highest_score()

    def game_turn(self):
        marble = self.next_marble()
        if marble is None:
            return None
        self.next_player()
        if marble % 23 != 0:
            self.place_marble()
        else:
            self.capture_marble()
        return marble

    def next_marble(self):
        if self.current_marble >= self.last_marble:
            return None
        self.current_marble += 1;
        return self.current_marble

    def next_player(self):
        if self.current_player is None:
            self.current_player = 0
        else:
            self.current_player = (self.current_player + 1) % self.num_players
        return self.current_player

    def place_marble(self):
        self.circle.rotate(CLOCKWISE)
        self.circle.append(self.current_marble)

    def capture_marble(self):
        # 1. Player gets to keep marble
        #print("capturing player = %d" % self.current_player)
        self.players[self.current_player] += self.current_marble
        # 2. In addition, the marble 7 marbles counter-clockwise from the current marble
        #    is removed from the circle and also added to the current player's score.
        #    The marble located immediately clockwise of the marble that was removed
        #    becomes the new current marble.
        self.circle.rotate(7 * COUNTER_CLOCKWISE)
        self.players[self.current_player] += self.circle.pop()
        self.circle.rotate(CLOCKWISE)

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 1. Return the solution for part one
        return self.play_game()


    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 1. Return the solution for part two
        self.last_marble *= 100
        return self.play_game()

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                           g a m e . p y                        end
# ======================================================================
