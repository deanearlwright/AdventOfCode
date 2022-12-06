# ======================================================================
# Supply Stacks
#   Advent of Code 2022 Day 05 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         c r a n e . p y
# ======================================================================
"Crane for the Advent of Code 2022 Day 05 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import stack

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                  Crane
# ======================================================================


class Crane(object):   # pylint: disable=R0902, R0205
    "Object for Supply Stacks"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.stacks = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        # 1. Find the number of stacks
        stack_text = []
        for line in text:
            if not line.startswith(" 1"):
                stack_text.append(line)
                continue
            num_stacks = len(line.split())
            break

        # 2. Create the stacks
        for number in range(num_stacks):
            self.stacks.append(stack.Stack(part2=False, text=stack_text, number=number + 1))

    def tops(self):
        "Return the labels on the top crate in each stack"

        # 1. Start with nothing
        result = []

        # 2. Loop for all the stacks
        for stk in self.stacks:

            # 3. Append the top of this stack
            #print(stk.number, stk.labels(), stk.top())
            result.append(stk.top())

        # 4. Return the labels
        return ''.join(result)

    def move(self, action):
        "Process a single move action"

        # 1. Break the action into number, from, to
        parts = action.split()
        number = int(parts[1])
        stack_from = int(parts[3]) - 1
        stack_to = int(parts[5]) - 1

        # 2. Get the crates removed from one stack
        removed = self.stacks[stack_from].remove(number)

        # 2.5 CrateMover 9001
        if self.part2:
            removed.reverse()

        # 3. Add then add them to the other
        self.stacks[stack_to].add(removed)

    def __len__(self):
        "Return the number of stacks"
        return len(self.stacks)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         c r a n e . p y                        end
# ======================================================================
