# ======================================================================
#  Springdroid Adventure
#   Advent of Code 2019 Day 21 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                           a o c _ s a . p y
# ======================================================================
"Solve the Springdroid Adventure problem for Advent of Code 2019 day 21"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import argparse
import sys

import droid
import intcode

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
WALK = [ord('W'), ord('A'), ord('L'), ord('K'), 10]
RUN = [ord('R'), ord('U'), ord('N'), 10]

PROG1 = [  # If we can't walk one space, we jump: #####.#..######## WWWWJ
    ord('N'), ord('O'), ord('T'), ord(' '), ord('A'), ord(' '), ord('J'), 10,
]
PROG2 = [  # If we can't jump, we walk: #####.#..######## JW sb WWJJW...
    ord('N'), ord('O'), ord('T'), ord(' '), ord('J'), ord(' '), ord('J'), 10,
    ord('A'), ord('N'), ord('D'), ord(' '), ord('D'), ord(' '), ord('J'), 10,
]
PROG3 = [  # If can jump (D) and we must (~A) or we should (~C): 19348359!
    ord('N'), ord('O'), ord('T'), ord(' '), ord('A'), ord(' '), ord('J'), 10,
    ord('N'), ord('O'), ord('T'), ord(' '), ord('C'), ord(' '), ord('T'), 10,
    ord('O'), ord('R'), ord(' '), ord('T'), ord(' '), ord('J'), 10,
    ord('A'), ord('N'), ord('D'), ord(' '), ord('D'), ord(' '), ord('J'), 10,
]  # But in part two: #####.#.##...####: WWJW Should be WWWJWJW...

# ------ Part 2

PROG4 = [  # Like part 1 but with added E and H sensors
    ord('N'), ord('O'), ord('T'), ord(' '), ord('A'), ord(' '), ord('T'), 10,
    ord('N'), ord('O'), ord('T'), ord(' '), ord('T'), ord(' '), ord('T'), 10,
    ord('A'), ord('N'), ord('D'), ord(' '), ord('B'), ord(' '), ord('T'), 10,
    ord('A'), ord('N'), ord('D'), ord(' '), ord('C'), ord(' '), ord('T'), 10,
    ord('N'), ord('O'), ord('T'), ord(' '), ord('T'), ord(' '), ord('J'), 10,
    ord('A'), ord('N'), ord('D'), ord(' '), ord('D'), ord(' '), ord('J'), 10,
    ord('N'), ord('O'), ord('T'), ord(' '), ord('E'), ord(' '), ord('T'), 10,
    ord('N'), ord('O'), ord('T'), ord(' '), ord('T'), ord(' '), ord('T'), 10,
    ord('O'), ord('R'), ord(' '), ord('H'), ord(' '), ord('T'), 10,
    ord('A'), ord('N'), ord('D'), ord(' '), ord('T'), ord(' '), ord('J'), 10,
]

# ----------------------------------------------------------------------
#                                                      parse_commnd_line
# ----------------------------------------------------------------------


def parse_command_line():
    "Parse the command line options"

    # 1. Create the command line parser
    desc = 'Springdroid Adventure - day 21 of Advent of Code 2019'
    sample = 'sample: python aoc_sa.py input.txt'
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
    duey = droid.Droid(text=input_lines[0])

    # 2. Get the damage
    halted = duey.get_damage(prog=PROG3 + WALK, watch=args.verbose)
    if halted != intcode.STOP_HLT:
        print("The springdroid, duey, stopped unexpectively, reason = %d" % (halted))
        solution = None
    else:
        solution = duey.damage
        if solution is None:
            print("The Droid's last moments\n%s\n" % (str(duey)))
        else:
            print("The amount is hull damage is %d" % (solution))

    # 3. Return result
    return solution is not None

# ----------------------------------------------------------------------
#                                                               part_two
# ----------------------------------------------------------------------


def part_two(args, input_lines):
    "Process part two of the puzzle"

    # 1. Create the droid
    duey = droid.Droid(text=input_lines[0])

    # 2. Get the damage
    halted = duey.get_damage(prog=PROG4 + RUN, watch=args.verbose)
    if halted != intcode.STOP_HLT:
        print("The springdroid, duey, stopped unexpectively, reason = %d" % (halted))
        solution = None
    else:
        solution = duey.damage
        if solution is None:
            print("The Droid's last moments\n%s\n" % (str(duey)))
        else:
            print("The amount is hull damage is %d" % (solution))

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
    """Read the Springdroid Adventure problem and solve it"""

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
# end                         a o c _ s a . p y                      end
# ======================================================================
