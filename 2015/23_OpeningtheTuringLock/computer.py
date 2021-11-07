# ======================================================================
# Opening the Turing Lock
#   Advent of Code 2015 Day 23 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         c o m p u t e r . p y
# ======================================================================
"A solver for the Advent of Code 2015 Day 23 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                               Computer
# ======================================================================


class Computer(object):   # pylint: disable=R0902, R0205
    "Object for Opening the Turing Lock"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        if text is None:
            self.text = []
        self.regs = {'a': 0, 'b': 0}
        self.addr = 0
        self.reset()

    def reset(self):
        "Reset the computer"

        # 1. Restore the initial values
        self.regs = {'a': 0, 'b': 0}
        self.addr = 0

        # 2. Part two has a twist
        if self.part2:
            self.regs['a'] = 1

    def step(self):
        "Execute a single instruction"

        # 1. Get the instruction
        if self.addr < 0 or self.addr >= len(self.text):
            return False
        inst = self.text[self.addr]

        # 2. Break the instruction info parts
        parts = inst.replace(',', '').split()
        opcode = parts[0]
        op1 = parts[1]
        if len(parts) == 3:
            op2 = parts[2]
        else:
            op2 = None
        next_addr = self.addr + 1
        # print(self.addr, inst, opcode, op1, op2, next_addr)

        # 3. Execute the instruction
        if opcode == 'hlf':
            # 3a. hlf r sets register r to half its current value
            self.regs[op1] = self.regs[op1] // 2
        elif opcode == 'tpl':
            # 3b. tpl r sets register r to triple its current value
            self.regs[op1] = self.regs[op1] * 3
        elif opcode == 'inc':
            # 3c. inc r increments register r, adding 1 to it
            self.regs[op1] = self.regs[op1] + 1
        elif opcode == 'jmp':
            # 3d. jmp offset is a relative jump
            next_addr = self.addr + int(op1)
        elif opcode == 'jie':
            # 3e. jie r, offset is like jmp, but if reg r is even
            if self.regs[op1] % 2 == 0:
                next_addr = self.addr + int(op2)
        elif opcode == 'jio':
            # 3f. jio r, offset is like jmp, but if reg r is one
            if self.regs[op1] == 1:
                next_addr = self.addr + int(op2)
        else:
            print("Bad inst", self.addr, inst, opcode, op1, op2, next_addr)
            return False

        # 4. Set the program counter to its next value
        self.addr = next_addr

        # 5. Return success
        return True

    def run(self):
        "Run the program"

        # 1. Loop with the program counter is good
        while self.step():
            pass

        # 2. Return the b register
        return self.regs['b']

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.run()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.run()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                      c o m p u t e r . p y                     end
# ======================================================================
