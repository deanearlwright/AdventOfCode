# ======================================================================
#  Alchemical Reduction
#   Advent of Code 2018 Day 5 -- Eric Wastl -- https://adventofcode.com
#
# Computer simulation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                               a r . p y
# ======================================================================
"Solve the Alchemical Reduction puzzle for day 05of Advent of Code 2018"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import argparse
import sys

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
PAIRS = ['aA', 'bB', 'cC', 'dD', 'eE', 'fF', 'gG', 'hH', 'iI', 'jJ',
         'kK', 'lL', 'mM', 'nN', 'oO', 'pP', 'qQ', 'rR', 'sS', 'tT',
         'uU', 'vV', 'wW', 'xX', 'yY', 'zZ',
         'Aa', 'Bb', 'Cc', 'Dd', 'Ee', 'Ff', 'Gg', 'Hh', 'Ii', 'Jj',
         'Kk', 'Ll', 'Mm', 'Nn', 'Oo', 'Pp', 'Qq', 'Rr', 'Ss', 'Tt',
         'Uu', 'Vv', 'Ww', 'Xx', 'Yy', 'Zz']
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# ----------------------------------------------------------------------
#                                                      parse_commnd_line
# ----------------------------------------------------------------------


def parse_command_line():
    "Parse the command line options"

    # 1. Create the command line parser
    desc = 'Alchemical Reduction - day 05 of Advent of Code 2018'
    sample = 'sample: python ar.py input.txt'
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
#                                                        reduce_by_pairs
# ----------------------------------------------------------------------

def reduce_by_pairs(sequence):
    "Eliminate opposite polarity pairs"

    # 1. Loop for all the pairs
    for pair in PAIRS:

        # 2. destroy all of those pairs
        sequence = sequence.replace(pair, '')

    # 3. Return the new sequence with pairs destroyed
    return sequence

# ----------------------------------------------------------------------
#                                                maximum_reduce_by_pairs
# ----------------------------------------------------------------------

def maximum_reduce_by_pairs(args, sequence):
    "Repediately eliminate opposite polarity pairs"

    # 1. Initialize loop enders
    old_sequence = 'maximum_reduce_py_pairs'
    loops = 0

    # 3. Loop until the sequence doesn't change
    while sequence != old_sequence:

        # 4. Replace pairs to create a new sequence
        old_sequence = sequence
        sequence = reduce_by_pairs(sequence)

        # 5. Make sure we aren't taking too long
        loops += 1
        if args.maxtime > 0 and loops > args.maxtime:
            sequence = None
            break

    # 6. Return the reduced sequence
    return sequence

# ----------------------------------------------------------------------
#                                                               part_one
# ----------------------------------------------------------------------

def part_one(args, input_lines):
    "Process part one of the puzzle"

    # 1. The sequence is on one line
    sequence = input_lines[0]
    if args.verbose:
        print("The initial sequence has %d characters" % len(sequence))

    # 2. Redunce the sequence
    sequence = maximum_reduce_by_pairs(args, sequence)

    # 3. Output the solution (if any)
    if sequence is None:
        print("No solution found")
    else:
        solution = len(sequence)
        print("The solution is %s" % solution)

    # 4. Return result
    return solution is not None

# ----------------------------------------------------------------------
#                                                               part_two
# ----------------------------------------------------------------------


def part_two(args, input_lines):
    "Process part two of the puzzle"

    # 1. The sequence is on one line
    sequence = input_lines[0]
    if args.verbose:
        print("The initial sequence has %d characters" % len(sequence))

    # 2. Assume the worst
    solution = len(sequence) + 1

    # 3. Loop for all of the letter pairs
    for letter in LETTERS:

        # 4. Remove those letters from original sequence
        sequence25 = sequence.replace(letter, '').replace(letter.lower(), '')

        # 5. See how that sequence reduces
        reduced25 = maximum_reduce_by_pairs(args, sequence25)
        if reduced25 is None:
            solution = None
            break
        len_r25 = len(reduced25)
        if args.verbose:
            print("Sequence without %s and %s reduces to %d characters" %
                  (letter, letter.lower(), len_r25))

        # 6. Keep the length of the shortest sequence
        if len_r25 < solution:
            solution = len_r25

    # 7. Output the solution (if any)
    if solution is None:
        print("No solution found")
    else:
        print("The solution is %s" % solution)

    # 8. Return result
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
    """Read Alchemical Reduction puzzle and solve it"""

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
# end                             a r . p y                          end
# ======================================================================
