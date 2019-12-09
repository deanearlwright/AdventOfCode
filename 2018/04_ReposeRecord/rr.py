# ======================================================================
#  Repose Record
#   Advent of Code 2018 Day 03 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                               r r . p y
# ======================================================================
"Solve the Repose Record puzzle for day 04 of Advent of Code 2018 day"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import argparse
import sys
import shift

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                      parse_commnd_line
# ----------------------------------------------------------------------


def parse_command_line():
    "Parse the command line options"

    # 1. Create the command line parser
    desc = 'Repose Recordt - day 04 of Advent of Code 2018'
    sample = 'sample: python ims.py input.txt'
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
#                                                           guard_totals
# ----------------------------------------------------------------------

def guard_totals(args, input_lines):
    "Process all of the guard log data"

    # 1. Start knowing nothing
    guards = {}
    guard = None

    # 2. Loop through all of the shift log
    for line in input_lines:

        # 3. Process each type of line
        line_type = line.split()[2]
        if line_type == "Guard":

            # 3a. Guard: Start a new shift
            new_shift = shift.Shift(text=line)
            guard = new_shift.number

            # 3b. Guard: Record this guard if new
            if guard not in guards:
                guards[guard] = new_shift

        elif line_type == "falls":

            # 3c. falls: Record falling asleep
            guards[guard].add_fall(text=line)

        elif line_type == "wakes" in line:

            # 3d. wakes: Record minutes asleep
            guards[guard].add_wake(text=line)

    # 4. Return accumulated log data
    if args.verbose:
        print("%d different guards" % len(guards))
    return guards

# ----------------------------------------------------------------------
#                                                               part_one
# ----------------------------------------------------------------------

def part_one(args, input_lines):
    "Process part one of the puzzle"

    # 1. Accumulate all of the log data
    guards = guard_totals(args, input_lines)

    # 2. Find the guard with the most minutes asleep
    max_minutes = (None, 0)
    for guard, combined in guards.items():
        asleep = combined.asleep()
        if asleep > max_minutes[1]:
            max_minutes = (guard, asleep)
    assert max_minutes[0] is not None
    if args.verbose:
        print("Guard #%04d has the most minutes asleep (%d)" % max_minutes)

    # 3. Get the minute most often asleep for the sleepest guard
    most_often = guards[max_minutes[0]].often()[0]

    # 4. Solution is ID of the guard you chose multiplied by the minute
    solution = max_minutes[0] * most_often

    # 5. Output the solution (if any)
    if solution is None:
        print("No solution found")
    else:
        print("The solution is %s" % solution)

    # 6. Return result
    return solution is not None

# ----------------------------------------------------------------------
#                                                               part_two
# ----------------------------------------------------------------------


def part_two(args, input_lines):
    "Process part two of the puzzle"

    # 1. Accumulate all of the log data
    guards = guard_totals(args, input_lines)

    # 2. Find the guard with the most times asleep at some minute
    max_often = (None, 0, 0) # guard, times, minute
    for guard, combined in guards.items():
        often = combined.often()
        if often[1] > max_often[1]:
            max_often = (guard, often[1], often[0])
    assert max_often[0] is not None
    if args.verbose:
        print("Guard #%04d was asleep %d times at minute %s" % max_often)

    # 3. Calculate solution
    solution = max_often[0] * max_often[2]

    # 6. Output the solution (if any)
    if solution is None:
        print("No solution found")
    else:
        print("The solution is %s" % solution)

    # 7. Return result
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
    "Break the text into trimed, claim-only lines"

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
    """Read No Matter How You Slice It puzzle and solve it"""

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
# end                             r r . p y                          end
# ======================================================================
