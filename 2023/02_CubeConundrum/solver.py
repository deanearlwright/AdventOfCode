
# ======================================================================
# Cube Conundrum
#   Advent of Code 2023 Day 02 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         s o l v e r . p y
# ======================================================================
"A solver for the Advent of Code 2023 Day 02 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import game

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                 Solver
# ======================================================================


class Solver(object):   # pylint: disable=R0902, R0205
    "Object for Cube Conundrum"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.games = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        assert text is not None and len(text) > 0

        # 1. Loop for all the lines of text
        for line in text:

            # 2. Create a game for that line
            a_game = game.Game(text=line, part2=self.part2)

            # 3. Add the game to all the others
            self.games.append(a_game)

    def check_games(self, red=12, green=13, blue=14):
        "Return the sum of ids for possible games"

        # 1. Start with nothing
        result = 0

        # 2. Loop for all the games
        for a_game in self.games:

            # 3. If the game is possible, add in the id
            if a_game.possible(red=red, green=green, blue=blue):
                result += a_game.id

        # 4. Return the sum of the possible ids
        return result

    def power_set(self):
        "Return the sum of the games power sets"

        # 1. Start with nothing
        result = 0

        # 2. Loop for all the games
        for a_game in self.games:

            # 3. Add in the power set for this game
            result += a_game.power_set()

        # 4. Return the sum of the possible ids
        return result

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        if self.text:
            return self.check_games()
        return None

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        if self.text:
            return self.power_set()
        return None

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                      s o l v e r . p y                     end
# ======================================================================
