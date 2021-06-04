# ======================================================================
# Two-Factor Authentication
#   Advent of Code 2016 Day 08 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         d i s p l a y . p y
# ======================================================================
"A solver for the Advent of Code 2016 Day 08 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
POFF = '.'
PON = '#'

# ======================================================================
#                                                                Display
# ======================================================================


class Display(object):   # pylint: disable=R0902, R0205
    "Object for Two-Factor Authentication"

    def __init__(self, text=None, part2=False, wide=50, tall=6):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.wide = wide
        self.tall = tall
        self.pixels = [[POFF for _ in range(self.wide)] for _ in range(self.tall)]
        self.inst = 0

    def __str__(self):
        return '\n'.join([''.join(self.pixels[row]) for row in range(self.tall)])

    def lit(self):
        "Return the number of lit pixels"
        result = 0
        for row in range(self.tall):
            for col in range(self.wide):
                if self.pixels[row][col] == PON:
                    result += 1
        return result

    def one_inst(self):
        "Execute a single instruction, return while there are more to do"

        # 1. Check the instruction counter
        if self.inst >= len(self.text):
            return False

        # 2. Get the instruction to execute
        inst = self.text[self.inst].split(' ')

        # 3. Execute the instruction
        if inst[0] == 'rect':
            self.inst_rect(inst)
        elif inst[0] == 'rotate':
            if inst[1] == 'column':
                self.inst_col(inst)
            else:
                self.inst_row(inst)
        else:
            print('Unknown instruction:', inst[0])
            return False

        # 4. Get set for next instruction
        self.inst += 1
        return True

    def inst_rect(self, inst):
        "Execute a rect AxB instruction"

        # 1. Decode the size of the rectangle
        size = [int(_) for _ in inst[1].split('x')]

        # 2. Loop for the number of rows and cols
        for row in range(size[1]):
            for col in range(size[0]):

                # 3. Turn on a pixel
                self.pixels[row][col] = PON

    def inst_col(self, inst):
        "Rotate a column downward"

        # 1. Decode the instructions
        col = int(inst[2].split('=')[1])
        num = int(inst[4])

        # 2. Loop for the number of downward rotations
        for _ in range(num):

            # 3. Save the bottom row
            bottom = self.pixels[self.tall - 1][col]

            # 4. Rotate the column downward
            for row in range(self.tall - 1, 0, -1):
                self.pixels[row][col] = self.pixels[row - 1][col]

            # 5. The bottom is now the top
            self.pixels[0][col] = bottom

    def inst_row(self, inst):
        "Rotate a row to the right"

        # 1. Decode the instructions
        row = int(inst[2].split('=')[1])
        num = int(inst[4])

        # 2. Loop for the number of rightward rotations
        for _ in range(num):

            # 3. Save the right most column
            right = self.pixels[row][self.wide - 1]

            # 4. Rotate the row to the right
            for col in range(self.wide - 1, 0, -1):
                self.pixels[row][col] = self.pixels[row][col - 1]

            # 5. The left is now the right
            self.pixels[row][0] = right

    def all_inst(self):
        "Execute all of the instructions"

        while self.one_inst():
            pass

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        self.all_inst()
        return self.lit()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        self.all_inst()
        return str(self)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                       d i s p l a y . p y                      end
# ======================================================================
