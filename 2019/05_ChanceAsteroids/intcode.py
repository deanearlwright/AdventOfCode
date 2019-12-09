# ======================================================================
# Sunny with a Chance of Asteroids
#   Advent of Code 2019 Day 05 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                           i n t c o m p  . p y
# ======================================================================
"Computer for Chance of Asteroids problem for Advent of Code 2018 Day 05"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
STOP_HLT = 0   # Executed Halt (99) Opcode
STOP_XPC = 1   # Bad Program Counter ( < 0 or > positions)
STOP_BAD = 2   # Bad opcode
STOP_OPS = 3   # Bad Operand
STOP_STR = 4   # Bad Store
STOP_RUN = 5   # Single Step executed correctly
STOP_STP = 6   # Too many steps

OP_ADD = 1
OP_MUL = 2
OP_INP = 3
OP_OUT = 4
OP_JIT = 5
OP_JIF = 6
OP_SLT = 7
OP_SEQ = 8
OP_HLT = 99

OP_CODES = set([OP_ADD, OP_MUL, OP_INP, OP_OUT,
                OP_JIT, OP_JIF, OP_SLT, OP_SEQ,
                OP_HLT])

OP_LEN = {
    OP_ADD: 4,
    OP_MUL: 4,
    OP_INP: 2,
    OP_OUT: 2,
    OP_JIT: 3,
    OP_JIF: 3,
    OP_SLT: 4,
    OP_SEQ: 4,
    OP_HLT: 1
}

OP_NAME = {
    OP_ADD: 'ADD',
    OP_MUL: 'MUL',
    OP_INP: 'INP',
    OP_OUT: 'OUT',
    OP_JIT: 'JIT',
    OP_JIF: 'JIF',
    OP_SLT: 'SLT',
    OP_SEQ: 'SEQ',
    OP_HLT: 'HLT',
}

OP_STORE = {
    OP_ADD: 3,
    OP_MUL: 3,
    OP_INP: 1,
    OP_OUT: 0,
    OP_HLT: 0,
    OP_JIT: 0,
    OP_JIF: 0,
    OP_SLT: 3,
    OP_SEQ: 3,
}

POS_MODE = 0
IMM_MODE = 1

ADDR_RSLT = 0
ADDR_NOUN = 1
ADDR_VERB = 2

# ======================================================================
#                                                      Utility Functions
# ======================================================================
def op_name(opcode):
    "Decode opcode for humans"

    # 1. If no opcode, use '<->'
    if opcode is None:
        return '<->'

    # 2. If valid opcode, return its name
    if opcode in OP_CODES:
        return OP_NAME[opcode]

    # 3. Else return unknown
    return '???'

def split_op(opcode):
    "Divide opcode into base code and position/immediate mode flags"

    # 1. Can't do much if we don't have an opcode
    if opcode is None:
        return None, []

    # 2. Break out opcode from modes
    modes, opcode = divmod(opcode, 100)

    # 3. If invalid opcode, ignore the modes
    if opcode not in OP_CODES:
        return opcode, []

    # 4, Number of modes is based on the opcode length
    number = OP_LEN[opcode] - 1

    # 5. Pad the modes as necessary
    modes = "%0*d" % (number, modes)

    # 6, Unpack them into individual flags
    modes = [int(m) for m in list(modes)]

    # 7. Reverse the order
    modes.reverse()

    # 8, Return opcode and modes
    return opcode, modes


# ======================================================================
#                                                                IntComp
# ======================================================================


