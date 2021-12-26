# ======================================================================
# Arithmetic Logic Unit
#   Advent of Code 2021 Day 24 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         a l u . p y
# ======================================================================
"Alu for the Advent of Code 2021 Day 24 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
INITIAL_REGS = {
    'w': 0,
    'x': 0,
    'y': 0,
    'z': 0,
}
REGS = set(list('wxyz'))
INSTRUCTIONS = set(["inp", "add", "mul", "div", "mod", "eql"])

# ======================================================================
#                                                                    Alu
# ======================================================================


class Alu(object):   # pylint: disable=R0902, R0205
    "Object for Arithmetic Logic Unit"

    def __init__(self, text=None, part2=False, inp=None):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.regs = INITIAL_REGS.copy()
        self.inst = []
        self.step = 0
        self.inp = []

        # 2. Process text
        if text:
            for line in text:
                parts = line.split()
                assert parts[0] in INSTRUCTIONS
                if len(parts) == 3:
                    if parts[2] not in REGS:
                        parts[2] = int(parts[2])
                self.inst.append(parts)

        # 3. Process input
        if inp:
            self.inp = [int(_) for _ in list(inp)]

    def reset(self):
        "Reset the alu"
        self.regs = INITIAL_REGS.copy()
        self.step = 0

    def get_arg(self, arg):
        "Get the value of the second argument"

        # 1. If string, return register value
        if isinstance(arg, str):
            return self.regs[arg]

        # 2. Else it is a constant number
        return arg

    def one_step(self):  # pylint: disable=too-many-branches
        "Execute a single step, Return False if done"

        # 1. Check if done
        if self.step >= len(self.inst):
            return False

        # 2. Get the instruction
        inst = self.inst[self.step]

        # 3. Execute the instruction
        arg1 = self.regs[inst[1]]
        if inst[0] == "inp":
            if len(self.inp) > 0:
                self.regs[inst[1]] = self.inp.pop(0)
            else:
                print("Out of input")
                return False
        elif inst[0] == "add":
            self.regs[inst[1]] = arg1 + self.get_arg(inst[2])
        elif inst[0] == "mul":
            self.regs[inst[1]] = arg1 * self.get_arg(inst[2])
        elif inst[0] == "div":
            arg2 = self.get_arg(inst[2])
            if arg2 == 0:
                print("Divide by zero")
                return False
            self.regs[inst[1]] = arg1 // arg2
        elif inst[0] == "mod":
            arg2 = self.get_arg(inst[2])
            if arg1 < 0 or arg2 <= 0:
                print("Illegal modulo")
                return False
            self.regs[inst[1]] = arg1 % arg2
        elif inst[0] == 'eql':
            arg2 = self.get_arg(inst[2])
            if arg1 == arg2:
                self.regs[inst[1]] = 1
            else:
                self.regs[inst[1]] = 0

        # 4. Increment program step counter
        self.step += 1

        # 5. Return Success
        return True

    def run(self):
        "Run the program"

        # 1. Loop for all the instructions
        while self.one_step():
            continue

        # 2. Return the value in the z register
        return self.regs['z']


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                           a l u . p y                          end
# ======================================================================
