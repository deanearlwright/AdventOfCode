# ======================================================================
# Handheld Halting
#   Advent of Code 2020 Day 08 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         c o n s o l e . p y
# ======================================================================
"A solver for the Advent of Code 2020 Day 08 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import instruction

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                Console
# ======================================================================


class Console(object):   # pylint: disable=R0902, R0205
    "Object for Handheld Halting"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.instructions = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            for line in text:
                self.instructions.append(instruction.Instruction(text=line, part2=part2))

    def run_until_dup(self):
        "Returns acc at first duplicate instruction"

        # 1. Initial values
        acc = 0
        pc = 0
        run = True

        # 2. Loop until dup
        while run:

            # 3. Run the single instruction
            run, pc, acc = self.instructions[pc].execute(pc, acc, limit=1)

        # 4. Return the accumulator before the first duplicate instruction
        return acc

    def run_until_dup_or_terminated(self):
        "Returns acc at first duplicate instruction or termination"

        # 1. Initial values
        acc = 0
        pc = 0
        run = True

        # 2. Loop until dup
        while run:

            # 3. Check for termination, Return True if so
            if pc >= len(self.instructions):
                return True, acc

            # 4. Run the single instruction
            run, pc, acc = self.instructions[pc].execute(pc, acc, limit=1)

        # 4. Return False and the accumulator before the first duplicate instruction
        return False, acc

    def reset(self):
        "Reset all of the execution counters"
        for inst in self.instructions:
            inst.reset()

    def find_repair(self):
        "Returns acc after repaired program terminates"

        # 1. Loop for all of the instructions
        for number, inst in enumerate(self.instructions):
            print(number)

            # 2. Repair this instruction
            repaired = inst.repair()
            if not repaired:
                continue

            # 3. Reset the counters
            self.reset()

            # 4. Run the boot code
            term, acc = self.run_until_dup_or_terminated()

            # 5. If it terminated, return the accumulator
            if term:
                return acc

            # 6. Put the instuction back
            inst.repair()

        # 7. Well that just not right
        return None

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 1. Return the solution for part one
        return self.run_until_dup()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 1. Return the solution for part two
        return self.find_repair()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                        c o n s o l e . p y                     end
# ======================================================================
