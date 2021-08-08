# ======================================================================
# Safe Cracking
#   Advent of Code 2016 Day 23 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         a s s e m b u n n y . p y
# ======================================================================
"A solver for the Advent of Code 2016 Day 23 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import math

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
EGGS_ONE = 7
EGGS_TWO = 12
TOGGLE = {
    'inc': 'dec',
    'dec': 'inc',
    'tgl': 'inc',
    'cpy': 'jnz',
    'jnz': 'cpy',
}

# ======================================================================
#                                                             Assembunny
# ======================================================================


class Assembunny(object):   # pylint: disable=R0902, R0205
    "Object for Safe Cracking"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
        self.program_counter = 0
        self.instructions = self.text

    def reset(self):
        "Restart the computer"
        self.registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
        self.program_counter = 0
        self.instructions = self.text

    def fetch(self, arg):
        "Get the literal or register value"
        if arg.isalpha():
            return self.registers[arg]
        return int(arg)

    def step(self, verbose=False):
        "Execute a single step of the computer"
        # 1. Can't execute instruction if pc too low or too high
        if self.program_counter < 0 or self.program_counter >= len(self.instructions):
            return False
        # 2. Fetch the instruction
        inst = self.instructions[self.program_counter].split()
        if verbose:
            print('pc: %d, %s' % (self.program_counter, ' '.join(inst)))
        # 3. Execute the instruction
        if inst[0] == 'cpy':
            if inst[2] in self.registers:
                self.registers[inst[2]] = self.fetch(inst[1])
            self.program_counter += 1
        elif inst[0] == 'inc':
            self.registers[inst[1]] += 1
            self.program_counter += 1
        elif inst[0] == 'dec':
            self.registers[inst[1]] -= 1
            self.program_counter += 1
        elif inst[0] == 'jnz':
            if self.fetch(inst[1]) != 0:
                self.program_counter += self.fetch(inst[2])
            else:
                self.program_counter += 1
        elif inst[0] == 'tgl':
            toggle_at = self.program_counter + self.fetch(inst[1])
            if 0 <= toggle_at < len(self.instructions):
                inst_old = self.instructions[toggle_at].split()
                inst_new = inst_old.copy()
                inst_new[0] = TOGGLE[inst_new[0]]
                self.instructions[toggle_at] = ' '.join(inst_new)
                if verbose:
                    print("Changed inst at %d from %s to %s" %
                          (toggle_at, ' '.join(inst_old), ' '.join(inst_new)))
            self.program_counter += 1
        else:
            print("Unknown instruction at %d: %s" % (self.program_counter, inst))
            return False
        return True

    def run(self, verbose=False, initial_a=0):
        "Execute instructions until stopped"
        self.registers['a'] = initial_a
        while self.step(verbose=verbose):
            pass
        return self.registers['a']

    def run_two(self, verbose=False, initial_a=0):
        "Do part two after decoding the assembler"

        # 1. Get the factorial of the input
        eggs_fact = math.factorial(initial_a)

        # 2, Find the big numbers
        nums = []
        for inst in self.instructions:
            inst_parts = inst.split()
            if inst_parts[1].isdigit():
                num = int(inst_parts[1])
                if num > 40:
                    nums.append(num)

        # 3. Return the final calculation
        if verbose:
            print(nums, eggs_fact)
        return nums[0] * nums[1] + eggs_fact

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.run(verbose=verbose, initial_a=EGGS_ONE)

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        if limit > 0:
            return self.run_two(verbose=verbose, initial_a=EGGS_TWO)
        return self.run(verbose=verbose, initial_a=EGGS_TWO)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    a s s e m b u n n y . p y                   end
# ======================================================================
