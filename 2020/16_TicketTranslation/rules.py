# ======================================================================
# Ticket Translation
#   Advent of Code 2020 Day 16 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                            r u l e s . p y
# ======================================================================
"A class for the Advent of Code 2020 Day 16 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import rule

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                  Rules
# ======================================================================


class Rules(object):   # pylint: disable=R0902, R0205
    "Object for Rules Translation"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.rules = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            for line in text:
                if line.startswith('your ticket'):
                    break
                self.rules.append(rule.Rule(text=line, part2=part2))

    def is_valid(self, number):
        "Returns True if the number is valid for any rule"

        # 1. Loop for all of the rules
        for rule in self.rules:

            # 2. Return True if the number is valid for this rule
            if rule.is_valid(number):
                return True

        # 3. Return False as the number is not valid for any rule
        return False

    def determine_fields(self, position, numbers):
        "Determine which rules matches all of these numbers"

        # 1. Loop for all of the rules
        for rul in self.rules:

            # 2. If all of the numbers valid for this rule, this is the position for it
            if rul.all_valid(numbers):
                rul.position.add(position)
                print('Adding position %d to rule %s' % (position, rul.name))

    def are_fields_resolved(self):
        "Return True when no field has more than one possible position"
        for rul in self.rules:
            if len(rul.position) > 1:
                return False
        return True

    def resolve_fields(self):
        "There can be only one"

        while not self.are_fields_resolved():
            for what, _ in enumerate(self.rules):
                where = []
                for rul in self.rules:
                    if what in rul.position:
                        where.append(rul)
                if len(where) == 1:
                    where[0].position = set([what])
                    print('Setting %s to %d' % (where[0].name, what))
                    for rul2 in self.rules:
                        if where[0] != rul2:
                            if what in rul2.position:
                                rul2.position -= what

    def __len__(self):
        return len(self.rules)

    def __iter__(self):
        return iter(self.rules)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                           r u l e s . p y                      end
# ======================================================================
