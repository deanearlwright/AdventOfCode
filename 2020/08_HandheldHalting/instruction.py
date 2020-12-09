# ======================================================================
# Handheld Halting
#   Advent of Code 2020 Day 08 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                      i n s t r u c t i o n . p y
# ======================================================================
"A single instruction for the Advent of Code 2020 Day 08 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
INSTRUCTIONS = ['nop', 'acc', 'jmp']

# ======================================================================
#                                                            Instruction
# ======================================================================


class Instruction(object):   # pylint: disable=R0902, R0205
    "Single Instruction Object for Handheld Halting"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.operation = None
        self.argument = 0
        self.executed = 0

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            parts = text.split(' ')
            assert len(parts) == 2
            assert parts[0] in INSTRUCTIONS
            self.operation = parts[0]
            self.argument = int(parts[1])

    def execute(self, pc, acc, verbose=False, limit=0):
        "Execute a single instruction, Returns T/F, pc, acc"

        # 1. Don't execute instruction if limit has been reached
        if self.executed >= limit:
            return False, pc, acc

        # 2. Execute the instruction
        if self.operation == 'nop':
            pc += 1
        elif self.operation == 'acc':
            acc += self.argument
            pc += 1
        else:
            pc += self.argument

        # 3. Record our passage
        self.executed += 1

        # 4. Return the results
        return True, pc, acc

    def reset(self):
        "Reset the number of times the instruction is executed"
        self.executed = 0

    def repair(self):
        "Repair jmp or nop instructions"
        if self.operation == 'nop':
            self.operation = 'jmp'
            return True
        if self.operation == 'jmp':
            self.operation = 'nop'
            return True
        return False


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                   i n s t r u c t i o n . p y                  end
# ======================================================================
