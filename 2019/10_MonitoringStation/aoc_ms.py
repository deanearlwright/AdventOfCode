# ======================================================================
#  Monitoring Station
#   Advent of Code 2019 Day 10 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                           a o c _ m s . p y
# ======================================================================
"Solve the Monitoring Station problem for Advent of Code 2019 day 10"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import argparse
import sys
import asteroids
import laser

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                      parse_commnd_line
# ----------------------------------------------------------------------


def parse_command_line():
    "Parse the command line options"

    # 1. Create the command line parser
    desc = 'Monitoring Station - day 10 of Advent of Code 2019'
    sample = 'sample: python aoc_ms.py input.txt'
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

    # 1. Create the astroids map
    a_map = asteroids.Asteroids(text=input_lines, verbose=args.verbose)

    # 2. Get the maximum number of asteroids viewable from one station
    solution = a_map.maximum()
    if not solution:
        print("Unable to determine maximum number of asteroids")
    else:
        print("Maximum asteroids that can be detected is %d at %s" % (solution))

    # 3. Return result
    return solution is not None

# ----------------------------------------------------------------------
#                                                               part_two
# ----------------------------------------------------------------------


def part_two(args, input_lines):
    "Process part two of the puzzle"

    # 1. Create the astroids map
    a_map = asteroids.Asteroids(text=input_lines, verbose=args.verbose)

    # 2. Get the maximum number of asteroids viewable from one station
    solution = a_map.maximum()
    if not solution:
        print("Unable to determine maximum number of asteroids")
        return False

    print("Maximum asteroids can be detected = %d at (%d,%d)" %
          (solution[0], solution[1][0], solution[1][1]))

    # 3. Put a laser there
    mylaser = laser.Laser(center=solution[1], text=input_lines)

    # 4. Go shoot 'em up
    loc = mylaser.shoot_until(number=args.maxtime, verbose=args.verbose)

    # 5. Announce the result
    if loc is not None:
        solution = 100 * loc[0] + loc[1]
        print("Shot the %d asteroid at %s, solution is %d" %
              (args.maxtime, loc, solution))
    else:
        solution = None

    # 6. Return result
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
        if line.startswith('!'):
            continue

        # 4. Add the line
        lines.append(line)

    # 5. Return a list of clean lines
    return lines

# ----------------------------------------------------------------------
#                                                                   main
# ----------------------------------------------------------------------


def main():
    """Read the Monitoring Stationproblem and solve it"""

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
# end                         a o c _ m s . p y                      end
# ======================================================================
