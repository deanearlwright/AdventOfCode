# ======================================================================
# Monkey in the Middle
#   Advent of Code 2022 Day 11 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         s o l v e r . p y
# ======================================================================
"A solver for the Advent of Code 2022 Day 11 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import math
import monkey

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                 Solver
# ======================================================================


class Solver(object):   # pylint: disable=R0902, R0205
    "Object for Monkey in the Middle"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.monkeys = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

        # 3. Adjust worry level for part 2
        #    I just knew there was a reason that all the tests were prime
        if part2:
            modulo = math.prod([_.test for _ in self.monkeys])
            for mon_key in self.monkeys:
                mon_key.modulo = modulo

    def _process_text(self, text):
        "Assign values from text"

        # 1. Start with nothing
        lines = []

        # 2. Loop through all the lines of text
        for line in text:

            # 3. Add line to the lines for this monkey
            lines.append(line)

            # 4. If this is not the final line for a monkey, continue
            if "If false:" not in line:
                continue

            # 5. Create a new monkey
            mon_key = monkey.Monkey(text=lines, part2=self.part2)

            # 6. Add to the barrel of monkeys
            self.monkeys.append(mon_key)

            # 7. Get ready to collect the lines for the next monkey
            lines.clear()

    def round(self):
        "Simulate one round of monkey business"

        # 1. Loop for all the monkeys
        for mon_key in self.monkeys:

            # 2. Get the actions of that monkey
            throws = mon_key.round()

            # 3. Execute the throws
            self.toss(throws)

    def toss(self, throws):
        "Execute the monkey tosses"

        # 1. Loop for the throws
        for throw in throws:

            # 2. Throw it
            self.monkeys[throw[1]].receive(throw[0])

    def monkey_business(self):
        "Return the product of the two monkeys with the most inspections"

        # 1. Get the inspections
        inspections = [_.inspections for _ in self.monkeys]

        # 2. Sort them
        inspections.sort()

        # 3. Return the product of the two most active
        return inspections[-1] * inspections[-2]

    def rounds(self, verbose=False, rounds=0):
        "Execute several rounds of monkey toss and return the monkey_business"

        # 1. Determine the number of rounds
        if rounds == 0:
            rounds = 20
            if self.part2:
                rounds = 10000

        # 2. Go monkeys go
        for number in range(rounds):
            self.round()
            if verbose and 0 == number % 1000:
                print(number, flush=True)

        # 3. Return the monkey_business
        return self.monkey_business()

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.rounds()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.rounds(verbose=verbose)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                        s o l v e r . p y                       end
# ======================================================================
