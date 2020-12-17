# ======================================================================
# Ticket Translation
#   Advent of Code 2020 Day 16 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         t i c k e t s . p y
# ======================================================================
"A solver for the Advent of Code 2020 Day 16 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import rules
import ticket

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                Tickets
# ======================================================================


class Tickets(object):   # pylint: disable=R0902, R0205
    "Object for Ticket Translation"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.rules = []
        self.mine = None
        self.nearby = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.process_text(text)

    def process_text(self, text):
        "Process the three part input"

        # 1. Start with the rules
        self.rules = rules.Rules(text=text, part2=self.part2)

        # 2. Process your ticket
        found = False
        for line in text:
            if found:
                self.mine = ticket.Ticket(text=line, part2=self.part2)
                break
            if line.startswith('your ticket'):
                found = True

        # 3. Process the other ticket
        found = False
        for line in text:
            if found:
                self.nearby.append(ticket.Ticket(text=line, part2=self.part2))
                continue
            if line.startswith('nearby ticket'):
                found = True

    def ticket_scanning_error_rate(self):
        "Return the sum of the invalid values"

        # 1. Start with nothing
        result = 0

        # 2. Loop for all of the nearby tickets
        for tik in self.nearby:

            # 3. Loop for all of the numbers on the ticket
            for number in tik:

                # 4. If the number is not valid, add it to the sum
                if not self.rules.is_valid(number):
                    result += number
                    # print('Marking ticket %s as invalid' % str(tik.numbers))
                    tik.valid = False

        # 5. Return the sum of the invalid values
        return result

    def departure_fields(self):
        "Return the sum of the departure fields"

        # 1. Mark invalid tickets as such
        self.ticket_scanning_error_rate()

        # 2. Find_field_position()
        self.find_field_positions()

        # 3. Return product of departure fields
        result = 1
        for rul in self.rules:
            if rul.name.startswith('departure'):
                if len(rul.position) != 1:
                    print('Unable to determine field for %s' % rul.name)
                    continue
                result *= self.mine.numbers[list(rul.position)[0]]
        return result

    def find_field_positions(self):
        "Find the positions for each field"

        # 1. Loop for each position
        for position in range(len(self.mine)):

            # 2. Get the numbers for that position
            numbers = [_.numbers[position] for _ in self.nearby if _.valid]

            # 3. Determine the field for those numbers
            self.rules.determine_fields(position, numbers)

        # 4. Resolve conflicts
        self.rules.resolve_fields()

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 1. Return the solution for part one
        return self.ticket_scanning_error_rate()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 1. Return the solution for part two
        return self.departure_fields()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                       t i c k e t s . p y                      end
# ======================================================================
