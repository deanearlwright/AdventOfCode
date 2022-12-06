# ======================================================================
# Supply Stacks
#   Advent of Code 2022 Day 05 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         s t a c k . p y
# ======================================================================
"Stack for the Advent of Code 2022 Day 05 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from collections import deque

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                  Stack
# ======================================================================


class Stack(object):   # pylint: disable=R0902, R0205
    "Object for Supply Stacks"

    def __init__(self, text=None, part2=False, number=0):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.number = number
        self.crates = deque()

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        # 1. Determine text offset from index
        offset = 1 + max(0, 4 * (self.number - 1))

        # 2. Loop for the lines of text
        for line in text:

            # 3. Is there a crate?
            if offset >= len(line) or line[offset] == " ":
                continue

            # 4. Add the crate
            # print(self.number, offset, line[offset], line)
            self.crates.appendleft(line[offset])

    def add(self, from_crane):
        "Add a create to the top of the stack"

        # 1. Loop for the crates
        for crate in from_crane:

            # 2. Add it to the stack
            self.crates.append(crate)

    def remove(self, number=1):
        "Take the top n crates(s) from the stack"

        # 1. Start with nothing
        result = []

        # 2. Loop for the number of crates to be removed
        for indx in range(number):

            # 3. Remove the crate and add it to the result
            result.append(self.crates.pop())

        # 4. Return the crates removed from the stack
        return result

    def top(self):
        "Return the label on the top crate"
        if len(self.crates) == 0:
            return " "
        return self.crates[-1]

    def labels(self):
        "Return the labels on the crates"

        result = []
        for label in self.crates:
            result.append(label)
        return ''.join(result)

    def __len__(self):
        "Return the number of crates in the stack"
        return len(self.crates)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         s t a c k . p y                        end
# ======================================================================
