# ======================================================================
# Program Alarm
#   Advent of Code 2019 Day 02 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                           i n t c o m p  . p y
# ======================================================================
"Computer Row for Program Alarm problem for Advent of Code 2018 Day 02"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
STOP_HLT = 0   # Executed Halt (99) Opcode
STOP_OP1 = 1   # Bad operand 1
STOP_OP2 = 2   # Bad operand 2
STOP_OP3 = 3   # Bad Operand 3
STOP_BAD = 4   # Bad opcode
STOP_XPC = 5   # Bad Program Counter ( < 0 or > positions)
STOP_RUN = 6   # Single Step executed correctly
STOP_STP = 7   # Too many steps

OP_ADD = 1
OP_MUL = 2
OP_HLT = 99

OPCODES = set([OP_ADD, OP_MUL, OP_HLT])

ADDR_RSLT = 0
ADDR_NOUN = 1
ADDR_VERB = 2

# ======================================================================
#                                                                IntComp
# ======================================================================


class IntCode():
    """Object representing a Intcode computer"""

    def __init__(self, # pylint: disable=R0913
                 counter=0, positions=None, text=None,
                 noun=None, verb=None):

        # 1. Set the values
        self.counter = counter
        if positions is None:
            self.positions = []
        else:
            self.positions = positions

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
        if opcode is None:
            opcode = '<->'
        elif opcode == OP_ADD:
            opcode = "ADD"
        elif opcode == OP_MUL:
            opcode = "MUL"
        elif opcode == OP_HLT:
            opcode = "HLT"
        else:
            opcode = '???'

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
        return "%s %d %d %d" % (opcode, op1, op2, op3)

    def instructions(self):
        "Output all the instructions"

        # 1. start at the beginning
        which = 0
        result = []

        # 2. Loop for all the instructions
        while which < len(self.positions):

            # 3. Output the instruction here
            result.append('%05d: %s' % (which, self.inst(which=which)))

            # 4. Advance to the next instruction
            which += 4

        # 5. Return all the instructions
        return '\n'.join(result)


    def operands(self):
        "Get the values of the operands"

        # 1. Assume all will be well
        result = STOP_RUN

        # 2. Get op1, op2, and op3
        op1 = self.fetch(self.counter+1)
        op2 = self.fetch(self.counter+2)
        op3 = self.fetch(self.counter+3)

        # 3. Get the indirrect values for op1 and op2
        if op1 is not None:
            op1 = self.fetch(op1)
        if op2 is not None:
            op2 = self.fetch(op2)

        # 4. Check that all went well
        if op1 is None:
            result = STOP_OP1
        elif op2 is None:
            result = STOP_OP2
        elif op3 is None:
            result = STOP_OP3

        # 5. Return the result and operands
        return result, op1, op2, op3

    def step(self, watch=False): #pylint: disable=R0912
        "Execute on instruction"

        # 1. Retrieve the opcode
        if watch:
            print("%05d %s:" % (self.counter, self.inst()), end=' ')
        opcode = self.fetch(self.counter)
        if opcode is None:
            result = STOP_XPC
            if watch:
                print("Invalid program counter: %d" % (self.counter))

        # 2. If opcode is halt, we are done
        elif opcode == OP_HLT:
            if watch:
                print("Opcode at %d is Halt" % (self.counter))
            result = STOP_HLT

        # 3. if opcode is not good, return error
        elif opcode not in OPCODES:
            if watch:
                print("Invalid opcode %d at %d" % (opcode, self.counter))
            result = STOP_BAD

        # 4. Retrieve the operands
        else:
            result, op1, op2, op3 = self.operands()

            # 5. Compute the value of the operanion on op1 and op2
            if result == STOP_RUN:
                if watch:
                    print("(%d %d -> %d)" % (op1, op2, op3), end=' ')
                if opcode == OP_ADD:
                    value = op1 + op2
                else:
                    value = op1 * op2

                # 6. Store the result
                result = self.alter(op3, value)
                if result is None:
                    result = STOP_OP3
                    if watch:
                        print("Error storing at %d" % (op3))
                else:
                    result = STOP_RUN
                    if watch:
                        print("%d -> %d" % (value, op3))
            elif watch:
                print("Invalid operands")

        # 7. Advence the program counter
        self.counter += 4

        # 8. Say we are ready for more (or not)
        return result


    def reset(self):
        "Reset the program counter to zero"

        self.counter = 0

    def run(self, max_steps=0, watch=False):
        "Run the computer"

        # 1. Initialize
        result = STOP_RUN
        steps = 0

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
