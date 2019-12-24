# ======================================================================
#  Category Six
#   Advent of Code 2019 Day 23 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                           a o c _ c s . p y
# ======================================================================
"Solve the Category Six problem for Advent of Code 2019 day 23"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import argparse
import sys

import network
import intcode

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
PART1_NUMBER = 255

# ----------------------------------------------------------------------
#                                                      parse_commnd_line
# ----------------------------------------------------------------------


def parse_command_line():
    "Parse the command line options"

    # 1. Create the command line parser
    desc = 'Category Six - day 23 of Advent of Code 2019'
    sample = 'sample: python aoc_cs.py input.txt'
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

    # 1. Create the network
    nwork = network.Network(text=input_lines[0])

    # 2. Boot them up
    halted = nwork.boot_up(watch=args.verbose)
    if halted != intcode.STOP_INP:
        print("The network failed to start up, reason = %d" % (halted))
        solution = None
    else:
        halted = nwork.run_until_msg_to(PART1_NUMBER,
                                        watch=args.verbose,
                                        maxtime=args.maxtime)
        if halted != intcode.STOP_INP:
            print("The network failed to output to %d, reason = %d" %
                  (PART1_NUMBER, halted))
            solution = None
        else:
            solution = nwork.get_first_msg_to(PART1_NUMBER)
            if solution is None:
                print("No message have been sent to address %d" % (PART1_NUMBER))
            else:
                print("The message sent to address %d was %s" %
                      (PART1_NUMBER, solution))

    # 3. Return result
    return solution is not None

# ----------------------------------------------------------------------
#                                                               part_two
# ----------------------------------------------------------------------


def part_two(args, input_lines):
    "Process part two of the puzzle"

    # 1. Create the network
    nwork = network.Network(text=input_lines[0])

    # 2. Boot them up
    halted = nwork.boot_up(watch=args.verbose)
    if halted != intcode.STOP_INP:
        print("The network failed to start up, reason = %d" % (halted))
        solution = None
    else:
        halted = nwork.run_until_nat_repeat(watch=args.verbose,
                                            maxtime=args.maxtime)
        if halted != intcode.STOP_INP:
            print("The network failed to output to %d, reason = %d" %
                  (PART1_NUMBER, halted))
            solution = None
        else:
            solution = nwork.get_last_nat_msg()
            if solution is None:
                print("The NAT has sent no messages")
            else:
                print("The last message the NAT sent was %s" %
                      (solution))

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
    """Read the Category Six problem and solve it"""

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
# end                         a o c _ c s . p y                      end
# ======================================================================
