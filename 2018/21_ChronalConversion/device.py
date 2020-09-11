# ======================================================================
# Chronal Conversion
#   Advent of Code 2018 Day 21 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         d e v i c e . p y
# ======================================================================
"A computing device for the Advent of Code 2018 Day 21/19/16 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
OPCODE = 0
REGA = 1
REGB = 2
REGC = 3

INSTRUCTION_NAMES = ['addr', 'addi',
                     'mulr', 'muli',
                     'banr', 'bani',
                     'borr', 'bori',
                     'setr', 'seti',
                     'gtir', 'gtri', 'gtrr',
                     'eqir', 'eqri', 'eqrr']

# ----------------------------------------------------------------------
#                                                           instructions
# ----------------------------------------------------------------------

# --- Addition:


def addr(inst, regs):
    # addr (add register) stores into register C the result of adding
    #      register A and register B.
    regs[inst[REGC]] = regs[inst[REGA]] + regs[inst[REGB]]


def addi(inst, regs):
    # addi (add immediate) stores into register C the result of adding
    #      register A and value B.
    regs[inst[REGC]] = regs[inst[REGA]] + inst[REGB]

# --- Multiplication:


def mulr(inst, regs):
    # mulr (multiply register) stores into register C the result of
    #      multiplying register A and register B.
    regs[inst[REGC]] = regs[inst[REGA]] * regs[inst[REGB]]


def muli(inst, regs):
    # muli (multiply immediate) stores into register C the result of
    #      multiplying register A and value B.
    regs[inst[REGC]] = regs[inst[REGA]] * inst[REGB]

# --- Bitwise AND:


def banr(inst, regs):
    # banr (bitwise AND register) stores into register C the result of the
    #      bitwise AND of register A and register B.
    regs[inst[REGC]] = regs[inst[REGA]] & regs[inst[REGB]]


def bani(inst, regs):
    # bani (bitwise AND immediate) stores into register C the result of the
    #      bitwise AND of register A and value B.
    regs[inst[REGC]] = regs[inst[REGA]] & inst[REGB]

# --- Bitwise OR:


def borr(inst, regs):
    # borr (bitwise OR register) stores into register C the result of the
    #      bitwise OR of register A and register B.
    regs[inst[REGC]] = regs[inst[REGA]] | regs[inst[REGB]]


def bori(inst, regs):
    # bori (bitwise OR immediate) stores into register C the result of the
    #      bitwise OR of register A and value B.
    regs[inst[REGC]] = regs[inst[REGA]] | inst[REGB]

# --- Assignment:


def setr(inst, regs):
    # setr (set register) copies the contents of register A into register C.
    #    (Input B is ignored.)
    regs[inst[REGC]] = regs[inst[REGA]]


def seti(inst, regs):
    # seti (set immediate) stores value A into register C.
    #    (Input B is ignored.)
    regs[inst[REGC]] = inst[REGA]

# --- Greater-than testing:


def gtir(inst, regs):
    # gtir (greater-than immediate/register) sets register C to 1 if value A
    #      is greater than register B. Otherwise, register C is set to 0.
    if inst[REGA] > regs[inst[REGB]]:
        regs[inst[REGC]] = 1
    else:
        regs[inst[REGC]] = 0


def gtri(inst, regs):
    # gtri (greater-than register/immediate) sets register C to 1 if
    #      register A is greater than value B. Otherwise, register C is set to 0.
    if regs[inst[REGA]] > inst[REGB]:
        regs[inst[REGC]] = 1
    else:
        regs[inst[REGC]] = 0


def gtrr(inst, regs):
    # gtrr (greater-than register/register) sets register C to 1 if register
    #      A is greater than register B. Otherwise, register C is set to 0.
    if regs[inst[REGA]] > regs[inst[REGB]]:
        regs[inst[REGC]] = 1
    else:
        regs[inst[REGC]] = 0


# --- Equality testing:

def eqir(inst, regs):
    # eqir (equal immediate/register) sets register C to 1 if value A is
    #      equal to register B. Otherwise, register C is set to 0.
    if inst[REGA] == regs[inst[REGB]]:
        regs[inst[REGC]] = 1
    else:
        regs[inst[REGC]] = 0


def eqri(inst, regs):
    # eqri (equal register/immediate) sets register C to 1 if register A is
    #      equal to value B. Otherwise, register C is set to 0.
    if regs[inst[REGA]] == inst[REGB]:
        regs[inst[REGC]] = 1
    else:
        regs[inst[REGC]] = 0


def eqrr(inst, regs):
    # eqrr (equal register/register) sets register C to 1 if register A is
    #      equal to register B. Otherwise, register C is set to 0
    if regs[inst[REGA]] == regs[inst[REGB]]:
        regs[inst[REGC]] = 1
    else:
        regs[inst[REGC]] = 0


INSTS = {
  'addr': addr,
  'addi': addi,
  'mulr': mulr,
  'muli': muli,
  'banr': banr,
  'bani': bani,
  'borr': borr,
  'bori': bori,
  'setr': setr,
  'seti': seti,
  'gtir': gtir,
  'gtri': gtri,
  'gtrr': gtrr,
  'eqir': eqir,
  'eqri': eqri,
  'eqrr': eqrr,
}

PC_REG = '#ip'

# ======================================================================
#                                                                 Device
# ======================================================================


class Device(object):   # pylint: disable=R0902, R0205
    "Object for Chronal Classification"

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
            elif parts[0] in INSTS:
                self.program.append([parts[0], int(parts[1]), int(parts[2]), int(parts[3])])
            else:
                print("*** Unexpected program line: %s" % line)

    def reset(self, r0=0):
        self.pc = 0
        self.regs = [r0, 0, 0, 0, 0, 0]

    def step(self):
        # 1. Check validity of program counter
        if self.pc < 0 or self.pc >= len(self.program):
            return False
        # 2. Set the register with the program counter (if needed)
        if self.pc_reg is not None:
            self.regs[self.pc_reg] = self.pc
        # 3. Execute the instruction
        inst = self.program[self.pc]
        INSTS[inst[OPCODE]](inst, self.regs)
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
                       inst[OPCODE], inst[REGA], inst[REGB], inst[REGC],
                       str(self.regs)))
            steps += 1
            pc_before = self.pc
            regs_before = [r for r in self.regs]


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         d e v i c e . p y                      end
# ======================================================================

