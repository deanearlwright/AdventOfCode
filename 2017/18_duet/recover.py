# ======================================================================
# duet
#   Advent of Code 2017 Day 18 -- Eric Wastl -- https://adventofcode.com
#
# Computer implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         r e c o v e r . p y
# ======================================================================
"A solver for recover for Advent of Code 2017 Day 18"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
from itertools import repeat

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
INSTS = frozenset(['snd', 'set', 'add', 'mul', 'mod', 'rcv', 'jgz'])
REGS = frozenset(list('abcdefghijklmnopqrstuvwxyz'))
OTHER = [1, 0]

# ======================================================================
#                                                                Recover
# ======================================================================


class Recover(object):   # pylint: disable=R0902, R0205
    "Object for duet"

    def __init__(self, steps=None, text=None, part2=False, proc=0):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.instructions = []
        self.position = [0, 0]
        self.sound = None
        self.recovered = None
        self.registers = [dict(zip(REGS, repeat(0, 26))), dict(zip(REGS, repeat(0, 26)))]
        self.proc = proc
        self.queues = [[], []]
        self.terminated = [False, False]
        self.waiting = [False, False]
        self.send_knt = [0, 0]

        # 2. Process text (if any)
        if text is not None:
            self.text_to_instructions()

        # 3. part2 has two processors
        if part2:
            self.registers[1]['p'] = 1

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
        return self.registers[self.proc][reg]

    def set_register(self, reg, value):
        "Set register value"

        assert reg in REGS
        self.registers[self.proc][reg] = value

    def get_value(self, reg_or_int):
        "Get register value"

        if reg_or_int in REGS:
            return self.get_register(reg_or_int)
        return reg_or_int

    def step(self, verbose=False):
        "Execute one instruction step"

        # 1. Verify the instruction counter
        pc = self.position[self.proc]
        if pc < 0 or pc >= len(self.instructions):
            if verbose:
                print("[%d] Invalid instuction position %d" %
                      (self.proc, pc))
            self.terminated[self.proc] = True
            return False

        # 2. Assume no branch
        next_position = pc + 1

        # 3. Get the instruction and operands
        inst, op1, op2 = self.instructions[pc]
        if verbose:
            print("[%d] %d: %s %s %s" %
                  (self.proc, pc, inst, op1, op2))

        # 4. Execute the instruction
        # 4a. snd X plays a sound with a frequency equal to the value of X.
        if inst == 'snd':
            if not self.part2:
                self.sound = self.get_value(op1)
                if verbose:
                    print("[%d]  Sound %d" %
                         (self.proc, self.sound))

            # 4a2. snd X sends the value of X to the other program. These values wait in
            #            a queue until that program is ready to receive them. Each program has
            #            its own message queue, so a program can never receive a message it
            #            sent.
            else:
                value = self.get_value(op1)
                self.queues[OTHER[self.proc]].append(value)
                self.waiting[OTHER[self.proc]] = False
                self.send_knt[self.proc] += 1
                if verbose:
                    print("[%d]  Sending %d, knt= %d" %
                         (self.proc, value, self.send_knt[self.proc]))

        # 4b. set X Y sets register X to the value of Y.
        elif inst == 'set':
            self.set_register(op1, self.get_value(op2))

        # 4c. add X Y increases register X by the value of Y.
        elif inst == 'add':
            self.set_register(op1, self.get_value(op1) + self.get_value(op2))
        # 4d. mul X Y sets register X to the result of multiplying the value
        #     contained in register X by the value of Y.
        elif inst == 'mul':
            self.set_register(op1, self.get_value(op1) * self.get_value(op2))

        # 4e. mod X Y sets register X to the remainder of dividing the value
        #     contained in register X by the value of Y (that is, it sets X to the
        #     result of X modulo Y).
        elif inst == 'mod':
            self.set_register(op1, self.get_value(op1) % self.get_value(op2))

        # 4f. rcv X recovers the frequency of the last sound played, but only when
        #     the value of X is not zero. (If it is zero, the command does nothing.)
        elif inst == 'rcv':
            if not self.part2:
                if self.get_value(op1) != 0:
                    self.recovered = self.sound
                    if verbose:
                        print("[%d]  Recovered sound %d" %
                              (self.proc, self.recovered))

            # 4f2. rcv X receives the next value and stores it in register X. If no
            #      values are in the queue, the program waits for a value to be sent to
            #      it. Programs do not continue to the next instruction until they have
            #      received a value. Values are received in the order they are sent.
            else:
                if self.queues[self.proc]:
                    self.set_register(op1, self.queues[self.proc].pop(0))
                    if verbose:
                        print("[%d]  Received %d" %
                              (self.proc, self.get_register(op1)))
                else:
                    next_position = pc
                    self.waiting[self.proc] = True
                    if verbose:
                        print("[%d]  Waiting" % (self.proc))

        # 4g. jgz X Y jumps with an offset of the value of Y, but only if the value
        #     of X is greater than zero. (An offset of 2 skips the next instruction,
        #     an offset of -1 jumps to the previous instruction, and so on.)
        elif inst == 'jgz':
            if self.get_value(op1) > 0:
                next_position = pc + self.get_value(op2)

        # 5. Set next instruction position
        self.position[self.proc] = next_position

        # 6. Return True
        return True

    def run(self, verbose=False, limit=0):
        "Run instructions"

        if not self.part2:
            self.part_one_run(verbose=verbose, limit=limit)
        else:
            self.part_two_run(verbose=verbose, limit=limit)

    def part_one_run(self, verbose=False, limit=0):
        "Run instructions until illegal position or recovered sound"

        # 1. Start count at zero
        knt_steps = 0

        # 2. Loop forever
        while True:

            # 3. Execute an instruction, stop if bad position
            if not self.step(verbose=verbose):
                break
            knt_steps += 1

            # 4. Stop if recovered a sound
            if self.recovered:
                break

            # 5. Stop if running too long
            if knt_steps > limit > 0:
                print("Reached execution limit")
                break

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 1. Run the instructions
        self.run(verbose=verbose, limit=limit)

        # 1. Return the solution for part one
        return self.recovered


    def part_two_run(self, verbose=False, limit=0):
        "Run instructions until illegal position or recovered sound"

        # 1. Start count at zero
        knt_steps = 0

        # 2. Loop forever
        while True:

            # 3. Loop for for the processors
            for proc in range(2):

                # 4. Ignore terminated processors
                if self.terminated[proc]:
                    continue

                # 5. Ignore if this processor still waiting
                if self.waiting[proc]:
                    continue

                # 6. Execute an instruction
                self.proc = proc
                self.step(verbose=verbose)

            # 7. Check for deadlock
            if self.waiting[0] and self.waiting[1]:
                if verbose:
                    print("Both processes deadlocked")
                break

            # 8. Check for both terminated
            if self.terminated[1] and self.terminated[1]:
                if verbose:
                    print("Both processes terminated")
                break

            # 9. Check if running too long
            if knt_steps > limit > 0:
                print("Reached execution limit")
                break

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 1. Run both processors
        self.run(verbose=verbose, limit=limit)

        # 2. Return the number of processor 1 sends
        return self.send_knt[1]

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                       r e c o v e r . p y                      end
# ======================================================================
