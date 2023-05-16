
# ======================================================================
# Monkey Math
#   Advent of Code 2022 Day 21 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         m o n k e y s . p y
# ======================================================================
"Monkeys for the Advent of Code 2022 Day 21 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from collections import defaultdict
import monkey

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
ROOT = "root"
YOU = "humn"

# ======================================================================
#                                                                Monkeys
# ======================================================================


class Monkeys(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Monkey Math"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.yellers = {}
        self.needs = defaultdict(list)
        self.root = None
        self.you = None

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

        # 3. Adjust for part two
        if self.part2:
            if self.root:
                self.root.operation = '=='
            if self.you:
                self.you.yells = monkey.VARIABLE

    def _process_text(self, text):
        "Assign values from text"

        # 1. Loop for all lines in the text
        for line in text:

            # 2. Create a monkey using that information
            a_monkey = monkey.Monkey(text=line, part2=self.part2)

            # 3. If this is the root monkey save him (or save you)
            if a_monkey.name == ROOT:
                self.root = a_monkey
            elif a_monkey.name == YOU:
                self.you = a_monkey

            # 4. If this monkey knows his/her number, add to yellers
            if a_monkey.yells is not None:
                self.yellers[a_monkey.name] = a_monkey

            # 5. Else add to the needy monkeys
            else:
                for need in a_monkey.needs:
                    self.needs[need].append(a_monkey)

    def satisfy_all(self):
        "Attempt to satisfy all the needs"

        # 1. We are done when the fat monkey sings,
        while self.root.yells is None:

            # 2. Loop for what needs to be satisified
            for what, who in list(self.needs.items()):

                # 3. Satisfy this need if we can, tell the waiting monkeys
                if what in self.yellers:
                    for a_monkey in who:
                        a_monkey.hears(what)

                        # 4. If the monkey now has all it needs, he yells
                        if len(a_monkey.needs) == 0:
                            a_monkey.do_the_math(
                                self.yellers[a_monkey.op1].yells,
                                self.yellers[a_monkey.op2].yells)
                            self.yellers[a_monkey.name] = a_monkey

                    # 5. No one is waiting for this anymore
                    del self.needs[what]

        # 9. Return what the root monkey is yelling
        return self.root.yells

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                      m o n k e y s . p y                     end
# ======================================================================
