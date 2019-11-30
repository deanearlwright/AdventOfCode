

# ======================================================================
#  No Matter How You Slice It
#   Advent of Code 2018 Day 03 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                           n m h y s i . p y
# ======================================================================
"Solve the No Matter How You Slice It problem Advent of Code 2018 day 3"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import argparse
import sys
from collections import Counter
from functools import reduce
import claim
import row

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                      parse_commnd_line
# ----------------------------------------------------------------------


def parse_command_line():
    "Parse the command line options"

    # 1. Create the command line parser
    desc = ' No Matter How You Slice It - day 03 of Advent of Code 2018'
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
#                                                        register_claims
# ----------------------------------------------------------------------


def register_claims(input_lines):
    "Return the number of characters that appear twice and three times"

    # 1. Start with no claims
    claims = []

    # 2. Loop through all of the claims
    for line in input_lines:

        # 3. Create claim from text
        one_claim = claim.Claim(text=line)

        # 4. Add the new claim to the list
        claims.append(one_claim)

    # 5. Return the all the claims
    return claims

# ----------------------------------------------------------------------
#                                                         first_and_last
# ----------------------------------------------------------------------


def first_and_last(claims):
    "Return the first and last row numbers from the claims"

    # 1. If there are no claims, return (0, 0)
    if not claims:
        return (0, 0)

    # 2. Get the row closest to the top
    first = reduce(lambda x,y: min(x,y), [c.top for c in claims])

    # 3. Get the row closest to the bottom
    last = reduce(lambda x,y: max(x,y), [c.bottom for c in claims])

    # 4. Return the top most and bottom most row numbers
    return first, last

# ----------------------------------------------------------------------
#                                                               part_one
# ----------------------------------------------------------------------

def part_one(args, input_lines):
    "Process part one of the puzzle"

    # 1. Register the claims
    claims = register_claims(input_lines)
    if args.verbose:
        print("%d claimes filed" % len(claims))

    # 2. Get the top most and bottom most row numbers of the claims
    first, last = first_and_last(claims)

    # 3. Start with no overlapping squares
    solution = 0

    # 4. Loop from the first to last rows with a claim
    for number in range(first, last-1):

        # 5. Create a row
        onerow = row.Row(number=number)

        # 6. Determine the claims on the squares in that row
        for c in claims:
            onerow.add_claim(c)

        # 7. Get the number of squares with overlapping claims
        squares = onerow.overlap()
        if args.verbose:
            print("%d overlapping squares in row %s" % (squares, number))

        # 8. Accumulate the total number of overlapping squares
        solution += squares

    # 9. Return result
    print("The solution is %d" % (solution))
    return solution is not None

# ----------------------------------------------------------------------
#                                                               part_two
# ----------------------------------------------------------------------


def part_two(args, input_lines):
    "Process part two of the puzzle"

    # 1. Register the claims
    claims = register_claims(input_lines)
    if args.verbose:
        print("%d claims filed" % len(claims))

    # 2. Start with no solution
    solution = None

    # 3. Loop for all of the claims
    for index1, claim1 in enumerate(claims):

        # 3. Assume this is the one
        solution = claim1.number

        # 4. Loop for all of the other claims
        for index2, claim2 in enumerate(claims):
            if index1 == index2:
                continue

            # 5. Do these claims overlap?
            #    If they do, them this is not the solution
            if claim1.does_overlap(claim2):
                solution = None
                break

        # 6. Did we find a solution?
        #    If we did, we don't have to look anymore
        if solution:
            break

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

        # 3. But ignore blank and non-claim lines
        line = line.rstrip(' \r')
        if not line:
            continue
        if not line.startswith('#'):
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
# end                         n m h y s i . p y                      end
# ======================================================================

