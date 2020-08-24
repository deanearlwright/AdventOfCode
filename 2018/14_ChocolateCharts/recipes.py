# ======================================================================
# Chocolate Charts
#   Advent of Code 2018 Day 14 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         r e c i p e s . p y
# ======================================================================
"A solver for the Advent of Code 2018 Day 14 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
NUMBER_OF_RECIPES = 10

# ======================================================================
#                                                                Recipes
# ======================================================================


class Recipes(object):   # pylint: disable=R0902, R0205
    "Object for Chocolate Charts"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.scores = [3, 7]
        self.elves = [0, 1]
        self.after = None

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.after = int(text[0], 10)

    def step(self):
        self.new_recipe()
        self.move_elves()

    def new_recipe(self):
        # To create new recipes, the two Elves combine their current recipes. This
        # creates new recipes from the digits of the sum of the current recipes'
        # scores. With the current recipes' scores of 3 and 7, their sum is 10, and
        # so two new recipes would be created: the first with score 1 and the second
        # with score 0. If the current recipes' scores were 2 and 3, the sum, 5,
        # would only create one recipe (with a score of 5) with its single digit.
        total = sum([ self.scores[_] for _ in self.elves])
        digits = [int(_) for _ in str(total)]
        self.scores.extend(digits)

    def move_elves(self):
        # After all new recipes are added to the scoreboard, each Elf picks a new
        # current recipe. To do this, the Elf steps forward through the scoreboard
        # a number of recipes equal to 1 plus the score of their current recipe. So,
        # after the first round, the first Elf moves forward 1 + 3 = 4 times, while
        # the second Elf moves forward 1 + 7 = 8 times. If they run out of recipes,
        # they loop back around to the beginning. After the first round, both Elves
        # happen to loop around until they land on the same recipe that they had in
        # the beginning; in general, they will move to different recipes.
        modulo = len(self.scores)
        for index in range(len(self.elves)):
            moves = 1 + self.scores[self.elves[index]]
            nxt_recipe = (self.elves[index] + moves) % modulo
            self.elves[index] = nxt_recipe

    def next_ten(self, after, number=NUMBER_OF_RECIPES):
        # 1. Determine length of steps needed
        need = after + number
        # 2. Loop until we have at least that many
        while len(self.scores) < need:
            self.step()
        # 3. Get the recipes scores
        recipes = self.scores[after:after+number]
        # 4. Turn then into one big number
        return ''.join([str(_) for _ in recipes])

    def first_appears(self, after):
        # 1. Get the individual digits of the number we want
        digits = [int(_) for _ in str(after)]
        # 2. Need to start with at least the number of digits
        while len(self.scores) < len(digits):
            self.step()
        while True:
            if self.match_digits(digits):
                return len(self.scores) - len(digits)
            if self.match_digits_minus_one(digits):
                return -1 + len(self.scores) - len(digits)
            self.step()
        return None

    def match_digits(self, digits):
        for index in range(-1, -len(digits) - 1, -1):
            if self.scores[index] != digits[index]:
                return False
        return True

    def match_digits_minus_one(self, digits):
        for index in range(-1, -len(digits) - 1, -1):
            if self.scores[index-1] != digits[index]:
                return False
        return True

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 1. Return the solution for part one
        return self.next_ten(self.after)


    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 1. Return the solution for part two
        return self.first_appears(self.after)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                        r e c i p e s . p y                     end
# ======================================================================
