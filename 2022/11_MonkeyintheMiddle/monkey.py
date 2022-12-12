# ======================================================================
# Monkey in the Middle
#   Advent of Code 2022 Day 11 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         m o n k e y . p y
# ======================================================================
"Monkey for the Advent of Code 2022 Day 11 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                 Monkey
# ======================================================================


class Monkey(object):   # pylint: disable=R0902, R0205
    "Object for Monkey in the Middle"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.number = 0
        self.items = []
        self.operation = []
        self.test = 0
        self.true = 0
        self.false = 0
        self.inspections = 0
        self.modulo = 3

        # 2. Process text (if any)
        if text is not None and len(text) == 6:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        # 1. Monkey number
        self.number = int(text[0].replace(":", "").split()[1])

        # 2. Starting items
        items = text[1].split(":")[1].split(",")
        self.items = [int(_) for _ in items]

        # 3. Operation
        self.operation = text[2].split(":")[1].split()[3:]

        # 4. Test
        self.test = int(text[3].split(":")[1].split()[2])

        # 5. If true
        self.true = int(text[4].split(":")[1].split()[3])

        # 5. If false
        self.false = int(text[5].split(":")[1].split()[3])

    def round(self):
        "A round for this single monkey"

        # 1. Start with nothing
        result = []

        # 2. Loop for each item
        for item in self.items:

            # 3. Inspect the item
            inspected = self.inspect(item)

            # 4. Add to the result
            result.append(inspected)

        # 5. All items will be throwm
        self.items.clear()

        # 6. Return the inspected items and the next monkey
        return result

    def inspect(self, item):
        "Inspect the item returning the new worry level and the next monkey"

        # 1. Update the worry level
        worry = self.new_worry(item)

        # 2. Is it divisible?
        divisible = 0 == worry % self.test

        # 3. Determine the next monkey
        if divisible:
            next_monkey = self.true
        else:
            next_monkey = self.false

        # 4. Increment the number of inspections
        self.inspections += 1

        # 5. Return the new worry level and next monkey
        return (worry, next_monkey)

    def new_worry(self, item):
        "Compute the new worry level"

        # 1. Determine the operand
        if self.operation[1] == "old":
            operand = item
        else:
            operand = int(self.operation[1])

        # 2. Do the initial calculation
        if self.operation[0] == "+":
            worry = item + operand
        else:
            worry = item * operand

        # 3. Don't worry be happy
        if self.part2:
            worry = worry % self.modulo
        else:
            worry = int(worry / self.modulo)

        # 4. Return the new worry level
        return worry

    def receive(self, item):
        "Receive an item from another monkey"

        # 1. Add the item
        self.items.append(item)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                        m o n k e y . p y                       end
# ======================================================================
