# ======================================================================
# Crab Cups
#   Advent of Code 2020 Day 23 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         g a m e . p y
# ======================================================================
"A solver for the Advent of Code 2020 Day 23 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
NUM_PART1_MOVES = 100
NUM_PART2_MOVES = 10000000
NUM_PART2_CUPS = 1000000


# ======================================================================
#                                                                   Game
# ======================================================================


class Game(object):   # pylint: disable=R0902, R0205
    "Object for Crab Cups"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.current = None
        self.maximum = None
        self.cups = {}

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text[0])

    def _process_text(self, text):
        "Convert text to cups"

        # 1. The initial current cup is the first one given
        self.current = int(text[0])

        # 2. Convert the text to integers
        values = [int(_) for _ in list(text)]

        # 3. Add the given values to the dictionary
        for index in range(len(values) - 1):
            self.cups[values[index]] = values[index + 1]
        self.cups[values[-1]] = values[0]
        self.maximum = max(values)

        # 4. For part two, add the rest of the one million cups
        if self.part2:
            self.cups[values[-1]] = self.maximum + 1
            for value in range(self.maximum + 1, NUM_PART2_CUPS):
                self.cups[value] = value + 1
            self.cups[NUM_PART2_CUPS] = values[0]
            self.maximum = NUM_PART2_CUPS

    def one_turn(self):
        "Do the four actions of a turn"

        # 1. Pick up three cups
        picked1 = self.cups[self.current]
        picked2 = self.cups[picked1]
        picked3 = self.cups[picked2]
        after_picked = self.cups[picked3]

        # 2. Select the destination cup
        destination = self.current - 1
        while destination <= 0 or \
                destination == picked1 or destination == picked2 or destination == picked3:
            if destination <= 0:
                destination = self.maximum
            else:
                destination -= 1

        # 3. Place the picked cups after the destination
        #    Befpre: ... -> c -> p1 -> p2 -> p3 -> a -> ...
        #            ... -> d -> x -> ...
        #    After:  ... -> c -> a -> ...
        #            ... -> d -> p1 -> p2 -> p3 -> x -> ...
        self.cups[self.current] = after_picked
        self.cups[picked3] = self.cups[destination]
        self.cups[destination] = picked1

        # 4. Select new current cup
        self.current = self.cups[self.current]

    def labeled(self):
        "Return the one less label"

        # 1. Get the values
        values = []
        where = 1
        for _ in range(self.maximum - 1):
            assert _ >= 0
            values.append(self.cups[where])
            where = self.cups[where]

        # 2. Return them as a string
        return ''.join(str(_) for _ in values)

    def get_stars(self):
        "Return the product of the star locations"

        # 1. Get the values
        values = []
        where = 1
        for _ in range(2):
            assert _ >= 0
            values.append(self.cups[where])
            where = self.cups[where]

        # 2. Return the product
        return values[0] * values[1]

    def multiple_turns(self, turns):
        "Run the game for the specified number of turns"

        # 1. Loop for the number of turns
        for _ in range(turns):
            assert _ >= 0

            # 2. Execute one turn
            self.one_turn()

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Execute multiple turns
        self.multiple_turns(NUM_PART1_MOVES)

        # 2. Return the solution for part one
        return self.labeled()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Execute multiple turns
        self.multiple_turns(NUM_PART2_MOVES)

        # 1. Return the solution for part two
        return self.get_stars()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                          g a m e . p y                         end
# ======================================================================
