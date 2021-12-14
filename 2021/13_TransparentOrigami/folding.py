# ======================================================================
# Transparent Origami
#   Advent of Code 2021 Day 13 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         f o l d i n g . p y
# ======================================================================
"A solver for the Advent of Code 2021 Day 13 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                                Folding
# ======================================================================


class Folding(object):   # pylint: disable=R0902, R0205
    "Object for Transparent Origami"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.dots = set()
        self.instructions = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:

            # 3. Loop for every line of the text
            for line in text:

                # 4. Add fold instructions
                if line.startswith('fold'):
                    fold_dir, fold_num = line.split(' ')[-1].split('=')
                    self.instructions.append((fold_dir, int(fold_num)))

                # 5. Or add dot
                else:
                    dot_col, dot_row = line.split(',')
                    self.dots.add((int(dot_col), int(dot_row)))

    def fold_up(self, line):
        "Execute a horizontal fold"

        # 1. Start a new set of dots
        folded = set()

        # 2. Loop for all the dots
        for dot in self.dots:
            dot_col, dot_row = dot

            # 3. If the dot is above the fold, it remains
            if dot_row < line:
                folded.add(dot)

            # 4. if the dot is on the line, something is wrong
            elif dot_row == line:
                print("dot %s is on the horizontal fold line", str(dot))

            # 5. Otherwize, fold the dot up
            else:
                new_row = dot_row - 2 * (dot_row - line)
                folded.add((dot_col, new_row))

        # 6. Set the new dots
        self.dots = folded

        # 7. Return the number of dots
        return len(folded)

    def fold_left(self, line):
        "Execute a vertical fold"

        # 1. Start a new set of dots
        folded = set()

        # 2. Loop for all the dots
        for dot in self.dots:
            dot_col, dot_row = dot

            # 3. If the dot is to the left of the fold, it remains
            if dot_col < line:
                folded.add(dot)

            # 4. if the dot is on the line, something is wrong
            elif dot_col == line:
                print("dot %s is on the vertical fold line", str(dot))

            # 5. Otherwize, fold the dot to the left
            else:
                new_col = dot_col - 2 * (dot_col - line)
                folded.add((new_col, dot_row))

        # 6. Set the new dots
        self.dots = folded

        # 7. Return the number of dots
        return len(folded)

    def fold(self, instruction):
        "Exececute a single fold"

        # 1. Get the instruction
        inst_way, inst_line = instruction

        # 2. Execute a fold up (way = y)
        if inst_way == 'y':
            return self.fold_up(inst_line)

        # 3. Or execute a fold left (way = x)
        if inst_way == 'x':
            return self.fold_left(inst_line)

        # 4. Unknown way
        print("Invalid folding instruction: %s,%d" % (inst_way, inst_line))
        return -1

    def fold_all(self):
        "Execute all the folds"

        # 1. Loop for all the instructions
        for inst in self.instructions:

            # 2. Execute it
            self.fold(inst)

        # 3. Print the resulting paper
        print(self)

        # 4. Return the number of dots
        return len(self.dots)

    def __str__(self):
        "Return the paper image"

        # 1. Start with nothing
        result = []
        max_col = 0
        max_row = 0

        # 2. Find the maximum row and col
        for dot in self.dots:
            if dot[0] > max_col:
                max_col = dot[0]
            if dot[1] > max_row:
                max_row = dot[1]

        # 3. Loop for all the rows
        for row in range(max_row + 1):
            dots = []

            # 4. Loop for all the columns
            for col in range(max_col + 1):

                # 5. Add a '.' or '#' to the row of dots
                if (col, row) in self.dots:
                    dots.append('#')
                else:
                    dots.append('.')

            # 6. Add the row of dots to the result
            result.append(''.join(dots))

        # 7. Return the complete image
        return '\n'.join(result)

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.fold(self.instructions[0])

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.fold_all()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                       f o l d i n g . p y                      end
# ======================================================================
