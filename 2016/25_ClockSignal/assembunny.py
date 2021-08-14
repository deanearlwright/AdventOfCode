# ======================================================================
# Clock Signal
#   Advent of Code 2016 Day 25 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         a s s e m b u n n y . p y
# ======================================================================
"A solver for the Advent of Code 2016 Day 25 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
TOGGLE = {
    'inc': 'dec',
    'dec': 'inc',
    'tgl': 'inc',
    'cpy': 'jnz',
    'jnz': 'cpy',
    'out': 'inc',
}
CLOCK_COUNT = 10
NEXT = [1, 0]
START_CLOCK = 0
LIMIT_CLOCK = 999

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
        self.output = []

    def reset(self):
        "Restart the computer"
        self.registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
        self.program_counter = 0
        self.instructions = self.text
        self.output = []

    def fetch(self, arg):
        "Get the literal or register value"
        if arg.isalpha():
            return self.registers[arg]
        return int(arg)

    def step(self, verbose=False):  # pylint: disable=too-many-branches
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
        elif inst[0] == 'out':
            self.output.append(self.fetch(inst[1]))
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

    def run_until_out(self, verbose=False):
        "Run until the next output and return that output"

        # 1. What is the length of the current output
        current = len(self.output)

        # 2. Run until the length of the output changes
        while current == len(self.output):
            self.step(verbose=verbose)

        # 3. Return the new output
        return self.output[-1]

    def check_clock(self, verbose=False, initial_a=0):
        "Check if this initial a returns a clock signal"
        if verbose:
            print("check_clock", initial_a)

        # 1. Set up to run the machine
        self.reset()
        self.registers['a'] = initial_a
        want = NEXT[self.run_until_out()]
        count = 0

        # 2. Loop until the we get enough output
        while count < CLOCK_COUNT:

            # 3. Check that the next output is what we want
            if want != self.run_until_out():
                if verbose:
                    print("clock fail", self.output)
                return False

            # 4. Set up for the next clock signal
            want = NEXT[want]
            count += 1

        # 5. Look good to me
        if verbose:
            print("clock OK", self.output)
        return True

    def find_clock(self, verbose=False, limit=LIMIT_CLOCK):
        "Find the lowest initial a value that gives a clock signal"

        # 1. Start at the very beginning
        result = START_CLOCK

        # 2. Loop until it works
        while not self.check_clock(verbose=verbose, initial_a=result):

            # 3. Set up to try again
            result += 1

            # 4. Bail if we have been at this too long
            if result > limit > 0:
                return None

        # 5. Return the lowest value for a that generates a good clock signal
        return result

    def part_one(self, verbose=False, limit=LIMIT_CLOCK):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.find_clock(verbose=verbose, limit=limit)

    def part_two(self, verbose=False, limit=LIMIT_CLOCK):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.find_clock(verbose=verbose, limit=limit)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    a s s e m b u n n y . p y                   end
# ======================================================================
