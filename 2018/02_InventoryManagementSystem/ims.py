

# ======================================================================
# Inventory Management Systemn
#   Advent of Code 2018 Day 02 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                               i m s . p y
# ======================================================================
"Solve the Inventory Management System problem Advent of Code 2018 day 2"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import argparse
import sys
from collections import Counter

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                      parse_commnd_line
# ----------------------------------------------------------------------


def parse_command_line():
    "Parse the command line options"

    # 1. Create the command line parser
    desc = 'Inventory Management System - day 01 of Advent of Code 2018'
    sample = 'sample: python ims.py input.txt'
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
#                                                        twos_and_threes
# ----------------------------------------------------------------------


def twos_and_threes(label):
    "Return the number of characters that appear twice and three times"

    # 1. Get the unique letters and their counts
    counts = Counter(label)

    # 2. Start with no twos or threes
    twos = 0
    threes = 0

    # 3. Loop through all of the letters and counts
    for letter in counts:
        count = counts[letter]

        # 4. Keep track of the number of twos and threes
        if count == 2:
            twos += 1
        elif count == 3:
            threes += 1

    # 5. Return the number of twos and threes
    return [twos, threes]

# ----------------------------------------------------------------------
#                                                               part_one
# ----------------------------------------------------------------------


def part_one(args, input_lines):
    "Process part one of the puzzle"

    # 1. Start with no twos or threes
    counts = [0, 0]

    # 2. Loop for all of the lines of input_text (one change per line)
    for label in input_lines:

        # 3. Determine the twos and threes for this label
        knts = twos_and_threes(label)
        if args.verbose:
            print("%s %d %d" % (label, knts[0], knts[1]))

        # 4. Accumulate the twos and threes
        if knts[0] > 0:
            counts[0] += 1
        if knts[1] > 0:
            counts[1] += 1

    # 5. Compute the checksum
    if args.verbose:
        print("totals: twos %d, threes %d" % (counts[0], counts[1]))
    solution = counts[0] * counts[1]
    print("The solution is %s" % (solution))

    # 5. Return result
    return solution is not None


# ----------------------------------------------------------------------
#                                                               only_one
# ----------------------------------------------------------------------


def only_one(label1, label2):
    "Return True if label1 and label2 differ by only one character"

    # 1. Start with no differences
    diff = 0

    # 2. Loop through the characters in the labels
    for i, letter in enumerate(label1):

        # 3. If the characters are differnt, increment count
        if letter != label2[i]:
            diff += 1

            # 4. If there are too many differences, return False
            if diff > 1:
                return False

    # 5. Only 1 (or 0) differences, return True
    return True

# ----------------------------------------------------------------------
#                                                         common_letters
# ----------------------------------------------------------------------


def common_letters(label1, label2):
    "Return the non-matching letter in the two labels"

    # 1. Start with no letters
    common = ''

    # 2. Loop through the characters in the labels
    for i, letter in enumerate(label1):

        # 3. If the characters are differnt, keep them
        if letter == label2[i]:
            common += letter

    # 4. Return the common letters
    return common

# ----------------------------------------------------------------------
#                                                               part_two
# ----------------------------------------------------------------------


def part_two(args, input_lines):
    "Process part two of the puzzle"

    # 1. Initialization
    solution = None
    previous = []

    # 2. Loop for all of the lines of input_text (one label per line)
    for label in input_lines:

        # 3. Loop for all of the previous labels
        for prev in previous:

            # 4. Is this one close enough to the input label?
            if only_one(label, prev):

                # 5. If it is, we have a solution
                solution = common_letters(label, prev)
                break

        # 5. if not that close, save it
        if solution:
            break
        else:
            previous.append(label)

    # 6. Output the solution (if any)
    if solution is None:
        print("No solution found")
        if args.verbose:
            print(len(previous))
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
    """Read a Inventory Management System puzzle and solve it"""

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
# end                            i m s . p y                         end
# ======================================================================
