# ======================================================================
# Leonardos Monorail
#   Advent of Code 2016 Day 12 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                       a s s e m b u n n y . p y
# ======================================================================
"A solver for the Advent of Code 2016 Day 12 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------


# ======================================================================
#                                                             Assembunny
# ======================================================================


class Assembunny(object):   # pylint: disable=R0902, R0205
    "Object for Leonardos Monorail"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
        self.pc = 0

    def reset(self):
        "Restart the computer"
        self.registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
        self.pc = 0

    def fetch(self, arg):
        "Get the literal or register value"
        if arg.isalpha():
            return self.registers[arg]
        return int(arg)

    def step(self):
        "Execute a single step of the computer"
        # 1. Can't execute instruction if pc too low or too high
        if self.pc < 0 or self.pc >= len(self.text):
            return False
        # 2. Fetch the instruction
        inst = self.text[self.pc].split()
        # 3. Execute the instruction
        if inst[0] == 'cpy':
            self.registers[inst[2]] = self.fetch(inst[1])
            self.pc += 1
        elif inst[0] == 'inc':
            self.registers[inst[1]] += 1
            self.pc += 1
        elif inst[0] == 'dec':
            self.registers[inst[1]] -= 1
            self.pc += 1
        elif inst[0] == 'jnz':
            if self.fetch(inst[1]) != 0:
                self.pc += self.fetch(inst[2])
            else:
                self.pc += 1
        else:
            print("Unknown instruction at %d: %s" % (self.pc, inst))
            return False
        return True

    def run(self):
        "Execute instructions until stopped"
        while self.step():
            pass
        return self.registers['a']

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
        self.registers['c'] = 1
        return self.run()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    a s s e m b u n n y . p y                   end
# ======================================================================
