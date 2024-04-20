
# ======================================================================
# Trebuchet
#   Advent of Code 2023 Day 01 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         s o l v e r . p y
# ======================================================================
"A solver for the Advent of Code 2023 Day 01 puzzle"

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
LETTERS = "abcdefghijklmnopqrstuvwxyz"
NUMBERS = "123456789"
WORDS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

# ----------------------------------------------------------------------
#                                                                utility
# ----------------------------------------------------------------------


def get_starting_number(line):
    while line[0] in LETTERS:
        for k, v in WORDS.items():
            if line.startswith(k):
                return line.replace(k, v, 1)
        line = line[1:]
    return line


def get_ending_number(line):
    while line[-1] in LETTERS:
        for k, v in WORDS.items():
            if line.endswith(k):
                return line[:len(line) - len(k)] + v
        line = line[:-1]
    return line

# ======================================================================
#                                                                 Solver
# ======================================================================


class Solver(object):   # pylint: disable=R0902, R0205
    "Object for Trebuchet"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.lines = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        assert text is not None and len(text) > 0
        for line in self.text:
            if not line:
                continue

            if self.part2:
                line = get_starting_number(line)
                line = get_ending_number(line)
            else:
                for letter in "abcdefghijklmnopqrstuvwxyz":
                    line = line.replace(letter, '')
            print(line)
            self.lines.append(line)

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        if self.lines:
            return sum([int(x[0] + x[-1]) for x in self.lines])
        return None

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        if self.text:
            return sum([int(x[0] + x[-1]) for x in self.lines])
        return None

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                        s o l v e r . p y                       end
# ======================================================================
