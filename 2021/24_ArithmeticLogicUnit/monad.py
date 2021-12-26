# ======================================================================
# Arithmetic Logic Unit
#   Advent of Code 2021 Day 24 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         m o n a d . p y
# ======================================================================
"A solver for the Advent of Code 2021 Day 24 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import alu

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
CONSTANTS = [4, 5, 15]
NUM_LOOP = 14
LEN_LOOP = 18
DIGITS = [1, 2, 3, 4, 5, 6, 7, 8, 9]
STIGID = [9, 8, 7, 6, 5, 4, 3, 2, 1]

# ======================================================================
#                                                                  Monad
# ======================================================================


class Monad(object):   # pylint: disable=R0902, R0205
    "Object for Arithmetic Logic Unit"

    def __init__(self, text=None, part2=False, inp=None):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.alu = None
        self.constants = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.alu = alu.Alu(text=text, part2=part2, inp=inp)
            for offset in CONSTANTS:
                constants = []
                for loop in range(NUM_LOOP):
                    index = loop * LEN_LOOP + offset
                    value = self.alu.inst[index][2]
                    constants.append(value)
                self.constants.append(constants)

    def block(self, which, digit, z_reg):
        "Execute a single digit block"

        # 1. Keep all previous digits or lose one
        z_1_26 = z_reg // self.constants[0][which]

        # 2. Do we match the adjusted last digit?
        if digit == z_reg % 26 + self.constants[1][which]:
            return z_1_26

        # 3. Else push the digit on the stack
        return 26 * z_1_26 + digit + self.constants[2][which]

    def run(self, digits):
        "Run the entire program block by block"

        # 1. Precondition axioms
        assert len(digits) == NUM_LOOP

        # 2. Start with nothing
        result = 0

        # 3. For for all the digits
        for index, digit in enumerate(digits):

            # 4. Execute the block
            result = self.block(index, int(digit), result)

        # 5. Return the final result
        return result

    def unblock(self, which, digit, z_reg):
        "Reverse a block of code to get possible previous z values"

        # 1. Start with nothing
        result = []

        # 2. Reconstruct the x register
        x_reg = z_reg - digit - self.constants[2][which]
        if x_reg % 26 == 0:
            result.append(x_reg // 26 * self.constants[0][which])

        # 3. Reconstruct the z register
        if 0 <= digit - self.constants[1][which] < 26:
            z_prev = z_reg * self.constants[0][which]
            result.append(digit - self.constants[1][which] + z_prev)

        # 4. Return the possible previous z values
        return result

    def unrun(self, digits=None):
        "Solve the puzzle by executing the blocks in reverse order"

        # 1. Have to start somewhere
        result = {}
        previous = set([0])

        # 2. Loop backwards through the blocks
        for which in range(13, -1, -1):

            # 3. Collect some z's [Sleep, I remember sleep]
            z_set = set()

            # 4. Loop for all of the digits and previous z's
            for digit in digits:

                # 5. Loop for all prevopus z's
                for z_reg in previous:

                    # 6. Undo this block with these inputs
                    z_possible = self.unblock(which, digit, z_reg)

                    # 7. Add all the possible z's to the set
                    for z_pos in z_possible:
                        z_set.add(z_pos)
                        if z_reg in result:
                            z_pos_digits = [digit]
                            z_pos_digits.extend(result[z_reg])
                            result[z_pos] = z_pos_digits
                        else:
                            result[z_pos] = [digit]

            # 8. Update previous
            previous = z_set

        # 9. Return the digits
        return ''.join([str(_) for _ in result[0]])

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.unrun(digits=DIGITS)

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.unrun(digits=STIGID)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                         m o n a d . p y                        end
# ======================================================================
