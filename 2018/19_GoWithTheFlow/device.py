# ======================================================================
# Go With The Flow
#   Advent of Code 2018 Day 19 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         d e v i c e . p y
# ======================================================================
"A computing device for the Advent of Code 2018 Day 19 (was 16) puzzle"

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

# ======================================================================
#                                                                 Device
# ======================================================================


class Device(object):   # pylint: disable=R0902, R0205
    "Object for Chronal Classification"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text

    def run_program(self, opcodes, verbose=False):
        # 1. Set the registers
        regs = [0, 0, 0, 0, 0, 0]

        # 2. Loop for all of the instructions
        for inst in self.program:

            # 3. Execute the instruction
            before = [r for r in regs]
            name = opcodes[inst[OPCODE]]
            INSTS[name](inst, regs)
            if verbose:
                print("%s before=%s inst=%s after=%s" % (name, before, inst, regs))

        # 4. Return the final registers
        return regs


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         d e v i c e . p y                      end
# ======================================================================