class IntCode():
    """Object representing a Intcode computer"""

    def __init__(self, # pylint: disable=R0913
                 counter=0, positions=None, text=None,
                 noun=None, verb=None, inp=None):

        # 1. Set the values
        self.counter = counter
        if positions is None:
            self.positions = []
        else:
            self.positions = positions
        if inp is None:
            self.inp = []
        else:
            self.inp = inp
        self.out = []

        # 2. If we have text, set the positions with it
        if text is not None:
            self.positions = [int(x) for x in text.split(',')]

        # 3. Set noun and verb if any values were given
        if noun is not None:
            self.positions[ADDR_NOUN] = noun
        if verb is not None:
            self.positions[ADDR_VERB] = verb

    def fetch(self, which):
        "Retrieve the value at a position, return None if which bad"

        # 1. Check which
        if which < 0 or which >= len(self.positions):
            return None

        # 2. Return the value
        return self.positions[which]

    def alter(self, which, what):
        "Set the value at a position, return None if which bad"

        # 1. Fetch the current value
        current = self.fetch(which)

        # 2. Set the value if which is good
        if current is not None:
            self.positions[which] = what

        # 3. Return the previous value or None if error
        return current

    def inst(self, which=None):
        "Return instruction for humans"

        # Use the supplied value or the program counter
        if which is None:
            which = self.counter

        # 1. Get the opcode
        opcode = self.fetch(which)
        opname = op_name(opcode)

        # 2. Get the operands
        op1 = self.fetch(which+1)
        op2 = self.fetch(which+2)
        op3 = self.fetch(which+3)
        if op1 is None:
            op1 = 0
        if op2 is None:
            op2 = 0
        if op3 is None:
            op3 = 0

        # 3. Return the instruction
        return "%s %d %d %d" % (opname, op1, op2, op3)

    def instructions(self):
        "Output all the instructions"

        # 1. start at the beginning
        which = 0
        result = []

        # 2. Loop for all the instructions
        while False: # which < len(self.positions):

            # 3. Output the instruction here
            result.append('%05d: %s' % (which, self.inst(which=which)))

            # 4. Advance to the next instruction
            which += 4

        # 5. Return all the instructions
        return '\n'.join(result)


    def operands(self, modes, store):
        "Get the values of the operands"

        # 1. Assume all will be well
        result = STOP_RUN
        ops = []
        store -= 1

        # 3. Loop for the number of operands
        for num, mode in enumerate(modes):

            # 4. Get the op from the instruction
            operand = self.fetch(self.counter)

            # 5. If not immediate mode, fetch value
            if operand is not None:
                if mode == 0 and num != store:
                    operand = self.fetch(operand)

            # 6. Check that operand was fetched
            if operand is None:
                result = STOP_OPS
                operand = 0

            # 7. Add operand to the list
            ops.append(operand)

            # 8. Increment program counter
            self.counter += 1

        # 9. Return the result and operands
        return result, ops

    def step(self, watch=False): #pylint: disable=R0912
        "Execute on instruction"

        # 1. Retrieve the opcode
        oploc = self.counter
        if watch:
            print("%05d " % (oploc), end=' ')
        opcode = self.fetch(oploc)

        # 2. Increment program counter
        self.counter += 1

        # 3. Seperate modes from opcode
        opcode, modes = split_op(opcode)
        if opcode is None:
            if watch:
                print("<-> Invalid program counter: %d" % (oploc), end='')
            result = STOP_XPC

        # 4. If opcode is halt, we are done
        elif opcode == OP_HLT:
            if watch:
                print("HLT stopping at %d" % (oploc), end="")
            result = STOP_HLT

        # 5. if opcode is not good, return error
        elif opcode not in OP_CODES:
            if watch:
                print("??? Invalid opcode %d at %d" % (opcode, oploc), end='')
            result = STOP_BAD

        # 6. Retrieve the operands
        else:
            result, ops = self.operands(modes, OP_STORE[opcode])

            # 5. Give error if bad operands
            if result != STOP_RUN:
                if watch:
                    print("Invalid operands for opcode %d at %d" % (opcode, oploc), end='')

            # 6. Else execute the instruction
            result = self.execute(opcode, ops, watch)

        # 7. Finish the watch output (if any)
        if watch:
            print("")

        # 8. Say we are ready for more (or not)
        return result


    def execute(self, opcode, ops, watch):
        "Execute a single instructions now that we have everything we need"

        # 1. Execute add
        if opcode == OP_ADD:
            result = self.execute_add(ops, watch)

        # 2. Or multiply
        elif opcode == OP_MUL:
            result = self.execute_mult(ops, watch)

        # 3. Or input
        elif opcode == OP_INP:
            result = self.execute_input(ops, watch)

        # 4. Or output
        elif opcode == OP_OUT:
            result = self.execute_output(ops, watch)

        # 5. Or Jump if True (non-zero)
        elif opcode == OP_JIT:
            result = self.execute_jit(ops, watch)

        # 6. Or Jump if False (zero)
        elif opcode == OP_JIF:
            result = self.execute_jif(ops, watch)

        # 7. Or Store 1/0 if less than
        elif opcode == OP_SLT:
            result = self.execute_slt(ops, watch)

        # 8. Or Store 1/0 if equal
        elif opcode == OP_SEQ:
            result = self.execute_seq(ops, watch)

        # 9. Return the result (STOP_RUN or Error)
        return result

    def execute_add(self, ops, watch):
        "Execute a single add instruction"

        # 1. Assume all be well
        result = STOP_RUN

        # 2. Conpute the value
        value = ops[0] + ops[1]

        # 3. Describe the operation
        if watch:
            print("ADD %d + %d is %d storing at %d" %
                  (ops[0], ops[1], value, ops[2]), end=' ')


        # 4. Store the computed value
        if self.alter(ops[2], value) is None:
            result = STOP_STR
            if watch:
                print("Bad store", end=' ')

        # 4. Return the result (STOP_RUN or Error)
        return result

    def execute_mult(self, ops, watch):
        "Execute a single multiply instruction"

        # 1. Assume all be well
        result = STOP_RUN

        # 2. Conpute the value
        value = ops[0] * ops[1]

        # 3. Describe the operation
        if watch:
            print("MUL %d * %d is %d storing at %d" %
                  (ops[0], ops[1], value, ops[2]), end=' ')

        # 4. Store the computed value
        if self.alter(ops[2], value) is None:
            result = STOP_STR
            if watch:
                print("Bad store", end=' ')

        # 4. Return the result (STOP_RUN or Error)
        return result

    def execute_input(self, ops, watch):
        "Execute a single input instruction"

        # 1. Assume all be well
        result = STOP_RUN

        # 2. Get the input value
        if len(self.inp) > 0:
            value = self.inp.pop(0)
        else:
            value = 0

        # 3. Describe the operation
        if watch:
            print("INP %d storing at %d" %
                  (value, ops[0]), end=' ')

        # 4. Store the input value
        if self.alter(ops[0], value) is None:
            result = STOP_STR
            if watch:
                print("Bad store", end=' ')

        # 4. Return the result (STOP_RUN or Error)
        return result

    def execute_output(self, ops, watch):
        "Execute a single output instruction"

        # 1. Assume all be well
        result = STOP_RUN

        # 2. Get the input value
        value = ops[0]
        self.out.append(value)

        # 3. Describe the operation
        if watch:
            print("OUT Outputing %d" % (value), end=' ')

        # 4. Return the result (STOP_RUN or Error)
        return result

    def execute_jit(self, ops, watch):
        "Execute a single jump if non-zero 0 instruction"

        # 1. Assume all be well
        result = STOP_RUN

        # 2. Conpute the value
        value = ops[0] != 0

        # 3. Describe the operation
        if watch:
            if value:
                print("JIT %d is non-zero, jumping to %d" %
                      (ops[0], ops[1]), end=' ')
            else:
                print("JIT %d is zero, not jumping to %d" %
                      (ops[0], ops[1]), end=' ')

        # 4. Jump (of not)
        if value:
            self.counter = ops[1]

        # 5. Return the result (STOP_RUN or Error)
        return result

    def execute_jif(self, ops, watch):
        "Execute a single add instruction"

        # 1. Assume all be well
        result = STOP_RUN

        # 2. Conpute the value
        value = ops[0] == 0

        # 3. Describe the operation
        if watch:
            if value:
                print("JIF %d is zero, jumping to %d" %
                      (ops[0], ops[1]), end=' ')
            else:
                print("JIF %d is not zero, not jumping to %d" %
                      (ops[0], ops[1]), end=' ')

        # 4. Jump (of not)
        if value:
            self.counter = ops[1]

        # 5. Return the result (STOP_RUN or Error)
        return result

    def execute_slt(self, ops, watch):
        "Execute a store 1/0 if less than instruction"

        # 1. Assume all be well
        result = STOP_RUN

        # 2. Conpute the value
        if ops[0] < ops[1]:
            value = 1
        else:
            value = 0

        # 3. Describe the operation
        if watch:
            print("SLT %d ?< %d storing %d at %d" %
                  (ops[0], ops[1], value, ops[2]), end=' ')

        # 4. Store the computed value
        if self.alter(ops[2], value) is None:
            result = STOP_STR
            if watch:
                print("Bad store", end=' ')

        # 5. Return the result (STOP_RUN or Error)
        return result

    def execute_seq(self, ops, watch):
        "Execute a store 1/0 if equal instruction"

        # 1. Assume all be well
        result = STOP_RUN

        # 2. Conpute the value
        if ops[0] == ops[1]:
            value = 1
        else:
            value = 0

        # 3. Describe the operation
        if watch:
            print("SEQ %d ?= %d storing %d at %d" %
                  (ops[0], ops[1], value, ops[2]), end=' ')

        # 4. Store the computed value
        if self.alter(ops[2], value) is None:
            result = STOP_STR
            if watch:
                print("Bad store", end=' ')

        # 5. Return the result (STOP_RUN or Error)
        return result

    def reset(self):
        "Reset the program counter to zero"

        self.counter = 0
        self.inp = []
        self.out = []

    def outputs(self):
        "Get the accumulated output and clear it"

        result = self.out
        self.out = []
        return result

    def run(self, max_steps=0, start=None, inp=None, watch=False):
        "Run the computer"

        # 1. Initialize
        result = STOP_RUN
        steps = 0
        if start is not None:
            self.counter = start
        if inp is not None:
            self.inp = inp

        # 2. Run intil not runnable or too many steps
        while result == STOP_RUN:

            # 3. Run a single step
            result = self.step(watch=watch)

            # 4. Increment the step count and check limit
            steps += 1
            if result == STOP_RUN and max_steps > 0:
                if steps >= max_steps:
                    result = STOP_STP

        # 5. Return the reason for stopping
        return result

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                     i n t c o m p  . p y                       end
# ======================================================================
