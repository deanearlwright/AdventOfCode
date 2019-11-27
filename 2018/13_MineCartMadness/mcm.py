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
    parser.add_argument('-t', '--max-time', action='store', default=0,
                        dest='maxtime', help='Maximum timer ticks before quitting')
    parser.add_argument('filepath', metavar='ticks', action='store', type=str,
                        help="Location of puzzle input")

    # 2. Get the options and arguments
    return parser.parse_args()

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

    # 3. Run the mine cars
    solution = tracks.solve(maxtime=args.maxtime)

    # 4. Output the solution (if any)
    if solution is None:
        print("No solution after %d ticks" % args.maxtime)
        sys.exit(2)
    else:
        print("The solution is (%d,%d) at %d ticks" % (solution[0], solution[1], tracks.time))
        sys.exit(0)

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()

# ======================================================================
# end                           m c m . p y                          end
# ======================================================================