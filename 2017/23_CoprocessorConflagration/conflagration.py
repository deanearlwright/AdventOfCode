# ======================================================================
# Coprocessor Conflagration
#   Advent of Code 2017 Day 23 -- Eric Wastl -- https://adventofcode.com
#
# Computer implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                  c o n f l a g r a t i o n . p y
# ======================================================================
"A solver for conflagration for Advent of Code 2017 Day 23"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from itertools import repeat

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
INSTS = frozenset(['set', 'sub', 'mul', 'jnz'])
REGS = frozenset(list('abcdefgh'))
OTHER = [1, 0]

# ----------------------------------------------------------------------
#                                                      Utility Functions
# ----------------------------------------------------------------------
def is_prime(number):  # based on code from Nikita Tiwari
    if number % 2 == 0 or number % 3 == 0:
        return False
    num = 5
    while num * num <= number:
        if number % num == 0 or number % (num + 2) == 0:
            return False
        num += 6
    return True

# ======================================================================
#                                                          Conflagration
# ======================================================================


class Conflagration(object):   # pylint: disable=R0902, R0205
    "Object for Coprocessor Conflagration"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.instructions = []
        self.reset()

        # 2. Process text (if any)
        if text is not None:
            self.text_to_instructions()

    def reset(self):
        "Reset the state of the coprocessor"

        # 1. Set it back to the initial values
        self.position = 0
        self.registers = dict(zip(REGS, repeat(0, len(REGS))))
        self.terminated = False
        self.mul_knt = 0

        # 2. For part two, turn the coprocessper on
        if self.part2:
            self.registers['a'] = 1

    def text_to_instructions(self):
        "Convert text to instructions, duh"

        # 1. Start with nothing
        self.instructions = []

        # 2. Loop for all of the lines of text
        for line in self.text:

            # 3. Break the line into instructions and operands
            parts = line.split()
            inst = parts[0]
            op1 = parts[1]
            if len(parts) > 2:
                op2 = parts[2]
            else:
                op2 = '0'

            # 4. Validate the instruction and operands
            assert inst in INSTS
            assert op1 in REGS or op1.isdigit() or op1[0] == '-' and op1[1:].isdigit()
            assert op2 in REGS or op2.isdigit() or op2[0] == '-' and op2[1:].isdigit()

            # 5. Convert digital operands
            if op1 not in REGS:
                op1 = int(op1)
            if op2 not in REGS:
                op2 = int(op2)

            # 6. Add the instruction
            self.instructions.append((inst, op1, op2))

    def get_register(self, reg):
        "Get register value"

        assert reg in REGS
        return self.registers[reg]

    def set_register(self, reg, value):
        "Set register value"

        assert reg in REGS
        self.registers[reg] = value
        if self.part2 and reg == 'h':
            print("regs: %s" % (self.registers), flush=True)

    def get_value(self, reg_or_int):
        "Get register value"

        if reg_or_int in REGS:
            return self.get_register(reg_or_int)
        return reg_or_int

    def step(self, verbose=False):
        "Execute one instruction step"

        # 1. Verify the instruction counter
        pc = self.position
        if pc < 0 or pc >= len(self.instructions):
            if verbose:
                print("Invalid instuction position %d" % pc, flush=True)
            self.terminated = True
            return False

        # 2. Assume no branch
        next_position = pc + 1

        # 3. Get the instruction and operands
        inst, op1, op2 = self.instructions[pc]
        if verbose:
            print("%d: %s %s %s" % (pc, inst, op1, op2), flush=True)

        # 4. Execute the instruction
        # 4a. set X Y sets register X to the value of Y.
        if inst == 'set':
            self.set_register(op1, self.get_value(op2))

        # 4b. sub X Y decreases register X by the value of Y.
        elif inst == 'sub':
            self.set_register(op1, self.get_value(op1) - self.get_value(op2))

        # 4c. mul X Y sets register X to the result of multiplying the value
        #     contained in register X by the value of Y.
        elif inst == 'mul':
            self.set_register(op1, self.get_value(op1) * self.get_value(op2))
            self.mul_knt += 1

        # 4d. jnz X Y jumps with an offset of the value of Y, but only if the value
        #     of X is not zero. (An offset of 2 skips the next instruction,
        #     an offset of -1 jumps to the previous instruction, and so on.)
        elif inst == 'jnz':
            if self.get_value(op1) != 0:
                next_position = pc + self.get_value(op2)

        # 5. Set next instruction position
        self.position = next_position

        # 6. Return True
        return True

    def run(self, verbose=False, limit=0):
        "Run instructions"

        # 1. Start count at zero
        knt_steps = 0

        # 2. Loop forever
        while True:

            # 3. Execute an instruction, stop if bad position
            if not self.step(verbose=verbose):
                break
            knt_steps += 1

            # 4. Stop if running too long
            if knt_steps > limit > 0:
                print("Reached execution limit")
                break

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 1. Calculate the part one result
        op_zero = self.instructions[0][2]
        result = (op_zero - 2) ** 2

        # 2. Return the solution for part one
        return result


    def part_one_slow(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 1. Run the instructions
        self.run(verbose=verbose, limit=limit)

        # 2. Return the solution for part one
        return self.mul_knt


    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 1. Start with nothing
        result = 0

        # 2. Loop from the lower_limit to the upper_limit by loop_skip
        lower_limit = (self.instructions[4][2] * self.instructions[0][2]) - self.instructions[5][2]
        upper_limit = lower_limit - self.instructions[7][2]
        loop_skip = -self.instructions[30][2]
        if verbose:
            print("Loop from %d to %d by %d" %
                  (lower_limit, upper_limit, loop_skip))
        for number in range(lower_limit, upper_limit+1, loop_skip):

            # 3. Check if the number is prime or composite
            if not is_prime(number):

                # 4. Count the number of composite numbers
                result += 1

        # 5. Return the solution for part two
        return result

    def part_two_slow(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 1. Run the instructions
        self.run(verbose=verbose, limit=limit)

        # 2. Return the solution for part two
        return self.registers['h']

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end               c o n f l a g r a t i o n . p y                  end
# ======================================================================
