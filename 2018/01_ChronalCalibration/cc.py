
# ======================================================================
# Chronal Calibration
#   Advent of Code 2018 Day 01 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                                c c . p y
# ======================================================================
"Solve the Chronal Calibration problem of day 01 of Advent of Code 2018"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import argparse
import sys

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                      parse_commnd_line
# ----------------------------------------------------------------------


def parse_command_line():
    "Parse the command line options"

    # 1. Create the command line parser
    desc = 'Chronal Calibration - day 01 of Advent of Code 2018'
    sample = 'sample: python mcm.py input.txt'
    parser = argparse.ArgumentParser(description=desc,
                                     epilog=sample)
    parser.add_argument('-v', '--verbose', action='store_true', default=False,
                        dest='verbose', help='Print status messages to stdout')
    parser.add_argument('-p', '--part', action='store', default=1, type=int,
                        dest='part', help='Puzzle Part (1 or 2)')
    parser.add_argument('-t', '--max-time', action='store', default=0, type=int,
                        dest='maxtime', help='Maximum timer ticks before quitting')
    parser.add_argument('filepath', metavar='ticks', action='store', type=str,
                        help="Location of puzzle input")

    # 2. Get the options and arguments
    return parser.parse_args()

# ----------------------------------------------------------------------
#                                                               part_one
# ----------------------------------------------------------------------


def part_one(args, input_lines):
    "Process part one of the puzzle"

    # 1. We start at zero
    solution = 0

    # 2. Loop for all of the lines of input_text (one change per line)
    for delta in input_lines:

        # 3. Modulate the frequeny
        solution += int(delta)
        if args.verbose:
            print("%d %s" % (solution, delta))

    # 4. Output the solution (if any)
    if solution is None:
        print("No solution after %d ticks" % args.maxtime)
    else:
        print("The solution is %s" % (solution))

    # 5. Return result
    return solution is not None

# ----------------------------------------------------------------------
#                                                               part_two
# ----------------------------------------------------------------------


def part_two(args, input_lines):
    "Process part two of the puzzle"

    # 1. Initialization
    solution = None
    freq = 0
    previous = set()
    time = 0

    # 2. Loop until we get a solution or time runs out
    while not solution and (args.maxtime == 0 or args.maxtime > time):

        # 3. Loop for all of the lines of input_text (one change per line)
        for delta in input_lines:

            # 4. Modulate the frequency
            freq += int(delta)
            if args.verbose:
                print("%d %s %s" % (freq, delta, previous))

            # 5. Have we seen this frequency before?
            if freq in previous:
                if args.verbose:
                    print("found %d in %s at time %d" % (freq, previous, time))
                solution = freq
                break

            # 6. Else add this frequency to the ones we have seen
            previous.add(freq)

            # 7. check that we haven't taken too long
            time += 1
            if args.maxtime > 0 and time >= args.maxtime:
                break

    # 8. Output the solution (if any)
    if solution is None:
        print("No solution after %d ticks" % time)
        print(len(previous))
        print(sorted(previous))
    else:
        print("The solution is %s" % (solution))

    # 9. Return result
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

        # 3. But ignore blank and comment lines
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
    """Read a Mine Cart Madness puzzle and solve it"""

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
# end                             c c . p y                          end
# ======================================================================
