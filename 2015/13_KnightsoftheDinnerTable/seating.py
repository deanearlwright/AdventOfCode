# ======================================================================
# Knights of the Dinner Table
#   Advent of Code 2015 Day 13 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         s e a t i n g . p y
# ======================================================================
"A solver for the Advent of Code 2015 Day 13 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import re
from itertools import permutations

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
RE_SEATING = re.compile("([A-Z][a-z]+) would (gain|lose) ([0-9]+) "
                        + "happiness units by sitting next to ([A-Z][a-z]+).")

# ======================================================================
#                                                                Seating
# ======================================================================


class Seating(object):   # pylint: disable=R0902, R0205
    "Object for Knights of the Dinner Table"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.people = set()
        self.preferences = {}

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            for line in text:
                self._process_line(line)

    def _process_line(self, line):
        "Parse and assign values from the line"

        # 1. Parse the line
        match = RE_SEATING.match(line)
        if not match:
            print("Unable to parse line:", line)
            return

        # 2. Get the interesting bits
        who, gain, amount, whom = match.groups()
        amount = int(amount)
        if gain == "lose":
            amount = -amount

        # 3. Save the information
        self.people.add(who)
        self.people.add(whom)
        self.preferences[(who, whom)] = amount

    def optimum(self, verbose=False):
        "Seat the people optimumly"

        # 1. Start with very low expectations
        result = -9999999
        best = []
        if len(self.people) < 2:
            return result

        # 2. Loop for all of the possible seatings
        for seating_chart in permutations(self.people):

            # 3. Determine the happiness score for this seating chart
            score = self.total_happiness(seating_chart)

            # 4. If this one is better, save it
            if score > result:
                result = score
                best = seating_chart

        # 5. Return the result
        if verbose:
            print("Best", best, result)
        return result

    def total_happiness(self, seating_chart):
        "Return the total happiness of this seating chart"

        # 1. Start with nothing
        result = 0

        # 2. Loop for all the pairs of people
        for indx in range(len(self.people) - 1):

            # 3. Score this pair of people
            result += self.preferences[(seating_chart[indx], seating_chart[indx + 1])]
            result += self.preferences[(seating_chart[indx + 1], seating_chart[indx])]

        # 4. Don't forget that the table is circular
        result += self.preferences[(seating_chart[0], seating_chart[-1])]
        result += self.preferences[(seating_chart[-1], seating_chart[0])]

        # 5. Return the score for this seating chart
        return result

    def seat_yourself(self):
        "Add yourself into the seating situation"

        # 1. Loop for all of the people
        for person in self.people:

            # 2. You are neutral about them and they are neutral about you
            self.preferences[("Me", person)] = 0
            self.preferences[(person, "Me")] = 0

        # 3. You are a person
        self.people.add("Me")

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.optimum(verbose=verbose)

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        self.seat_yourself()
        return self.optimum(verbose=verbose)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                       s e a t i n g . p y                      end
# ======================================================================
