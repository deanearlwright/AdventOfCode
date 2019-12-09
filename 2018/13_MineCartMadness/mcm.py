# ======================================================================
# Mine Cart Madness
#   Advent of Code 2018 Day 13 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                               m c m . p y
# ======================================================================
"Solve the Mine Card Madness problem of day 13 of Advent of Code 2018"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import argparse
import sys
import track

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                      parse_commnd_line
# ----------------------------------------------------------------------


def parse_command_line():
    "Parse the command line options"

    # 1. Create the command line parser
    desc = 'Mine Cart Madness - day 13 of Advent of Code 2018'
    sample = 'sample: python mcm.py input.txt'
    parser = argparse.ArgumentParser(description=desc,
                                     epilog=sample)
    parser.add_argument('-v', '--verbose', action='store_true', default=False,
                        dest='verbose', help='Print status messages to stdout')
    parser.add_argument('-p', '--part', action='store', default=1, type=int,
                        dest='part', help='Puzzle Part (1 or 2)')
    parser.add_argument('-f', '--final', action='store_true', default=False,
                        dest='final', help='Show the final state')
    parser.add_argument('-t', '--max-time', action='store', default=0, type=int,
                        dest='maxtime', help='Maximum timer ticks before quitting')
    parser.add_argument('filepath', metavar='ticks', action='store', type=str,
                        help="Location of puzzle input")

    # 2. Get the options and arguments
    return parser.parse_args()

# ----------------------------------------------------------------------
#                                                               part_one
# ----------------------------------------------------------------------


def part_one(args, tracks):
    "Process part one of the puzzle - first crash"

    # 1. Elves, to your carts
    if args.verbose:
        print("Initial number of carts = %d" % len(tracks.carts))

    # 2. Run the mine cars
    solution = tracks.solve(maxtime=args.maxtime)

    # 3. Output the solution (if any)
    if solution is None:
        print("No solution after %d ticks" % args.maxtime)
    else:
        print("The solution is (%d,%d) at %d ticks" % (solution[0], solution[1], tracks.time))

    # 4. Return Result
    return solution is not None

# ----------------------------------------------------------------------
#                                                               part_two
# ----------------------------------------------------------------------


def part_two(args, tracks):
    "Process part one of the puzzle - last cart standing"

    # 1. Elves, to your carts
    if args.verbose:
        print("Initial number of carts = %d" % len(tracks.carts))

    # 2. Run the mine cars until only one is left
    solution = tracks.derby(maxtime=args.maxtime)

    # 3. Output the solution (if any)
    if solution is None:
        print("No solution after %d ticks" % args.maxtime)
    else:
        print("The solution is (%d,%d) at %d ticks" % (solution[0], solution[1], tracks.time))

    # 4. Return result
    return solution is not None

# ----------------------------------------------------------------------
#                                                                   main
# ----------------------------------------------------------------------


def main():
    """Read a Mine Cart Madness puzzle and solve it"""

    # 1. Get the command line options
    args = parse_command_line()

    # 2. Read the puzzle file
    tracks = track.Track()
    tracks.from_file(args.filepath)

    # 3. Process the appropiate part of the puzzle
    if args.part == 1:
        result = part_one(args, tracks)
    else:
        result = part_two(args, tracks)

    # 4. Output the final grid (if requested)
    if args.final:
        print(str(tracks))

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
# end                           m c m . p y                          end
# ======================================================================
