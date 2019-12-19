# ======================================================================
#  Set and Forget
#   Advent of Code 2019 Day 17 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                           a o c _ s f . p y
# ======================================================================
"Solve the Set and Forget problem for Advent of Code 2019 day 17"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import argparse
import sys

import aii
import intcode

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
PROG = [
    65, 44, 66, 44, 65, 44, 67, 44, 66, 44, 67, 44, 65, 44, 66, 44, 65, 44, 67, 10,
    82, 44, 54, 44, 76, 44, 49, 48, 44, 82, 44, 56, 44, 82, 44, 56, 10,
    82, 44, 49, 50, 44, 76, 44, 56, 44, 76, 44, 49, 48, 10,
    82, 44, 49, 50, 44, 76, 44, 49, 48, 44, 82, 44, 54, 44, 76, 44, 49, 48, 10,
    ord('n'), 10
]

# ----------------------------------------------------------------------
#                                                      parse_commnd_line
# ----------------------------------------------------------------------


def parse_command_line():
    "Parse the command line options"

    # 1. Create the command line parser
    desc = 'Set and Forget - day 17 of Advent of Code 2019'
    sample = 'sample: python aoc_sf.py input.txt'
    parser = argparse.ArgumentParser(description=desc,
                                     epilog=sample)
    parser.add_argument('-v', '--verbose', action='store_true', default=False,
                        dest='verbose', help='Print status messages to stdout')
    parser.add_argument('-p', '--part', action='store', default=1, type=int,
                        dest='part', help='Puzzle Part (1 or 2)')
    parser.add_argument('-t', '--max-time', action='store', default=0, type=int,
                        dest='maxtime', help='Maximum timer ticks before quitting')
    parser.add_argument('filepath', metavar='FILENAME', action='store', type=str,
                        help="Location of puzzle input")

    # 2. Get the options and arguments
    return parser.parse_args()

# ----------------------------------------------------------------------
#                                                               part_one
# ----------------------------------------------------------------------

def part_one(args, input_lines):
    "Process part one of the puzzle"

    # 1. Create the droid
    mapper = aii.AII(text=input_lines[0])

    # 2. Get the map
    halted = mapper.get_map(watch=args.verbose)
    if halted != intcode.STOP_HLT:
        print("The ASCII computer stopped unexpectively, reason = %d" % (halted))
        solution = None
    else:
        solution = str(mapper)
        print("The ASCII computer produced a map")
        print(solution)

    # 3. Return result
    return solution is not None

# ----------------------------------------------------------------------
#                                                               part_two
# ----------------------------------------------------------------------


def part_two(args, input_lines):
    "Process part two of the puzzle"

    # 1. Create the droid
    duster = aii.AII(text=input_lines[0])

    # 2. Get the dust
    halted = duster.get_dust(watch=args.verbose, movement=PROG)
    if halted != intcode.STOP_HLT:
        print("The vacuum stopped unexpectively, reason = %d, dust = %d" % (halted, duster.dust))
        solution = None
    else:
        solution = duster.dust
        print("The vacumm collected %s dust" % (solution))
        print(solution)

    # 3. Return result
    return solution is not None

# ----------------------------------------------------------------------
#                                                              from_file
# ----------------------------------------------------------------------


def from_file(filepath):
    "Read the file"

    return from_text(open(filepath).read())

# ----------------------------------------------------------------------
#                                                              from_text
# ----------------------------------------------------------------------


def from_text(text):
    "Break the text into trimed, non-comment lines"

    # 1. We start with no lines
    lines = []

    # 2. Loop for lines in the text
    for line in text.split('\n'):

        # 3. But ignore blank and non-claim lines
        line = line.rstrip(' \r')
        if not line:
            continue
        if line.startswith('#'):
            continue

        # 4. Add the line
        lines.append(line)

    # 5. Return a list of clean lines
    return lines

# ----------------------------------------------------------------------
#                                                                   main
# ----------------------------------------------------------------------


def main():
    """Read the Set and Forget problem and solve it"""

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
# end                         a o c _ s f . p y                      end
# ======================================================================
