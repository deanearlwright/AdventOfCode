
# ======================================================================
# Chronospatial Computer
#   Advent of Code 2024 Day 17 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         c o m p u t e r . p y
# ======================================================================
"A solver for the Advent of Code 2024 Day 17 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
A_REG = 0
B_REG = 1
C_REG = 2
BAD7 = "Combo operand 7 is reserved and will not appear in valid programs"

# ======================================================================
#                                                               Computer
# ======================================================================


class Computer(object):   # pylint: disable=R0902, R0205
    "Object for Chronospatial Computer"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.registers = [0, 0, 0]
        self.instructions = []
        self.pointer = 0
        self.output = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text()

    def _process_text(self):
        "Assign values from text"

        assert self.text is not None and len(self.text) > 0

        # 1. Loop for each line of the input text
        for line in self.text:

            # 2. Split the line into label and values
            label, values = line.split(":")

            # 3. Process the different types of labels
            match label:
                case "Register A":
                    self.registers[0] = int(values)
                case "Register B":
                    self.registers[1] = int(values)
                case "Register C":
                    self.registers[2] = int(values)
                case "Program":
                    self.instructions = [int(x) for x in values.split(",")]
                case _:
                    print(f"Unexpected '{line}'")

    def combo(self, operand):
        "Return the value for a 'combo' operand"

        # 1. Get the operand value
        match operand:
            case 0 | 1 | 2 | 3:
                return operand  # Literal
            case 4 | 5 | 6:
                return self.registers[operand - 4]  # register
            case 7:
                print(BAD7)
            case _:
                print(f"Non octal operand {operand}")

        # 2. Something went wrong
        return 0

    def step(self):
        "Run a single step of the computer, return True if it should stop"

        # 1. Fetch the opcode and the operand
        if self.pointer < 0 or self.pointer >= len(self.instructions):
            return True
        opcode = self.instructions[self.pointer]
        operand = self.instructions[self.pointer + 1]
        self.pointer += 2

        # 2. Execute the instruction
        match opcode:
            case 0:  # adv
                cop2 = pow(2, self.combo(operand))
                self.registers[A_REG] = self.registers[A_REG] // cop2
            case 1:  # bxl
                self.registers[B_REG] = self.registers[B_REG] ^ operand
            case 2:  # bst
                self.registers[B_REG] = self.combo(operand) % 8
            case 3:  # jnz
                if self.registers[A_REG] != 0:
                    self.pointer = operand
            case 4:  # bxc
                # print("bxc", self.registers[B_REG], self.registers[C_REG])
                regc = self.registers[C_REG]
                self.registers[B_REG] = self.registers[B_REG] ^ regc
            case 5:  # out
                value = self.combo(operand) % 8
                # print(f"Outputing {value}")
                self.output.append(value)
            case 6:  # bdv
                cop2 = pow(2, self.combo(operand))
                self.registers[B_REG] = self.registers[A_REG] // cop2
            case 7:  # cdv
                cop2 = pow(2, self.combo(operand))
                self.registers[C_REG] = self.registers[A_REG] // cop2

        # 3. Return inidication that the program should continue
        return False

    def run(self, limit=None):
        "Run the program until it stops"

        # 1. Run the program until it stops
        stop = False
        while not stop:
            stop = self.step()
            if limit is not None and len(self.output) > limit:
                stop = True

    def find_copy(self):
        """Find the lowest initial value for register A
           that outputs a copy of the program
           --- way to slow ---
        """

        # 1. Loop for a long time
        for a in range(117000, 118000):

            # 2. Reset the computer
            self.registers = [a, 0, 0]
            self.pointer = 0
            self.output = []

            # 3. Run the computer
            self.run(limit=len(self.instructions))

            # 4. Did it output the instructions
            if self.output == self.instructions:
                return a

        # 6. At least we tried
        return None

    def work_backwards(self):
        """Work backwards to find the value for register A

        00: 2 4 bst b <- A % 8 ! lower 3 bits of A only
        02: 1 3 bxl b <- a ^ 3 ! invert lower 2 bits of A
        04: 7 5 cdv c <- a // pow(2,B)
        06: 0 3 adv a <- a // 8 ! left shift a 3 bits
        10: 1 4 bxl b <- b ^ 4 ! inverts the 3 bit of B
        12: 4 7 bxc b <- b ^ c
        14: 5 5 out output <- b
        16: 3 0 jnz if a !=0, goto 0

        Output depends only only on a with b and c uses as work regs
        Things progress three bits at a time
        """

        # 1. Lets take this octal by octal with no assumptions for the first
        octals = [[0, 1, 2, 3, 4, 5, 6, 7]]

        # 2. Let's take it a instruction at a time
        inst_len = len(self.instructions)
        for indx in range(1, inst_len):

            # 3. Don't know what this will be yet
            octals.append([])

            # 4. Try based on what we have learned (or quessed) so far
            for prev_octal in octals[indx - 1]:

                # 5. It must be 0, 1, 2, 3, 4, 5, 6, or 7
                for octal in range(8):

                    # 6. Calculate the value for the A register
                    reg_a = 8 * prev_octal + octal

                    # 7. Try it out
                    self.registers = [reg_a, 0, 0]
                    self.pointer = 0
                    self.output = []
                    self.run()

                    # 8. Did this much work?
                    check_len = inst_len - len(self.output)
                    if self.output == self.instructions[check_len:]:
                        octals[indx].append(reg_a)

                    # 9. Is it the total solution?
                    if self.output == self.instructions:
                        return reg_a

        # 10. At least we tried
        return None

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. No solution if no text
        if self.text is None:
            return None

        # 2. Return the solution for part one
        self.run()
        return ",".join(str(x) for x in self.output)

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. No solution if no text
        if self.text is None:
            return None

        # 2. Return the solution for part two
        return self.work_backwards()

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                      c o m p u t e r . p y                     end
# ======================================================================
