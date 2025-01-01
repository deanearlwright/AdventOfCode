
# ======================================================================
# Bridge Repair
#   Advent of Code 2024 Day 07 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                           a o c _ 0 7 . p y
# ======================================================================
"Solve the puzzles for Advent of Code 2024 day 07"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import argparse
import sys

import equations

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
KEEP_BLANK = False
IGNORE_COMMENTS = False
COMMENT = "!"

# ----------------------------------------------------------------------
#                                                     parse_command_line
# ----------------------------------------------------------------------


def parse_command_line():
    "Parse the command line options"

    # 1. Create the command line parser
    desc = 'Bridge Repair - Day 07 of Advent of Code 2024'
    sample = 'sample: python aoc_07.py input.txt'
    parser = argparse.ArgumentParser(description=desc,
                                     epilog=sample)
    parser.add_argument('-v', '--verbose', action='store_true',
                        default=False, dest='verbose',
                        help='Print status messages to stdout')
    parser.add_argument('-p', '--part', action='store', default=1, type=int,
                        dest='part', help='Puzzle Part (1 or 2)')
    parser.add_argument('-l', '--limit', action='store', default=0, type=int,
                        dest='limit',
                        help='Maximum (time, size, depth) before stopping')
    parser.add_argument('filepath', metavar='FILENAME',
                        action='store', type=str,
                        help="Location of puzzle input")

    # 2. Get the options and arguments
    return parser.parse_args()

# ----------------------------------------------------------------------
#                                                               part_one
# ----------------------------------------------------------------------


def part_one(args, input_lines):  # pylint: disable=E1128
    "Process part one of the puzzle"

    # 1. Create the puzzle solver
    my_solver = equations.Equations(part2=False, text=input_lines)

    # 2. Determine the solution for part one
    solution = my_solver.part_one(verbose=args.verbose, limit=args.limit)
    if solution is None:
        print("There is no solution")
    else:
        print(f"The solution for part one is {solution}")

    # 3. Return result
    return solution is not None

# ----------------------------------------------------------------------
#                                                               part_two
# ----------------------------------------------------------------------


def part_two(args, input_lines):  # pylint: disable=E1128
    "Process part two of the puzzle"

    # 1. Create the puzzle solver
    my_solver = equations.Equations(part2=True, text=input_lines)

    # 2. Determine the solution for part two
    solution = my_solver.part_two(verbose=args.verbose, limit=args.limit)
    if solution is None:
        print("There is no solution")
    else:
        print(f"The solution for part two is {solution}")

    # 3. Return result
    return solution is not None

# ----------------------------------------------------------------------
#                                                              from_file
# ----------------------------------------------------------------------


def from_file(filepath):
    "Read the file"

    return from_text(open(filepath, encoding="utf8").read())

# ----------------------------------------------------------------------
#                                                              from_text
# ----------------------------------------------------------------------


def from_text(text):
    "Break the text into trimed, non-comment lines"

    # 1. We start with no lines
    lines = []

    # 2. Loop for lines in the text
    for line in text.splitlines():

        # 3. But ignore blank and comment lines
        line = line.rstrip()
        if (not line) and (not KEEP_BLANK):
            continue
        if line.startswith(COMMENT) and IGNORE_COMMENTS:
            continue

        # 4. Add the line
        lines.append(line)

    # 5. Return a list of clean lines
    return lines

# ----------------------------------------------------------------------
#                                                                   main
# ----------------------------------------------------------------------


def main():
    "Read the Advent of Code problem and solve it"

    # 1. Get the command line options
    args = parse_command_line()

    # 2. Read the puzzle file
    input_text = from_file(args.filepath)

    # 3. Process the appropiate part of the puzzle
    if args.part == 1:
        result = part_one(args, input_text)
    else:
        result = part_two(args, input_text)

    # 5. Set return code (0 if solution found, 2 if not)
    if result:
        sys.exit(0)
    sys.exit(2)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    main()

# ======================================================================
# end                         a o c _ 0 7 . p y                      end
# ======================================================================
