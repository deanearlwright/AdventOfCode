# ======================================================================
# Go With The Flow
#   Advent of Code 2018 Day 19 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                        b a c k g r o u n d . p y
# ======================================================================
"A solver for the Advent of Code 2018 Day 19 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import device
# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
PC_REG = '#ip'

# ======================================================================
#                                                             Background
# ======================================================================


class Background(object):   # pylint: disable=R0902, R0205
    "Object for Go With The Flow"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.pc_reg = None
        self.program = None
        self.regs = None
        self.pc = None

        # 2. Process text (if any)
        if text is not None:
            self.process_text(text)

    def process_text(self, text):
        # 1. Starts with nothing
        self.program = []
        # 2. Loop for all of the lines of the text
        for line in text:
            parts = line.split(' ')
            if parts[0] == PC_REG:
                self.pc_reg = int(parts[1])
            elif parts[0] in device.INSTS:
                self.program.append([parts[0], int(parts[1]), int(parts[2]), int(parts[3])])
            else:
                print("*** Unexpected program line: %s" % line)

    def reset(self):
        self.pc = 0
        self.regs = [0, 0, 0, 0, 0, 0]
        if self.part2:
            self.regs[0] = 1

    def step(self):
        # 1. Check validity of program counter
        if self.pc < 0 or self.pc >= len(self.program):
            return False
        # 2. Set the register with the program counter (if needed)
        if self.pc_reg is not None:
            self.regs[self.pc_reg] = self.pc
        # 3. Execute the instruction
        inst = self.program[self.pc]
        device.INSTS[inst[device.OPCODE]](inst, self.regs)
        # 4. Set the program counter from the register (if needed)
        if self.pc_reg is not None:
            self.pc = self.regs[self.pc_reg]
        # 5. Increment the program counter
        self.pc += 1
        # 6. Return success
        return True

    def run(self, verbose=False, limit=0):
        self.reset()
        steps = 0
        pc_before = self.pc
        regs_before = [r for r in self.regs]

        while self.step() and (limit == 0 or steps < limit):
            if verbose:
                inst = self.program[pc_before]
                print("ip=%d %s %s %d %d %d %s" %
                      (pc_before, str(regs_before),
                       inst[device.OPCODE], inst[device.REGA], inst[device.REGB], inst[device.REGC],
                       str(self.regs)))
            steps += 1
            pc_before = self.pc
            regs_before = [r for r in self.regs]

    def run_factor(self, verbose=False, limit=0):
        # 1. Start at the beginning
        self.reset()
        result = 0
        # 2. Get number to factor
        num = 919 + self.regs[0] * 10550400
        if verbose:
            print("Factoring %d" % num)
        # 3. Loop for the possible factors
        for factor in range(1, num + 1):
            # 3. Is the number a factor?
            if num % factor == 0:
                result += factor
                if verbose:
                    print("Adding in %d giving %d" % (factor, result))
        # 5. Return the sum of the divisors
        return result

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 1. Run the background program
        factoring = self.run_factor(verbose=verbose, limit=limit)
        self.run(verbose=verbose, limit=limit)
        if factoring != self.regs[0]:
            print("factoring = %d, run_r0 = %d" % (factoring, self.regs[0]))
        # 2. Return the solution for part one
        return self.regs[0]

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 1. Return the solution for part two
        return self.run_factor(verbose=verbose, limit=limit)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                     b a c k g r o u n d . p y                  end
# =====================================================================
