# ======================================================================
# Dirac Dice
#   Advent of Code 2021 Day 21 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         g a m e . p y
# ======================================================================
"A solver for the Advent of Code 2021 Day 21 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from collections import defaultdict
from collections import namedtuple

import die
import player

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
TRACK_BEG = 1
TRACK_END = 10
GOAL_ONE = 1000
GOAL_TWO = 21
TIMES = 3
NO_WINNER = -1
QUANTUM = {
    3: 1,  # 111
    4: 3,  # 112, 121, 211
    5: 6,  # 113, 131, 311, 122, 212, 221
    6: 7,  # 123, 132, 213, 231, 312, 321, 222
    7: 6,  # 322, 232, 223, 133, 313, 331
    8: 3,  # 332, 323, 233
    9: 1,  # 333
}
assert sum(QUANTUM.values()) == 3 * 3 * 3

# ----------------------------------------------------------------------
#                                                            namestuples
# ----------------------------------------------------------------------
Universe = namedtuple('Universe', 'scores positions current')

# ======================================================================
#                                                                   Game
# ======================================================================


class Game(object):   # pylint: disable=R0902, R0205
    "Object for Dirac Dice"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.track = list(range(TRACK_BEG, TRACK_END + 1))
        self.players = []
        self.die = None
        if part2:
            self.goal = GOAL_TWO
        else:
            self.goal = GOAL_ONE
        self.times = TIMES

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            for line in text:
                self.players.append(player.Player(text=line, part2=part2))
            self.die = die.Die(part2=part2)

    def turn(self, plyr):
        "Turn for one of the players"

        # 1. Roll the die
        rolled = sum([self.die.roll() for _ in range(self.times)])

        # 2. Advance the player
        position = (plyr.position + rolled) % len(self.track)
        plyr.position = position

        # 3. Increase and return the player's score
        score = self.track[position]
        plyr.score += score
        return plyr.score

    def full_turn(self):
        "Play one full turn -- both player, unless the first wins, return winner index"

        # 1. Loop for all of the players
        for pindex, plyr in enumerate(self.players):

            # 2. Let the player have a turn
            score = self.turn(plyr)

            # 3. Did the player win?
            if score >= self.goal:
                return pindex

        # 4. No winner this turn
        return NO_WINNER

    def play(self):
        "Play an entire game"

        # 1. Play turns until a player wins
        while True:
            winner = self.full_turn()
            if winner != NO_WINNER:
                break

        # 2. Get the score(s) of the other players
        score = 0
        for pindex, plyr in enumerate(self.players):
            if pindex != winner:
                score += plyr.score

        # 3. Return the losing score time the number of times the die was rolled
        return score * self.die.rolled

    def play_two(self):
        "Whole nother game"

        # 1. Start at the very beginning, a very good place to start
        universes = defaultdict(int)
        universes[
            Universe(scores=(0, 0),
                     positions=(self.players[0].position, self.players[1].position),
                     current=0)
        ] = 1

        # 2. While that are universes to explore
        while universes:

            # 3. Loop for all of the known universes
            for universe, knt in list(universes.items()):
                del universes[universe]

                # 4. Loop for all of the possible throws of the dice
                for throw, throw_knt in QUANTUM.items():

                    # 5. Update the positions, scores, and counts for current player
                    new_pos = (universe.positions[universe.current] + throw) % len(self.track)
                    new_score = universe.scores[universe.current] + self.track[new_pos]
                    new_knt = knt * throw_knt

                    # 6. If there is a winner, record it
                    if new_score >= self.goal:
                        self.players[universe.current].wins += new_knt
                        continue

                    # 7. Else we will need to explore this new universe
                    if universe.current == 0:
                        new_universe = Universe(scores=(new_score, universe.scores[1]),
                                                positions=(new_pos, universe.positions[1]),
                                                current=1)
                    else:
                        new_universe = Universe(scores=(universe.scores[0], new_score),
                                                positions=(universe.positions[0], new_pos),
                                                current=0)

                    # 8. Add it to our todo list (actually a dict to handle collasping universes)
                    universes[new_universe] += new_knt

        # 9. Return the number of universes for the most successful player
        return max([plyr.wins for plyr in self.players])

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.play()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.play_two()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                          g a m e . p y                         end
# ======================================================================
